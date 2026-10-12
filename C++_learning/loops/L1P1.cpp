// 1. ১ থেকে N পর্যন্ত যোগফল: একটি positive integer N নিয়ে 1 + 2 + ... + N বের করো। N <= 0 হলে error দেখাও।

#include <iostream>
int main () {
    int n;
    std::cout << "Enter the number N: "; std::cin >> n;

    if(n >= 0){
        int sum = 0;
        for(int i = 1; i <= n; i++){
            sum = sum + i;
        }
        std::cout << sum <<"\n";
    }
    else{
        std::cout << "Please Enter a Positive Number...";
    }

    return 0;
}