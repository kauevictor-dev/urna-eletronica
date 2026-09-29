numero = input("Digite o número do candidato: ")

if numero in candidatos:
    candidato = candidatos[numero]
    print("Nome:", candidato["nome"])
    print("Partido:", candidato["partido"])
else:
    print("Número inexistente. Voto nulo.")