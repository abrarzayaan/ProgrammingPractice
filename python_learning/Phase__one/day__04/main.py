"""
পাইথনে সরাসরি কোড লেখা শুরু করার আগে ইন্ডাস্ট্রি স্ট্যান্ডার্ড এবং এর আন্ডার-দ্য-হুড মেকানিজম বুঝে নেওয়াটা দারুণ সিদ্ধান্ত। 
বিশেষ করে আপনি যখন C++, Go বা C# এর মতো স্ট্যাটিকালি টাইপড ভাষার সাথে তুলনা করছেন, তখন পাইথনের Type System এবং I/O (Input/Output) কীভাবে কাজ করে তা পরিষ্কার হওয়া দরকার।



১. পাইথনে কি সবসময় Type উল্লেখ করে কোড লেখা উচিত? (Type Hints)

সংক্ষিপ্ত উত্তর: হ্যাঁ, আধুনিক ইন্ডাস্ট্রিতে (Production-level code) সবসময় Type Hints ব্যবহার করা স্ট্যান্ডার্ড প্র্যাকটিস। 
কেবলমাত্র ছোটখাটো ৫-১০ লাইনের ওয়ান-টাইম অটোমেশন স্ক্রিপ্ট ছাড়া সব জায়গাতেই এখন টাইপ মেনশন করা হয়।

তবে C++ / C# / Go এর সাথে পাইথনের টাইপিংয়ের মৌলিক পার্থক্য কোথায়?
C++ বা Go-তে আপনি যখন int x = 10; লেখেন, কম্পাইলার তখন মেমরিতে ঠিক ৪ বাইট বা ৮ বাইট জায়গা বরাদ্দ করে এবং অন্য কোনো টাইপ অ্যাসাইন করলে কম্পাইল টাইমেই আটকে দেয়।

পাইথনে বিষয়টি সম্পূর্ণ আলাদা:

 > Runtime-এ Type Hint-এর কোনো ভ্যালু নেই: আপনি পাইথনে x: int = 10 লিখুন বা x = 10 লিখুন—পাইথন ইন্টারপ্রেটার (CPython) রানটাইমে এই : int অংশটুকু পুরোপুরি ইগনোর করে। 
    এটি কোডের স্পিড বাড়ায় না বা মেমরিও কম নেয় না (আন্ডার দ্য হুড এটি সেই ২৮ বাইটের PyObject-ই তৈরি করে)।
 > তাহলে কেন ব্যবহার করা হয়?
    - Static Analysis (IDE & Linter): VS Code (Pylance) বা mypy / pyright এর মতো স্ট্যাটিক টাইপ চেকার টুলগুলো কোড রান করার আগেই (Compile-time এর মতো) আপনার টাইপ মিসম্যাচ বাগ ধরে ফেলে।
    - Code Readability & Architecture: বড় কোডবেসে একটি ফাংশন কী রিসিভ করছে এবং কী রিটার্ন করছে, তা ফাংশনের ভেতরে না ঢুকে দেখেই বোঝা যায়।
    - Modern Frameworks: আধুনিক ফ্রেমওয়ার্কগুলো (যেমন FastAPI, Pydantic) এই Type Hints রিড করে স্বয়ংক্রিয়ভাবে ডাটা ভ্যালিডেশন, সিরিয়ালাইজেশন এবং API ডকুমেন্টেশন তৈরি করে ফেলে।

# Bad Practice (স্ক্রিপ্টিং লেভেল)
def calculate_discount(price, discount):
    return price - (price * discount)

# Industry Standard (Production লেভেল)
def calculate_discount(price: float, discount: float) -> float:
    return price - (price * discount)



    


২. Python Input এবং Output (I/O): বেসিক থেকে ইন্ডাস্ট্রি স্ট্যান্ডার্ড

ক. Standard Output (আউটপুট দেখানো)
পাইথনে আউটপুটের জন্য print() ফাংশন ব্যবহার করা হয়। কিন্তু ভেরিয়েবল প্রিন্ট করার ক্ষেত্রে ইন্ডাস্ট্রিতে শুধুমাত্র f-strings (Formatted String Literals) ব্যবহার করা হয়। 
এটি শুধু পড়তেই সুন্দর নয়, বাইটকোড লেভেলে + বা .format() এর চেয়ে দ্রুত কাজ করে (কারণ এটি BUILD_STRING অপকোড ব্যবহার করে)।

name: str = "Abrar"
score: int = 95

# 1. পুরনো বা ধীরগতির পদ্ধতি (এড়িয়ে চলুন)
print("User " + name + " scored " + str(score))
print("User {} scored {}".format(name, score))

# 2. Industry Standard (f-string)
print(f"User {name} scored {score}")

# এক্সপ্রেশন বা ফরম্যাটিং সরাসরি ভেতরেই করা যায়:
pi: float = 3.14159265
print(f"Pi value up to 2 decimal: {pi:.2f}") # Output: 3.14

print() এর দুটি গুরুত্বপূর্ণ প্যারামিটার:
C++ এ যেমন cout বাটনে অটোমেটিক নতুন লাইন তৈরি করে না (\n দিতে হয়), পাইথনের print() ডিফল্টভাবে শেষে একটি নিউলাইন (\n) যোগ করে দেয়। এটি কন্ট্রোল করা যায় end এবং sep দিয়ে:
# নতুন লাইন না চেয়ে স্পেস চাইলে:

print("Hello", end=" ")
print("World") # Output: Hello World

# একাধিক ভ্যালুর মাঝখানে কাস্টম সেপারেটর:
print("2026", "10", "21", sep="-") # Output: 2026-10-21




খ. Standard Input (ইনপুট নেওয়া)

পাইথনে input() ফাংশন কনসোল বা টার্মিনাল থেকে সম্পূর্ণ একটি লাইন রিড করে এবং সবসময় str (String) হিসেবে রিটার্ন করে।

C++ এ যেমন cin >> x লিখলে ভেরিয়েবলের টাইপ অনুযায়ী বাফার থেকে অটোমেটিক পার্স করে নেয়, পাইথনে তা হয় না। আপনাকে এক্সপ্লিসিটলি Type Casting করতে হবে।
# 1. সাধারণ String ইনপুট
username: str = input("Enter your name: ")

# 2. সংখ্যা (int/float) ইনপুট নেওয়া (Explicit Type Casting)
age: int = int(input("Enter your age: "))
height: float = float(input("Enter height in feet: "))

# 3. এক লাইনে একাধিক ইনপুট নেওয়া (যেমন: 10 20) - Problem Solving / CLI Standard
# input().split() স্ট্রিংটিকে স্পেস অনুযায়ী ভেঙে লিস্ট তৈরি করে, map() সেগুলোকে int এ রূপান্তর করে
a: int
b: int
a, b = map(int, input("Enter two numbers separated by space: ").split())
print(f"Sum is: {a + b}")


গ. Fast I/O এবং Production Reality
আপনি যখন প্রবলেম সলভিং (যেমন HackerRank/Codeforces) বা প্রোডাকশন ব্যাকএন্ডে কাজ করবেন, তখন সাধারণ input() এবং print() এর বাইরে কিছু বিষয় মাথায় রাখতে হয়:
 1. Fast I/O (বড় ডাটা সেট বা কম্পিটিটিভ প্রোগ্রামিংয়ের জন্য):

    পাইথনের input() ফাংশনটি বেশ ধীরগতির কারণ এটি প্রতিবার প্রম্পট চেক করে এবং নিউলাইন স্ট্রিপ করে। 
    লাখ লাখ লাইনের ইনপুট রিড করতে হলে sys.stdin.readline ব্যবহার করা হয় (অনেকটা C++ এর ios_base::sync_with_stdio(false); এর মতো)।
    import sys

    # অনেক দ্রুত ইনপুট নেওয়ার জন্য
    fast_input: str = sys.stdin.readline().strip()

    # দ্রুত আউটপুটের জন্য
    sys.stdout.write(f"{fast_input}\n")


 2. Production Code-এ print() ও input() থাকে না:

    রিয়েল-ওয়ার্ল্ড সফটওয়্যার বা মাইক্রোসার্ভিসে কেউ টার্মিনালে বসে input() দেয় না; তখন ইনপুট আসে API Request, CLI Arguments (argparse), বা Environment Variables থেকে। 
    আর প্রোডাকশনে কখনোই print() ব্যবহার করা হয় না, তার বদলে স্ট্যান্ডার্ড logging মডিউল ব্যবহার করা হয় (যাতে টাইমস্ট্যাম্প, লগ লেভেল যেমন INFO, ERROR ইত্যাদি ট্র্যাক করা যায়)।


    

৩. প্রফেশনাল পাইথন কোড লেখার Best Practices (চেকলিস্ট)

    C++, C# বা Go থেকে আসার সময় পাইথনে নিচের স্ট্যান্ডার্ডগুলো শুরু থেকেই অভ্যাস করলে আপনার কোড একদম সিনিয়র ইঞ্জিনিয়ারদের মতো ক্লিন হবে:
    ১. Naming Convention (PEP 8):
        - Variables & Functions: snake_case (যেমন: user_age, calculate_total_price()) — C# বা Go এর মতো camelCase বা PascalCase ফাংশনে ব্যবহার করবেন না।
        - Classes: PascalCase (যেমন: PaymentProcessor)।
        - Constants: UPPER_SNAKE_CASE (যেমন: MAX_RETRY_LIMIT: int = 5)।

    ২. Entry Point Guard (if __name__ == "__main__":):
        C++ বা C# এ যেমন main() ফাংশন ছাড়া কোড চলে না, পাইথন উপর থেকে নিচ পর্যন্ত লাইন বাই লাইন এক্সিকিউট করে। 
        কিন্তু প্রফেশনাল কোডে সবসময় একটি main() ফাংশন তৈরি করে নিচের গার্ডটি ব্যবহার করবেন। এতে আপনার ফাইলটি অন্য কোনো ফাইলে import করলে অযথা কোড রান হয়ে যাবে না।

    ৩. Error Handling ইনপুট নেওয়ার সময়:
        ইউজার ইন্টিজারের জায়গায় টেক্সট ইনপুট দিলে int() ফাংশন সাথে সাথে ValueError থ্রো করে প্রোগ্রাম ক্র্যাশ করাবে। তাই কাস্টিংয়ের সময় try-except ব্লক ব্যবহার করা নিরাপদ।

    সবগুলো নিয়ম মেনে একটি আদর্শ (Production-Style) পাইথন কোড টেমপ্লেট:

"""

import sys


def get_user_data() -> tuple[str, int]:
    """Reads user name and age from standard input safely."""
    name: str = input("Enter your name: ").strip()
    
    try:
        age: int = int(input("Enter your age: ").strip())
    except ValueError:
        print("Error: Age must be a valid integer.", file=sys.stderr)
        sys.exit(1)
        
    return name, age


def main() -> None:
    user_name: str
    user_age: int
    
    user_name, user_age = get_user_data()
    print(f"Welcome {user_name}! Next year you will be {user_age + 1}.")


if __name__ == "__main__":
    main()
