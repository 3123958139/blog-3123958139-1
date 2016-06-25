#include <iostream>

using namespace std;

// 导入结构体定义
struct struck_import_ {
    char *stock_name_;
    char *stock_date_[];
    double stock_open_[];
    double stock_high_[];
    double stock_low_[];
    double stock_close_[];
    double stock_volume_[];
    int stock_len_;
    int ma_len_;
};

// 导出结构体定义
struct struct_export_ {
    char *stock_name_;
    double w_price_[];
    double w_price_rate_[];
    double w_price_rate_ma_[];
};

// 声明为标准 C 格式导出的函数
extern "C" {

// 传入结构体指针，传出结构体指针
struct_export_ *dll_function_1(struck_import_ *struck_import_pointer_) {

    // 打印导入的 python 结构体数据
    cout << struck_import_pointer_->stock_name_ << endl;
    cout << struck_import_pointer_->stock_date_ << endl;
    cout << struck_import_pointer_->stock_open_ << endl;
    cout << struck_import_pointer_->stock_len_ << endl;

    // 输出经过处理的 c++ 结构体指针
    struct_export_ struct_export_1;
    struct_export_1.stock_name_ = "股票名称";
    struct_export_1.w_price_ = {1, 2, 3, 4};

    struct_export_ *struct_export_pointer_;
    struct_export_pointer_ = &struct_export_1;
    return struct_export_pointer_;
}
}
