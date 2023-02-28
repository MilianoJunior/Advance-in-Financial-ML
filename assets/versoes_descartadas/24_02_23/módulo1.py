# -*- coding: utf-8 -*-
import time
import os

import tensorflow as tf



def teste():
    op = [s for s in range(0,1000000)]
    for s in op:
        if s % 100000==0:
            print(s)
inicio = time.time()
teste()
print('1: ',time.time() - inicio)
with tf.device('/device:GPU:0'):
    inicio = time.time()
    teste()
    print('2: ',time.time() - inicio)

# for s in dir(tf):
#     print(s)

# print(tf.device('/device'))

# Duas dúvidas

def atualizar_pacotes():
    import pkg_resources
    from subprocess import call
    
    for dist in pkg_resources.working_set:
        # pacote= dist.split(' ')
        print(dist.__dict__['project_name'])
    
        call("python -m pip install --upgrade " + dist.__dict__['project_name'], shell=True)
        print('----')
