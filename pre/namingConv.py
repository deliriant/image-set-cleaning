import os

'''
## SCRIPT RUNS IN WORKING DIR

for f in os.listdir("."):
    r = f.replace(" ","") 
    if( r != f):
        os.rename(f,r)

for f in os.listdir("."):
    r = f.replace("copy","CROP")  -> replace copy with crop
    if( r != f):
        os.rename(f,r)

'''

#replace accented characters with same letter without accent in files name

from unidecode import unidecode
for f in os.listdir("."):    # in terminal: cd inside files location
    #print(f," >>> ", unidecode(f))
    os.rename(f,unidecode(f))

