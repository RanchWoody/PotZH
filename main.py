import jarmu

j = jarmu.Jarmu()
jarmuvekAdatai = j.beolvasas("jarmu.txt")


j.munkaido(jarmuvekAdatai)
j.elhaladtJarmuvek(jarmuvekAdatai)
j.fMentes(jarmuvekAdatai)
j.rendszamEllenorzes(jarmuvekAdatai)
j.kiiratas(jarmuvekAdatai)