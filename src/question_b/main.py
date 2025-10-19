
from question_b import get_miles_per_hour

def main():
    print("Miles Per Hour Calculator. Type 'q' to quit.")
    while True:
        km_input = input("Enter kilometers: ")
        if km_input.lower() == 'q':
            break
        min_input = input("Enter minutes: ")
        if min_input.lower() == 'q':
            break

        try:
            kilometers = int(km_input)
            minutes = int(min_input)
        except ValueError:
            print("Please enter valid integers.")
            continue

        result = get_miles_per_hour(kilometers, minutes)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()

