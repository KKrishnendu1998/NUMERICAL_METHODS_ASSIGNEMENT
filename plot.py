'''
Creator :Krishnendu Maji
 progam to verfify the CMB data with theory
'''
import numpy as np
import matplotlib.pyplot as plt

def irradiance(f): #this fucntion calculates the Spectral Iiradiance of a Blackbody at 2.725K
	h = 6.626 * 10**-34.0 #units Js
	c = 3.0*10**8.0 # units ms^-1
	kB = 1.38064852 * 10**-23.0 # S.I units
	T = 2.725

	value = (2.0*h*c*f**3.0)/((np.exp((h*c*f)/(kB*T))-1.0))*10**20 # unit MJy/sr
	return value
'''
This sections creates data poins for plotting Blackbody radiation of a Blackbody at 2.725K
'''
wavenumber = np.arange(2.20,22.20,0.01) # units cm^-1
plt.xlabel("Wave Number 1/λ (in $cm^-$)")
plt.ylabel("Intenity B$_λ$ (in MJy/sr)")
I = irradiance(100*wavenumber)
#here I have found the wave number corresponding to the maximum irradiance#
maxvalue = "The peak value at (wave number) "+str(wavenumber[np.where(I == np.amax(I))[0]])
print(maxvalue)


'''
This section plots the data from NASA
'''

wavenumber_data = np.loadtxt("C:/Users/user/Desktop/nasa_data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (0))
Irradiance_data = np.loadtxt("C:/Users/user/Desktop/nasa_data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (1))

plt.scatter(wavenumber_data , Irradiance_data, color = 'red', label='NASA Data', s = 12.0)
plt.plot(wavenumber, irradiance(100.0*wavenumber),label='Planck\'s Law at T = 2.725K', color = 'green')
plt.legend(loc = 'upper right', frameon = True, shadow = True)
plt.title("Comparing CMB background flux  with Blackbody of temperature 2.725K")
plt.text(12.5,200,maxvalue)
plt.grid(True)
plt.show()
#So, from the graph we see that the maximum of the graph occurs for the wavenumber 5.34 cm-1. So the corresponding wavelength is 0.1872 cm. This lies in the microwave region#
