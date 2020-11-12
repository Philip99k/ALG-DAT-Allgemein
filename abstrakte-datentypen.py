print("Hallo was geht")

### Sequenz, Array, List
liste = ["Anna", "Berta", "Carla", "Dieter"]

###Lesezugriff
# print(liste[0]) # "Anna"

###Schreibzugriff über Index
liste[1] = "Bertram"
# print(liste)

###Löschen
# liste.remove("Anna")
# print(liste)

###Löschen des Elements mit Index 1
neue_liste = []
for i in range(0, len(liste)):
    if i !=1:
        neue_liste.append(liste[i])

# print("neue Liste1!")
# print(neue_liste)

###Einfügen eines Elements am Index 1
neue_liste2 = []
for i in range(0, len(neue_liste)):
    if i ==1:
        neue_liste2.append("Bertaniene")
    neue_liste2.append(neue_liste[i])

#print("neue Liste12")
# print(neue_liste2)


### Stack, Stapel, LIFO (Last in First Out)
stapel = []
stapel.append('Anna')
stapel.append('Berta')
stapel.append('Carla')

print("###---1---###")
print(stapel.pop())
print(stapel)

### Anwendung für Stapel: Undo-Funktion

### Queue, Warteschlange, FIFO (First In First Out)
schlange = []
schlange.append('Anna')
schlange.append('Berta')
schlange.append('Carla')

### Element an Schlange entfernen
print("###---2---###")
print(schlange.pop(0))
print(schlange)

### Dictrionary, Key-Value-Store
### Dictionary
woerterbuch = {"Hallo":"hello", "Katze":"cat","Hund":"dog","Maus":"mouse",}

### Lesezugriff
print("###---3---###")
print("###---Dictionary---###")
print(woerterbuch["Katze"])
print(woerterbuch["Maus"])

### Neues Paar hinzufügen
woerterbuch["Haus"] = "house"

### Neues Paar löschen
woerterbuch.pop('Haus', None)

if "Haus" in woerterbuch:
    print(woerterbuch["Haus"])
else:
    print("Keine Ahnung!")

### Set, Menge
print("###---4---###")
print("###---Set, Menge---###")
menge = {"Anna", "Berta", "Carla"}

### Element hinzufügen
menge.add("Alf")
menge.add("Anna") # Wird nicht nochmal hinzugefügt, weil es schon drin ist
menge.add("anna") # Wird hinzugefügt, weil es noch nicht drin ist
print(menge)

### Element entfernen
menge.remove("Berta")
print(menge)

### Ist Element in Menge
if "Berta" in menge:
    print("ist drin")
else: 
    print("ist NICHT drin")
