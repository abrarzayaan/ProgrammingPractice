#include <iostream>

int addition(int val01, int val02) {
    int result = val01 + val02;
    return result;
}

int main() {
    std::cout << addition(1,2) << std::endl;
    std::cout << addition(7,4)<< std::endl;
    return 0;
}