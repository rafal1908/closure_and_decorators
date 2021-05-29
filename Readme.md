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

## Main rules:
-DRY - don't repeat yourself
-KISS - keep it simple

# Decorator
-add additional functionality to function (augmented function)
- 3 types of decorators
    1. function decorator
        - need to use closure for creating
    2. class decorator
    3. decorator as a design patter
        -different from python decorator functionality