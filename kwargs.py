def print_kwargs(**kwargs):
        print(kwargs)

print_kwargs(kwargs_1="Sim", kwargs_2=4.5, kwargs_3=True)
print_kwargs()

"""
Below will generate error 
# TypeError: print_kwargs() takes exactly 0 arguments (1 given)
"""
#print_kwargs("Sim")

myargs = {"arg3": 3, "arg2": "two"}

print_kwargs(**myargs)
