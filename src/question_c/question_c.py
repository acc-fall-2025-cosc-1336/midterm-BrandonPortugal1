def test_config():
    return True

def get_day_of_week(day):
    """Return the name of the day for numbers 1–7, or 'Invalid number' otherwise."""
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day, "Invalid number")

# Test cases
def run_tests():
    assert get_day_of_week(0) == "Invalid number", "Test failed: 0"
    assert get_day_of_week(1) == "Monday", "Test failed: 1"
    assert get_day_of_week(2) == "Tuesday", "Test failed: 2"
    assert get_day_of_week(3) == "Wednesday", "Test failed: 3"
    assert get_day_of_week(8) == "Invalid number", "Test failed: 8"
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()

