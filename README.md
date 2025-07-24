# comfyui-werkzeug

comfyui-werkzeug (German for "tool") is a collection of custom nodes for ComfyUI, designed to enhance functionality and provide additional features.

<!-- internal node prefix name `Wz` -->

# Values

### Int (WzInt)
1 widget => 1 out
integer input
integer output

### Float (WzFloat)
1 widget => 1 out
float input
float output

### String (WzStr)
1 widget => 1 out
string input
string output

### Bool (WzBool)
1 widget => 1 out
boolean input
boolean output

# Conversion (between types)

### Int to String (WzIntToStr)
1 in => 1 out
integer input
string output

### String to Int (WzStrToInt)
1 in => 1 out
string input
integer output

### Float to String (WzFloatToStr)
1 in => 1 out
float input
string output

### String to Float (WzStrToFloat)
1 in => 1 out
string input
float output

### Int to WidthHeight Tuple (WzIntToWxH)
2 widgets => 1 out
width: integer
height: integer
(width,height) tuple output (custom type: WzWxH)

### WidthHeight Tuple to Int (WzWxHToInt)
1 in => 2 out
(width,height) tuple input  (custom type: WzWxH)
width integer output
height integer output

# Transform

### Split String List (WzSplitStrList)
2 widgets => 1 out
string input
delimiter input
list of strings output

### Join List Strings (WzJoinStrList)
1 in, widget => 1 out
list of strings input
delimiter widget input
string output

### Join Strings (WzJoinStr)
3 in => 1 out
string_a input
string_b input
delimiter input
string output

<!-- # Control (flow) -->

# Extra

### Clean GPU (WzCleanGpuPass)
1 in => 1 out
any input
any output