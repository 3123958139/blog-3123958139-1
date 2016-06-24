### dll_.cpp
    1. dll_function_1
        * 定义 c++ 结构体
        * 参数为结构体指针
        * 结果输出到 csv 文件

### test_dll_.py
    1. 定义一个与 dll 相对应的 python 结构体
        * class xxx(Structure):
              _fields_ = [("aaa", c_bbb), ("", )]

    2. 结构体实例化，初始化
        * 结构体实例化：yyy = xxx()
        * 指针数组：string_array_ = c_char_p * 10
                   zzz = string_array_()
                   zzz[0] = "abcdef"
        * 字符串赋值要加 b：b"Hello world!"

    3. 取结构体实例指针
        * POINTER 或者 byref