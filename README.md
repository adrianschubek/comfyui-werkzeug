# comfyui-zeug

comfyui-zeug (German for "gear" or "stuff") is a collection of custom nodes for ComfyUI, designed to provide missing features and improve usability. It includes various utility nodes which make it easier to work with data and perform common tasks e.g. specifying width and height tuples, passthrough logging, and more.


# Values
Basic data input nodes

### Int (ZeugInt)
1 widget => 1 out
integer input
integer output

### Float (ZeugFloat)
1 widget => 1 out
float input
float output

### String (ZeugStr)
1 widget => 1 out
string input
string output

### Bool (ZeugBool)
1 widget => 1 out
boolean input
boolean output

# Conversion (between types)
Nodes that convert between different data types.

### Int to String (ZeugIntToStr)
1 in => 1 out
integer input
string output

### String to Int (ZeugStrToInt)
1 in => 1 out
string input
integer output

### Float to String (ZeugFloatToStr)
1 in => 1 out
float input
string output

### String to Float (ZeugStrToFloat)
1 in => 1 out
string input
float output

### Int to WidthHeight Tuple (ZeugIntToWxH)
2 widgets => 1 out
width: integer
height: integer
(width,height) tuple output (custom type: WxH)

### WidthHeight Tuple to Int (ZeugWxHToInt)
1 in => 2 out
(width,height) tuple input  (custom type: WxH)
width integer output
height integer output

# Transform
Transform nodes that modify or process data.

### Split String List (ZeugSplitStrList)
2 widgets => 1 out
string input
delimiter input
list of strings output

### Join List Strings (ZeugJoinStrList)
1 in, widget => 1 out
list of strings input
delimiter widget input
string output

### Join Strings (ZeugJoinStr)
3 in => 1 out
string_a input
string_b input
delimiter input
string output

<!-- # Control (flow) -->

# Extra
Miscellaneous nodes that don't fit into other categories.

### Print (ZeugPrintPass)
3 in => 1 out
any input
prefix string widget input (default "")
message string widget input
any output
> Prints prefix+message to the console. pass through the input unchanged.

### Clean GPU (ZeugCleanGpuPass)
1 in => 1 out
any input
any output