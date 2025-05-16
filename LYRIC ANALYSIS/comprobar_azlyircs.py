with open("unpopus.txt", "r", encoding="latin-1") as file:
    contenido = file.read()

lista = contenido.split("---------------------------------------------------")
print(len(lista)-1)