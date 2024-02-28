#!/usr/bin/env python
# coding: utf-8

# In[29]:


import matplotlib.pyplot as plt
import numpy as np

# Assuming you have the drawdown and time data in two lists
drawdown = [0.40, 0.74, 1.00, 1.35, 1.55, 2.08, 2.70, 3.02, 3.95, 5.71, 7.03, 8.45, 9.87, 10.20, 10.98]
time = [3.5, 5.0, 6.2, 8.0, 9.2, 12.4, 16.5, 20, 30, 60, 100, 200, 320, 380, 500]

# Set the figure size
plt.figure(figsize=(9, 5))

# Plot drawdown vs. time on a log-log scale with specified axis limits
plt.loglog(time, drawdown, 'bo')  # 'bo' means blue color and circle markers
plt.xlabel('Log Time (min)')
plt.ylabel('Log Drawdown (ft)')
plt.title('Aquifer Test - Theis Type Curve Method (Log-Log Scale)')
plt.grid(True, which='both',axis='both', linestyle='-', linewidth=0.5)  # Add gridlines
plt.xlim(0.1, 10**8)  # Set x-axis limits from 0.1 to 10^8
plt.ylim(0.1, 100)    # Set y-axis limits from 0.1 to 100
plt.show()


# In[30]:


import matplotlib.pyplot as plt
import numpy as np

# Assuming you have the drawdown and time data in two lists
drawdown = [0.40, 0.74, 1.00, 1.35, 1.55, 2.08, 2.70, 3.02, 3.95, 5.71, 7.03, 8.45, 9.87, 10.20, 10.98]
time = [3.5, 5.0, 6.2, 8.0, 9.2, 12.4, 16.5, 20, 30, 60, 100, 200, 320, 380, 500]

# Set the figure size
plt.figure(figsize=(9, 5))

# Plot drawdown vs. time on a log-log scale with specified axis limits
plt.semilogy(time, drawdown, 'bo')  # 'bo' means blue color and circle markers
plt.xlabel('Log Time (min)')
plt.ylabel('Log Drawdown (ft)')
plt.title('Aquifer Test - Theis Type Curve Method (Log-Log Scale)')
plt.grid(True, which='both', linestyle='-', linewidth=0.5)  # Add gridlines

plt.show()


# In[31]:


import matplotlib.pyplot as plt
import numpy as np

# Assuming you have the drawdown and time data in two lists
drawdown = [0.40, 0.74, 1.00, 1.35, 1.55, 2.08, 2.70, 3.02, 3.95, 5.71, 7.03, 8.45, 9.87, 10.20, 10.98]
time = [3.5, 5.0, 6.2, 8.0, 9.2, 12.4, 16.5, 20, 30, 60, 100, 200, 320, 380, 500]

# Set the figure size
plt.figure(figsize=(9, 5))

# Plot drawdown vs. time on a semi-log scale with specified axis limits
plt.plot(time, drawdown, 'bo')  # 'bo' means blue color and circle markers
plt.xscale('log')  # Set the x-axis to a logarithmic scale
plt.xlabel('Time (min)')
plt.ylabel('Drawdown (ft)')
plt.title('Aquifer Test - Jacob time-drawdown Method (Semi-Log Scale)')
plt.grid(True, which='both', axis='both', linestyle='-', linewidth=0.5)  # Add both vertical and horizontal gridlines

plt.show()


# In[32]:


import matplotlib.pyplot as plt
import numpy as np

# Assuming you have the drawdown and time data in two lists
drawdown = [0.40, 0.74, 1.00, 1.35, 1.55, 2.08, 2.70, 3.02, 3.95, 5.71, 7.03, 8.45, 9.87, 10.20, 10.98]
time = [3.5, 5.0, 6.2, 8.0, 9.2, 12.4, 16.5, 20, 30, 60, 100, 200, 320, 380, 500]

# Set the figure size
plt.figure(figsize=(9, 5))

# Plot drawdown vs. time on a semi-log scale with specified axis limits
plt.plot(time, drawdown, 'bo')  # 'bo' means blue color and circle markers
plt.xscale('log')  # Set the x-axis to a logarithmic scale
plt.xlabel('Time (min)')
plt.ylabel('Drawdown (ft)')
plt.title('Aquifer Test - Jacob time-drawdown Method (Semi-Log Scale)')
plt.grid(True, which='both', axis='both', linestyle='-', linewidth=0.5)  # Add both vertical and horizontal gridlines

# Find the index of the minimum drawdown
min_drawdown_index = np.argmin(drawdown)

# Connect most of the time points through a line
plt.plot(time, drawdown, 'r-')


plt.show()


# In[ ]:




