list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["rehan", "farhan", "selamet", "reza"]
list_mix = [20, "adi", True, "bryan"]

print("data sebelum diubah:", list_string)
list_string[1] = "jamal"
print("data setelah diubah:", list_string)

print("data sebelum diubah:", list_string)
list_string[0] = "mizan"
print("data setelah diubah:", list_string)

print("data sebelum diubah:", list_mix)
list_mix[0] = 4
print("data setelah diubah:", list_mix)

print("data sebelum diubah:", list_mix)
list_mix[1] = "duggong"
print("data setelah diubah:", list_mix)

print("data sebelum diubah:", list_mix)
list_mix[2] = "False"
print("data setelah diubah:", list_mix)

print("data sebelum diubah:", list_mix)
list_mix[3] = "kuda terbang"
print("data setelah diubah:", list_mix)

#perulangan for

for x in list_string:
    print(x)

for a in list_integer:
    print(a)

for y in list_mix:
    print(y)
