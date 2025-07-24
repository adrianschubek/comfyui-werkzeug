import torch
import gc
import comfy.model_management as model_mgmt


class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False


any_type = AlwaysEqualProxy("*")


class PrintPassthrough:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": (any_type, {}),
                "prefix": ("STRING", {"default": ""}),
                "message": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("output",)

    OUTPUT_NODE = True

    FUNCTION = "print_pass"
    CATEGORY = "werkzeug/extra"

    @classmethod
    def VALIDATE_INPUTS(cls, input_types):
        # Get the actual type of the input
        input_type = input_types.get("input")
        if input_type is not None:
            # Update RETURN_TYPES to match the input type
            cls.RETURN_TYPES = (input_type,)
        return True

    def print_pass(self, input, prefix, message):
        print(f"{prefix}{message}")
        return (input,)


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


