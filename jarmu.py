import ido

class Jarmu:

    def __init__(self):
        pass

    def beolvasas(self, filepath: str) -> list:

        try:
            file = open(filepath, "r")
            sor = file.readline()
            adatok = []

            while(sor != ""):
                adatok.append(sor.strip().split(" "))

                sor = file.readline()

            print("1. feladat: A jarmu.txt beolvasása.")

            return adatok

        except FileNotFoundError:
            print("Hiba a fájl beolvasásakor!")

    def munkaido(self, ad: list):

        if(ad[len(ad)-1][1] == "00" and ad[len(ad)-1][2] == "00"):
            ido = int(ad[len(ad)][0]) - int(ad[0][0])
        else:
            ido = (int(ad[len(ad)-1][0])+1) - int(ad[0][0])

        print(f"2. feladat: Az ellenőrzést végzők legalább {ido} órát dolgoztak.")

    def elhaladtJarmuvek(self, ad: list):
        elhaladt = [["B", "Autóbusz", "0"], ["K", "Kamion", "0"], ["M", "Motor", "0"], ["", "Személygépkocsi", "0"]]

        elhaladtDict = {"Autóbusz":0, "Kamion":0, "Motor":0, "Személygépkocsi":0}

        temp = 0
        for i in range(len(ad)):

            if(ad[i][3][0] == "B"):
                elhaladtDict["Autóbusz"]+= 1

            elif(ad[i][3][0] == "K"):
                elhaladtDict["Kamion"]+= 1

            elif (ad[i][3][0] == "M"):
                elhaladtDict["Motor"]+= 1

            else:
                elhaladtDict["Személygépkocsi"]+= 1

        print("3. feladat: Elhaladt járművek mennyisége típusonként:")
        print(f"\t- Autóbusz: {elhaladtDict['Autóbusz']}")
        print(f"\t- Kamion: {elhaladtDict['Kamion']}")
        print(f"\t- Motor: {elhaladtDict['Motor']}")
        print(f"\t- Személygépkocsi: {elhaladtDict['Személygépkocsi']}")

    def rendszamEllenorzes(self, ad: list):

        '''
        print("5. feladat: Adja meg a keresett rendszámot: ")
        keresett = input()
        while(len(keresett) != 7 and keresett[2] != "-"):
            keresett = input()

        adCpy = ad

        for i in range(len(keresett)):
            if(keresett[i] == "*"):
                for j in range(len(adCpy)):
                    adCpy[j][3][i] = '*'

        indexek = []

        voltE = False

        for i in range(len(adCpy)):
            if(adCpy[i][3] == keresett):
                indexek.append(i)
                voltE = True

        if(voltE):
            for i in range(len(indexek)):
                print(f"\t {ad[indexek[i]][3]}")

        else:
            print("Nem haladt el ilyen rendszámmal jármű.")


        pass'''

    def kiiratas(self, ad: list):

        print("6. feladat: Az ellenőrzések adatainak kiíratása.")
        ismSzama = int(ad[len(ad)-1][0])-int(ad[0][0])
        ora = 8

        try:
            irando = open("ellenorzes.txt", "r+")
            irando.write(f"{ora} ora: {ad[0][3]}\n")
            ora = 9

            i = 0

            while(ad[i][0] != "9" and i > len(ad)):
                i += 1

            irando.write(f"{ora} ora: {ad[i][3]}\n")


            for j in range(ismSzama):
                for i in range(len(ad)):
                    if(ad[i][0] == str(ora)):
                        irando.write(f"{ora} ora: {ad[i][3]}\n")
                        break

                ora += 1




        except FileNotFoundError:
            print("Hiba a fájl beolvasásakor!")

    def fMentes(self, ad: list):
        mpercek = []

        for i in range(len(ad)):
            ossz = (int(ad[i][0])*60) + int(ad[i][1]) + (int(ad[i][0])/60)
            mpercek.append(ossz)

        legnagyobbKulonbseg = mpercek[1]-mpercek[0]
        legnagyobbKulIdx = 0

        for i in range(len(mpercek)-1):
            if(mpercek[i+1]-mpercek[1] > legnagyobbKulonbseg):
                legnagyobbKulonbseg = mpercek[i+1]-mpercek[1]
                legnagyobbKulIdx = i



        print(f"4. feladat: A leghosszabb forgalommentes időszak: {ad[legnagyobbKulIdx][0]}:{ad[legnagyobbKulIdx][1]}:{ad[legnagyobbKulIdx][2]} - {ad[legnagyobbKulIdx+1][0]}:{ad[legnagyobbKulIdx+1][1]}:{ad[legnagyobbKulIdx+1][2]}")
