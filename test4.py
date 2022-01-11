a = 42
def affichage():
    print(a)

affichage() #fait appel à la fonction affichage

def change(valeur):
    global a 
    a = valeur 

print(a)
change(10)
print(a)

nombre = 5
nombre = int(input("La table de multiplication que vous souhaitez voir : "))
print("Voici la table de multiplication de ", nombre) 
for x in range(1, 11):
    print(x, "x ", nombre, " = ", x*nombre)