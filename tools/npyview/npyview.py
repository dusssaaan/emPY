#!/usr/bin/env /data/juraj/anaconda3/envs/geo/bin/python

"""

npy viewer 

Function:    
view 2D npy array, 3D and 4D array it can view as well, summing the first or first two indices, respectively.


Revision History:
    
09.08.2019 D. Stefanik: creating first version of script


"""
import matplotlib.pyplot as plt
import sys
import numpy as np
from matplotlib.colors import from_levels_and_colors

plt.rcParams['figure.figsize'] = 15,8




input_dir=sys.argv[1]
a=np.load(input_dir)
if len(a.shape) == 3:
   a=np.sum(a,axis=0) 
if len(a.shape) == 4:
   a=np.sum(a,axis=(0,1)) 

minimun=a.min()
maximum=a.max()   

farby=['darkblue','blue','lightskyblue','grey','lime','yellow','red','black']
levely=[0,maximum/(2**7),maximum/(2**6),maximum/(2**5),maximum/(2**4),maximum/(2**3),maximum/(2**2),maximum/2,maximum]
cmap, norm = from_levels_and_colors(levely,farby )


plt.pcolormesh(a,cmap=cmap,norm=norm)
plt.colorbar()
plt.title(' {0} : total value = {1}, min={2:.2f}, max={3:.2f}'.format(input_dir,a.sum(),minimun,maximum), size=15)
plt.show()    

