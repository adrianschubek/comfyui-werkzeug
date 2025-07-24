class WzInt:
    """
    A ComfyUI node that provides an integer input widget and outputs an integer.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0, "min": -999999999, "max": 999999999}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int",)
    FUNCTION = "int_value"
    CATEGORY = "werkzeug/values"

    def int_value(self, value):
        return (value,)


class WzFloat:
    """
    A ComfyUI node that provides a float input widget and outputs a float.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0, "min": -999999999.0, "max": 999999999.0, "step": 0.01}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float",)
    FUNCTION = "float_value"
    CATEGORY = "werkzeug/values"

    def float_value(self, value):
        return (value,)


class WzStr:
    """
    A ComfyUI node that provides a string input widget and outputs a string.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("STRING", {"default": "", "multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "string_value"
    CATEGORY = "werkzeug/values"

    def string_value(self, value):
        return (value,)


class WzBool:
    """
    A ComfyUI node that provides a boolean input widget and outputs a boolean.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("bool",)
    FUNCTION = "bool_value"
    CATEGORY = "werkzeug/values"

    def bool_value(self, value):
        return (value,)