#6. সংখ্যা উল্টানো: integer-এর digit reverse করো—যেমন 4070 → 704। Negative sign কীভাবে রাখবে ঠিক করো; string conversion ছাড়া করার চেষ্টা করো।

"""
can use technique:
string reverse এর জন্য python e [::-1] use করে ও number k string e convert kore reverce kora jai.
loop ekta technique
"""

inputDigit:int = int( input( "Enter the Value: " ))
inputDigit = str(inputDigit)
degitLength = len(inputDigit)
print(degitLength)
reverce_digit = inputDigit[::-1]
print(f"after inputDigit[::-1] reverce_digit will be {reverce_digit}")

