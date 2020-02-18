def bumpUp(lg):
    if lg == "c":
        lg = "b"
        return lg
    elif lg == "b":
        lg = "a"
        return lg
    else:
        lg = "a+"
        return lg

print(bumpUp("c"))
print(bumpUp("b"))
print(bumpUp("a"))
