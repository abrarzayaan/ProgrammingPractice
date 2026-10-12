// 2. নির্দিষ্ট ব্যবধানে সংখ্যা: start, end, step ইনপুট নিয়ে ওই range-এর সংখ্যা print করো। step শূন্য বা ভুল direction-এর হলে সেটি handle করো।

#include <iostream>
int main () {
    int start, end, step;
    std::cout << "start number: "; std::cin >> start;
    std::cout << "step number: "; std::cin >> step;
    std::cout << "end number: "; std::cin >> end;

    if(step > 0) {
        for(int i = start; i <= end; i= i + step){
            std::cout << i; std::cout <<"\n";
        }
    }
}