"""
    Объявить переменные name, age, city,
    присвоив им значения с помощью input().

    Вывести на экран текст типа:

    Max from Kiev
    He is 21
"""

# Solutions

# 1
name = input("Name: ")
age = input("Age: ")
city = input("City: ")

print(name, "from", city)
print("He is", age)

# 2
print(name, "from", city, "\nHe is", age)

# 3
print(name + " из города " + city)
print("Возраст " + age)

# 4
print(name + " from " + city, "He is " + age, sep="\n")
