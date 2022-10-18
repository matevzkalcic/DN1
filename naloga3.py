st1 = input("Vnesi prvo število: ")
st2 = input("Vnesi drugo število: ")
st3 = input("Vnesi tretjo število: ")

print(st1)
print(type(st1))
print(st2)
print(type(st2))
print(st3)
print(type(st3))

if st1 == st2 or st3<=st1:
    print("Pogoj ustreza")
else:
    print("Pogoj ne ustreza")