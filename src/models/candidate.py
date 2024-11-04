"""
## Candidatos

Esta classe define o objeto Candidates, que são os candidatos à prefeito
"""
class Candidate:
    """
    ## Candidate

    ```
    name: str
    code: int
    party: str
    votes: int = 0
    ```
    """
    def __init__(self, name: str = "default", code: str = '0',
                    party: str = "sem partido", votes: int = 0):
        self.name: str = name
        self.code: str = code
        self.party: str = party
        self._votes: int = votes

    @property
    def get_votes(self) -> int:
        """
        Retorna a quantidade de votos do candidato
        """
        return self._votes

    @property
    def get_dict(self) -> dict:
        """
        Retorna um dicionário com os dados do candidato
        """
        return {
            "code": self.code,
            "name": self.name,
            "party": self.party,
            "votes": self._votes
            }

    def vote_for(self) -> None:
        """
        Adiciona um voto ao candidato
        """
        self._votes += 1

    def __repr__(self) -> str:
        part1 = f"\n\tcandidate:\t{self.name}\n\tcode:\t\t{self.code}"
        part2 = f"\n\tparty:\t\t{self.party}\n\tvotes:\t\t{self.get_votes}\n"
        text = part1+part2
        return text
