#task1
a = True
b = False
c = True

result_and = a and b  # False, since both a and b are not True


result_or = a or b   # True, since at least one (a) is True


result_not = not a   # False, since a is True

combined_result = (a and b) or not c  # False, since (a and b) is False and not c is False

print(f"AND result: {result_and}")
print(f"OR result: {result_or}")
print(f"NOT result: {result_not}")
print(f"Combined result: {combined_result}")


#task2
a = 2
b = 3
c = 4
d = 5

normal_result = a + b * c - d

parentheses_result = (a + b) * (c - d)

print(f"Result without parentheses: {normal_result}")
print(f"Result with parentheses: {parentheses_result}")

#task3
e = 2
f = 4
g = 10
h = 12
i = 6
(a + b > c) and ((d * e <= f) or (g - h != i))
