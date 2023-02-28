# -*- coding: utf-8 -*-
import time
import os

import tensorflow as tf
from numba import vectorize, float64, int32, int64, float32, njit,jit,cuda
# from numba import jit
import numpy as np
# from numba import cuda
# to measure exec time
from timeit import default_timer as timer
import random
# print(tf.version.VERSION)
test = tf.config.list_physical_devices()
tf.config.list_physical_devices('GPU')

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')),'\nDevice: ', tf.config.list_physical_devices('GPU'))
# print(test)

@cuda.jit
def teste_a():
    op = [s for s in range(0,1000000)]
    y1 = 0
    acc= 0
    for s in op:
        y1 += s
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
        if s % 100000==0:
            print(s)
    return y1

@njit
def teste_b():
    op = [s for s in range(0,1000000)]
    z = 0
    acc = 0
    for s in op:
        z += s
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
        if s % 100000==0:
            print(s)
    return z

@njit(fastmath=True)
def teste_c():
    op = [s for s in range(0,1000000)]
    f = 0
    acc = 0
    for s in op:
        f += s
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
        if s % 100000==0:
            print(s)
    return f

@jit(nopython=True)
def teste_d():
    op = [s for s in range(0,1000000)]
    e = 0
    acc = 0
    for s in op:
        e += s
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
        if s % 100000==0:
            print(s)
    return e
inicio = time.time()
print('resultado a: ',teste_a())
print('1: ',time.time() - inicio)
print('----------------')
inicio = time.time()
print('resultado b',teste_b())
print('2: ',time.time() - inicio)
print('----------------')
inicio = time.time()
print('resultado c: ',teste_c())
print('3: ',time.time() - inicio)
print('----------------')
inicio = time.time()
print('resultado d: ',teste_d())
print('4: ',time.time() - inicio)
print('----------------')
# with tf.device('/device:GPU:0'):
#     inicio = time.time()
#     teste()
#     print('3: ',time.time() - inicio)


  
# # normal function to run on cpu
# def ident_npa(x):
#     return np.cos(x) ** 2 + np.sin(x) ** 2
  
# function optimized to run on gpu
# @vectorize([float64(float64)])
# def func2(x):
#     for i in range(10000000):
#         x[i]+= 1

# @njit
# def ident_npb(x):
#     return np.cos(x) ** 2 + np.sin(x) ** 2

# if __name__=="__main__":
#     n = 10000000                            
#     a = np.ones(n, dtype = np.float64)
#     b = np.ones(n, dtype = np.float32)
      
#     start = timer()
#     ident_npa(a)
#     print("without GPU:", timer()-start)    
      
#     start = timer()
#     ident_npb(a)
#     print("with GPU:", timer()-start)

# print(tf.device('/device'))

# Duas dúvidas

# def atualizar_pacotes():
#     import pkg_resources
#     from subprocess import call
    
#     for dist in pkg_resources.working_set:
#         # pacote= dist.split(' ')
#         print(dist.__dict__['project_name'])
    
#         call("python -m pip install --upgrade " + dist.__dict__['project_name'], shell=True)
#         print('----')