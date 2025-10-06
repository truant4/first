from utils import estPremier

n = int(input("Entrer une nombre: "))

if estPremier(n):
    print("n, n'est pas premier")
else:
    print(n, "est premier")
