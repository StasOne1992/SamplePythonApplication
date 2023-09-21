

# Стандартный ввод и вывод
#first_name = input("Input your first name: ")
#last_name=input("Input your last name: ")
#middle_name =input("Input your middle name: ")
#print ("Hello ", first_name,"!",sep="")
#Вывод f - строк
#print (f"Hello, {last_name} {first_name} {middle_name}")
#number = input ("Input number")
#print ("Standart output ",number)
#print ("F-string output 0000#")
#print (f"{number:0>5}")
#print ("F-string output #0000")
#print (f"{number:0<5}")
#print ("F-string output 00#00")
#print (f"{number:0^5}")
# back \ formating
# \n go to new row
# \t add tabulation
# \r return to row start
# \b return back one char
# command "print ("\\")"  return \
#print ("\\")
#print (f"Hello, {last_name} {first_name} {middle_name}")


#Объединение строк

#print ("Na"+"me")

#Вывод нескольких символов подряд
#print("*"*10)

#Динамическая типизация

n=10 #n - int
print (n+10) 

n="10" # n - string
print (n+str(10)) # Преобразование 10 в строку с помощью функции str()
print (int(n)+10) # Преобразование 10 из строки в int  с помощью функции int()

pi = 3.14
print (pi) # Выведет 3.14
print (int(pi)) # Выведет целую часть (3)
print (pi-int(pi)) #Выведет дробную часть (0.14)

# Работа с числами
x = 4
y = 7

print(x+y) #Сложение
print(y-x) #Вычитание
print(x*y) #Умножение
print(y/x) #Деление
print(y**x) #Возведение в степень

print(y//x) # Целочисленное деление 
print(y%x) # Остаток от деления