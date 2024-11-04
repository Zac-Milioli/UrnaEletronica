"""
Versão que executa a urna localmente
"""
from os import system
from src.models.election import Election
from src.models.candidate import Candidate

election = Election({
            "1": Candidate(name="Angela Pepino", code='1', party="PMDB"),
            "2": Candidate(name="Gean da Silva", code='2', party='PT'),
            "3": Candidate(name='Cesar Souza Neto', code='3', party="DEM")
            })
WINNER = None

while election.is_active:
    system('cls')
    print(election.get_candidates)
    print("\nDeseja votar ou encerrar?\n[1] Votar\n[ENTER] Encerrar\n")
    option = input('...')
    if option == "1":
        print("\n\nVotar em quem?\n")
        vote = input('...')
        election.vote_for(vote)
    else:
        WINNER = election.end_election

system('cls')
print(election.get_candidates)
print(f"\n{WINNER =}")
