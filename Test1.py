import math
god_cvet_mas= ['зеленый','красный','желтый','белый','черный']
god_giv_mas = ['крысы','коровы','тигра','зайца','дракона','змеи','лошади','овцы','обезьяны','курицы','собаки','свиньи']
god = int(input("Введите год "))
cislo = god/60
cislo= math.floor(cislo) * 60
god_cvet = god - cislo
god_cvet/=12
god_cvet = math.floor(god_cvet)

if god_cvet <= 0:
    print("зелёный")
elif god_cvet == 1:
    print("красный")
elif god_cvet == 2:
    print("желтый")
elif god_cvet == 3:
    print("белый")
elif god_cvet == 4:
    print("черный")
    
#god_giv,cislo2 = god - 4 -

cislo2 = god/12
cislo2 = math.floor(cislo2) * 12
god_giv = god - cislo2
god_giv-=4 
if god_giv <= 0:
    print("крысы")
elif god_giv == 1:
    print ("коровы")
elif god_giv == 2:
    print ("тигра")
elif god_giv == 3:
    print ("зайца")
elif god_giv == 4:
    print ("дракона")
elif god_giv == 5:
    print ("змеи")
elif god_giv == 6:
    print ("лошади")
elif god_giv == 7:
    print ("овцы")
elif god_giv == 8:
    print ("обезьяны")
elif god_giv == 9:
    print ("курицы")
elif god_giv == 10:
    print ("собаки")
elif god_giv == 11:
    print ("свиньи")



print(god_cvet_mas[god_cvet],god_giv_mas[god_giv])

