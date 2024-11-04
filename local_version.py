"""
Versão que executa a urna localmente
"""
from os import system
from src.models.election import Election

election = Election()
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
