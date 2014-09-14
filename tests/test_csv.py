
# coding: utf-8

# In[1]:

from pipeline import pipeline


# In[3]:

s = pipeline.Pipeline("sreeraj")


# In[15]:

import csv


# In[16]:

c = csv.DictReader(open("/Users/sreeraj.a/qualfile.csv"))


# In[5]:

def testFun(csvObj):
    ret_obj = {}
    for key in csvObj:
        ret_obj[key] = str(csvObj[key]) + ' sreeraj'
    return ret_obj


# In[6]:

rowP = pipeline.RowPhase(testFun)


# In[7]:

p = pipeline.Pipeline('testPipeline', [rowP])


# In[8]:

def printObj(o):
    print o
    return o


# In[10]:

printP = pipeline.RowPhase(printObj, name="printObject")


# In[11]:

p.add_phase(printP)


# In[17]:

p.run(c)

