cidades = ["Brazlandia", "Ceilândia", "Varjão", "Taguatinga", "Gama", "Guará", "Samambaia", "Recanto das Emas", "Santa Maria", "Lago Norte", "Plano Piloto", "Aguas Claras", "Cruzeiro", "Itapoa", "São Sebastião", "Planaltina", "Planltina de Goiás", "Aguas Quentes", "Rio Verde", "Anápolis", "Pirinópolis", "Rio de Janeiro", "São Paulo", "Teresina", "Teresina", "Brasilia"]

# usuário informa o nome que deseja procurar
cidade = input("Informe o nome da cidade que deseja procurar: ")

# informa a quantidade de vezes que o termo foi achado
quantidade = cidades.count(cidade)

# exibe o resultado na tela 
if cidade in cidades: 
    print(F"{cidade} foi encontrado na lista {quantidade} de vezes.")
else: 
    print(f"{cidade} não foi encontrado.")



