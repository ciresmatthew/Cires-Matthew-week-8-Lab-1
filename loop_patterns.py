
# Matthew Cires
# CMP 131
# Week 8 - Lab 1
# Increasing and Decreasing Patterns
# 11/06/2026

print("--------------------------------")
print("Increasing and Decreasing Patterns")
print("--------------------------------")

# Pattern A - Increasing
print()
print("Pattern A - Increasing")

for i in range(1, 11):
    for j in range(i):
        print("+", end="")
    print()

# Pattern B - Decreasing
print()
print("Pattern B - Decreasing")

for i in range(10, 0, -1):
    for j in range(i):
        print("+", end="")
    print()
