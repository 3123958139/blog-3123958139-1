import tushare
from ctypes import *

# 下载测试数据
sh_data_frame_ = tushare.get_hist_data('sh')
stock_name_ = 'sh'
stock_date_ = sh_data_frame_.index.values
stock_open_ = sh_data_frame_['open'].values
stock_high_ = sh_data_frame_['high'].values
stock_low_ = sh_data_frame_['low'].values
stock_close_ = sh_data_frame_['close'].values
stock_volume_ = sh_data_frame_['volume'].values
stock_len_ = len(sh_data_frame_)
ma_len_ = 2

# 打印旧数据作为比较
print("old_date_ = ", stock_date_)
print("old_open_ = ", stock_open_)

# python 结构体定义
class py_struct_(Structure):
    _fields_ = [("stock_name_", c_wchar_p),

                # 注意字符串格式要用 c_wchar_p 而不是 c_char_p
                ("stock_date_", c_wchar_p * stock_len_),
                ("stock_open_", c_double * stock_len_),
                ("stock_high_", c_double * stock_len_),
                ("stock_low_", c_double * stock_len_),
                ("stock_close_", c_double * stock_len_),
                ("stock_volume_", c_double * stock_len_),
                ("stock_len_", c_int),
                ("ma_len_", c_int)]


# python 结构体实例化，初始化
py_struct_1 = py_struct_()
py_struct_1.stock_name_ = stock_name_
py_struct_1.stock_date_ = (c_wchar_p * stock_len_)(*stock_date_)
py_struct_1.stock_open_ = (c_double * stock_len_)(*stock_open_)

# 传入指针实例
py_struct_1_pointer_ = byref(py_struct_1)

# 获取 dll 句柄
h_dll_ = CDLL(
    'C:\\Users\\Perelman\\.CLion2016.1\\system\\cmake\\generated\\blog-3123958139-1-6c04ac5e\\6c04ac5e\\Debug\\libdll_.dll')

# 定义 dll 返回值类型为 python 结构体指针
h_dll_.dll_function_1.restype = POINTER(py_struct_)

# 返回 dll 结构体指针
cpp_struct_pointer_ = h_dll_.dll_function_1(py_struct_1_pointer_)

# 结构体指针取内容
cpp_struct_contents_ = cpp_struct_pointer_.contents

# 保存结果为 python list 格式
new_date_ = []
for value in cpp_struct_contents_.stock_date_:
    new_date_.append(value)
print("new_date_ = ", new_date_)

# 保存结果为 python list 格式
new_open_ = []
for value in cpp_struct_contents_.stock_open_:
    new_open_.append(value)
print("new_open_ = ", new_open_)
