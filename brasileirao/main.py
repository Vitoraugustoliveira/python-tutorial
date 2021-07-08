import pandas as pd
import pdb
# ler os datasets
# definir os dados de entrada (data inicial, data final e nome do time)
# fazer select (selecionar) os registros (as linhas) que estão no período exigido e para o time exigido
# contar a quantidade de partidas no periodo e multiplicar por 3 (é o meu máximo)
# contar exatamente o quantos pontos o time fez, ver quantos empates e multiplicar por 1, ver vitorias multiplicar por 3 e somar isso
# por fim, basta dividir o resultado anterior pelo do maximo possivel a ser obtido e temos o desempenho



def read_dataset(path, sep):
    """
    path: path to dataset file
    return: Dataframe -> pandas type
    """
    return pd.read_csv(path, sep=sep)


def convert_date(dataset):
    dataset["Data"] = pd.to_datetime(dataset["Data"], format='%d/%m/%Y')
    return dataset

def get_point(host_score, visitant_score):
    if host_score > visitant_score:
        return 3
    elif host_score < visitant_score:
        return 0
    elif host_score == visitant_score:
        return 1

def find_status_final(dataset, club):
    matrix = []
    for line in dataset.iterrows():
        if not (line[1]["Mandante"].lower() == club or line[1]["Visitante"].lower() == club):
            continue
        host_score = get_point(line[1]["Mandante Placar"], line[1]["Visitante Placar"])
        visitant_score = get_point(line[1]["Visitante Placar"], line[1]["Mandante Placar"])

        content = [line[1]["Data"], line[1]["Mandante"], line[1]["Visitante"], host_score, visitant_score]
        matrix.append(content)
    header = ["Data", "Mandante", "Visitante", "Mandante Pontos", "Visitante Pontos"]
    dataframe = pd.DataFrame(matrix, columns = header)
    return dataframe

def filter_period(begin_date, end_date, dataset):
    after_start_date = dataset["Data"] >= begin_date
    before_end_date = dataset["Data"] <= end_date
    between_two_dates = after_start_date & before_end_date
    filtered_dates = dataset.loc[between_two_dates]
    return filtered_dates

def max_perfomance(dataset):
    quantity_matches = len(dataset.index)
    return quantity_matches*3

def get_perfomance(dataset, club):
    score_total = 0
    for line in dataset.iterrows():
        score_total = score_total + line[1]["Mandante Pontos"] if line[1]["Mandante"].lower() == club else score_total + line[1]["Visitante Pontos"]
    return score_total

def main():
    relative_path_to_dataset = "datasets/campeonato-brasileiro-full.csv"
    dataset = read_dataset(relative_path_to_dataset, ";")
    dataset = convert_date(dataset)
    club = "cruzeiro"
    begin_date="2013-01-01"
    end_date = "2014-12-31"
    dataset_club = find_status_final(dataset, club)
    dataset_filtered = filter_period(begin_date, end_date, dataset_club)
    print(dataset_filtered)
    score_total_club = get_perfomance(dataset_filtered, club)
    print(score_total_club)
    print(score_total_club/max_perfomance(dataset_filtered))

main()