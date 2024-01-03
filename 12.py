class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for num in range(0, self.n + 1):
            if num % 7 == 0:
                yield num

# Example usage:
n = 50
generator_instance = DivisibleBySevenGenerator(n)

# Iterate over numbers divisible by 7
for num in generator_instance.generate_divisible_by_seven():
    print(num)
