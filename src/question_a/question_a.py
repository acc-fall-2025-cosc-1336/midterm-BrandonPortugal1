def test_config():
    return True

def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
def run_tests():
    assert is_prime(4) == False, "Test failed: 4 is not prime"
    assert is_prime(5) == True, "Test failed: 5 is prime"
    assert is_prime(11) == True, "Test failed: 11 is prime"
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()

