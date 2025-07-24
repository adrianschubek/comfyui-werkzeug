from .nodes.values import WzInt, WzFloat, WzStr, WzBool
from .nodes.convert import StringToInt, IntToString, FloatToString, StringToFloat, IntToWxH, WxHToInt
from .nodes.transform import SplitString, JoinStrings, JoinTwoStrings
from .nodes.extra import CleanVRAMPassthrough, PrintPassthrough


NODE_CLASS_MAPPINGS = {
    # Values
    "ZeugInt": WzInt,
    "ZeugFloat": WzFloat,
    "ZeugStr": WzStr,
    "ZeugBool": WzBool,
    # Convert
    "ZeugStrToInt": StringToInt,
    "ZeugIntToStr": IntToString,
    "ZeugFloatToStr": FloatToString,
    "ZeugStrToFloat": StringToFloat,
    "ZeugIntToWxH": IntToWxH,
    "ZeugWxHToInt": WxHToInt,
    # Transform
    "ZeugSplitStrList": SplitString,
    "ZeugJoinStrList": JoinStrings,
    "ZeugJoinStr": JoinTwoStrings,
    # Extra
    "ZeugCleanGpuPass": CleanVRAMPassthrough,
    "ZeugPrintPass": PrintPassthrough,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # Values
    "ZeugInt": "Int",
    "ZeugFloat": "Float",
    "ZeugStr": "String",
    "ZeugBool": "Bool",
    # Convert
    "ZeugStrToInt": "String to Int",
    "ZeugIntToStr": "Int to String",
    "ZeugFloatToStr": "Float to String",
    "ZeugStrToFloat": "String to Float",
    "ZeugIntToWxH": "Int to WidthHeight Tuple",
    "ZeugWxHToInt": "WidthHeight Tuple to Int",
    # Transform
    "ZeugSplitStrList": "Split String to List",
    "ZeugJoinStrList": "Join Strings List",
    "ZeugJoinStr": "Join Strings",
    # Extra
    "ZeugCleanGpuPass": "Clean GPU",
    "ZeugPrintPass": "Print",
}
