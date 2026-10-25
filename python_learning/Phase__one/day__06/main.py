"""
প্রতিটা loop-এ মূলত ৪টা জিনিস থাকে:

 > Initialization: loop শুরুর আগে state তৈরি করা, যেমন i = 0
 > Condition: কখন চলবে, কখন থামবে
 > Body: প্রতি iteration-এ যে কাজ হবে
 > Update / advancement: state পরিবর্তন, যেমন i += 1

Example:
__CODE__(01):
i = 0
while i < 5:
    print(i)
    i += 1

এখানে i হলো loop-এর state। প্রতি চক্রে CPU একই instruction গুলো আবার execute করে, কিন্তু memory-তে i-র মান বদলায়। তাই loop আসলে “নতুন কিছু” না—একই code path বারবার চলে, শুধু data/state পাল্টায়।


__$__ Memory level-এ loop
এটাই সাধারণত মানুষ ভাবে না: loop variable মানে একটা memory location, যেখানে প্রতি iteration-এ নতুন মান লেখা হয়।

__CODE__(02):
for i in range(3):
    print(i)
Python 3-এ range(3) পুরো [0, 1, 2] list বানায় না। এটা শুধু start, stop, step—তিনটা সংখ্যা রাখে; প্রতি ধাপে পরের মান calculate করে। তাই range(10_000_000)-ও বড় list-এর মতো memory খায় না।


Python-এর for internally এমন কাজ করে:

__CODE__(03):
it = iter([10, 20, 30])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

মানে Python-এর for আসলে একটা iterator protocol engine: প্রথমে iter() দিয়ে iterator নেয়, তারপর বারবার next() কল করে, আর StopIteration পেলে থেমে যায়।




"""


it = iter([10, 20, 30])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break