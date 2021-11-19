#Implementation of various cryptography methods
print("Select the Cryptography Method you want to implement :")
print("1: Substitution method")
print("2: ROT 13 method")
print("3: Transposition method")
print("4: Double Transposition method")
print("5: Vernam Cipher method")
print("6: End Program")
loop=True
while loop:
  choice=int(input("\nEnter Your Choice : "))
  if choice==1:
    print("1. Substitution method")
    text1=input("Enter the text to be encrypted :")
    k=int(input("Enter the no. of Position shift :"))
    text2=""
    print("The Encrypted Message is: ")
    for i in range(0,len(text1)):
      if ord(text1[i])+k<=122:
        print(chr(ord(text1[i])+k),end="")
        text2+=chr(ord(text1[i])+k)
      else:
        print(chr(ord(text1[i])+k-26),end="")
        text2+=chr(ord(text1[i])+k-26)
    print()
    print("The Decrypted Message is: ")
    for i in range(0,len(text2)):
      if ord(text2[i])-k>=97:print(chr(ord(text2[i])-k),end="")
      elif ord(text2[i])-k==32:print(chr(ord(text2[i])-k),end="")
      else:print(chr(ord(text2[i])-k+26),end="")
    print()
    
  elif choice==2:
    print("2. ROT 13 method")
    text1=input("Enter the text to be encrypted :")
    print("The Encrypted Message is: ")
    text2=""
    for i in range(0,len(text1)):
      if ord(text1[i])+13<=122:
        print(chr(ord(text1[i])+13),end="")
        text2+=chr(ord(text1[i])+13)
      else:
        print(chr(ord(text1[i])-13),end="")
        text2+=chr(ord(text1[i])-13)
    print()
    print("The Decrypted Message is: ")
    for i in range(0,len(text2)):
      if ord(text2[i])-13>=97:print(chr(ord(text2[i])-13),end="")
      elif ord(text2[i])-13==32:print(chr(ord(text2[i])-13),end="")
      else:print(chr(ord(text2[i])+13),end="")
    print()
    
  elif choice==3:
    print("3. Transposition method")
    text1=input("Enter the text to be encrypted :")
    text2=""
    print("The Encrypted Message is: ")
    if len(text1)<2:print(text1)
    else:
      for i in range(0,2):
        j=2
        print(text1[i],end="")
        text2+=text1[i]
        while i+j<len(text1):
          print(text1[i+j],end="")
          text2+=text1[i+j]
          j+=2
    print()
    print("The Decrypted Message is: ")
    if len(text2)<2:print(text2)
    else:
      if len(text2)%2==0:a=int(len(text2)/2)
      else: a=int(len(text2)//2+1)
      for i in range(0,a):
        j=a
        print(text2[i],end="")
        while i+j<len(text2):
          print(text2[i+j],end="")
          j+=a
    print()
    
  elif choice==4:
    print("4. Double Transposition method")
    text1=input("Enter the text to be encrypted :")
    text2=""
    str1=""
    str2=""
    print("The Encrypted Message is: ")
    if len(text1)<2:print(text1)
    else:
      for i in range(0,2):
        j=2
        str1+=text1[i]
        while i+j<len(text1):
          str1+=text1[i+j]
          j+=2
      for i in range(0,2):
        j=2
        print(str1[i],end="")
        text2+=str1[i]
        while i+j<len(str1):
          print(str1[i+j],end="")
          text2+=str1[i+j]
          j+=2
    print()
    print("The Decrypted Message is: ")
    if len(text2)<2:print(text2)
    else:
      if len(text2)%2==0:a=int(len(text2)/2)
      else: a=int(len(text2)//2+1)
      for i in range(0,a):
        j=a
        str2+=text2[i]
        while i+j<len(text2):
          str2+=text2[i+j]
          j+=a
      for i in range(0,a):
        j=a
        print(str2[i],end="")
        while i+j<len(str2):
          print(str2[i+j],end="")
          j+=a
    print()
    
  elif choice==5:
    print("5. Vernam Cipher method")
    text2=""
    text1=input("Enter the text to be encrypted :")
    key=input("Enter the key text :")
    print("The Encrypted Message is: ")
    for i in range(0,len(text1)):
      if ord(text1[i])+ord(key[i])-194>25:
        print(chr(ord(text1[i])+ord(key[i])-123),end="")
        text2+=chr(ord(text1[i])+ord(key[i])-123)
      else:
        print(chr(ord(text1[i])+ord(key[i])-97),end="")
        text2+=chr(ord(text1[i])+ord(key[i])-97)
    print()
    print("The Decrypted Message is: ")
    for i in range(0,len(text2)):
      if ord(text2[i])<ord(key[i]):print(chr(ord(text2[i])-ord(key[i])+123),end="")
      else:print(chr(ord(text2[i])-ord(key[i])+97),end="")
    print()
    
  else:
    print('Thank You')
    loop=False
