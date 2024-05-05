from polynomial import Polynomial

example1 = Polynomial([1, 2, 3])
example2 = Polynomial({0: -3, 2: 1, 5: 4})
example3 = Polynomial(1, 2, 3, 0, 0, 0, 5, 0, 0)
example4 = Polynomial([1, 2, 3, 0, 0, 0, 5])
print()
print(repr(example2))
print(repr(example4))
print()
print(f"{example1} is {"not " if example1 != example2 else ""}equal to {example2}")
print(f"{example3} is {"not " if example3 != example4 else ""}equal to {example4}")
print()
print(example1 + example2)
print(example1 + example2 + 2)
example1 += 2
print(example1)
print(-example1)
example1 -= Polynomial(0, 0, 3)
print(example1)
print(example1.degree())
print(example1 * example2)
print()
print(example2.der())
print(example2.der(2))
print(example2(1))
print(example2(2))

