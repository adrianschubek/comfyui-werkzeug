from .nodes.values import WzInt, WzFloat, WzStr, WzBool
from .nodes.convert import StringToInt, IntToString, FloatToString, StringToFloat, IntToWxH, WxHToInt
from .nodes.transform import SplitString, JoinStrings, JoinTwoStrings
from .nodes.extra import CleanVRAMPassthrough, PrintPassthrough


NODE_CLASS_MAPPINGS = {
    # Values
    "WzInt": WzInt,
    "WzFloat": WzFloat,
    "WzStr": WzStr,
    "WzBool": WzBool,
    # Convert
    "WzStrToInt": StringToInt,
    "WzIntToStr": IntToString,
    "WzFloatToStr": FloatToString,
    "WzStrToFloat": StringToFloat,
    "WzIntToWxH": IntToWxH,
    "WzWxHToInt": WxHToInt,
    # Transform
    "WzSplitStrList": SplitString,
    "WzJoinStrList": JoinStrings,
    "WzJoinStr": JoinTwoStrings,
    # Extra
    "WzCleanGpuPass": CleanVRAMPassthrough,
    "WzPrintPass": PrintPassthrough,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # Values
    "WzInt": "Int",
    "WzFloat": "Float",
    "WzStr": "String",
    "WzBool": "Bool",
    # Convert
    "WzStrToInt": "String to Int",
    "WzIntToStr": "Int to String",
    "WzFloatToStr": "Float to String",
    "WzStrToFloat": "String to Float",
    "WzIntToWxH": "Int to WidthHeight Tuple",
    "WzWxHToInt": "WidthHeight Tuple to Int",
    # Transform
    "WzSplitStrList": "Split String to List",
    "WzJoinStrList": "Join Strings List",
    "WzJoinStr": "Join Strings",
    # Extra
    "WzCleanGpuPass": "Clean GPU",
    "WzPrintPass": "Print",
}
