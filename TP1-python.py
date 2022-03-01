n=int(input("choisir un nombre: " ))
p=int(input("choisir un nombre: " ))

prod=0
while n!=0:
    if n%2==1:
        prod+=p
    n//=2
    p+=p
print(prod)
