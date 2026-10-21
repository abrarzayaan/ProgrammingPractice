"""
Why Python? (কেন এটি এত জনপ্রিয়?):
Python-এর জনপ্রিয়তার মূল দর্শন হলো: "Developer Time > Machine Time"। কম্পিউটারের প্রসেসিং পাওয়ার সস্তা, কিন্তু ইঞ্জিনিয়ারের সময় ও মেধা অত্যন্ত ব্যয়বহুল।

 > Minimalist & Human-Readable Syntax: পাইথনে বয়লারপ্লেট কোড (যেমন মেমরি ম্যানেজমেন্ট, টাইপ ডেফিনিশন, জটিল সিনট্যাক্স) লিখতে হয় না বললেই চলে। 
    অ্যালগরিদমের সিউডোকোড সরাসরি এক্সিকিউটেবল কোডে রূপান্তর করা যায়।
 > বিশাল Ecosystem & Packages (PyPI): AI/ML (PyTorch, TensorFlow), Data Science (Pandas, NumPy), Automation, Web (FastAPI, Django)—এমন কোনো ডোমেইন নেই যেখানে পাইথনের প্রোডাকশন-রেডি লাইব্রেরি নেই।
 > Glue Language: পাইথন খুব সহজে C, C++, বা Rust দিয়ে লেখা লো-লেভেল বাইনারির সাথে ইন্টারফেস করতে পারে। 
    ফলে হাই-লেভেল লজিক পাইথনে রেখে হেভি কম্পিউটেশনাল টাস্ক ব্যাকগ্রাউন্ডে C/C++ দিয়ে করানো যায়।
 > Rapid Prototyping: আইডিয়া থেকে প্রুফ-অফ-কনসেপ্ট (PoC) তৈরি করতে পাইথনে সবচেয়ে কম সময় লাগে।

Python ধীরগতির হওয়া সত্ত্বেও কেন ডেভেলপারদের প্রধান পছন্দ?
পাইথন ইন্টারপ্রেটেড এবং ডায়নামিকালি টাইপড হওয়ায় এটি স্বভাবতই C++ বা Go-এর চেয়ে ১০x থেকে ১০০x পর্যন্ত ধীরগতির। তবুও ডেভেলপার কমিউনিটি এটি বেছে নেওয়ার মূল কারণগুলো:
 - হেভি টাস্কের নিচে আসলে পাইথন চলে না:
 - I/O Bound বনাম CPU Bound রিয়্যালিটি:
 - কস্ট এফিশিয়েন্সি ও টাইম-টু-মার্কেট (TTM):



C++ / Go: compiler
C++ বা Go-তে তুমি code লেখো, তারপর compile করো। Compiler পুরো source code নিয়ে CPU-র জন্য native machine code তৈরি করে, 
যেমন Windows-এ .exe বা Linux-এ executable binary। এরপর OS সেই executable-কে load করে, আর CPU সরাসরি তার instruction execute করে।

your.cpp  →  compiler (g++/clang)  →  machine code (.exe / binary)  →  CPU

তাই C++/Go program সাধারণত দ্রুত চলে, কারণ run-time-এ বারবার translation হয় না; CPU আগে থেকে তৈরি native instruction চালায়।



Python: interpreter
Python-এ তুমি python app.py চালাও। এখানে Python interpreter (সাধারণত CPython, যেটা C দিয়ে লেখা) তোমার .py file পড়ে। CPython আসলে Python source-কে প্রথমে bytecode-এ compile করে, 
তারপর তার নিজের virtual machine/interpreter সেই bytecode এক একটা instruction করে execute করে।

app.py  →  Python interpreter  →  bytecode  →  Python VM  →  CPU instructions

সহজ করে বললে, C++-এ CPU সরাসরি তোমার compiled program চালায়। Python-এ CPU আসলে Python interpreter program চালায়; 
সেই interpreter তোমার Python code-এর instruction পড়ে এবং CPU-র জন্য কাজ করে।


__$__: File processing কীভাবে হয়?
File processing-এ পার্থক্য মূলত কে file read করে ও কে processing logic চালায়—দুই ক্ষেত্রেই শেষ পর্যন্ত OS ও CPU কাজ করে।

 > Python: open("data.txt") call করলে Python interpreter OS-এর system call ব্যবহার করে file খোলে, disk থেকে data memory-তে আনে, তারপর Python-level loop/logic চালায়।
 > C++/Go: তুমি নিজেই file open/read/write-এর API ব্যবহার করো, যেমন C++-এ fstream, Go-তে os.ReadFile। এগুলোও OS system call-এ যায়, কিন্তু compiled native code হওয়ায় processing loop অনেক দ্রুত হয়।

উদাহরণ: ১০ লাখ লাইনের CSV-তে প্রতিটা row check করতে হলে:
# Python
with open("sales.csv") as f:
    for line in f:
        if "Dhaka" in line:
            count += 1


এখানে প্রতিটা iteration-এ Python interpreter অনেক কাজ করে: object তৈরি, type check, string operation, memory management ইত্যাদি। 
C++/Go-তে একই logic compiled machine instruction হিসেবে চলে, তাই সাধারণত অনেক faster।



"""

print("Hello, world...!")