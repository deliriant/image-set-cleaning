import os
'''
#path = '/Users/muhannad/University/Masters-3rd/AdvMachineLearning/project/subset512'

## SCRIPT RUNS IN WORKING DIR

for f in os.listdir("."):
    r = f.replace(" ","")
    if( r != f):
        os.rename(f,r)


for f in os.listdir("."):
    r = f.replace("copy","CROP")
    if( r != f):
        os.rename(f,r)

#######################

# i448hq to Kalotaszeg

for f in os.listdir("."):
    r = f.replace("i448hq","Kalotaszeg")
    if( r != f):
        os.rename(f,r)


# i450hq to Kalotaszeg'''

for f in os.listdir("./"):
    r = f.replace("_titles","0_titles")
    if( r != f):
        os.rename(f,r)

