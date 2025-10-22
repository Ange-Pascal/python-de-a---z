#Leçon 1
# Ecris une ligne de code pour l'ordinateur


# print("Je m'appelle Alex et j'apprends Python !")

# Leçon 2 Les variables 

# Quel est le reusltat ici ? 

#Leçon 3 les types 

# a = 10 
# b = 3.14 
# is_valid = True
# vide = None 

# print(f"La valeur de a est {a} et son type est {type(a)}")
# print(f"La valeur de b est {b} et son type est {type(b)}")
# print(f"La valeur de is_valid est {is_valid} et son type est {type(is_valid)}")
# print(f"La valeur de vide est {vide} et son type est {type(vide)}")

# Leçon 4 : Les chaines de caractères 

# message = "Bonjour" 
# text = """Je suis plus que focus sur Dieu et sur mes objectifs
# Je ne vais plus au Damier
# ça ne s'inscrit pas dans mes objectifs"""
# print(len(message))
# print(message.find(str(a))) 

# print(text) 

# # Exercice 

# phrase = input("Entrer une phrase") 

# print(f"la longueur de la phrase est: {len(phrase)}" )
# print(f"Phrase en majiscule:  {phrase.upper()}")
# print(f"Phrase sans espace:  {phrase.strip()}") 
# print(f"Nombre de e : {phrase.lower().count('e')}")

# # Exercice 3 :

# texte = input("Entrer une phrase")
# if "python" in texte.lower() : 
#     print(f"oui, cette phrase contient le mot python")
# else: 
#     print("Non, le mot python n'est pas présent")


# Les structures conditionnelles 

# nombre = int(input("Entrer un nombre"))

# if nombre % 2 == 0 : 
#     print(f" {nombre} est paire")
# else :
#     print(f" {nombre} est impair")

# Exercice 1 : Age 

# age = int(input("Entrez votre age"))

# if age < 18 : 
#     print("Mineur")
# else: 
#     print("Majeur")

# Exercice 2 

# nombre = float(input("Entrez un nombre : "))

# if nombre > 0 : 
#     print("Positif")
# elif nombre < 0 :
#     print("Negatif")
# else : 
#     print("Zéro")

# Exercice 3 

# print("Je veux deux nombres pour les comparer:")

# nombre1 = float(input("Entrez le nombre numero 1 : "))
# nombre2 = float(input("Entrez le nombre numero 2 : "))

# if nombre1 > nombre2 : 
#     print(f"{nombre1} est le plus grand")
# else : 
#     print(f"{nombre2} est le plus grand")



# Leçon 6 les boucles 

#Exercice 1 : Somme 

somme = 0
for i in range(1, 11):
    somme += i
print("Somme =", somme)
