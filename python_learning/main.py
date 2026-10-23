def greet_function(name: str) -> str:
    name: str = name 
    return f"Good Morning, {name} sir, hope ur day going great...!!!"

def main():
    print(greet_function("abrar"))

if __name__ == '__main__':
    main()