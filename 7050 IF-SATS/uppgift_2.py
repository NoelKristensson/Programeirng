# Be användaren att mata in näst sista siffran i sitt personnummer
siffra = int(input("Ange näst sista siffran i ditt personnummer: "))

# Kontrollera om siffran är udda eller jämn
if siffra % 2 == 0:
    print("du är tjej")
else:
    print("du är kille")