def affiche_menu():
    print("Menu :")
    print("*Action 1")
    print("*Action 2")

affiche_menu()

def dire(text): #def est la Définition de la fonction
    print('#' + text)

dire('Bonjour')
dire('Au revoir')
dire('A Demain')

def addition(a, b): # a et b sont des arguments
    return a + b

somme = addition(2, 5)
print(somme)

def saluer(nom ='Visiteur'):
    print('Bonjour ' + nom)

saluer('Clem')
saluer()