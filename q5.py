import random
import statistics
numbers = [random.randint(1, 10) for _ in range(25)]
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
mode_value = statistics.mode(numbers)
print("Random numbers:", numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)