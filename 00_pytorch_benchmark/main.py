r"""
This script is mostly code copied from https://pytorch.org/tutorials/intermediate/realtime_rpi.html
"""

import tqdm
import time
import timeit
import subprocess

import torch
from torchvision import models, transforms
torch.backends.quantized.engine = 'qnnpack'

preprocess = transforms.Compose([
    #transforms.ToTensor(),
    # normalize the colors to the range that mobilenet_v2/3 expect
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
net = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
torch.backends.quantized.engine = 'qnnpack'

def get_temp():
    command = "vcgencmd measure_temp"
    result_string = subprocess.run(command.split(" "), capture_output=True).stdout
    return float(result_string[5:-3])


with open("./test.csv", "w") as outfile:

    print("timestamp,execution_time,temperature", file=outfile)
    init_time = time.time()

    with torch.no_grad():
        pbar = tqdm.tqdm(desc="Logging runs...")
        while True:
            # Generate some noise as input, we currently don't have a camera.
            # TODO This changes when the camera arrives.
            image = torch.randn(1,3,224,224)
    
            # TODO Handling of image capture errors.
            #if not ret:
            #    raise RuntimeError("failed to read frame")
    
            # convert opencv output from BGR to RGB
            #image = image[:, :, [2, 1, 0]]
            #permuted = image
    
            # preprocess
            input_tensor = preprocess(image)
    
            # create a mini-batch as expected by the model
            #input_batch = input_tensor.unsqueeze(0)
    
            # run model and log some info
            timestamp = time.time()
            func_time = timeit.timeit(lambda : net(image), number=1)
            rpi_temp = get_temp()
            if outfile is not None: print(
                    "{},{},{}".format(
                        timestamp - init_time,
                        func_time,
                        rpi_temp), file=outfile)
            pbar.update()
