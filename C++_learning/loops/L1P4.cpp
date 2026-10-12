// 4. Multiplication table: একটি সংখ্যা N এবং limit L নিয়ে N × 1 থেকে N × L পর্যন্ত print করো। L positive কি না যাচাই করো।
#include <iostream>
using namespace std;
int main () {
    int n, limit;
    cout << "Enter the value of N: "; cin >> n;
    cout << "Enter the value of Limit: "; cin >> limit;

    for(int i = 1; i <=limit; i++){
        int returnValue = 0;
        returnValue = n*i;
        cout <<n <<" * " <<i <<" = " <<returnValue; cout<<"\n";
    }
    return 0;
}