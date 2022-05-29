# Total number of users
n = 1001
# Starting number of users
i = 100

# empty arrays to fill in the dataframe later
array_a = []
array_b = []
array_c = []

while i < n:
    # PRODUCT A
    a1 = 100
    a2 = 150
    a3 = 300
    a4 = 5000
    a5 = 4000
    a6 = 3000
    
    a11 = i*a1
    a21 = i*a2
    a31 = i*a3

    if i < 301:
        a41 = a4*2
        a51 = a5*2
        a61 = a6*2
        cpu_cost = 5000 * 2
        cpu_maintenance = ((cpu_cost * .10) * 4 + cpu_cost) * 2
    elif 301 < i < 601:
        a41 = a4*4
        a51 = a5*4
        a61 = a6*4
        cpu_cost = 5000 * 4
        cpu_maintenance = ((cpu_cost * .10) * 4 + cpu_cost) * 2
    elif 601 < i < 1001:
        a41 = a4*8
        a51 = a5*8
        a61 = a6*8
        cpu_cost = 5000 * 8
        cpu_maintenance = ((cpu_cost * .10) * 4 + cpu_cost) * 2


    overall_license = a11 + a21 + a31 + a41 + a51 + a61

    disaster_recovery = (a41 + a51 +a61) * 0.3

    
    dist_license = overall_license + disaster_recovery
    maintenance_a = (dist_license * .18) * 4
    almost_total_a = maintenance_a + dist_license

    customization = 200000 + ((200000 * .15) * 4)

    total_a = almost_total_a + customization + cpu_maintenance
    array_a.append(total_a)

    # PRODUCT B
    lic = 350 * i
    sub = 300 * i * 5
    total_b = lic + sub
    array_b.append(total_b)

    # PRODUCT C
    if i < 401:
        c = 2 * 25000 * 5
        cpu_cost = 5000 * 2
        cpu_maintenance = ((cpu_cost * .10) * 4 + cpu_cost) * 2
    elif 401 < i < 601:
        c = 6 * 25000 * 5
        cpu_cost = 5000 * 6
        cpu_maintenance = ((cpu_cost * .10) * 4 + cpu_cost) * 2
    elif 601 < i < 1001:
        c = 8 * 25000 * 5
        cpu_cost = 5000 * 8
        cpu_maintenance = ((cpu_cost * .10) * 4 + cpu_cost) * 2

    total_c = c + 500000 + cpu_maintenance
    array_c.append(total_c)
    
    i += 50


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

users = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]
df =  pd.DataFrame(users, columns=['Users'])
df['Product A'] = array_a
df['Product B'] = array_b
df['Product C'] = array_c
print(df)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
major_ticks = np.arange(100, 1001, 50)
y_major_ticks = np.arange(100000, 2000000, 100000)

ax.set_xticks(major_ticks)
ax.set_yticks(y_major_ticks)


plt.plot('Users', 'Product A', data = df, color='red', linewidth = 4)
plt.plot('Users', 'Product B', data = df, color='green', linewidth = 4)
plt.plot('Users', 'Product C', data = df, color='blue', linewidth = 4)
plt.legend()
plt.show()