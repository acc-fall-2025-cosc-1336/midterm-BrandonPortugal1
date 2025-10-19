def test_config():
    return True

def get_bonus_pay_amount(sales):
    """Return bonus pay amount based on sales range, or 'Invalid arguments' if out of bounds."""
    if sales < 0 or sales > 1999:
        return "Invalid arguments"
    elif sales <= 499:
        return sales * 0.05
    elif sales <= 999:
        return sales * 0.06
    elif sales <= 1499:
        return sales * 0.07
    else:  # sales <= 1999
        return sales * 0.08

# Test cases
def run_tests():
    assert get_bonus_pay_amount(-1) == "Invalid arguments", "Test failed: -1"
    assert get_bonus_pay_amount(200) == 10, "Test failed: 200"
    assert get_bonus_pay_amount(600) == 36, "Test failed: 600"
    assert get_bonus_pay_amount(1000) == 70, "Test failed: 1000"
    assert get_bonus_pay_amount(1500) == 120, "Test failed: 1500"
    assert get_bonus_pay_amount(2000) == "Invalid arguments", "Test failed: 2000"
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()


