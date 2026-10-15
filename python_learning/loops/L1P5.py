"""
5. Digit count ও digit sum: একটি integer-এর digit কয়টি এবং digit-গুলোর যোগফল বের করো। 
0 এবং negative number-এর ক্ষেত্রেও সঠিক output দাও।
"""

inputNumber: int = int (input("Enter the input number: "))
inputNumber = str (inputNumber)
numCount = 0
totalSum = 0

for num in inputNumber:
    totalSum = totalSum + int(num)
    numCount = numCount + 1

print(f"the count of the {inputNumber} is: {numCount}")
print(f"the sum of the {inputNumber} is: {totalSum}")


"""
$ best approch for solve this problem:

inputNumber = int(input("Enter the input number: "))

# Negative সংখ্যার জন্য abs() দিয়ে পজিটিভ করে নেওয়া হচ্ছে
n = abs(inputNumber)

numCount = 0
totalSum = 0

# 0-এর জন্য স্পেশাল কেস (কারণ 0-তে একটি ডিজিট আছে)
if n == 0:
    numCount = 1
else:
    while n > 0:
        last_digit = n % 10          # শেষ ডিজিট বের করা
        totalSum += last_digit       # যোগফলের সাথে যুক্ত করা
        numCount += 1                # ডিজিট সংখ্যা ১ বাড়ানো
        n = n // 10                  # শেষ ডিজিট বাদ দেওয়া

print(f"The count of {inputNumber} is: {numCount}")
print(f"The sum of {inputNumber} is: {totalSum}")

"""