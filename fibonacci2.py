'''printing first 100 fibonacci numbers by importing the module
creator : Krishnendu Maji  '''
import fibonacci_module as mod
import timeit as t
mod.fibonacci(100)
print('the time taken :',t.timeit())