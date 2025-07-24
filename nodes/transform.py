class SplitString:
    """
    A ComfyUI node that splits a string by a delimiter into a list of strings.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "delimiter": ("STRING", {"multiline": False, "default": ","}),
                "strip_whitespace": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("strings",)
    FUNCTION = "split_string"
    CATEGORY = "zeug/transform"
    OUTPUT_IS_LIST = (True,)

    def split_string(self, text, delimiter, strip_whitespace):
        if not text:
            return ([],)

        result = text.split(delimiter)
        # Strip whitespace from each part
        result = [part.strip() for part in result] if strip_whitespace else result
        return (result,)


class JoinStrings:
    """
    A ComfyUI node that joins a list of strings into a single string.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "strings": ("STRING", {}),
                "delimiter": ("STRING", {"multiline": False, "default": ","}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "join_strings"
    CATEGORY = "zeug/transform"
    INPUT_IS_LIST = True

    def join_strings(self, strings, delimiter):
        if not strings:
            return ("",)
        # Extract delimiter from list since INPUT_IS_LIST = True
        delimiter_str = delimiter[0] if delimiter else ","
        result = delimiter_str.join(strings)
        return (result,)


class JoinTwoStrings:
    """
    A ComfyUI node that joins two individual strings with a delimiter.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_a": ("STRING", {"multiline": False, "default": ""}),
                "string_b": ("STRING", {"multiline": False, "default": ""}),
                "delimiter": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "join_two_strings"
    CATEGORY = "zeug/transform"

    def join_two_strings(self, string_a, string_b, delimiter):
        result = string_a + delimiter + string_b
        return (result,)
