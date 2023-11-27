s = float(input("Digite seu salário:"))
if s <= 1000:
    print("Seu salário é de {}, seu aumento é de 20%, seu novo salário é {}".format(s,(s*20)/100))
elif s >= 1500:
    print("Seu salário é de {}, seu aumento é de 15%, seu novo salário é {}".format(s,(s*15)/100))
elif s >= 2000:
    print("Seu salário é de {}, seu aumento é de 5%, seu novo salário é {}".format(s,(s*5)/100))
else:
    print("Seu salário é de {}, seu aumento é de 2%, seu novo salário é {}".format(s,(s*2)/100))