"""
পাইথনে if-else বাইরে থেকে দেখতে একদম সিম্পল মনে হলেও, মেমরি, স্কোপ (Scope) এবং বাইটকোড এক্সিকিউশনের জায়গায় C++, C# বা Go-এর তুলনায় এর আচরণে বিশাল পার্থক্য রয়েছে।
আগের সব ইন্ডাস্ট্রি স্ট্যান্ডার্ড (Type Hints, PEP 8, Entry Point) মেনে প্রথমে একটি ক্লিন কোড দেখে নিই, তারপর এর মেমরি ও আর্কিটেকচারাল পার্থক্যগুলো ব্যবচ্ছেদ করা যাক।

১. Industry Standard if-else ও match-case টেমপ্লেট
পাইথনে কার্লি ব্রেস {} বা কন্ডিশনের চারপাশে প্যারেন্থেসিস () লাগে না। এখানে Indentation (৪টি স্পেস) দিয়েই কোড ব্লক নির্ধারণ করা হয়।
def evaluate_Order_status(amount: float, is_vip: bool, status_code: int) -> str:
    # ১. Chained Comparison (পাইথনের বিশেষ ফিচার: 0 < amount <= 1000)
    if amount <= 0:
        return "Invalid amount"
    elif 0 < amount <= 500 and not is_vip:
        discount: float = 0.0
    elif is_vip or amount > 500:
        discount = 0.10
    else:
        discount = 0.05

    # ২. Ternary Operator (এক লাইনে কন্ডিশনাল অ্যাসাইনমেন্ট)
    shipping_fee: float = 0.0 if is_vip else 50.0

    # ৩. Structural Pattern Matching (Python 3.10+ এর আধুনিক switch-case)
    match status_code:
        case 200 | 201:
            state: str = "Success"
        case 400:
            state = "Bad Request"
        case _:  # Default case
            state = "Unknown"

    final_payable: float = (amount - (amount * discount)) + shipping_fee
    return f"[{state}] Payable: {final_payable:.2f} BDT"


def main() -> None:
    result: str = evaluate_Order_status(amount=600.0, is_vip=False, status_code=200)
    print(result)


if __name__ == "__main__":
    main()



২. C++, Go এবং C# এর সাথে মেমরি ও লো-লেভেল পার্থক্য:
অন্যান্য ল্যাঙ্গুয়েজে কন্ডিশন চেক করা মানে সরাসরি CPU রেজিস্টারে থাকা ভ্যালুগুলোর তুলনা করা। কিন্তু পাইথনে আন্ডার দ্য হুড মেমরি লেভেলে যা ঘটে:

ক. Block Scope নেই (Function-Level Scoping ও Stack Frame)
এটি C++, C# বা Go ডেভেলপারদের জন্য সবচেয়ে বড় শক: পাইথনে if-else (এমনকি লুপেরও) নিজস্ব কোনো Block Scope নেই!
 > C++ / C# / Go তে কী হয়?
   আপনি যখন if (true) { int x = 10; } লেখেন, তখন x ভেরিয়েবলটি ওই ব্লকের লোকাল স্ট্যাক ফ্রেমে তৈরি হয় এবং } শেষ হওয়ার সাথে সাথে মেমরি থেকে ধ্বংস (pop) হয়ে যায়। 
   ব্লকের বাইরে x অ্যাক্সেস করলে কম্পাইল এরর দেয়।
 > Python-এ কী হয়?
   পাইথনে স্কোপ তৈরি হয় শুধুমাত্র Function (def), Class, বা Module লেভেলে। উপরে আমাদের কোডে elif ব্লকের ভেতরে যে discount ভেরিয়েবলটি তৈরি করা হয়েছে, 
   সেটি পুরো evaluate_order_status ফাংশনের লোকাল নেমস্পেসে (fast locals অ্যারেতে) জায়গা পায়। 
   if-else ব্লক শেষ হয়ে গেলেও ফাংশন শেষ না হওয়া পর্যন্ত ভেরিয়েবলটি মেমরিতে বেঁচে থাকে এবং ব্লকের বাইরে থেকেও অ্যাক্সেস করা যায়!

   
খ. কন্ডিশন ইভ্যালুয়েশন: Register CMP বনাম PyObject Pointer Dereferencing, 
ধরুন আপনি লিখলেন if a < b:
 > C++ / Go: কম্পাইলার সরাসরি দুটি স্ট্যাক বা রেজিস্টার ভ্যালুর মধ্যে একটি অ্যাসেম্বলি ইনস্ট্রাকশন চালায় (CMP EAX, EBX তারপর JL বা Jump if Less)। এটি করতে মাত্র ১টি CPU Cycle লাগে।
 > Python (CPython):
    1. a এবং b কোনো কাঁচা সংখ্যা নয়; এরা হিপ (Heap) মেমরিতে থাকা দুটি PyObject স্ট্রাকচারের পয়েন্টার।
    2. ইন্টারপ্রেটার প্রথমে LOAD_FAST বাইটকোড দিয়ে পয়েন্টার দুটি স্ট্যাকে আনে।
    3. এরপর COMPARE_OP অপকোড চালায়। ইন্টারপ্রেটারকে পয়েন্টার ডিরেফারেন্স করে হিপ মেমরিতে যেতে হয়, অবজেক্ট দুটির টাইপ চেক করতে হয় (ob_type), 
       তারপর ইন্টিজার অবজেক্টের ভেতরের tp_richcompare নামের C-ফাংশন পয়েন্টার কল করতে হয়।
    4. তুলনা শেষে এটি মেমরিতে থাকা সিঙ্গেলটন বুলিয়ান অবজেক্ট Py_True অথবা Py_False এর রেফারেন্স রিটার্ন করে, এবং সবশেষে POP_JUMP_IF_FALSE দিয়ে বাইটকোড জাম্প করে।

গ. == (Value Equality) বনাম is (Memory Address / Pointer Equality)
পাইথনের কন্ডিশনে দুটি অপারেটর খুব ব্যবহৃত হয় যা সরাসরি মেমরির সাথে যুক্ত:

 > a == b: এটি দুটি অবজেক্টের হিপ মেমরির ভেতরের ভ্যালু সমান কি না তা চেক করে (আন্ডার দ্য হুড __eq__() মেথড কল করে)।
 > a is b: এটি চেক করে a এবং b মেমরির একই ফিজিক্যাল অ্যাড্রেসকে (Pointer) নির্দেশ করছে কি না (অর্থাৎ id(a) == id(b))। 
    এটি সরাসরি C++ এর পয়েন্টার কম্প্যারিজনের (ptrA == ptrB) সমতুল্য এবং == এর চেয়ে অনেক দ্রুত।

Industry Rule: কখনো if x == None: লিখবেন না। সবসময় লিখবেন if x is None: বা if x is not None:। 
কারণ পাইথন মেমরিতে None (C++ এর nullptr এর মতো) একটিই সিঙ্গেলটন অবজেক্ট হিসেবে থাকে, তাই পয়েন্টার কম্প্যারিজন করাটাই স্ট্যান্ডার্ড এবং দ্রুত।










"""

def evaluate_Order_status(amount: float, is_vip: bool, status_code: int) -> str:
    # ১. Chained Comparison (পাইথনের বিশেষ ফিচার: 0 < amount <= 1000)
    if amount <= 0:
        return "Invalid amount"
    elif 0 < amount <= 500 and not is_vip:
        discount: float = 0.0
    elif is_vip or amount > 500:
        discount = 0.10
    else:
        discount = 0.05

    # ২. Ternary Operator (এক লাইনে কন্ডিশনাল অ্যাসাইনমেন্ট)
    shipping_fee: float = 0.0 if is_vip else 50.0

    # ৩. Structural Pattern Matching (Python 3.10+ এর আধুনিক switch-case)
    match status_code:
        case 200 | 201:
            state: str = "Success"
        case 400:
            state = "Bad Request"
        case _:  # Default case
            state = "Unknown"

    final_payable: float = (amount - (amount * discount)) + shipping_fee
    return f"[{state}] Payable: {final_payable:.2f} BDT"


def main() -> None:
    result: str = evaluate_Order_status(amount=600.0, is_vip=False, status_code=200)
    print(result)


if __name__ == "__main__":
    main()