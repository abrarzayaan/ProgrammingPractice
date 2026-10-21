"""
পাইথনে if-else বাইরে থেকে দেখতে একদম সিম্পল মনে হলেও, মেমরি, স্কোপ (Scope) এবং বাইটকোড এক্সিকিউশনের জায়গায় C++, C# বা Go-এর তুলনায় এর আচরণে বিশাল পার্থক্য রয়েছে।
আগের সব ইন্ডাস্ট্রি স্ট্যান্ডার্ড (Type Hints, PEP 8, Entry Point) মেনে প্রথমে একটি ক্লিন কোড দেখে নিই, তারপর এর মেমরি ও আর্কিটেকচারাল পার্থক্যগুলো ব্যবচ্ছেদ করা যাক।

১. Industry Standard if-else ও match-case টেমপ্লেট
পাইথনে কার্লি ব্রেস {} বা কন্ডিশনের চারপাশে প্যারেন্থেসিস () লাগে না। এখানে Indentation (৪টি স্পেস) দিয়েই কোড ব্লক নির্ধারণ করা হয়।
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