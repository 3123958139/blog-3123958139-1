#include <iostream>

using namespace std;

// c++ 结构体定义
struct struck_ {

    char *stock_name_;
    char **stock_date_;

    double stock_open_;
    double stock_high_;
    double stock_low_;
    double stock_close_;

    double stock_volume_;

    int stock_len_;
    int ma_len_;
};

// 声明为标准 C 格式导出的函数
extern "C" {

// 传入结构体指针，传出结构体指针
struck_ *dll_function_1(struck_ *struck_pointer_) {
    return struck_pointer_;
}
}
