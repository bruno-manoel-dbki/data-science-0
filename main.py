#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[20]:



#black_friday.head()


# In[100]:


#bf_g = black_friday.groupby("Age")


#for gender, dt in bf_g:
#    print(gender)
#    print(dt.count())
#    print()

#3

#black_friday["User_ID"].value_counts().count().item()


#5
#type((black_friday.isnull().sum().sort_values()[-1]/black_friday.shape[0]).item())

#6
#a = black_friday.Product_Category_3
#a.values_count()

#7

#bf = black_friday.Product_Category_3.dropna()
#bf.value_counts().index[0].item()

#8
#bf = black_friday.Purchase
#bf_n = (bf-bf.min())/(bf.max()-bf.min())
#bf_n = (bf-bf.mean())/bf.std()


#9
#bf = black_friday.Purchase
#bf_n = (bf-bf.mean())/bf.std()
#((bf_n<1)&(bf_n>-1)).value_counts()[1]


#10
bf_2 = black_friday.Product_Category_2
bf_3 = black_friday.Product_Category_3
type((bf_2.isna() & bf_3.isna()).all().item())
    


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    bf_a = black_friday[black_friday.Age == "26-35"]
    bf = bf_a[bf_a.Gender == "F"]
    return bf.shape[0]
    # Retorne aqui o resultado da questão 2.
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    return black_friday["User_ID"].value_counts().count().item()
    # Retorne aqui o resultado da questão 3.
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    return black_friday.dtypes.value_counts().count().item()
    # Retorne aqui o resultado da questão 4.
    pass


# ## Questão 5
# 
# Qual porcentagem das colunas possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[124]:


def q5():
    return ((black_friday.isnull().sum().sort_values()[-1]/black_friday.shape[0]).item())
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[138]:


def q6():
    return black_friday.isnull().sum().sort_values()[-1].item()
    # Retorne aqui o resultado da questão 6.
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    bf = black_friday.Product_Category_3.dropna()
    return bf.value_counts().index[0].item()
    # Retorne aqui o resultado da questão 7.
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    bf = black_friday.Purchase
    bf_n = (bf-bf.min())/(bf.max()-bf.min())
    return bf_n.mean()
    # Retorne aqui o resultado da questão 8.
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    bf = black_friday.Purchase
    bf_n = (bf-bf.mean())/bf.std()
    return ((bf_n<1)&(bf_n>-1)).value_counts()[1]
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[96]:


def q10():
    bf_2 = black_friday.Product_Category_2
    bf_3 = black_friday.Product_Category_3
    return False

    pass

