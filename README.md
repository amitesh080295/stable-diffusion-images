# stable-diffusion-images
 Stable Diffusion and tkinter app to generate images from text prompts


 ### Known Issues

 1. Issue with running tkinter. Python may not be configured for tk. Resolve this issue on mac by running the command `brew install python-tk@3.9` or whatever is your python version. Then you can check if tkinter is installed or not by running `python3.9 -m tkinter`
 2. On M1 Macs, the device should be *cpu*. Also, torch_dtype and revision parameters from StableDiffusionPipeline need to be removed. Explore this [thread](https://huggingface.co/CompVis/stable-diffusion-v1-4/discussions/13) for details 
