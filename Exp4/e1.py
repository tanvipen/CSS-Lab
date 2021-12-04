p=13
q=11
N=p*q

PHI=(p-1)*(q-1)
e=9
for d in range(1,100):
    if ((e*d % PHI)==1): break

print("N(p.q): ",N)
print("PHI [(p-1).(q-1)]:",PHI)
print("e: ",e)
print("d: ",d)
M=78
cipher = M**e % N
print("Cipher: ",cipher)
message = cipher**d % N
print("Message: ",message)
