i = input("Digite sua idade atual: ")
i = int(i)
if i < 0:
    print ("impossível!")
elif i < 18:
    print("não precisa se alistar.")
elif i == 18 or i < 65:
    print("Não esqueça de votar na próxima eleição")
elif i > 65: 
    print("Vá descansar.")
else:
    print("eita!")