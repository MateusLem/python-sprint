# Sprint 1
# Computational Thinking Using Python

## Descrição do Projeto
Este projeto visa aplicar conceitos de pensamento computacional utilizando a linguagem de programação Python. Nele, simulamos a avaliação de desempenho de corredores em uma temporada de corridas, gerando dados fictícios para análise e ordenação. Através deste projeto, é possível entender melhor o uso de estruturas de dados, funções, loops e manipulação de dados em Python.

## AVISO
É necessário o uso de [Python 3.10+](https://www.python.org/downloads/)

## Imports
Estamos utilizando a biblioteca [random](https://docs.python.org/pt-br/3/library/random.html) para simular a avaliação de desempenho dos corredores.

```python
import random
```

## Funções Principais

### generate_racers_data() -> dict
Agrupa os nomes e dados dos corredores. (Simulação do payload esperado). Retorna um dicionário com os nomes (key) e a lista de desempenho dos corredores (value).

```python
def generate_racers_data() -> dict:
    racers_names = [
        "Jake Dennis", "Stoffel Vandoorne", "Sergio Camara", "Robin Frijns", 
        "Jake Hughes", "Maximilian Gunther", "Sam Bird", "Mitch Evans", 
        "Lucas di Grassi", "Antonio Felix da Costa", "Sébastien Buemi", 
        "Norman Nato", "Jehan Daruvala", "Nyck de Vries", "Oliver Rowland", 
        "Sacha Fenestraz", "Jean-Eric Vergne", "Dan Ticktum", "Nick Cassidy", 
        "Edoardo Mortara", "Nico Müller", "Pascal Wehrlein"
    ]
    
    racers_data = {
        racer: [random.randint(0, 100) for races in range(17)] for racer in racers_names
    }

    return racers_data
```

### rank_racers(data) -> list
Ordena os corredores com base no desempenho performado. Retorna uma lista com os corredores (dict) ordenados.

```python
def rank_racers(data) -> list:
    data_copy = data.copy()
    size = len(data_copy)
    recommendation_order = []

    while len(recommendation_order) < size:
        best_racer_name = None
        for i in data_copy:
            if not best_racer_name:
                best_racer_name = i

            desempenho = data_copy[i]

            average_current = sum(desempenho) / len(desempenho)
            average_best_racer_name = sum(data_copy[best_racer_name]) / len(data_copy[best_racer_name])

            if average_current > average_best_racer_name:
                best_racer_name = i

        recommendation_order.append(
            {best_racer_name: sum(data_copy[best_racer_name]) / len(data_copy[best_racer_name])}
        )
        data_copy.pop(best_racer_name)

    return recommendation_order
```

### generate_ranked_racers_names(racers_data) -> list
Retorna uma lista com o nome dos corredores, ordenada pelo seu rank.

```python
def generate_ranked_racers_names(racers_data) -> list:
    return [list(racer_name.keys())[0] for racer_name in racers_data]
```

### show_racers_template(msg, function, parameters) -> None
Template para exibição dos corredores.

```python
def show_racers_template(msg, function, parameters) -> None:
    print("*" * 20)
    print(f"Corredores: {msg}")
    function(parameters)
    print("*" * 20)
```

### show_racer_all(racers_data) -> None
Exibe apenas os nomes dos corredores.

```python
def show_racer_all(racers_data) -> None:
    for racer in racers_data:
        print(f"- {racer}")
```

### show_racers_all_points(racers_data) -> None
Exibe os nomes dos corredores e o desempenho em cada corrida da season.

```python
def show_racers_all_points(racers_data) -> None:
    for racer in racers_data:
        notas = "pts |".join(map(str, racers_data[racer]))
        print(f"{racer} -> {notas}pts")
```

### show_racers_ranking(racers_data) -> None
Exibe o nome dos corredores, seu ranking e seu desempenho médio na season.

```python
def show_racers_ranking(racers_data) -> None:
    racers_ranked = rank_racers(racers_data)

    for rank in range(len(racers_ranked)):
        racer_name = list(racers_ranked[rank].keys())[0]
        print(f"{rank+1}° - {racer_name}: {racers_ranked[rank][racer_name]:.2f}pts")
```

### force_question(msg, lista, error_msg="Valor não encontrado") -> str
Obriga que o usuário dê uma resposta específica. Permite o uso de uma mensagem customizada, tanto de input quanto de erro. Retorna a resposta do usuário.

```python
def force_question(msg, lista, error_msg="Valor não encontrado") -> str:
    var = input(msg)
    while not verify_variable(lista, var):
        if type(error_msg) == str:
            print(error_msg)
        else:
            error_msg(lista)

        var = input(msg)
    return var
```

### verify_variable(lista, var) -> bool
Verifica se uma variável existe em uma lista. Retorna True em caso positivo e False caso negativo.

```python
def verify_variable(lista, var) -> bool:
    for i in range(len(lista)):
        if lista[i].lower() == var.lower():
            return True
    return False
```

### search_variable(lista, var) -> int
Retorna o index de uma variável em uma lista.

```python
def search_variable(lista, var) -> int:
    for i in range(len(lista)):
        if lista[i] == var:
            return i
```

### search_racer(racers_data) -> None
Busca um corredor com base em seu nome. Exibe seu nome, rank e média de desempenho na temporada.

```python
def search_racer(racers_data) -> None:
    racers_ranked = rank_racers(racers_data)
    racers_names = generate_ranked_racers_names(racers_ranked)
    racer_name = force_question("\nNome do corredor: ", racers_names, search_racer_error_message)

    for racer in racers_names:
        if racer_name == racer.lower():
            rank = search_variable(racers_names, racer)
            print("\nRank | Nome | Média de Desempenho")
            print(f"{rank+1}° | {racer} | {racers_ranked[rank][racer]:.2f}pts")
```

### search_racer_error_message(racers_data) -> None
Mensagem de erro para caso o nome do corredor esteja incorreto. Ao final, executa `show_racer_all(racers_data)` para exibir todos os corredores da season.

```python
def search_racer_error_message(racers_data) -> None:
    print("\nCorredor não encontrado!")
    print("Confira a lista de corredores:")
    show_racer_all(racers_data)
```

### close_session() -> bool
Verifica se o usuário realmente quer encerrar o programa.

```python
def close_session() -> bool:
    confirmation_text = "Você tem certeza que deseja sair?(Sim - Nao): "
    confirmation = force_question(confirmation_text, ["Sim", "Nao"])
    if confirmation == "sim":
        return False
    return True
```

### menu() -> None
Exibe o menu de seleção de ações.

```python
def menu() -> None:
    print("\nSelecione um de nossos serviços!!!")
    print("1- Ranking Geral")
    print("2- Listar todos os corredores")
    print("3- Resultados de desempenho nas corridas")
    print("4- Buscar corredor")
    print("5- Sair\n")
```

### executa_servico(escolha, racers_data) -> bool
Verifica a escolha de ação do usuário e age de acordo.

```python
def executa_servico(escolha, racers_data) -> bool:
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
```

### main(continua_execuacao=True) -> None
Função principal de execução do projeto. Nela são inicializadas as variáveis e contém o loop de execução. Ao fim do programa, exibe uma mensagem de encerramento.

```python
def main(continua_execuacao=True) -> None:
    racers_data = generate_racers_data()
    print("Bem Vindo à Formula EX!!!!")

    while continua_execuacao:
        menu()
        escolha = force_question("Escolha um serviço: ", ["1", "2", "3", "4", "5"])
        continua_execuacao = executa_servico(int(escolha), racers_data)

    print("Obrigado pela

 preferência!!!!")
    print("Volte Sempre <3")
```

## Tecnologias utilizadas
<a href="https://www.python.org/downloads/" target="_blank" style="margin-right:10px"><img src="https://img.shields.io/badge/Python-1277c9?style=for-the-badge&logo=python&logoColor=yellow&labelColor=0d4991"></a>

## Colaboradores do Projeto
<div style="display: flex; justify-content: space-between; align-items: center;">
<a href="https://github.com/AnaTorresLoureiro" target="_blank" style="text-align: center; margin-right: 10px;">
<img loading="lazy" src="https://avatars.githubusercontent.com/AnaTorresLoureiro" width=120>
<p style="font-size:min(2vh, 36px); margin-top: 10px;">Ana Laura Torres Loureiro - RM 554375</p>
</a>
<a href="https://github.com/MuriloCngp" target="_blank" style="text-align: center; margin-right: 10px;">
<img loading="lazy" src="https://avatars.githubusercontent.com/MuriloCngp" width=120>
<p style="font-size:min(2vh, 36px); margin-top: 10px;">Murilo Cordeiro Ferreira - RM 556727</p>
</a>
<a href="https://github.com/MateusLem" target="_blank" style="text-align: center; margin-right: 10px;">
<img loading="lazy" src="https://avatars.githubusercontent.com/MateusLem" width=120>
<p style="font-size:min(2vh, 36px); margin-top: 10px;">Mateus da Costa Leme - RM 557803</p>
</a>
<a href="https://github.com/Vitorr-AF" target="_blank" style="text-align: center; margin-right: 10px;">
<img loading="lazy" src="https://avatars.githubusercontent.com/Vitorr-AF" width=120>
<p style="font-size:min(2vh, 36px); margin-top: 10px;">Vitor Augusto França de Oliveira - RM 555469</p>
</a>
<a href="https://github.com/Geronimo-augusto" target="_blank" style="text-align: center; margin-right: 10px;">
<img loading="lazy" src="https://avatars.githubusercontent.com/Geronimo-augusto" width=120>
<p style="font-size:min(2vh, 36px); margin-top: 10px;">Geronimo Augusto Nascimento Santos - RM 557170</p>
</a>
</div>