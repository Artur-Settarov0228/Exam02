def soz_sanash(matn):
    sozlar = matn.split()
    natija = {}

    for soz in sozlar:
        if soz in natija:
            natija[soz] += 1
        else:
            natija[soz] = 1

    return natija

Matn = input("matn kiriting :")
sanash = soz_sanash(Matn)
print(sanash)        