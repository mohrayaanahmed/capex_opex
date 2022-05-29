# Number of users
i = 300

# PRODUCT A

# Sub-products
a1 = i*100
a2 = i*150
a3 = i*300
a4 = 5000*2
a5 = 4000*2
a6 = 3000*2

# Total license
overall_license = a1 + a2 + a3 + a4 + a5 + a6

# Disaster recovery
disaster_recovery = (a4 + a5 +a6) * 0.3

dist_license = overall_license + disaster_recovery

# Hardware costs
cpu_cost_a = 5000 * 2 * 2
cpu_maintenance_a = ((cpu_cost_a * .10) * 4)

# CAPEX
capex_a = dist_license + 200000 + cpu_cost_a

# OPEX
opex_a = ((dist_license * .18) * 4) + ((200000 * .15) * 4) + cpu_maintenance_a

print("The CAPEX for Product A is", int(capex_a))
print("The OPEX for Product A is", int(opex_a))


# PRODUCT B

# License
capex_b = 350 * i

# Subscription
opex_b = 300 * i * 5

print("\n")
print("The CAPEX for Product B is", capex_b)
print("The OPEX for Product B is", opex_b)


# PRODUCT C

# Hardware costs
cpu_cost_c = 5000 * 2 * 2
cpu_maintenance_c = (cpu_cost_c * .10) * 4

# Subscription
subscription_c = 2 * 25000 * 5

# CAPEX
capex_c = 500000 + cpu_cost_c

# OPEX
opex_c = cpu_maintenance_c + subscription_c

print("\n")
print("The CAPEX for Product C is", capex_c)
print("The OPEX for Product C is", int(opex_c))
