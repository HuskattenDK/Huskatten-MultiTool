import os

print('#' * 60)

print('IP PINGER Huskatten MultiTool') 

print('#' * 60)
print('-' * 60)      

ip_to_check = input('Sæt den ip du vil pinge ind: ')

print('-' * 60)
os.system('ping -n 50000 {}'.format(ip_to_check))
print('-' * 60)

input('Press Enter to exit.')
