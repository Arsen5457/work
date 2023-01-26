def smart_divide(func):
    def inner(a, b):
        print(" i am going")
        if b == 0:
            print("whoops!")
            return
        return func(a, b)
    return inner

@smart_divide
def divide (a,b):
    print(a/b)

divide(4, 5)
divide(2, 0)        