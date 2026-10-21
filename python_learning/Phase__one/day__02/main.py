"""
সহজ কথায়: type মানে data-র ধরন—এটা number কি, text কি, true/false কি। আর static vs dynamic typing মানে language সেই ধরন কখন check করে: compile/run করার আগে নাকি program চলার সময়।
Basic data types
-----------------------------------------------------
| Type           | মানে          | Example          |
| -------------- | ------------- | ---------------- |
| int            | পূর্ণসংখ্যা   | 25, -10, 0           |
| float / double | দশমিক সংখ্যা  | 19.5, -3.14       |
| str / string   | Text          | "Dhaka", "hello" |
| bool           | True বা False | true, false       |
-----------------------------------------------------

Python-এ:
age = 25            # int
price = 199.99      # float
name = "Rakib"      # str
is_active = True    # bool




C++-এ প্রায় একই, শুধু type আগে বলে দিতে হয়:
int age = 25;
double price = 199.99;
std::string name = "Rakib";
bool is_active = true;

float আর double দুটোই decimal number; double সাধারণত বেশি precision/বড় মান রাখতে পারে। তাই practical কাজে C++/Go-তে প্রায়ই double ব্যবহার হয়


Static typing
Static typing মানে variable-এর type আগেই ঠিক করা থাকে, আর compiler program চালানোর আগেই check করে। C++, Go, Java, Rust এই category-তে পড়ে।
// Go
var age int = 25
age = "twenty five"  // Error: string দেওয়া যাবে না

এখানে age একবার int হলে পরে সহজে string হতে পারবে না। ভুল থাকলে compile-এর সময়ই ধরা পড়বে।

"""