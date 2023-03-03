# X>Y>Z y sus variaciones

print("-------------------------------------------------")
print("------------Quien es mayor------------")
print("-------------------------------------------------")

#input

x= int(input("Digite el valor de x: "))
y= int(input("Digite el valor de y: "))
z= int(input("Digite el valor de z: "))
#Procesing

if x>y : 
    rta = " X es mayor"

else:
    rta = " Y es mayor"
if y>z :
    rta = " Y es mayor que z"
    
else: 
    rta = " Z es mayor que y"

if x>z : 
    rta = " X es mayor que z"

else:
    rta = "Z es mayor que x"

print("El valor " + str(rta))