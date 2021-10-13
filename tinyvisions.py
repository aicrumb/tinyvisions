import sys
sys.path.append('./CLIP')
from tqdm import tqdm
import torch as t
from torchvision.transforms import Compose, Resize, Normalize, RandomAffine, Lambda, RandomGrayscale
import clip as c
import PIL
from torch.nn import functional as F

prompt=sys.argv[1]
d='cuda'
z=t.rand((1, 3, 256, 256), device=d, requires_grad=True)
o=t.optim.Adam((z,),0.1)
f=Compose([Resize(224),lambda x:t.clamp((x+1)/2,min=0,max=1),Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711)),
    RandomAffine(degrees=60, translate=(0.1, 0.1)),RandomGrayscale(p=0.2),Lambda(lambda x: x + t.randn_like(x) * 0.01),])
m=c.load('ViT-B/32', jit=False)[0].eval().requires_grad_(False).to(d)
te=m.encode_text(c.tokenize(prompt).to(d))
for i in tqdm(range(int(sys.argv[2]))):
    o.zero_grad()
    x = F.normalize(m.encode_image(t.cat([f(z.add(1).div(2)) for _ in range(4)])), dim=-1)
    y = F.normalize(te.unsqueeze(0), dim=-1)
    l = (x - y).norm(dim=-1).div(2).arcsin().pow(2).mul(2).mean() +  (z - z.clamp(-1, 1)).pow(2).mean([1, 2, 3]).mean()/2
    l.backward()
    o.step()
PIL.Image.fromarray((z.permute(0, 2, 3, 1)*127.5+128).clamp(0,255).to(t.uint8)[0].cpu().numpy(),'RGB').save(sys.argv[1].replace(" ", "")+".png")
print(sys.argv[1].replace(" ", "")+".png saved")