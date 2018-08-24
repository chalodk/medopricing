
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import math



def precio_mueble(params, precios):
    #función para calcular precio de cada parte del mueble
    precio_final = {'tablero':0, 'union':0, 'apoyos':0}
    
    for i in params:
        precio_final[i]  = precio_final[i]+(precios[params[i]['veneer']]+precios[params[i]['width']])*params[i]['area']+precios['prmt']*params[i]['prmt']
    precio_final['final']=precio_final['tablero']+precio_final['union']
    return precio_final    


# In[21]:


