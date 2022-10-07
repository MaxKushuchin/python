name = input('Введите имя')
surname = input('Введите фамилию')
born  = int(input('Введите год рождения'))
print (name, "_", surname,"_", born)

name, surname = surname, name
born += 60
print (name, surname, born)


















