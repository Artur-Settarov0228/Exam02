def fish_tariblash(fish):
    ajiratish = fish.split()

    familya = ajiratish[0]
    ism = ajiratish[1]
    sharif = ajiratish[2]


    natija = f"{ism}, {sharif} ,{familya}"
    return natija

FISH = input("Fish kiriitng : familya ism  sharf = ")
chiqarish = fish_tariblash(FISH)

print(chiqarish)