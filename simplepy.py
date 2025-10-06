n = int(input("Entrer une nombre: "))
print(n)
premier = True


for diviseur in range(2,n):
    reste = n % diviseur
    if reste == 0:
        print("n, n'est pas premier car divisible par", diviseur)
        premier = False

if premier:
    print(n, "est premier")
         