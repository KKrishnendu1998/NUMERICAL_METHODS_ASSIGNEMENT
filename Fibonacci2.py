'''printing first 100 fibonacci numbers by importing the module
creator : Krishnendu Maji  '''
import timeit as t
import fibonacci_module as mod
mod.fibonacci(100)
print('the time taken :',t.timeit())