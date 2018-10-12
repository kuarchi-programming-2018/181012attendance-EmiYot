# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return b
print([fib(i) for i in range(10)])
    
    
print("フィボナッチ数列の2018番目は" + str(fib(2018)) + "です")

      
        
        
        
    
    
    