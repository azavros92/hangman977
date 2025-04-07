# main.py

# Importing function_1 and function_2 from module_1
from module_1 import function_1 as function_1_module_1, function_2

# Importing function_1 from module_2
from module_2 import function_1 as function_1_module_2

# Call functions from module_1
function_1_module_1()  # Should print: "This is function 1 in module 1"
function_2()           # Should print: "This is function 2 in module 1"

# Call function from module_2
function_1_module_2()  # Should print: "This is function 1 in module 2"