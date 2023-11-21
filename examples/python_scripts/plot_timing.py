import matplotlib.pyplot as plt
import numpy as np

n_part = [10,100,1000,10000]
python_timestep = np.zeros(len(n_part))
python_timestep[0] = 1.643
python_timestep[1] = 27.417
python_timestep[2] = 1*60 + 31.322 
python_timestep[3] = 2*60 + 12.00
python_to_fortran = np.zeros(len(n_part))
python_to_fortran[0] = 1.872
python_to_fortran[1] = 27.417 
python_to_fortran[2] = 1*60 + 31.322
python_to_fortran[3] = 2*60 + 12.00
fortran = np.zeros(len(n_part)) 
fortran[0] = 1.01 
fortran[1] = 26.0 
fortran[2] = 1*60 + 24.448
fortran[3] = 2*60 + 13.688 

plt.plot(n_part, python_timestep,label='python')
plt.plot(n_part, python_to_fortran,label='python to fortran')
plt.plot(n_part, fortran, label='fortran')

plt.xlabel('Computational particles')
plt.ylabel('Wall clock time (s)')
plt.xscale('log')
plt.legend()
plt.grid()

plt.savefig('timing.pdf')
