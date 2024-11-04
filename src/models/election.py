"""
## Classe referente à eleição como um todo
"""
from pandas import DataFrame
from .candidate import Candidate

class Election:
    """
    ## Election

    Define os candidatos disponíveis e suas respectivas informações

    ```
    candidates: dict
    ```
    """
    def __init__(self):
        self.is_active = True
        self.candidates: dict = {
            "1": Candidate(name="Angela Pepino", code='1', party="PMDB"),
            "2": Candidate(name="Gean da Silva", code='2', party='PT'),
            "3": Candidate(name='Cesar Souza Neto', code='3', party="DEM"),
            "n": Candidate(name="Voto Nulo", code='n'),
            "b": Candidate(name="Voto em Branco", code='b')
        }

    @property
    def most_voted(self) -> Candidate | list[Candidate]:
        """
        Retorna o candidato com maior número de votos, ou múltiplos em caso de empate
        """
        max_vote_number = -1
        most_votes = []
        for candidate in self.candidates.values():
            if candidate.code in ['n', 'b']:
                continue
            if candidate.get_votes > max_vote_number:
                max_vote_number = candidate.get_votes
                most_votes = [candidate]
            elif candidate.get_votes == max_vote_number:
                most_votes.append(candidate)

        if len(most_votes) == 1:
            return most_votes[0].get_dict
        most_votes_list = []
        for option in most_votes:
            most_votes_list.append(option.get_dict)
        return most_votes_list

    @property
    def end_election(self) -> Candidate | list[Candidate]:
        """
        Finaliza a eleição, gera um arquivo com resultados e indica o vencedor
        """
        candidates = [candidate.get_dict for candidate in self.candidates.values()]
        df = DataFrame(candidates)
        df.to_csv("resultados.csv", sep=';', encoding='latin-1')
        self.is_active = False
        return self.most_voted

    def get_candidate(self, option: str) -> Candidate:
        """
        Retorna o candidato com código equivalente ao inserido, senão `None`
        """
        return self.candidates.get(option, 404)

    def vote_for(self, code: str) -> str:
        """
        Adiciona 1 voto ao candidato
        """
        candidate = self.get_candidate(code)
        if candidate != 404 and self.is_active:
            candidate.vote_for()
            return "OK"
        return "ERROR"

    @property
    def get_candidates(self) -> dict[str: Candidate]:
        """
        Retorna o dicionário contendo os candidatos
        """
        return self.candidates
