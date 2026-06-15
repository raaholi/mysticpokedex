#Projeto desenvolvido por:
# Pietro Marques Araujo RA 1680972521035
# Rafael da Silva Garcia RA 1680972521020
# Raizza Olivia Pinto Bezerra RA 1680972521022
# Sofia dos Santos Arruda RA 1680975221011
# Yasmin Turossi Ferreira RA 1680972521033

# ◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓◓

import hashlib
import os
from time import sleep as soneca

# ==========================================
# ◓ CONFIGURAÇÕES GLOBAIS DE INTERFACE ◓
# ==========================================
#Essa parte possui funções simples pra definir regras de identação e GUI para o usuário, de forma mais bonita. Organizando a largura, como os titulos vão funcionar, centralizar e deixar os
#     ASCII mais centralizados.
LARGURA = 80

def linha(caractere="="):
    print((caractere * LARGURA))

def titulo(texto, icone="◓⃙"):
    print()
    linha("◓")
    print(f"{icone} {texto.upper()} {icone}".center(LARGURA))
    linha("◓")
    print()

def print_centro(texto):
    print(texto.center(LARGURA))

def print_ascii(arte):
    print()
    for l in arte.strip("\n").split("\n"):
        print(l.center(LARGURA))
    print()


# ==========================================
# ◓ LÓGICA DE CRIPTOGRAFIA E VALIDAÇÃO ◓
# ==========================================
#O deslocamento escolhido foi apenas pra diferença do comum, mas ainda dentro dos mais usados.
DESLOCAMENTO = 5

# O que faz? A Cifra de César "escorrega" as letras do alfabeto. Um 'A' vira 'F', por exemplo.
# Por que usamos? Escolhemos a Cifra de César para salvar os dados dos Pokémons porque ela é reversível (precisamos decifrar na hora de ler), além de ser teoricamente simples e
#     rápida de decifrar e cifrar. Além disso, não usa nenhuma biblioteca especial, apenas cálculos matemáticos e lógica geral.
def cifra_cesar(texto, modo='cifrar'):
    resultado = ""
    passo = DESLOCAMENTO if modo == 'cifrar' else -DESLOCAMENTO
    for char in str(texto):
        codigo = ord(char)
        if 32 <= codigo <= 126:
            novo_codigo = 32 + ((codigo - 32 + passo) % 95)
            resultado += chr(novo_codigo)
        else:
            resultado += char
    return resultado


# O que faz? Pega a senha do usuário e transforma num código gigantesco e irreconhecível.
# Por que usamos? O Hash é uma via de mão única:você transforma a senha no código, mas não consegue pegar o código e transformar na senha de novo.  Isso é útil afinal, caso uma cifra
#     de César pura seja testada, em algum momento a senha será achada de novo, porém com o Hash, a senha fica oculta, o que ocorre é uma validação com o hash já criado no BD.
def gerar_hash(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()


#O que faz? Vê o como a senha foi escrita pelo usuário e cria condições para a senha, as condições são simples pra não ter muitos problemas no calculo de hashs.
#Por que usamos? Essa verificação torna a senha mais complexa de se descobrir e aumenta o sistema de segurança.
def validar_senha(senha):
    #Verifica se a senha tem pelo menos 6 caracteres, contendo letras e números.
    if len(senha) < 6:
        return False
    tem_letra = any(c.isalpha() for c in senha)
    tem_num = any(c.isdigit() for c in senha)
    return tem_letra and tem_num



# ==========================================
# ◓ LOGIN E CREDENCIAIS ◓
# ==========================================
#O que faz? Verifica se o login já existe, se não existe, cria um novo, de forma identada e visual para o usuário. Assim que o login for criado, ele salva essas informações criptografadas no
#     arquivo de login, além disso, já possui tratamento de erros, caso as informações digitadas estejam incorretas.
#Por que usamos? Pra o usuário ter apenas um registro e esse registro ser validado pela lógica, aumentando a facilidade do sistema e a segurança.
def verificar_ou_criar_login():
    arquivo_login = "login.txt"
    soneca(1)
    loading = "⬛⬛⬛⬜⬜"

    #verifica o arquivo de login e entra no modo de leitura, lê linha por linha e vê as separações por ;. 
    if os.path.exists(arquivo_login):
        with open(arquivo_login, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
            if ';' in conteudo:
                hash_usuario, hash_senha = conteudo.split(';', 1)
                return hash_usuario, hash_senha

    #printa tudo que é necessário pro usuário e salva a senha e login digitados. Já com tratamento caso o usuário não digite o correto.
    print_centro(loading)
    soneca(1)
    pikapika = """⠀⢀⢀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀
⠀⠀⠀⠀⣿⡀⠙⠁⠀⢠⡀⣐⠓⠬⢠⢀⠉⠄⠠⠆⣄⠀⡤⢬⡀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠋⠒⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠈⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⡄⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠃
⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡀⠀⠀⠈⠲⠒⠉⠉⠉⠁⠐⠺⢦⡀⢸
⠀⠀⠀⠀⠀⢀⣱⢠⠀⡆⠀⠀⠀⠀⠀⠀⠉⠓⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾
⠀⠤⠤⢤⣀⣘⢯⣾⢾⡷⡚⠉⠀⠀⠀⠀⠀⡘⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄
⡀⠀⠀⠀⠀⠈⠉⠉⠒⠲⠮⣉⣀⠀⠀⠀⢠⡇⠀⠀⣶⣟⡆⠀⠀⠀⠀⢰⣲⡆⠀⡇
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⠀⠈⠸⡇⢀⠤⡛⠛⠁⠀⠀⠠⠀⠸⠟⠋⢰⣅⡆
⢡⠀⠀⠀⠀⠂⠀⠀⠀⠀⢰⠀⡸⠁⠀⠀⠀⠇⣇⠀⢸⠀⠰⣤⣤⣤⣤⠄⠀⢠⢺⡿⠃
⡈⣆⣠⠤⠤⠤⠐⠖⢲⠀⡄⢰⠁⠀⠀⠀⠀⡜⠈⠓⠋⠀⠀⢣⡀⣠⠎⠀⠀⣾⡎
⠀⠀⠀⠠⣀⡁⠀⠀⡎⢠⠃⣇⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⣲⢤⣄⡠⢤⡖⠋⠀⢡
⠀⠀⣆⠀⣘⠛⠂⠰⢇⣘⠂⠬⣁⠒⡄⠀⢸⢷⡀⠀⠀⠀⠀⠀⠀⠉⠛⢄⠀⠀⠸⢣⡀⣤⡄
⠀⠐⣸⡾⢋⣀⡄⠀⠀⠀⠉⠳⣤⣡⡇⠀⢸⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⣃⣠⠃⠀⡏⡿⠁
⠀⠀⠋⠃⡾⠟⠓⠀⠀⠀⠀⠀⠧⠥⠭⡝⡎⣧⡀⠀⠀⠀⠉⠐⠒⠐⠒⠊⢣⢀⣴⣶⣷⠇
⠀⠀⠀⠘⠁⠁⠀⠨⡀⠀⠀⠀⠀⠀⠀⠳⠷⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣶⠤⢄⡀⠀⠀⢀⡀⣾⣻⡟⠁"""
    print_ascii(pikapika)
    print_centro("◓⃙ Pronto para iniciar sua jornada Pokémon? ◓⃙")
    soneca(2)
    print_centro("Então vamos lá! Ϟ(๑⚈ ․̫ ⚈๑)⋆")
    print_centro('Seja nem-vindo a Equipe Mystic!')
    mystic = """⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡞
⠈⠛⢿⣿⣶⣥⣢⡀⠀⠀⠀⠀⠀⢀⣠⣄⡀⠀⠀⠀⠀⠀⢀⣶⣵⣾⣿⢿⡋⠀
⠀⠈⠻⣾⣿⣿⣿⣷⡄⣠⡴⠶⠛⠉⠁⡈⠙⠛⠶⣦⣄⢠⣿⣿⣿⣿⡿⠟⠀⠀
⠀⠀⠈⢶⣯⣿⣿⣿⣷⡁⠀⠀⣀⡀⣼⣧⢀⣀⠀⠀⢠⣿⣿⣿⣿⣷⠟⠀⠀⠀
⠀⠀⠀⠀⢩⣿⣿⣿⣿⣷⣀⠀⠘⠿⡽⢯⠿⠃⣀⣠⣾⣿⣿⣯⣽⠇⡀⠀⠀⠀
⠀⠀⠀⢠⣆⢩⣭⣿⣿⣿⣿⣿⣷⡄⣷⣾⢠⣾⣿⣿⣿⣿⢿⣿⠄⣼⠀⠀⠀⠀
⠀⠀⠀⢸⣿⡆⠀⠾⢻⣿⣿⣿⡟⣰⣿⣿⣆⠻⣿⡻⣿⡝⠛⠀⢸⣿⠇⠀⠀⠀
⠀⠀⠀⠘⣿⡇⠀⠀⠀⠉⠘⠋⠠⣿⣿⣿⣿⡄⠉⠁⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀
⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀
⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣤⣤⣴⣶⣶⣶⣄⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⡿⠿⠿⠿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣎⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣵⡿⠿⣿⣶⣤⣀⠀⠀⠀⢀⣠⣾⣿⣿⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠏⠀⠈⠙⠪⢝⡿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠟⠃⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
"""
    print(mystic)
    soneca(1)
    loading = "⬛⬛⬛⬜⬜"
    print_ascii (loading)
    print_centro("Primeiro, vamos criar seu nome de usuário e senha!")
    
    titulo("Iniciando seu cadastro na Pokédex")
    
    usuario = input(" ▸ Defina seu nome de treinador: ").strip()
    while usuario == "":
        print(" ❌ O usuário não pode ficar em branco!")
        usuario = input(" ▸ Defina seu nome de treinador: ").strip()
    hash_usuario = gerar_hash(usuario)
    
    while True:
        senha = input(" ▸ Defina a sua senha (mín. 6 caracteres, com letras e números): ").strip()
        if validar_senha(senha):
            break
        print(" ❌ A senha não atende aos requisitos mínimos!")
    hash_senha = gerar_hash(senha)

    with open(arquivo_login, 'w', encoding='utf-8') as f:
        f.write(f"{hash_usuario};{hash_senha}")

    print("\n" + "✅ Credenciais iniciais configuradas com sucesso!".center(LARGURA) + "\n")
    return hash_usuario, hash_senha


#Verifica o login e o realiza caso seja validado corretamente
def realizar_login(hash_usuario_salvo, hash_senha_salvo):
    titulo("Faça Login para acessar sua Pokédex")
    soneca(1)
    print_centro("Lembre-se: deixe essas informações seguras, cuidado com a Equipe Rocket!")
    
    haunter = """⠀⠀⠀⠲⣦⣤⣀⣀⠀⠀⠀⣀⣀⣠⣤⣀⣀⠀⢀⣀⣠⣤⣶⣶⠟⠀⠀⠀
⠀⠀⠀⠀⠙⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⠟⢻⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠲⣶⣶⣾⣿⣿⠀⢨⠙⢿⣿⣿⠏⣅⠀⢸⣿⣿⣷⣾⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠻⢿⣿⣿⢷⣶⣶⣾⣿⣿⣶⣶⣾⠟⣿⣿⣿⣋⠀⠀⠀⠀⠀
⠀⠀⢀⣀⣀⠐⢶⣿⣿⣧⠁⠀⠋⠁⠈⠋⠀⢀⣾⣿⣿⡿⣷⣶⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣷⣤⣙⣿⣿⣷⣶⣶⣴⣴⣴⣶⣿⣿⣿⠟⣡⣿⣿⣧⣄⣀⡀
⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⡿⠿⣿⣿⣿⣿
⣿⡿⠛⠿⠟⠉⠉⠉⠸⠋⠀⠻⡿⣿⣿⣿⣿⠻⠇⠀⠀⠈⠀⠀⠈⠉⢸⠃
⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    print_ascii(haunter)
    soneca(1)
    
    while True:
        usuario = input("  ▸ Treinador: ").strip()
        senha = input("  ▸ Senha: ").strip()
        
        print_centro("Verificando credenciais...")
        soneca(1)
        
        if gerar_hash(usuario) == hash_usuario_salvo and gerar_hash(senha) == hash_senha_salvo:
            linha("◓")
            print_centro("✅ Verificação concluída com sucesso! Ϟ(๑⚈ ․̫ ⚈๑)⋆")
            print_centro("Ϟ(๑⚈ ․̫ ⚈๑)⋆ Seja bem-vindo treinador!! Ϟ(๑⚈ ․̫ ⚈๑)⋆")
            return True  
        else:
            print(" ❌ Usuário ou senha incorretos. Tente novamente.\n")

#Função para editar as credencias, baseando-se nas opções dadas pro usuário e as salvarem no arquivo de login.
def editar_credenciais(hash_u_atual, hash_s_atual):
    titulo("Alterar Credenciais de Acesso")
    print_centro("O que você deseja alterar?")
    print("  1 - Apenas o Nome de Treinador".center(LARGURA))
    print("  2 - Apenas a Senha".center(LARGURA))
    print("  3 - Ambos (Nome e Senha)".center(LARGURA))
    print("  4 - Cancelar e voltar ao menu".center(LARGURA))
    print()
    
    op = input("  ▸ Escolha uma opção: ").strip()
    
    if op == '4':
        return hash_u_atual, hash_s_atual
        
    novo_usuario_hash = hash_u_atual
    nova_senha_hash = hash_s_atual

    #a linha op in [n, m] apenas faciliza o uso de ifs. por exemplo, no 1 e no 3, ele pede usuario novo, e já chama na opção 1 e 3.
    if op in ['1', '3']:
        usuario_novo = input("\n  ▸ Novo Treinador: ").strip()
        while usuario_novo == "":
            print(" ❌ O nome não pode ficar em branco!")
            usuario_novo = input("  ▸ Novo Treinador: ").strip()
        novo_usuario_hash = gerar_hash(usuario_novo)

    #caso vá pra linha 2 ou 3, ele chama a criação nova de senha também.
    if op in ['2', '3']:
        while True:
            senha_nova = input("\n  ▸ Nova senha (mín. 6 caracteres, letras e números): ").strip()
            if validar_senha(senha_nova):
                nova_senha_hash = gerar_hash(senha_nova)
                break
            print(" ❌ A senha não atende aos requisitos mínimos!")

    #escreve nova senha e usuario.
    with open("login.txt", "w", encoding="utf-8") as f:
        f.write(f"{novo_usuario_hash};{nova_senha_hash}")
    
    print("\n" + "✅ Credenciais atualizadas com sucesso e salvas! ◓⃙".center(LARGURA))
    return novo_usuario_hash, nova_senha_hash



# ==========================================
# ◓ BUSCA E ORDENAÇÃO ◓
# ==========================================
# O que faz? O Bubble Sort empurra os itens maiores para o final da lista, trocando de dois em dois.
# Por que usamos? Programado para rodar se a lista for pequena (menos de 100 itens). Afinal, nesse limite o bubble e o merge são basicamente o mesmo tempo.
def bubble_sort(lista, index=1):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = lista[j][index]
            val2 = lista[j + 1][index]
            if isinstance(val1, str): val1 = val1.lower()
            if isinstance(val2, str): val2 = val2.lower()
            
            if val1 > val2:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# O que faz? O Merge Sort pica a lista na metade várias vezes até ficarem pedacinhos, e depois vai costurando (dando merge) de volta, só que já na ordem certa.
# Por que usamos? Programado para rodar se a lista for grande (mais de 100 itens). Afinal, nesse numero o merge é bem mais efetivo e rápido que o merge
def merge_sort(lista, index=1):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda, index)
        merge_sort(direita, index)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            val_esq = esquerda[i][index]
            val_dir = direita[j][index]
            
            if isinstance(val_esq, str): val_esq = val_esq.lower()
            if isinstance(val_dir, str): val_dir = val_dir.lower()

            if val_esq <= val_dir:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

#Ordena o inventario em ordem.
def ordenar_inventario(inventario, por_id=False):
    lista_dados = []
    for p_id, dados in inventario.items():
        lista_dados.append([p_id] + dados)
    
    index_ordenacao = 0 if por_id else 1

    #condição de qual sort escolher
    if len(lista_dados) > 100:
        merge_sort(lista_dados, index_ordenacao)
    else:
        bubble_sort(lista_dados, index_ordenacao)
        
    return lista_dados

# O que faz? Vai olhando Pokémon por Pokémon, desde o primeiro até achar o que você digitou.
# Por que usar? É excelente se a lista estiver totalmente bagunçada. Como ele olha todos, a ordem não importa.
def busca_linear(inventario, nome_busca):
    nome_busca = nome_busca.strip().lower()
    for p_id, dados in inventario.items():
        if dados[0].lower() == nome_busca:
            return [p_id] + dados
    return None

# O que faz: Funciona como procurar uma palavra no dicionário de papel: você abre no meio.Se a palavra for antes, você ignora a metade da frente e abre no meio da primeira metade,
#     e assim por diante.
# Por que usar: É infinitamente mais rápido que a busca linear, especialmente se você tivesse 10.000 Pokémons.
def busca_binaria(inventario, nome_busca):
    nome_busca = nome_busca.strip().lower()
    lista_ordenada = ordenar_inventario(inventario, por_id=False)
    
    baixo = 0
    alto = len(lista_ordenada) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        nome_atual = lista_ordenada[meio][1].lower()
        
        if nome_atual == nome_busca:
            return lista_ordenada[meio]
        elif nome_atual < nome_busca:
            baixo = meio + 1
        else:
            alto = meio - 1
    return None



# ==========================================
# ◓ CONTROLE DO BANCO DE DADOS ◓
# ==========================================
#Carrega o arquivo do bd e suas informações já com hash
def carregar_arquivo():
    inventario = {}
    arquivo = "inventario.csv"

    #abre o arquivo com read e escreve os campos separados por ;, já com seus tipos de dados e cifrados.
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha_txt in f:
                linha_txt = linha_txt.strip()
                if not linha_txt:
                    continue

                campos = linha_txt.split(";")
                if len(campos) < 11:
                    continue

                id_decifrado = int(cifra_cesar(campos[0], 'decifrar'))
                nome_decifrado = cifra_cesar(campos[1], 'decifrar')
                altura_decifrada = float(cifra_cesar(campos[2], 'decifrar'))
                peso_decifrado = float(cifra_cesar(campos[3], 'decifrar'))
                tipo_decifrado = cifra_cesar(campos[4], 'decifrar')
                lendario_decifrado = cifra_cesar(campos[5], 'decifrar') == 'True'
                shiny_decifrado = cifra_cesar(campos[6], 'decifrar') == 'True'
                iv_decifrado = float(cifra_cesar(campos[7], 'decifrar'))
                ev_decifrado = float(cifra_cesar(campos[8], 'decifrar'))
                forma_reg_decifrada = cifra_cesar(campos[9], 'decifrar')
                tipo_alt_decifrado = cifra_cesar(campos[10], 'decifrar')

                inventario[id_decifrado] = [
                    nome_decifrado, altura_decifrada, peso_decifrado, tipo_decifrado,
                    lendario_decifrado, shiny_decifrado, iv_decifrado, ev_decifrado,
                    forma_reg_decifrada, tipo_alt_decifrado
                ]
    #caso não tenha o arquivo.
    except FileNotFoundError:
        with open(arquivo, "w", encoding="utf-8"):
            pass

    return inventario

#salva as informações do arquivo quando é finalizado o programa
def salvar_arquivo_em_lote(inventario):
    arquivo = "inventario.csv"
    with open(arquivo, "w", encoding="utf-8") as f:
        for p_id, dados in inventario.items():
            linha_csv = (
                f"{cifra_cesar(str(p_id), 'cifrar')};{cifra_cesar(dados[0], 'cifrar')};"
                f"{cifra_cesar(str(dados[1]), 'cifrar')};{cifra_cesar(str(dados[2]), 'cifrar')};"
                f"{cifra_cesar(dados[3], 'cifrar')};{cifra_cesar(str(dados[4]), 'cifrar')};"
                f"{cifra_cesar(str(dados[5]), 'cifrar')};{cifra_cesar(str(dados[6]), 'cifrar')};"
                f"{cifra_cesar(str(dados[7]), 'cifrar')};{cifra_cesar(dados[8], 'cifrar')};"
                f"{cifra_cesar(dados[9], 'cifrar')}\n"
            )
            f.write(linha_csv)

#função de adicionar pokemons no bd. Já com verificações de erros em cada uma das perguntas.
def adicionar_pokemon(inventario):
    titulo("Adicionar Novo Pokémon à Pokédex")
    
    while True:
        try:
            p_id_str = input(" ▸ Digite a ID do Pokémon (1-151): ").strip()
            if not p_id_str:
                print(" ❌ Este campo não pode ficar em branco.")
                continue
            p_id = int(p_id_str)
            if 1 <= p_id <= 151:
                break
            print(" ❌ ID deve ser entre 1 e 151.")
        except ValueError:
            print(" ❌ Valor inválido! Digite um número inteiro.")
    
    if p_id in inventario:
        print("\n ❌ Erro: Este Pokémon já se encontra cadastrado no sistema.")
        return
        
    print("\n" + "--- Adicione as Características ---".center(LARGURA) + "\n")
    
    while True:
        nome = input(" ▸ Nome do Pokémon: ").strip().lower()
        if nome:
            break
        print(" ❌ Este campo não pode ficar em branco.")

    nome_validacao = nome.lower()
    
    if nome_validacao in ["moltres", "articuno", "zapdos", "mew", "mewtwo"]:
        print('\nParabéns treinador! Você descobriu um Pokémon lendário!')
        soneca(2)
        
        if nome_validacao == "moltres":
            print('Este é o Moltres, Pokémon lendário do tipo fogo')
            soneca(2)
            moltres = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣶⣴⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣯⢿⣿⣻⣟⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣯⢿⡷⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⣜⣣⢛⣷⣿⠋⠀⠀⠠⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⢍⢷⡹⣆⠎⣿⣦⣶⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⢶⡱⢻⡈⡾⡹⣻⣽⡏⢀⡾⢀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠟⣦⢝⡻⣽⠲⡟⡝⣯⣷⣿⡧⣯⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡹⣎⠾⣱⢎⣳⠃⡜⣹⣾⣿⡇⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣧⢳⢭⡳⡱⣎⢧⣀⣴⢫⣿⣿⣶⡾⠟
⠀⠀⠀⠀⠀⡀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⣾⢣⡻⢬⢳⡱⢎⡚⡼⣮⠝⣿⣾⣝⣁⡀
⠀⠀⠀⠀⠀⢧⣀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣏⠷⣭⢛⢦⡙⢮⠵⠛⢉⡜⣶⣯⣿⣿⡇
⠀⠀⠀⡄⣾⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢷⡷⢎⡻⣔⡫⢖⣹⠡⠀⠐⣢⣟⣾⠷⢫⠅⡀
⠀⠀⠀⢱⣿⣿⢯⣷⡿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⡿⣜⢯⡱⢎⡵⢃⢾⠀⠠⣑⢶⡿⡿⠀⠭⠈⠀
⠀⠀⠀⢈⣿⣿⡻⢌⠳⢛⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣽⡳⢭⢖⡹⢎⡴⢫⠏⢀⠥⣯⣿⠟⠡⡈⠀⠀⠀
⠀⣆⠰⣮⣿⣷⠏⡐⠒⠅⡵⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣹⡯⣝⡎⢮⣱⢋⠾⢃⡰⣋⢾⣳⣿⣿⣶⣯⣤⡤⠄
⠀⠈⢷⣿⡿⣞⠁⢎⠐⠠⢀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣽⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣳⢯⡳⣥⢛⡼⡇⡀⠄⣦⣳⢯⡿⠿⠚⠛⠺⠣⠀⠀⠀
⢠⣾⣮⣿⣟⠧⡈⢊⠄⠡⠂⠸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⣆⣠⣾⣿⣿⣿⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣳⢯⠧⣝⡲⢯⡿⣁⠶⣹⢶⣻⠿⠶⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢻⣿⡽⣶⠑⡂⠌⠠⠁⠂⠩⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⣿⣻⣿⡎⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢿⡹⢎⡽⣜⡏⠁⢡⢰⣫⢞⣿⡿⣿⣶⣶⡶⠂⠀⠀⠀⠀⠀
⢁⢿⣷⣿⡿⣵⠊⠌⠠⢁⠂⠁⠄⠉⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⣿⣟⣿⢿⣿⡽⡿⠟⠉⠁⠀⠀⠀⠀⠀⠀⡠⣫⡙⢧⡹⣍⢾⠟⠠⡍⣖⣯⣞⣿⣳⣿⣻⣾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢹⣿⣿⣟⡳⣌⣁⡂⠄⠡⠀⢈⠈⠮⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⣿⢚⢻⢿⠻⣿⣵⠂⠀⠀⠀⠀⠀⠀⠀⡰⡽⣡⠛⣦⡛⢨⠚⢏⡱⣞⣽⡾⠿⠾⠽⠾⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠹⣿⣿⡵⢢⡙⢪⡄⠁⢂⠀⠠⠈⠻⠦⡀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⣿⣿⣟⠻⣷⡇⠀⠀⠀⠀⠀⠀⢀⡠⡪⢍⡶⣡⢏⣞⣽⡠⣚⣼⣳⣯⣿⣮⡝⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣯⢿⡷⣝⣢⠱⣈⠄⢢⠁⡐⢀⠂⡙⠶⠤⣀⠀⠀⠀⠀⠀⣴⠛⠛⠻⣯⡿⣖⢷⡀⠀⠀⠀⢀⢴⠗⣩⡷⣻⡼⠵⠞⡓⣤⣳⣽⣞⣯⣿⣣⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⢯⣟⣿⣻⣽⣳⣮⡝⢎⣉⠳⣄⠒⣈⠰⡀⢡⢉⣓⡒⠲⠦⣤⣀⣀⣤⣬⣷⣿⡜⣻⡈⣉⢩⢃⣮⣽⣳⠽⣱⣞⡳⣼⣽⣶⣿⠷⢯⡍⠉⠉⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠻⠉⣻⠿⠟⠭⢛⣿⣷⣿⣻⢶⣹⢮⣙⣦⡛⠢⢇⡲⠤⢏⡟⡳⢶⡶⣦⣤⣤⣤⣧⡹⡷⡜⣰⢋⡝⣻⢷⡻⣯⣷⣾⣟⠿⣟⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠉⣻⣽⣿⠿⠻⢿⣯⣿⣿⣮⣭⡝⣦⡜⣹⠲⠼⡚⣅⠫⡜⢼⡷⢀⠳⣌⠳⣜⡱⣎⢷⡹⣏⠉⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠏⢯⣽⣖⠆⣍⣽⣷⣯⡿⣯⣿⣿⣿⣿⢿⠷⣿⣿⠞⣻⣧⢇⣎⡳⣭⢞⣽⣎⢏⡿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠀⠀⠛⡼⠙⣜⡟⣻⡟⠁⠊⠻⠇⠉⠉⠛⠐⠛⠛⢀⣿⠻⠈⢷⠿⣷⣿⣿⣷⣟⣾⣯⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣳⣿⣿⣾⣿⣿⣿⡿⣿⣷⣦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣠⣄⢨⡿⠺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠿⠿⢿⣿⣥⠀⣹⣿⣿⣿⣷⣿⣿⣽⣟⣿⣯⣩⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⢸⣿⣿⣾⡽⣿⣻⣾⡽⣟⣿⣿⣟⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⡿⣿⣏⡀⠻⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠄⠈⠁⠻⠈⠛⠍⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
            print(moltres)
            
        elif nome_validacao == "articuno":
            print('Este é o Articuno, Pokémon lendário do tipo gelo')
            soneca(2)
            articuno = """⢀⣿⡙⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠴⠶⢶⡶⠀⠀
⠀⣿⣿⣷⡄⢹⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⡾⠛⠙⠉⣁⣤⡶⠟⠃⠀⠀
⠀⠹⣯⠻⣿⣦⠙⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⣿⣿⡿⠏⢀⣤⣶⣟⣋⣁⣀⠀⠀⠀⠀
⠀⠀⠙⣧⡈⠿⣿⣟⢻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣟⣽⣿⡿⠋⠰⡾⠛⠋⠉⣉⣡⣽⠟⠀⠀⠀⠀
⠀⣿⢦⣌⢿⣽⣌⠉⠘⣿⣿⡏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⣵⣿⣿⠋⠀⠀⢀⣠⣴⣾⡿⠯⣷⠆⠀⠀⠀⠀⠀
⢀⣿⣦⣉⡛⢿⣿⡂⠀⢸⣿⣇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣸⣿⣿⠃⠀⣤⡾⠟⠉⠁⣀⣤⡶⠟⠀⠀⠀⠀⠀⠀
⢸⡿⢯⣿⣽⣦⠋⠻⠆⢸⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣿⣿⠃⠀⠀⠀⣠⣤⠶⣛⣉⣡⡄⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣔⢍⡻⠿⠦⠀⠀⢸⣿⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢼⣿⠇⠀⠀⠰⠿⠟⠛⠛⠉⣉⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡙⢿⣅⠄⠀⠀⠀⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⣾⡟⠀⠀⠀⠀⣀⣤⡴⠞⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⣤⡈⢻⣦⢙⢻⣾⠀⠀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢻⣿⠃⠀⢠⣶⠿⠭⠦⠤⠤⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⡟⠳⣿⣿⣷⠀⠀⢀⣿⣿⠀⠀⠀⠀⢠⡄⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣯⣾⡟⠀⠀⠀⠀⠀⢀⣰⣤⡶⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣈⡻⢿⣷⡌⠻⠇⠀⣸⣷⣿⠀⠀⠀⢠⣿⣧⣾⣿⣃⣤⡄⠀⠀⠀⠀⠀⠀⠀⣼⢧⣿⠃⠀⣠⣴⠶⢛⣋⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣙⠛⡛⠛⠛⠀⢀⣿⡟⣿⡀⠀⠀⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣰⡟⣾⡟⠀⣀⣤⡴⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠉⢛⣳⣶⠶⠀⢸⣿⣿⣾⣷⡄⢀⣽⣿⣿⣿⡿⢻⡆⠀⠀⠀⠀⠀⣠⣾⢟⣰⡿⠀⠀⠛⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⣿⣯⣤⣤⡄⢸⣿⣿⣿⣯⣿⣞⢿⣿⠟⠁⠀⢸⡇⠀⠀⣀⣴⢿⣫⣷⣿⣿⡇⠀⢴⣦⣆⣆⡌⠙⢷⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠉⢀⣼⢟⣴⡆⠻⣿⣿⣿⣧⢻⣾⠷⢦⣆⠀⠈⣧⣠⣾⢟⣽⣿⣿⣿⣿⡿⠉⢻⣦⡘⣿⡍⠛⠻⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⢃⡈⢿⣿⣿⣾⠏⠀⠀⠈⢷⡄⣿⡿⢡⣾⣿⣿⣿⣿⣟⣅⣰⣮⡻⣷⣬⣿⡆⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠙⠋⣾⣳⣿⢇⣤⢙⣿⡟⠀⠀⠀⠀⠈⣿⣉⣥⣿⣿⣿⣿⣿⣿⣤⣻⣿⣿⡿⡿⠋⠉⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⠿⢋⣿⣿⣏⣾⣿⠃⠀⠀⠀⠀⠀⣿⣧⢹⣿⡟⢻⣟⣿⣮⣿⣿⠿⠏⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠹⣿⣿⣿⡀⠀⠀⠀⣀⣶⣿⡿⢸⣿⣿⣿⠻⣾⣿⠛⠋⠀⠀⠀⣰⣾⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣠⡄⢠⣿⣫⣿⠁⠈⠙⣿⠉⠁⠉⠀⠀⠀⢀⣠⣾⣿⣿⣮⣿⣿⣿⣿⡿⠟⠋⠉⠙⢿⣿⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡟⠀⠀⠀⣿⠀⠀⠀⣀⣠⣴⣿⣿⣿⣿⣿⣿⣶⡶⠛⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣦⠀⠀⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⣿⡟⠙⣿⣧⣶⣿⠿⢿⣿⣿⣿⡿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣛⡿⢿⣿⣿⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣦⣾⣷⣶⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣟⠁⠀⠀⠀⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⢿⣧⡴⢾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡿⣷⣿⣿⣷⣿⣿⣿⣿⣿⠛⠛⠛⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⢿⡿⣽⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⢿⣿⡟⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡄⠉⠁⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠇⠀⠀⠀⠀⠀⠀"""
            print(articuno)
            
        elif nome_validacao == 'zapdos':
            print('Este é o Zapdos, Pokémon lendário do tipo elétrico')
            soneca(2)
            zapdos = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⡿
⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣄⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⢀⣴⣿⠇⠀⠀⠀⠀⠀⠀⠀⣠⣶⡿⢀⣀⠀⠀⠀⠀⠀⣀⣠⣴⡶⠿⠛⣩⣿⠟⠁⠀
⠈⠻⣿⣟⡿⢶⣦⣤⣀⠀⠀⠀⣤⣀⡀⠈⣿⣿⣷⣄⠀⠀⠀⠀⢸⣿⡆⠀⠀⠀⠀⣰⣿⣿⠇⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣶⣿⠟⢀⣀⣤⣶⠿⠛⣭⠅⠀⣠⣾⠟⠁⠀⠀⠀
⠀⠀⠈⠙⢿⣦⡀⠉⠛⠻⠷⣦⣽⣿⣿⣷⣾⣿⣞⢿⣷⡀⣤⡀⢸⣿⣿⡀⠀⢠⣾⢟⣿⠃⠀⠀⠀⠀⢀⣴⡿⣫⣿⣿⣿⣿⣷⠿⠛⠋⠁⠀⠀⠀⢀⣴⡿⢋⣀⣀⣀⣀⣤⠀
⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀⠈⠙⠛⠿⢿⣿⣿⣞⢿⣿⣿⣿⣾⣿⢹⣷⣰⡿⣧⣿⣏⣠⣤⣶⣿⣿⠟⠉⣴⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀
⠀⠀⠀⠀⠸⢿⣶⣾⣿⣷⣦⡀⠀⠀⠀⠀⠀⠈⠉⠉⠈⢻⣯⠉⠙⣿⡄⣿⢟⣼⣿⠿⣻⣽⣿⣿⣿⣷⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣦⣄⠀⠘⣋⠛⠃⠀⠀⠀⠻⣷⡀⣿⡀⠀⣾⣿⠇⠀⠉⠉⣁⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠉⠛⠿⣿⣷⣄⡉⠀⠀⠀⠀⠀⢀⣽⣿⣿⣧⣴⣿⣿⢀⣤⣴⣾⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣟⣋⣁⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠿⢿⣿⣟⣛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⣠⣿⣯⣿⣿⣿⣿⡿⠙⣛⡉⠀⠘⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⣉⣉⣭⣽⡿⠿⠟⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠷⣶⣤⣤⣀⡀⠀⠀⠀⠛⢩⣿⣿⣿⣿⣿⢷⣦⣿⣿⠷⣶⣼⣿⣧⡀⠀⠀⠀⠀⠀⢀⣀⣤⣤⡶⠾⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣶⣶⠀⠀⣽⣿⣿⠋⠀⠀⠙⠻⣿⡆⠀⠈⠉⠛⠃⢠⣤⣴⡾⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡟⠁⣀⣼⣿⣿⢿⣦⡀⠀⠀⢀⣿⣶⣶⣤⣀⠀⠀⠈⣻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣻⣿⡿⣩⣿⣿⣿⡄⠀⣸⣿⠏⠻⣿⡙⠻⣷⣿⣿⡋⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣯⣜⣿⣿⣿⡿⢱⣿⣥⣿⣿⡆⠀⢻⣿⣇⣀⣿⣧⠀⣿⣿⡟⠻⢷⣮⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢻⣿⣿⣿⣿⣿⣵⣿⣿⣿⡿⣿⡇⠀⠀⢻⣿⠿⣿⣿⣾⣿⣿⣠⣶⣿⣿⡿⠿⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⣿⣿⣿⣿⠟⠁⠀⢀⣼⣿⣦⠀⠸⠟⢿⣮⣿⣿⣿⣿⣿⣿⣯⣥⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠟⠉⠀⠀⠀⠈⣿⣿⡇⢀⣴⡿⢋⡘⠿⠀⠀⠀⠀⣨⣿⣿⣿⣿⠿⠿⠿⠿⠿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⣿⣫⣴⣿⡃⣀⡀⠀⡀⠀⣿⣿⣟⡙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⡟⣰⣿⡇⢸⣿⣄⠻⣿⣿⣿⣶⣽⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⣿⢿⡟⣰⣿⣿⣿⣾⣿⣿⣶⡾⣿⠻⠿⠙⠛⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡟⣿⣿⡇⣾⢿⣿⡿⣷⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠏⠀⠛⠹⣷⣿⠀⠙⠃⠘⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠙⠃⠀⠀"""
            print(zapdos)
            
        elif nome_validacao == 'mew':
            print('Este é o Mew, Pokémon lendário do tipo psíquico')
            soneca(2)
            mew = """⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⢳⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠋⠀⢰⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢆⣤⡞⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢠⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣾⢳⠀⠀⠀⠀⢸⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⡤⠴⠊⠉⠀⠀⠈⠳⡀⠀⠀⠘⢎⠢⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠳⣄⠀⠀⡠⡤⡀⠀⠘⣇⡀⠀⠀⠀⠉⠓⠒⠺⠭⢵⣦⡀⠀⠀⠀
⠀⢹⡆⠀⢷⡇⠁⠀⠀⣸⠇⠀⠀⠀⠀⠀⢠⢤⠀⠀⠘⢷⣆⡀⠀
⠀⠀⠘⠒⢤⡄⠖⢾⣭⣤⣄⠀⡔⢢⠀⡀⠎⣸⠀⠀⠀⠀⠹⣿⡀
⠀⠀⢀⡤⠜⠃⠀⠀⠘⠛⣿⢸⠀⡼⢠⠃⣤⡟⠀⠀⠀⠀⠀⣿⡇
⠀⠀⠸⠶⠖⢏⠀⠀⢀⡤⠤⠇⣴⠏⡾⢱⡏⠁⠀⠀⠀⠀⢠⣿⠃
⠀⠀⠀⠀⠀⠈⣇⡀⠿⠀⠀⠀⡽⣰⢶⡼⠇⠀⠀⠀⠀⣠⣿⠟⠀
⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⡶⠤⣷⣅⡀⠀⠀⠀⣀⡠⢔⠕⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠫⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀"""
            print(mew)
            
        elif nome_validacao == 'mewtwo':
            print('Este é o Mewtwo, Pokémon lendário do tipo psíquico')
            soneca(2)
            mewtwo = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⠀⠀⠀⠀⣸⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡞⣿⣷⣮⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡝⢿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⠸⣸⣻⣏⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⡿⡀⠀⠀⠀⠀⠀⣾⡞⡝⣿⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠩⣾⣿⣶⢦⣤⣀⠸⠻⢭⣥⡻⣧⠀⡙⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⢠⣴⣾⣿⣿⣿⣏⣶⣾⡽⣿⣷⣟⣿⣿⣿⣻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠸⣿⡿⠘⠻⢿⣿⣿⠟⠛⠿⠿⠃⢍⣿⣿⢸⣿⣿⣿⡽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣟⠛⠛⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣜⢿⣿⡿⡷⡿⣼⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⠃⠀⠀⠀⠈⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣯⣾⣿⡀⠀⠙⠻⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⢻⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣧⡀⠀⠀⠀⠙⢿⣧⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣬⣽⣿⣿⢟⣛⣳⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣷⢻⣾⣿⣿⣷⡽⣄⠀⠀⢀⣾⣿⣷⣄⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣄⡀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⢹⣦⠀⢸⣇⠀⠹⣏⢧⡀
⠀⠀⠀⠀⠀⠀⠹⣿⣷⡀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⢸⣿⡄⠈⠛⠀⣶⠟⠼⠇
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⣤⡀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣿⡿⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣶⣄⠀⠀⠈⠻⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⡿⣱⣿⣿⣿⣿⢟⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣧⡀⠀⠀⠈⠻⢿⣿⢸⣿⣿⣿⡿⢟⣫⣾⣿⣿⠿⣛⣵⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣾⣿⡟⠙⠚⠛⠛⠋⠉⠀⠘⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠁⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣯⢻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠘⠻⣿⣿⣷⣶⣒⣒⢢⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⣏⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠟⠈⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡿⠿⠿⠿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀"""
            print(mewtwo)
    while True:
        try:
            altura_str = input(" ▸ Altura (em metros, > 0): ").strip()
            if not altura_str:
                print(" ❌ Este campo não pode ficar em branco.")
                continue
            altura = float(altura_str)
            if altura > 0:
                break
            print(" ❌ A altura deve ser maior que 0.")
        except ValueError:
            print(" ❌ Valor inválido! Digite um número decimal.")
    
    while True:
        try:
            peso_str = input(" ▸ Peso (em kg, > 0): ").strip()
            if not peso_str:
                print(" ❌ Este campo não pode ficar em branco.")
                continue
            peso = float(peso_str)
            if peso > 0:
                break
            print(" ❌ O peso deve ser maior que 0.")
        except ValueError:
            print(" ❌ Valor inválido! Digite um número decimal.")
    
    while True:
        tipo = input(" ▸ Tipo Primário: ").strip()
        if tipo:
            break
        print(" ❌ Este campo não pode ficar em branco.")
    
    while True:
        resp_lendario = input(" ▸ É Lendário? (S/N): ").strip().lower()
        if resp_lendario in ['s', 'n']:
            lendario = (resp_lendario == 's')
            break
        print(" ❌ Responda com 'S' ou 'N'.")
    
    while True:
        resp_shiny = input(" ▸ É Shiny? (S/N): ").strip().lower()
        if resp_shiny in ['s', 'n']:
            shiny = (resp_shiny == 's')
            break
        print(" ❌ Responda com 'S' ou 'N'.")
    
    while True:
        try:
            iv_str = input(" ▸ Valor do IV (0 a 31): ").strip()
            if not iv_str:
                print(" ❌ Este campo não pode ficar em branco.")
                continue
            iv = float(iv_str)
            if 0 <= iv <= 31:
                break
            print(" ❌ IV deve estar entre 0 e 31.")
        except ValueError:
            print(" ❌ Valor inválido!")
    
    while True:
        try:
            ev_str = input(" ▸ Valor do EV (0 a 252): ").strip()
            if not ev_str:
                print(" ❌ Este campo não pode ficar em branco.")
                continue
            ev = float(ev_str)
            if 0 <= ev <= 252:
                break
            print(" ❌ EV deve estar entre 0 e 252.")
        except ValueError:
            print(" ❌ Valor inválido!")
    
    while True:
        resp_var = input(" ▸ Possui variação regional? (S/N): ").strip().lower()
        if resp_var in ['s', 'n']:
            break
        print(" ❌ Responda com 'S' ou 'N'.")
    
    forma_regional = "Normal"
    if resp_var == 's':
        while True:
            forma_regional = input(" ▸ Qual região ele está? ").strip()
            if forma_regional:
                break
            print(" ❌ Este campo não pode ficar em branco.")
        
    tipo_alternativo = input(" ▸ Tipo Secundário (Aperte Enter se não houver): ").strip()
    if not tipo_alternativo: 
        tipo_alternativo = "Nenhum"

    # adiciona no inventario as informações
    inventario[p_id] = [nome, altura, peso, tipo, lendario, shiny, iv, ev, forma_regional, tipo_alternativo]
    
    linha("-")
    print_centro(f"✅ '{nome}' registrado com sucesso!")
    linha("-")

#função de remover pokemons do bd. Já com as verificações de erros.
def remover_pokemon(inventario):
    titulo("Remover um Pokémon pela ID")
    
    while True:
        try:
            p_id_str = input(" ▸ Digite o ID a ser removido: ").strip()
            if not p_id_str:
                print(" ❌ Este campo não pode ficar em branco.")
                continue
            p_id = int(p_id_str)
            break
        except ValueError:
            print(" ❌ Valor inválido! Digite um número inteiro.")

    #Remove o id do inventario
    if p_id in inventario:
        removido = inventario.pop(p_id)
        print(f"\n ✅ Pokémon '{removido[0]}' removido com sucesso.")
    else:
        print("\n ❌ Pokémon não localizado na Pokédex.")
        soneca(1)
        imagempsy = """⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣆⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣷⣮⣿⣿⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡠⠒⠉⠀⠀⠀⠀⠀⠀⠈⠁⠲⢖⠒⡀⠀⠀
⠀⠀⠀⡠⠴⣏⠀⢀⡀⠀⢀⡀⠀⠀⠀⡀⠀⠀⡀⠱⡈⢄⠀
⠀⠀⢠⠁⠀⢸⠐⠁⠀⠄⠀⢸⠀⠀⢎⠀⠂⠀⠈⡄⢡⠀⢣
⠀⢀⠂⠀⠀⢸⠈⠢⠤⠤⠐⢁⠄⠒⠢⢁⣂⡐⠊⠀⡄⠀⠸
⠀⡘⠀⠀⠀⢸⠀⢠⠐⠒⠈⠀⠀⠀⠀⠀⠀⠈⢆⠜⠀⠀⢸
⠀⡇⠀⠀⠀⠀⡗⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⢀⠎
⠀⢃⠀⠀⠀⢀⠃⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠷⡃⠀
⠀⠈⠢⣤⠀⠈⠀⠀⠑⠠⠤⣀⣀⣀⣀⣀⡀⠤⠒⠁⠀⢡⠀
⡀⣀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠀
⠑⢄⠉⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀
⠀⠀⠑⠢⢱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀
⠀⠀⠀⠀⢀⠠⠓⠢⠤⣀⣀⡀⠀⠀⣀⣀⡀⠤⠒⠑⢄⠀⠀
⠀⠀⠀⠰⠥⠤⢄⢀⡠⠄⡈⡀⠀⠀⣇⣀⠠⢄⠀⠒⠤⠣⠀"""
        print_ascii(imagempsy)

#função para escolher algum id e atualizar os dados escolhidos. Já com os tratamentos de erros.
def atualizar_pokemon(inventario):
    titulo("Atualizar Dados de um Pokémon")
    
    while True:
        try:
            p_id_str = input(" ▸ Digite a ID do Pokémon a alterar: ").strip()
            if not p_id_str:
                print(" ❌ Este campo não pode ficar em branco.")
                continue
            p_id = int(p_id_str)
            break
        except ValueError:
            print(" ❌ Valor inválido! Digite um número inteiro.")

    #Define os dados no inventario e se é lendario ou shiny
    if p_id in inventario:
        dados = inventario[p_id]
        lend_atual = "Sim" if dados[4] else "Não"
        shiny_atual = "Sim" if dados[5] else "Não"

        #mostra os dados atuais do inventário
        print("\n" + "--- Dados Atuais do Pokémon ---".center(LARGURA))
        print(f"Nome: {dados[0]} | Altura: {dados[1]:.2f}m | Peso: {dados[2]} kg | Tipo: {dados[3]}".center(LARGURA))
        print(f"Lendário: {lend_atual} | Shiny: {shiny_atual} | IV: {dados[6]} | EV: {dados[7]}".center(LARGURA))
        print(f"Forma Regional: {dados[8]} | Tipo Alternativo: {dados[9]}".center(LARGURA))
        print("-" * LARGURA)
        
        print("\nEscolha o campo que deseja alterar:")
        menu_opcoes = "1-Nome | 2-Altura | 3-Peso | 4-Tipo | 5-Lendário | 6-Shiny\n7-IV | 8-EV | 9-Forma Regional | 10-Tipo Alt."
        for linha_op in menu_opcoes.split("\n"):
            print(linha_op.center(LARGURA))

        #Adiciona as opções de qual dado alterar, já com tratamento de erro. Se o dado estiver correto, atualiza ele no inventario pelo ID.
        while True:
            opcao = input("\n ▸ Digite o número do campo (ou Enter para concluir): ").strip()
            if not opcao: break
            
            if opcao == "1":
                while True:
                    nv = input(" ▸ Novo Nome: ").strip()
                    if nv:
                        dados[0] = nv
                        break
                    print(" ❌ O campo não pode ficar em branco.")
            elif opcao == "2":
                while True:
                    try:
                        nv = float(input(" ▸ Nova Altura (> 0): ").strip())
                        if nv > 0:
                            dados[1] = nv
                            break
                        print(" ❌ Deve ser maior que 0.")
                    except ValueError:
                        print(" ❌ Valor inválido!")
            elif opcao == "3":
                while True:
                    try:
                        nv = float(input(" ▸ Novo Peso (> 0): ").strip())
                        if nv > 0:
                            dados[2] = nv
                            break
                        print(" ❌ Deve ser maior que 0.")
                    except ValueError:
                        print(" ❌ Valor inválido!")
            elif opcao == "4":
                while True:
                    nv = input(" ▸ Novo Tipo: ").strip()
                    if nv:
                        dados[3] = nv
                        break
                    print(" ❌ O campo não pode ficar em branco.")
            elif opcao in ["5", "6"]:
                while True:
                    nv = input(" ▸ É Verdadeiro? (S/N): ").strip().lower()
                    if nv in ['s', 'n']:
                        if opcao == "5":
                            dados[4] = (nv == 's')
                        else:
                            dados[5] = (nv == 's')
                        break
                    print(" ❌ Use S ou N")
            elif opcao == "7":
                while True:
                    try:
                        nv = float(input(" ▸ Novo IV (0-31): ").strip())
                        if 0 <= nv <= 31:
                            dados[6] = nv
                            break
                        print(" ❌ Entre 0 e 31.")
                    except ValueError:
                        print(" ❌ Valor inválido!")
            elif opcao == "8":
                while True:
                    try:
                        nv = float(input(" ▸ Novo EV (0-252): ").strip())
                        if 0 <= nv <= 252:
                            dados[7] = nv
                            break
                        print(" ❌ Entre 0 e 252.")
                    except ValueError:
                        print(" ❌ Valor inválido!")
            elif opcao == "9":
                while True:
                    nv = input(" ▸ Nova Forma Regional: ").strip()
                    if nv:
                        dados[8] = nv
                        break
                    print(" ❌ O campo não pode ficar em branco.")
            elif opcao == "10":
                nv = input(" ▸ Novo Tipo Alt: ").strip()
                dados[9] = nv if nv else "Nenhum"
            else:
                print(" ❌ Opção inválida.")

        print('\nAtualizando Pokédex...')
        soneca(1)
        imagemsnorlax = """⠀⠀⠀⠀⠀⠀⠀⢠⣤⣀⠀⠀⠀⠀⢀⣀⣤⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⢀⠀⠀⠀⢸⡿⠛⠛⠛⠛⠛⠉⠛⢿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣿⣿⣿⣄⠀⣼⠀⠀⠀⢂⣀⣀⡀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⡷⠋⠈⠀⠀⠀⠀⠀⠀⠀⠈⠘⠣⡀⠀⠀⠀⠀⠀
⠀⠈⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣦⡀⠀⠀
⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣦⠀
⠀⠀⣼⣿⣿⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⠀⣤⡟⠛⠋⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠈⠋⠈⢿⣿⡿
⢀⡉⠀⠀⣀⣤⣄⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣤⣤⣄⠀⠀⣴⡄
⠘⢇⠀⠰⣿⣿⢟⢼⣿⣿⣿⣿⣿⣿⣿⣿⡿⢜⠿⠿⠿⠀⡀⠀⠀
⠀⠀⠁⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠈⠀⠀⠀"""
        print_ascii(imagemsnorlax)
        print_centro("✅ Dados atualizados com sucesso!")
    else:
        print(" ❌ Pokémon não encontrado.")

#função pra pesquisar um registro no inventario pelo id ou pelo nome
def pesquisar_interface(inventario):
    titulo("Vamos buscar por um Pokémon")
    print("  1 - Pelo ID".center(LARGURA))
    print("  2 - Pelo nome (Busca Linear)".center(LARGURA))
    print("  3 - Pelo nome (Busca Binária)".center(LARGURA))
    print()
    op = input(" ▸ Opção desejada: ").strip()

    #define a pesquisa pelo id, Com tratamentos de erros
    if op == '1':
        while True:
            try:
                p_id_str = input(" ▸ Digite o ID: ").strip()
                if not p_id_str:
                    print(" ❌ Este campo não pode ficar em branco.")
                    continue
                p_id = int(p_id_str)
                break
            except ValueError:
                print(" ❌ Valor inválido! Digite um número inteiro.")

        #Existe o pokemon e mostra as info dele.
        if p_id in inventario:
            d = inventario[p_id]
            poder = (d[6] + d[7]) / 2
            linha("-")
            print(f"[Existe] ID: {p_id} | Nome: {d[0]} | Altura: {d[1]:.2f}m | Peso: {d[2]:.2f}kg | Tipo: {d[3]}")
            print(f"Lendário: {'Sim' if d[4] else 'Não'} | Shiny: {'Sim' if d[5] else 'Não'} | IV: {d[6]:.1f} | EV: {d[7]:.1f} | Poder: {poder:.1f} | Forma: {d[8]} | Alt.: {d[9]}")
            linha("-")
        else:
            print(" ❌ ID não consta no inventário.")
    #se for as duas outras opções, ele decide qual função de busca usar e realiza.
    elif op in ['2', '3']:
        nome = input(" ▸ Nome do Pokémon: ").strip()
        res = busca_linear(inventario, nome) if op == '2' else busca_binaria(inventario, nome)
        if res:
            poder = (res[7] + res[8]) / 2
            linha("-")
            print(f"[Achado] ID: {res[0]} | Nome: {res[1]} | Altura: {res[2]:.2f}m | Peso: {res[3]:.2f}kg | Tipo: {res[4]}")
            print(f"Lendário: {'Sim' if res[5] else 'Não'} | Shiny: {'Sim' if res[6] else 'Não'} | IV: {res[7]:.1f} | EV: {res[8]:.1f} | Poder: {poder:.1f} | Forma: {res[9]} | Alt.: {res[10]}")
            linha("-")
        else:
            print(" ❌ Pokémon não localizado!")
            imagempichu = """ ⣀⣠⣾⢿⣻⣿⣿⣿⣿⣟⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⢧⠀⠀⠀⠀⡀⢤⠰⣴
⣿⢿⣽⣻⣷⣻⣿⣿⣿⣾⣳⢿⣞⡷⣟⣾⢷⣻⣾⣳⢿⡧⠀⠀⠀⢂⠘⢦⣟⣿
⣿⣻⢾⣳⣿⡯⣳⢏⡿⣷⢿⣯⢿⣽⣻⣽⣻⢷⣯⣟⣯⣷⡁⠄⡈⢄⠚⡴⣹⢾
⣿⣽⣻⡟⢻⡇⠀⠉⠘⠿⣿⣞⣯⣟⣷⢯⣟⡿⣾⣽⣳⣿⣽⣾⣵⣮⡷⠾⠑⣿
⣿⢾⣽⡘⢦⣻⡄⠀⠀⠀⠈⠻⣽⢾⣯⣟⣯⢿⣳⣯⡷⣯⠿⠟⠋⠁⠀⠀⢠⣿
⣿⢯⣗⣸⢲⣟⣿⣄⠀⠀⠀⠀⠈⠋⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⢀⣾⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⡤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡔⣏⢽⣻
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢠⢤⡀⠀⠀⠀⠀⠀⢀⡤⣄⠀⠀⠀⢻⣾⡼⣯⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠘⠛⠃⠀⢀⡀⠀⠀⠈⠻⠋⠀⠀⠀⠈⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣳⡴⣶⢦⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢠⣞⡶⣆⠀⢹⣿⢿⣿
⣿⣏⠟⡭⢛⡜⢲⢹⠈⠈⠁⠀⠀⠀⠰⣋⠥⢛⠀⠀⠀⠀⠙⠚⠁⠀⠀⡫⣞⣿
⣿⣜⣣⢜⡡⢎⡱⢎⣧⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⢮⣿
⡿⣞⣷⣯⣽⣾⣽⣾⣽⣻⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿"""
            print_ascii(imagempichu)

#exibir pokemons em ordem definida pelo if
def exibir_pokemons_ordenados(inventario):
    if not inventario:
        print("\n ❌ Você ainda não tem Pokémons cadastrados.")
        return
        
    print("\nDeseja ordenar por:")
    print("  1 - Nome")
    print("  2 - ID")
    op = input(" ▸ Opção: ").strip()
    por_id = (op == '2')

    titulo("🧧 POKÉDEX 🧧")
    
    lista_ordenada = ordenar_inventario(inventario, por_id)
    
    # Reduzindo um pouco o tamanho das colunas para caber melhor na tela
    cabecalho = f"| {'ID':<3} | {'Nome':<12} | {'Tipo':<10} | {'Poder':<5} | {'Lend':<5} | {'Shiny':<5} | {'Alt/Peso':<10} |"
    linha("-")
    print(cabecalho)
    linha("-")

    for p in lista_ordenada:
        lend_str = "Sim" if p[5] else "Não"
        shiny_str = "Sim" if p[6] else "Não"
        poder_total = (p[7] + p[8]) / 2
        medidas = f"{p[2]:.1f}m/{p[3]:.1f}kg"
        
        linha_tabela = f"| {p[0]:<3} | {p[1][:12]:<12} | {p[4][:10]:<10} | {poder_total:<5.1f} | {lend_str:<5} | {shiny_str:<5} | {medidas:<10} |"
        print(linha_tabela)
        
    linha("-")

#Exibe o calculo total das estatisticas dos pokemons
def exibir_estatisticas(inventario):
    titulo("Estatísticas da Pokédex")
    total_itens = len(inventario)
    print(f"  ▸ Total de Pokémons registrados: {total_itens}")

    #realiza os calculos pra cada um dos dados mostrados.
    if total_itens > 0:
        peso_medio = sum(dados[2] for dados in inventario.values()) / total_itens
        print(f"  ▸ Peso médio dos Pokémons: {peso_medio:.2f} kg")
        
        poder_total_geral = sum((dados[6] + dados[7]) / 2 for dados in inventario.values())
        print(f"  ▸ Poder total de combate (IV+EV/2): {poder_total_geral:.2f}")
        
        lendarios = [dados[0] for dados in inventario.values() if dados[4]]
        print(f"  ▸ Quantidade de Pokémons Lendários: {len(lendarios)}")
        if lendarios:
            print("\n    Lista de Lendários:")
            for l in lendarios: print(f"      - {l}")
    else:
        print("  ❌ Sem dados estatísticos disponíveis (base vazia).")
    print()


# ==========================================
# ◓ EXECUTOR COM REPETIÇÃO ◓
# ==========================================
#todo final de operações, dá a opção de repetir pro user
def executar_com_loop(funcao, inventario):
    while True:
        funcao(inventario)
        repetir = input("\n 🔄 Deseja realizar esta mesma operação novamente? (S/N): ").strip().upper()
        if repetir != 'S':
            break



# ==========================================
# ◓ MENU PRINCIPAL ◓
# ==========================================
#puxa a função principal e mostra o menu.
def main():
    hash_u, hash_s = verificar_ou_criar_login()
    
    if not realizar_login(hash_u, hash_s):
        return 
        
    loading = "⬛⬛⬛⬜⬜"
    print_centro(loading)
    soneca(1)
    print_centro("Inciando sistema Pokédex...")
    
    inventario_memoria = carregar_arquivo()
    
    while True:
        soneca(1)
        titulo("MENU DE FUNÇÕES")
        print("  1. Adicionar Pokémon".ljust(40).rjust(LARGURA//2 + 20))
        print("  2. Remover Pokémon por ID".ljust(40).rjust(LARGURA//2 + 20))
        print("  3. Atualizar Dados do Pokémon".ljust(40).rjust(LARGURA//2 + 20))
        print("  4. Pesquisar Pokémon".ljust(40).rjust(LARGURA//2 + 20))
        print("  5. Exibir Todos os Pokémons".ljust(40).rjust(LARGURA//2 + 20))
        print("  6. Exibir Estatísticas".ljust(40).rjust(LARGURA//2 + 20))
        print("  7. Editar Nome de Usuário e/ou Senha".ljust(40).rjust(LARGURA//2 + 20))
        print("  8. Salvar e Sair".ljust(40).rjust(LARGURA//2 + 20))
        linha("◓")
        print()
            
        opcao = input(" ▸ Selecione uma opção: ").strip()
        print()
        print_centro(loading)
        soneca(1)

        #puxa as funções dependendo da opção escolhida
        if opcao == '1':
            executar_com_loop(adicionar_pokemon, inventario_memoria)
        elif opcao == '2':
            executar_com_loop(remover_pokemon, inventario_memoria)
        elif opcao == '3':
            executar_com_loop(atualizar_pokemon, inventario_memoria)
        elif opcao == '4':
            executar_com_loop(pesquisar_interface, inventario_memoria)
        elif opcao == '5':
            executar_com_loop(exibir_pokemons_ordenados, inventario_memoria)
        elif opcao == '6':
            executar_com_loop(exibir_estatisticas, inventario_memoria)
        elif opcao == '7':
            hash_u, hash_s = editar_credenciais(hash_u, hash_s)
        elif opcao == '8':
            print_centro("Cifrando dados Pokémon e atualizando banco de dados externo (CSV)...")
            salvar_arquivo_em_lote(inventario_memoria)
            soneca(1)
            print_centro("✅ Concluído! Sua jornada foi salva em segurança. Até mais, treinador!")
            eeve = """⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
⣿⣧⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⢸⣿⣿
⣿⣿⡄⠘⣷⣤⡉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣥⣶⠇⢠⣿⣿⣿
⣿⣿⣿⣦⠈⠻⣿⣷⣄⠻⡿⠋⠙⠉⠋⠛⢿⡟⢡⣶⣿⡿⠃⣰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣈⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠐⢿⠿⢋⣤⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⡤⠄⠀⠀⠀⢀⠤⡀⢰⣿⡿⠛⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡾⠀⠀⠀⢸⣶⡇⢸⠟⠁⠀⠈⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠁⠤⠬⠤⠄⠉⠀⢀⠀⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢟⣵⢄⣀⡀⠀⠀⣀⣠⣰⣿⡶⣆⡄⣀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣟⣾⡏⣿⣿⣿⣿⣿⣿⣿⡷⣿⣯⣿⣿⣿⣇⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣤⡈⢷⢹⣿⣿⣿⣿⣿⣿⠁⡿⢟⣿⣿⣿⣹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠁⠉⠻⣿⣿⠟⠀⠘⢸⣿⣿⡿⣡⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠘⠀⠀⠀⢠⣭⣭⣵⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠓⠒⠛⠓⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋"""
            print(eeve)            
            break
        else:
            print_centro("❌ Opção inválida! 📢❗️")

if __name__ == "__main__":
    main()

