base = int(input("입력 진수 결정(16/10/8/2) : "))
num_str = input("값 입력 : ")

num = int(num_str, base)

print("16진수 ==> ", hex(num))
print("10진수 ==> ", num)
print("8진수 ==> ", oct(num))
print("2진수 ==> ", bin(num))