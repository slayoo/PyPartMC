import matplotlib.pyplot as plt
import numpy as np

n_part = [10,100,1000,10000]

# output from running cd partmc_run; ./run.sh > fortran.txt
fortran = np.loadtxt('partmc_run/fortran.txt')
np.testing.assert_array_equal(fortran[:,0], n_part)
fortran = fortran[:,1]

# output from running ./run_python_full.sh > python_full.txt
python_to_fortran = np.loadtxt('python_full.txt')
np.testing.assert_array_equal(python_to_fortran[:,0], n_part)
python_to_fortran = python_to_fortran[:,1]

# output from running ./run_python_timestep.sh > python_timestep.txt
python_timestep = np.loadtxt('python_timestep.txt')
np.testing.assert_array_equal(python_timestep[:,0], n_part)
python_timestep = python_timestep[:,1]

style = {'marker':'.'}

plt.plot(n_part, python_timestep, label='PyPartMC, timestepping in Fortran', **style)
plt.plot(n_part, python_to_fortran, label='PyPartMC, timestepping in Python', **style)
plt.plot(n_part, fortran, label='PartMC (binary called from shell)', **style)

plt.xlabel('Computational particles')
plt.ylabel('User CPU time (s)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid()

plt.savefig('timing.pdf')
