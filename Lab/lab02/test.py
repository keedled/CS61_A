# def make_addr(n):
#     def adder():
#         return n
#     return adder
#
# make = make_addr(3)
# print(make())
# print(make_addr(5)(5))
# print(make(6))
#
# c,d = 1,2
# ans = lambda a,b : c + d
# print(ans(6,2))

# print(lambda x: x)
# from operator import add, mul, mod
# def lambda_curry2(func):
#     """
#     # Returns a Curried version of a two-argument function FUNC.
#     # >>> from operator import add, mul, mod
#     # >>> curried_add = lambda_curry2(add)
#     # >>> add_three = curried_add(3)
#     # >>> add_three(5)
#     # 8
#     # >>> curried_mul = lambda_curry2(mul)
#     # >>> mul_5 = curried_mul(5)
#     # >>> mul_5(42)
#     # 210
#     # >>> lambda_curry2(mod)(123)(10)
#     # 3
#     """
#     "*** YOUR CODE HERE ***"
#     return lambda f:lambda x:lambda y:f(x,y)
#
#
# print(lambda_curry2(mod)(mod)(123)(10))
# def both_paths(sofar="S"):
    # """
    # >>> up, down = both_paths()
    # S
    # >>> upup, updown = up()
    # SU
    # >>> downup, downdown = down()
    # SD
    # >>> _ = upup()
    # SUU
    # """
    # "*** YOUR CODE HERE ***"
#     upsofar = sofar
#     downsofar = sofar
#
#     def up():
#         nonlocal upsofar#nonlocal 是一个关键字，用于在嵌套函数中修改位于外部函数作用域中的变量。
#         upsofar += 'U'
#         print(upsofar)
#         return up, up
#
#     def down():
#         nonlocal downsofar
#         downsofar += 'D'
#         print(downsofar)
#         return down, down
#
#     print(sofar)
#     return up, down
#
# up, down = both_paths()
# upup, updown = up()
# print(upup())
# print(updown())

#i = 1
for i in range(1,4):
    print(i)