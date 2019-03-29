def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_args(1, "two", 3)
print("__________")


test_var_args(1, "another one")
print("__________")

test_var_args(False, 4.55)
print("__________")

def multiply(*args):
    ans = 1
    for num in args:
        ans *= num
    print(ans)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)
