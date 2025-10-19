
from question_c import get_day_of_week

def main():
    print("Day of the Week Program. Type 'q' to quit.")
    while True:
        user_input = input("Enter a number (1–7): ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        day_number = int(user_input)
        result = get_day_of_week(day_number)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()

