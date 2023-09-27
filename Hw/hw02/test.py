from operator import add, mul, sub
def zero(f):
    return lambda x: x
def add_1(x):
    return x + 1
def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"#按照推断，successor(zero) = lambda f : lambda x : f(zero(f)(x))，
                            #又因为zero(f)(x) = x,所以有以下结果。
    return lambda x : f(x)

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x : f(f(x))
three = successor(two)


print(two(add_1)(100))