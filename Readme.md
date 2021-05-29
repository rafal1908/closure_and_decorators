# python
- everything in python is object
-function in python is first class function (you can pass function as a parametr )

# Closure
- access to variables, functions, classes from different (outer) scope
// dostęp do zmiennych  spoza aktualnie używanego zasięu
- variables are stored in function object
  

## Creation
1. Need to have min 2 functions, one outer and one inner
2. Outer function should return declaration of inner function
3. Inner function have to use something from outer function (variiable, other function, class), and only this will be recorded

## Use case:
-persistance (trwałość)


### Cons
-if you not understand you can leak memory



