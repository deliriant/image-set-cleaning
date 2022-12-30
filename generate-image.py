from diffusers import StableDiffusionPipeline
import torch
import sys

model_path = "diffusers/examples/text_to_image/trained-model/"
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16)
pipe.to("cuda")
image = pipe(prompt=sys.argv[1]).images[0]
image.save(sys.argv[2])