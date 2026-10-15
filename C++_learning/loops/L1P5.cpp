/*
5. Digit count ও digit sum: একটি integer-এর digit কয়টি এবং digit-গুলোর যোগফল বের করো। 
0 এবং negative number-এর ক্ষেত্রেও সঠিক output দাও।
*/

#include <iostream>
#include <cmath> // std::abs() এর জন্য

int main() {
    long long inputNumber;
    std::cout << "Enter the input number: ";
    std::cin >> inputNumber;

    // Negative সংখ্যার জন্য std::abs() দিয়ে পজিটিভ করে নেওয়া হচ্ছে
    long long n = std::abs(inputNumber);

    int numCount = 0;
    int totalSum = 0;

    // 0-এর জন্য স্পেশাল কেস (কারণ 0-তে একটি ডিজিট আছে)
    if (n == 0) {
        numCount = 1;
    } else {
        while (n > 0) {
            int last_digit = n % 10;     // শেষ ডিজিট বের করা
            totalSum += last_digit;      // যোগফলের সাথে যুক্ত করা
            numCount += 1;               // ডিজিট সংখ্যা ১ বাড়ানো
            n = n / 10;                  // শেষ ডিজিট বাদ দেওয়া (C++ এ পূর্ণসংখ্যার ভাগ অটোমেটিক ফ্লোর ডিভিশন করে)
        }
    }

    std::cout << "The count of " << inputNumber << " is: " << numCount << "\n";
    std::cout << "The sum of " << inputNumber << " is: " << totalSum << "\n";

    return 0;
}