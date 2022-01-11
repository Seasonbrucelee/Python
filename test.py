a = 7
print(a+3)
b=3
print(a+b) #ici on aditionne les variables a et b ce qui nous donne le résultat de 9
print(a)

#a = b + 1
#print(a) #valeur de a est de 3 après modification
#print(a+b)

a += b # a = a + b
#a = a + b
print(a)

a, b = 11, 4
c= a//b
d=a%b
print('La division de ' + str(a) + ' par ' + str(b) + ' est égal à ' + str(c)+'. Il reste ' + str(d))
print(d)

string = "Et voilà du texte"
#string = "Nous l\'avons "réparée"
chaine1=  'Nous l\'avons'
chaine2 = "\"réparée\""
print(chaine1 + "" +chaine2)

#reponse = input() # une ligne vide apparaît et attend que l'utilisateur entre une information

age = int (input("Quel est votre âge ?"))
print ("Vous avez " + str(age) + " ans") 

#if age > 16 :
    #print("Vous avez plus de 16 ans")
#elif age < 0 :
    #print("Tu te moquerais pas de moi ?")
#else : 
    #print("Tu es encore un peu jeune")
if age > 16 and age < 100:
    print("Vous avez plus de 16 ans")
elif age > 100 :
    print("Tu te moquerais pas de moi ?")
else :
    print("Tu es encore un peu jeune")

#print (type(age))

a=3
print(type(a))
b=8.2
print(type(b))
chaine = "Au revoir"
print(type(chaine))
vrai = True
print(type(vrai))

print(7 > 5 > 1)

print(7 > 11 < 9 != 10) 





















