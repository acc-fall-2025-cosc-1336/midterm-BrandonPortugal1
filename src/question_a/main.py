from question_a import is_prime

def main():
    print("Prime Checker Program. Type 'q' to quit.")
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        if not user_input.isdigit():
            print("Please enter a valid positive integer.")
            continue
        number = int(user_input)
        result = is_prime(number)
        print(f"{number} is {'a prime' if result else 'not a prime'} number.")

if __name__ == "__main__":
    main()

