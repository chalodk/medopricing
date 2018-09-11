
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import math


def precio_mueble(params, precios):
    
    precio_final = dict()
    final = 0
    parts = list(params)
   
    for i in parts:
        
        aux = 0
        vn = params[i]['veneer']
        gr = params[i]['thickness']
        
        if gr >= 30:
        
            gr = 'tmm'
        
        elif gr < 30 and gr >=18:
        
            gr = 'dmm'
        
        else:
        
            gr = 'qmm'
        
        keys = list(params[i])
        
        for k in keys:
            
            
            if k == 'area':
                aux = aux + params[i][k]*(precios[vn]+precios[gr])
                    
            elif k == 'perimeter':
                aux = aux + params[i][k]*precios['prmtr']

            else:
                pass
            precio_final[i] = aux
        final = final+precio_final[i]
    final_p = {'final':final}
                
    return final_p



