candidatos = {
    "10": {"nome": "Ana Souza", "partido": "Partido do Café"},
    "20": {"nome": "Bruno Lima", "partido": "Partido do Bolo"},
    "30": {"nome": "Carla Dias", "partido": "Partido da Pipoca"},
    "40": {"nome": "Diego Rocha", "partido": "Partido do Suco"},
}
votos = {numero: 0 for numero in candidatos}
brancos = 0
nulos = 0

numero = input("Digite o número (ou 'b' para branco): ")

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
else:
    print("Voto cancelado.")