from ctypes import *


# python 结构体定义
class py_struct_(Structure):
    _fields_ = [("stock_code_", c_char_p), ("stock_open_", c_double)]


# python 结构体实例化，初始化
py_struct_1 = py_struct_()
py_struct_1.stock_code_ = b"Hello world!"
py_struct_1.stock_open_ = 123456

# 取结构体指针
py_struct_1_pointer_ = byref(py_struct_1)

# 获取 dll 句柄
h_dll_ = CDLL(
    'C:\\Users\\Perelman\\.CLion2016.1\\system\\cmake\\generated\\blog-3123958139-1-6c04ac5e\\6c04ac5e\\Debug\\libdll_.dll')

# 打印结果
print(h_dll_.dll_function_1(py_struct_1_pointer_))
