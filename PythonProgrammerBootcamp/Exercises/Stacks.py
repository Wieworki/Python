# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:15:20 2022

@author: Augusto
"""

class Stack():
    def __init__(self):
        self.list_stack = []
    
    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False
        
    def push(self,item):
        return self.list_stack.append(item)
    
    def pop(self):
        return self.list_stack.pop()
    
    def peek(self):
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]
        
    def __repr__(self):
        return repr(self.list_stack)
    

def balance(lista):
    if not lista:
        #Lista vacia
        return True
    
    brackets_list = {'{':'}','[':']','(':')'}
    brackets_stack = Stack()
    top_index = 0
    for index,bracket in enumerate(lista):
        if bracket in brackets_list:
            brackets_stack.push(bracket)
        else:
            top_index = index
            break
    for i in range(top_index,len(lista)):
        
        if(brackets_stack.is_empty()):
            ##Si llegamos al final de la pila pero quedan brackets en la lista
            return False
        
        bracket_left = brackets_stack.peek()
        if(brackets_list[bracket_left] == lista[i]):
            brackets_stack.pop()
        else:
            return False
    return True

x = balance(['[','(',')',']'])
print(x)
