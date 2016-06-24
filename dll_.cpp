#include <iostream>

using namespace std;

// c++ 结构体定义
struct struck_ {

    // 股票名，字符串
    char *stock_code_;

    // 开盘价
    double stock_open_;
};

// 声明为标准 C 格式导出的函数
extern "C" {

// 参数接受结构体指针
int dll_function_1(struck_ *struck_pointer_) {
    cout << struck_pointer_->stock_code_ << endl;
    cout << struck_pointer_->stock_open_ << endl;
    return 0;
}
}
