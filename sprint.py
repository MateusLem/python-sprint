import random

def generate_racers_data() -> dict:
    # Lista de nomes dos corredores
    racers_names = [
        "Jake Dennis", "Stoffel Vandoorne", "Sergio Camara", "Robin Frijns", 
        "Jake Hughes", "Maximilian Gunther", "Sam Bird", "Mitch Evans", 
        "Lucas di Grassi", "Antonio Felix da Costa", "Sébastien Buemi", 
        "Norman Nato", "Jehan Daruvala", "Nyck de Vries", "Oliver Rowland", 
        "Sacha Fenestraz", "Jean-Eric Vergne", "Dan Ticktum", "Nick Cassidy", 
        "Edoardo Mortara", "Nico Müller", "Pascal Wehrlein"
    ]
    
    # Gera dados de desempenho para cada corredor (17 corridas, pontuações entre 0 e 100)
    racers_data = {
        racer: [random.randint(0, 100) for races in range(17)] for racer in racers_names
    }

    return racers_data

def rank_racers(data) -> list:
    # Cria uma cópia dos dados para preservar o original
    data_copy = data.copy()
    # Tamanho do dicionário de dados dos corredores
    size = len(data_copy)
    # Lista para armazenar a ordem recomendada dos corredores
    recommendation_order = []

    while len(recommendation_order) < size:
        best_racer_name = None
        # Loop para encontrar o corredor com a melhor média de desempenho
        for i in data_copy:
            if not best_racer_name:
                best_racer_name = i

            desempenho = data_copy[i]

            average_current = sum(desempenho) / len(desempenho)
            average_best_racer_name = sum(data_copy[best_racer_name]) / len(data_copy[best_racer_name])

            if average_current > average_best_racer_name:
                best_racer_name = i

        # Adiciona o corredor com a melhor média à lista de recomendação e remove dos dados
        recommendation_order.append(
            {best_racer_name: sum(data_copy[best_racer_name]) / len(data_copy[best_racer_name])}
        )
        data_copy.pop(best_racer_name)

    return recommendation_order

def generate_ranked_racers_names(racers_data) -> list:
    # Extrai os nomes dos corredores ordenados por rank
    return [list(racer_name.keys())[0] for racer_name in racers_data]

def show_racers_template(msg, function, parameters) -> None:
    # Template para exibir informações dos corredores
    print("*" * 20)
    print(f"Corredores: {msg}")
    function(parameters)
    print("*" * 20)

def show_racer_all(racers_data) -> None:
    # Exibe o nome de todos os corredores
    for racer in racers_data:
        print(f"- {racer}")

def show_racers_all_points(racers_data) -> None:
    # Exibe o nome dos corredores e suas pontuações em cada corrida
    for racer in racers_data:
        notas = "pts |".join(map(str, racers_data[racer]))
        print(f"{racer} -> {notas}pts")

def show_racers_ranking(racers_data) -> None:
    # Exibe o ranking dos corredores
    racers_ranked = rank_racers(racers_data)

    for rank in range(len(racers_ranked)):
        racer_name = list(racers_ranked[rank].keys())[0]
        print(f"{rank+1}° - {racer_name}: {racers_ranked[rank][racer_name]:.2f}pts")

def force_question(msg, lista, error_msg="Valor não encontrado") -> str:
    # Força o usuário a responder com um valor específico
    var = input(msg)
    while not verify_variable(lista, var):
        if type(error_msg) == str:
            print(error_msg)
        else:
            error_msg(lista)

        var = input(msg)
    return var

def verify_variable(lista, var) -> bool:
    # Verifica se a variável está na lista (case insensitive)
    for i in range(len(lista)):
        if lista[i].lower() == var.lower():
            return True
    return False

def search_variable(lista, var) -> int:
    # Retorna o índice da variável na lista
    for i in range(len(lista)):
        if lista[i] == var:
            return i

def search_racer(racers_data) -> None:
    # Busca e exibe informações de um corredor específico
    racers_ranked = rank_racers(racers_data)
    racers_names = generate_ranked_racers_names(racers_ranked)
    racer_name = force_question("\nNome do corredor: ", racers_names, search_racer_error_message)

    for racer in racers_names:
        if racer_name == racer.lower():
            rank = search_variable(racers_names, racer)
            print("\nRank | Nome | Média de Desempenho")
            print(f"{rank+1}° | {racer} | {racers_ranked[rank][racer]:.2f}pts")

def search_racer_error_message(racers_data) -> None:
    # Mensagem de erro caso o nome do corredor não seja encontrado
    print("\nCorredor não encontrado!")
    print("Confira a lista de corredores:")
    show_racer_all(racers_data)

def close_session() -> bool:
    # Confirmação para encerrar o programa
    confirmation_text = "Você tem certeza que deseja sair?(Sim - Nao): "
    confirmation = force_question(confirmation_text, ["Sim", "Nao"])
    if confirmation == "sim":
        return False
    return True

def menu() -> None:
    # Exibe o menu de seleção de ações
    print("\nSelecione um de nossos serviços!!!")
    print("1- Ranking Geral")
    print("2- Listar todos os corredores")
    print("3- Resultados de desempenho nas corridas")
    print("4- Buscar corredor")
    print("5- Sair\n")

def executa_servico(escolha, racers_data) -> bool:
    # Executa o serviço selecionado pelo usuário
    match escolha:
        case 1:
            show_racers_template("Recomendados", show_racers_ranking, racers_data)
        case 2:
            show_racers_template("Listagem", show_racer_all, racers_data)
        case 3:
            show_racers_template(" Desempenho", show_racers_all_points, racers_data)
        case 4:
            search_racer(racers_data)
        case 5:
            return close_session()
            
    return True

def main(continua_execuacao=True) -> None:
    # Função principal que inicializa variáveis e contém o loop de execução
    racers_data = generate_racers_data()
    print("Bem Vindo à Formula EX!!!!")

    while continua_execuacao:
        menu()
        escolha = force_question("Escolha um serviço: ", ["1", "2", "3", "4", "5"])
        continua_execuacao = executa_servico(int(escolha), racers_data)

    print("Obrigado pela preferência!!!!")
    print("Volte Sempre <3")

# Executa a função principal
main()
