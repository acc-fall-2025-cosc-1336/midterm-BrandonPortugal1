def test_config():
    return True

def get_miles_per_hour(kilometers, minutes):
    """Convert kilometers and minutes to miles per hour using 0.621371 as the conversion ratio."""
    if kilometers < 0 or minutes <= 0:
        return "Invalid arguments"
    
    miles = kilometers * 0.621371
    hours = minutes / 60
    mph = miles / hours
    return mph

# Test case
def run_tests():
    result = get_miles_per_hour(32, 60)
    expected = 19.883872
    assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()

