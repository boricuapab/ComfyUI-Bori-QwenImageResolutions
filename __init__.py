from .nodes.Bori_QwenImgRes import *

NODE_CLASS_MAPPINGS = {
    "Bori Qwen Image Resolution": Bori_QwenImageResolution,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Bori Qwen Img Res": "Bori Qwen Img Res", 
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]