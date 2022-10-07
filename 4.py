years = int(input("количество лет"))
number = 8 * 60 // 5 #количество просмотренных экспонатов за день
print(years * 365 * number)

exhibits = int(input("количество экспонатов"))
mins = exhibits * 5
days = mins // 480
mins -= days * 480
years = days // 365
days %= 365
print("years", years, "days", days, "mins", mins)