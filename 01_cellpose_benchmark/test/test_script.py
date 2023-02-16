from cellpose.models import Cellpose
import imageio
import timeit
from tqdm import tqdm

img = imageio.imread("testimg.png")[...,1]
cp = Cellpose()

n_evals = 3
diam_ = 50
mask_name = "mask.png"

times = []
for idx in tqdm(range(n_evals), desc="Evaluating..."):
    time = timeit.timeit(lambda : cp.eval(img, diameter=diam_), number=1)
    times.append(time)

print("img shape: {}".format(img.shape))
print("Saving {} for visualization (one more run)...".format(mask_name))
outp_ = cp.eval(img, diameter=diam_)
mask = outp_[0]
mask[mask != 0] = 255
imageio.imsave(mask_name, mask)

avg_time = sum(times) / n_evals
print("Image shape: {}\nAvg exec time: {}s/it".format(img.shape, avg_time))

