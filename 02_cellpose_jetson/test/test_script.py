from resnet_torch import CPnet
from cellpose.dynamics import compute_masks
import matplotlib.pyplot as plt
from tqdm import tqdm
import imageio
import timeit
import torch

######
n_evals = 50
diam_ = 50
mask_name = "mask.png"
######

img = torch.from_numpy( imageio.imread("testimg.png")[...,1] ) # (H,W)
inp_tensor = img[None,None].expand(-1,2,-1,-1)

# Initialize the network similarly to in the CP code
cp = CPnet([2, 32, 64, 128, 256], 3, 3)#, residual_on=False, style_on=False, concatenation=True, mkldnn=None, diam_mean=30)
cp.load_model("../cyto2torch_0")

cp = cp.to('cuda')
cp.eval()
inp_tensor = inp_tensor.float() / 255. # Normalize
#inp_tensor = inp_tensor.to('cuda')

#def rescale(x):
#    r"""
#    Rescale to in (0,255).
#    """
#    out = x - x.min()
#    out = (out / out.max()) * 255.
#
#    return out

#with torch.no_grad():
#    outp_, _ = cp(inp_tensor.to('cuda'))
#    dP = outp_[0,:2]
#    cellprob = outp_[0,2]
#    masks = compute_masks(
#            dP.cpu().numpy(), 
#            cellprob.cpu().numpy(),
#            use_gpu=True,
#            device=torch.device('cuda'))
#    for ch_ in range(3):
#        # Save for visualization.
#        #imageio.imsave("./ch{}.png".format(ch_), rescale(outp_[0][0,ch_]).cpu().numpy())
#        plt.imshow(outp_[0][0,ch_].cpu().numpy()); plt.title("CH {}".format(ch_)); plt.show()

def run_cp_full(inp_tensor):
    with torch.no_grad():
        outp_, _ = cp(inp_tensor.to('cuda'))
        dP = outp_[0,:2]
        cellprob = outp_[0,2]
        masks = compute_masks(
                dP.cpu().numpy(), 
                cellprob.cpu().numpy(),
                use_gpu=True,
                device=torch.device('cuda'))

times = []
with torch.no_grad():
    for idx in tqdm(range(n_evals), desc="Evaluating full pipeline..."):
        # Time moving the data to GPU and running inference.
        time = timeit.timeit(lambda : run_cp_full(inp_tensor), number=1)
        times.append(time)

avg_time = sum(times) / n_evals
print("Image shape: {}\nAvg exec time: {}s/it".format(inp_tensor.shape, avg_time))
