parameter = int(input("Skriv inn et posetivt heltall her: "))
n = 1

while n <= parameter:
    if n == 1:
        print(str(n) + " laks")
    else:
        print(str(n) + " lakser")
    n = n + 1
