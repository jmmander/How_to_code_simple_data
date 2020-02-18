def teenager(age):
    if 12 < age < 20:
        return "teen"
    else:
        return "not teen"

print(teenager(10))
print(teenager(12))
print(teenager(16))
print(teenager(121))

def monthsold(age):
    months = age * 12
    return months

print(monthsold(12))