from abc import ABC, abstractmethod
from typing import Any, Mapping, Sequence, Tuple

QWEN_IMAGE_SUPPORTED_RESOLUTIONS = [
    (1328, 1328, 1.0),
    (1664, 928, 1.793),
    (928, 1664, 0.558),
    (1472, 1140, 1.291),
    (1140, 1472, 0.774),
    (1584, 1056, 1.5),
    (1056, 1584, 0.667),
]

class Resolution(ABC):
    @classmethod
    @abstractmethod
    def resolutions(cls) -> Sequence[Tuple[int, int, float]]: ...

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return{
            "required": {
                "resolution": ([f"{res[0]}x{res[1]}" for res in cls.resolutions()],)
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "op"
    CATEGORY = "Bori_QwenImgRes"

    def op(self, resolution: str) -> tuple[int, int]:
        width, height = resolution.split("x")
        return (int(width), int(height))
    
class Bori_QwenImageResolution(Resolution):
    @classmethod
    def resolutions(cls):
        return QWEN_IMAGE_SUPPORTED_RESOLUTIONS