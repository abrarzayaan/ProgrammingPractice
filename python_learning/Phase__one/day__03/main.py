"""
Operators মানে value নিয়ে কাজ করার symbol—যেমন যোগ, তুলনা, শর্ত যাচাই। Type conversion/casting মানে এক type-এর value-কে অন্য type-এ বদলানো, যেমন "25" string-কে 25 int-এ নেওয়া।

1. Arithmetic operators: এগুলো দিয়ে গণিত করা হয়।
----------------------------------------------------------
| Operator | কাজ               | Example | Result       |
| -------- | ----------------- | ------- | ------------ |
| +        | যোগ               | 7 + 3   | 10           |
| -        | বিয়োগ            | 7 - 3   | 4            |
| *        | গুণ               | 7 * 3   | 21           |
| /        | ভাগ               | 7 / 2   | Python-এ 3.5 |
| //       | ভাগফলের পূর্ণ অংশ | 7 // 2  | 3            |
| %        | ভাগশেষ            | 7 % 2   | 1            |
| **       | power             | 2 ** 3  | 8            |
---------------------------------------------------------
Python-এ / সবসময় float দেয়, কিন্তু // integer division করে।


2. Comparison operators: এগুলো দুটো value তুলনা করে এবং সবসময় True বা False দেয়। 
-------------------------------------------------
| Operator | মানে            | Example | Result |
| -------- | --------------- | ------- | ------ |
| ==       | সমান কি?        | 5 == 5  | True   |
| !=       | সমান না কি?     | 5 != 3  | True   |
| >        | বড় কি?         | 5 > 3   | True   |
| <        | ছোট কি?         | 5 < 3   | False  |
| >=       | বড় বা সমান কি? | 5 >= 5  | True   |
| <=       | ছোট বা সমান কি? | 5 <= 4  | False  |
--------------------------------------------------
সাবধান: = মানে value assign করা, আর == মানে দুটো value সমান কিনা check করা।


3. Comparison operators: এগুলো দুটো value তুলনা করে এবং সবসময় True বা False দেয়।

-------------------------------------------------
| Operator | মানে            | Example | Result |
| -------- | --------------- | ------- | ------ |
| ==       | সমান কি?        | 5 == 5  | True   |
| !=       | সমান না কি?     | 5 != 3  | True   |
| >        | বড় কি?         | 5 > 3   | True   |
| <        | ছোট কি?         | 5 < 3   | False  |
| >=       | বড় বা সমান কি? | 5 >= 5  | True   |
| <=       | ছোট বা সমান কি? | 5 <= 4  | False  |
--------------------------------------------------
 - and: দুটো condition-ই True হলে result True
 - or: যেকোনো একটা True হলে result True
 - not: True-কে False এবং False-কে True করে


Type conversion: Implicit conversion হলো language নিজে থেকে convert করা; explicit conversion/casting হলো তুমি নিজে বলে দেওয়া।
Python-এ explicit conversion:
age_text = "25"
age = int(age_text)       # "25" → 25

price = float("199.99")   # "199.99" → 199.99
count = str(10)           # 10 → "10"
active = bool(1)          # 1 → True

C++-এ:
int a = 7;
double b = 2.0;

double result = static_cast<double>(a) / b;  // 3.5
int whole = static_cast<int>(3.9);           // 3

C++-এ int আর double একসাথে থাকলে compiler প্রায়ই automatic/implicit conversion করে; কিন্তু নিজে static_cast দিলে intention পরিষ্কার থাকে।









"""