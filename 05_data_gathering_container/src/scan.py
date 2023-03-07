import openflexure_microscope_client as ofm_client
import numpy as np
import imageio
import tqdm

class OFMPosition:

    def __init__(self, position: dict):
        self.position_vector = np.array(list(position.values()))

    def to_dict(self, vector):

        x = vector[0]
        y = vector[1]
        z = vector[2]

        return {'x' : x, 'y' : y, 'z' : z}

    @property
    def dict(self):
        r"""
        Returns position in the format OFM accepts, which is:

        {'x' : int, 'y' : int, 'z' : int}

        """
        return self.to_dict(self.position_vector)

    @property
    def numpy(self):
        r"""
        Returns np.ndarray of ints (3,) which are ordered [x,y,z].
        """
        return self.position_vector

    def __iadd__(self, other: np.ndarray):
        self.position_vector += other
        return self

    def __repr__(self):
        return "xyz: {}".format(self.position_vector)

def process_image(img, img_tag=None):
    r"""
    The image might have to be sent over the network, or saved to disk. This
    function handles either case.

    Inputs:
        :img: np.ndarray (H,W,C)
    """
    imageio.imsave("./test_img_{:05d}.png".format(img_tag), img)

def process_location(microscope, tag=None) -> None:
    r"""
    Run the necessary processing at the current location of the OFM.

    Inputs:
        :microscope: handle for the active OFM.
    """
    ret = microscope.autofocus()
    img_ = microscope.grab_image_array()
    process_image(img_, img_tag=tag)

def main():

    OFM_ADDRESS = "10.253.202.162"
    SCAN_STEPS = (4,4) # n steps
    SCAN_DELTA = (-200,-200) # umeters

    microscope = ofm_client.MicroscopeClient(OFM_ADDRESS)
    ret = microscope.autofocus() # Initial autofocus
    initial_position = OFMPosition(microscope.position)

    loc_counter = 0
    process_img = lambda idx : process_location(microscope, tag=idx)
    try:
        current_position = OFMPosition(initial_position.dict)
        process_img(loc_counter); loc_counter += 1

        # The following parameter is in {+1, -1} and determined which way the 
        # y scan will go. The sign flips at the start of each y scan loop, so
        # that the scan follows a snaking pattern rather than returning all
        # the way to the beginning of the next line, which is unnecessary.
        y_direction = -1
        pbar = tqdm.tqdm(total=SCAN_STEPS[0]*SCAN_STEPS[1], desc="Taking images...")
        for step_x in range(SCAN_STEPS[0]):

            y_direction *= -1 # Flip direction of scan

            for step_y in range(SCAN_STEPS[1]):

                current_position += np.array([0, y_direction*SCAN_DELTA[1] ,0])
                microscope.move(current_position.dict)
                process_img(loc_counter); loc_counter += 1

                pbar.update()

            current_position += np.array( [SCAN_DELTA[0], 0, 0] )
            microscope.move(current_position.dict)
            process_img(loc_counter); loc_counter += 1

    finally:
        print("Returning to starting position...")
        microscope.move(initial_position.dict)
        print("Done")

if __name__ == "__main__":
    main()
