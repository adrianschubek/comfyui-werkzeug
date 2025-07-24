import torch
import gc
import comfy.model_management as model_mgmt


class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False


any_type = AlwaysEqualProxy("*")


class CleanVRAMPassthrough:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": (any_type, {}),
            }
        }

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("output",)

    OUTPUT_NODE = True

    FUNCTION = "clean_vram"
    CATEGORY = "werkzeug/extra"

    def clean_vram(self, input):
        print("Cleaning VRAM...")
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
        model_mgmt.soft_empty_cache()
        model_mgmt.cleanup_models()
        model_mgmt.unload_all_models()
        return (input,)


