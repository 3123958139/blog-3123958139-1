#include <iostream>

using namespace std;

// c++ 结构体定义
struct cpp_struck_ {

    // 股票代码，字符串
    char *stock_name_;

    // 日期，字符串数组
    char *stock_date_[];

    // 开高低收四组价格，浮点型数组
    double stock_open_[];
    double stock_high_[];
    double stock_low_[];
    double stock_close_[];

    // 成交量，浮点型数组
    double stock_volume_[];

    // 长度，整型
    int stock_len_;
    int ma_len_;
};

// 声明为标准 C 格式导出的函数
extern "C" {

// 传入结构体指针，传出结构体指针
cpp_struck_ *dll_function_1(cpp_struck_ *py_struck_pointer_) {
    /*
     * 数据处理部分...
     *
     *
     *
     */
    cpp_struck_ *cpp_struck_pointer_;
    cpp_struck_pointer_ = py_struck_pointer_;
    return cpp_struck_pointer_;
}
}
