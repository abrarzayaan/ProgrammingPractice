// 3. Even/odd count: 1 থেকে N পর্যন্ত কয়টি even এবং কয়টি odd সংখ্যা আছে তা বের করো; দুই ধরনের সংখ্যার যোগফল N-এর সমান কি না যাচাই করো।
#include <iostream>
int main() {
    int N;
    std::cout << "Enter the number N: "; std::cin >> N;

    for (int i = 1; i <=N; i++){
        if (i % 2 == 0){
            std::cout <<i <<": is: " << "Odd\n";
        }
        else{
            std::cout <<i <<": is: " << "Even\n";
        }
    }
}