class StringToInt:
    """
    A ComfyUI node that converts a string input to an integer.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": False, "default": "0"}),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "string_to_int"
    CATEGORY = "werkzeug/convert"

    def string_to_int(self, text):
        try:
            # Strip whitespace and convert to int
            result = int(text.strip())
            return (result,)
        except ValueError:
            raise ValueError(f"Cannot convert '{text}' to an integer.")


class IntToString:
    """
    A ComfyUI node that converts an integer input to a string.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "int_to_string"
    CATEGORY = "werkzeug/convert"

    def int_to_string(self, value):
        return (str(value),)


class FloatToString:
    """
    A ComfyUI node that converts a float input to a string.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "float_to_string"
    CATEGORY = "werkzeug/convert"

    def float_to_string(self, value):
        return (str(value),)


class StringToFloat:
    """
    A ComfyUI node that converts a string input to a float.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": False, "default": "0.0"}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float",)
    FUNCTION = "string_to_float"
    CATEGORY = "werkzeug/convert"

    def string_to_float(self, text):
        try:
            # Strip whitespace and convert to float
            result = float(text.strip())
            return (result,)
        except ValueError:
            raise ValueError(f"Cannot convert '{text}' to a float.")


class IntToWxH:
    """
    A ComfyUI node that converts two integer inputs (width, height) to a WxH tuple.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 1, "max": 8192}),
                "height": ("INT", {"default": 512, "min": 1, "max": 8192}),
            },
        }

    RETURN_TYPES = ("WzWxH",)
    RETURN_NAMES = ("wxh",)
    FUNCTION = "int_to_wxh"
    CATEGORY = "werkzeug/convert"

    def int_to_wxh(self, width, height):
        return ((width, height),)


class WxHToInt:
    """
    A ComfyUI node that converts a WxH tuple to two integer outputs (width, height).
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "wxh": ("WzWxH", {}),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "wxh_to_int"
    CATEGORY = "werkzeug/convert"

    def wxh_to_int(self, wxh):
        width, height = wxh
        return (width, height)
