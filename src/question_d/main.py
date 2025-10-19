from question_d import get_bonus_pay_amount

def main():
    print("Bonus Pay Calculator. Type 'q' to quit.")
    while True:
        user_input = input("Enter sales amount: ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        try:
            sales = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        result = get_bonus_pay_amount(sales)
        print(f"Bonus: {result}")

if __name__ == "__main__":
    main()

