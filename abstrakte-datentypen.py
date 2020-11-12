print("Hallo")

### Sequenz, Array, List
liste = ["Anna", "Berta", "Carla", "Dieter"]

###Lesezugriff
print(liste[0]) # "Anna"

###Schreibzugriff über Index
liste[1] = "Bertram"
print(liste)

###Löschen
# liste.remove("Anna")
# print(liste)

###Löschen des Elements mit Index 1
neue_liste = []
for i in range(0, len(liste)):
    if i !=1:
        neue_liste.append(liste[i])

print("neue Liste1!")
print(neue_liste)

###Einfügen eines Elements am Index 1
neue_liste2 = []
for i in range(0, len(neue_liste)):
    if i ==1:
        neue_liste2.append("Bertaniene")
    neue_liste2.append(neue_liste[i])

print("neue Liste12")
print(neue_liste2)