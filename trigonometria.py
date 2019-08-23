ca=float(input("Cateto adyacente: "))
co=float(input("Cateto opuesto: "))
h=((ca**2)+(co**2))**(1/2)
sen=co/h
cos=ca/h
tan=co/ca
print("Seno", sen)
print("Coseno", cos)
print("tangente", tan)
