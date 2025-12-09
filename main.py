# 11
import math
nums = [4, 9, 16, 25]
roots = [math.sqrt(x) for x in nums]
print(roots)

# 12
divisible_by_5 = [x for x in range(51) if x % 5 == 0]
print(divisible_by_5)

# 13
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)

# 14
vehicles = ["car", "bike", "bus"]
reversed_words = [word[::-1] for word in vehicles]
print(reversed_words)

# 15
nums = [1, 2, 3, 4]
doubled = [x * 2 for x in nums]
print(doubled)
