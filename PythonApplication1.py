

# Стандартный ввод и вывод
first_name = input("Input your first name: ")
last_name=input("Input your last name: ")
middle_name =input("Input your middle name: ")

print ("Hello ", first_name,"!",sep="")

#Вывод f - строк
print (f"Hello, {last_name} {first_name} {middle_name}")

number = input ("Input number")

print ("Standart output ",number)

print ("F-string output 0000#")
print (f"{number:0>5}")
print ("F-string output #0000")
print (f"{number:0<5}")
print ("F-string output 00#00")
print (f"{number:0^5}")