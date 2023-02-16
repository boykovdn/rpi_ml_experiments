import openflexure_microscope_client as ofm_client
microscope = ofm_client.find_first_microscope()

pos = microscope.position
#pos['x'] -= 100
#microscope.move(pos)

# Check the microscope will autofocus
ret = microscope.autofocus()

# Acquire an image for sanity-checking too
image = microscope.grab_image_array()
