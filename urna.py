import pygame

pygame.mixer.init()
som = pygame.mixer.Sound("sons/confirma-urna.wav")
senha_mesario = "1234"
candidatos = {
    "10": {"nome": "Ana Souza", "partido": "Partido do Café"},
    "20": {"nome": "Bruno Lima", "partido": "Partido do Bolo"},
    "30": {"nome": "Carla Dias", "partido": "Partido da Pipoca"},
    "40": {"nome": "Diego Rocha", "partido": "Partido do Suco"},
}
votos = {numero: 0 for numero in candidatos}
brancos = 0
nulos = 0

while True:
    numero = input("Digite o número ('b' para branco, 'fim' para encerrar): ")
    if numero == "fim":
        senha = input("Senha do mesário: ")
        if senha == senha_mesario:
            break
        print("Senha incorreta.")
        continue    

    if numero == "b":
        tipo = "branco"
    elif numero in candidatos:
        tipo = "candidato"
        print("Nome:", candidatos[numero]["nome"])
        print("Partido:", candidatos[numero]["partido"])
    else:
        tipo = "nulo"
        print("Número inexistente.")

    acao = input("Confirmar (c) ou corrigir (x)? ")

    if acao == "c":
        if tipo == "candidato":
            votos[numero] += 1
        elif tipo == "branco":
            brancos += 1
        else:
            nulos += 1
        print("Voto registrado!")
        som.play()
        pygame.time.wait(int(som.get_length() * 1000))
    else:
        print("Voto cancelado.")

print("\n=== RESULTADO FINAL ===")
for numero, total in votos.items():
    print(candidatos[numero]["nome"], "-", total, "votos")
print("Brancos:", brancos)
print("Nulos:", nulos)

maior = max(votos.values())
vencedores = [candidatos[n]["nome"] for n, t in votos.items() if t == maior]
if maior == 0:
    print("Nenhum voto válido.")
elif len(vencedores) > 1:
    print("Empate entre:", ", ".join(vencedores))
else:
    print("Vencedor:", vencedores[0])