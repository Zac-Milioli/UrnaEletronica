"""
Testes unitários para Election
"""
from glob import glob
import os
from src.models.election import Election

class TestElection:
    """
    Classe para testes de Candidate
    """
    def test_01_create_election(self):
        """
        Testa se a eleição é instanciada adequadamente
        """
        election = Election()
        assert isinstance(election.get_candidates, dict)

    def test_02_get_candidate(self):
        """
        Testa o sistema de votos na eleição
        """
        election = Election()
        candidate = {"name": "Angela Pepino"}
        first_candidate = election.get_candidate('1').get_dict
        assert first_candidate["name"] == candidate["name"]

    def test_03_vote_for_candidate_in_election(self):
        """
        Testa o sistema de votos na eleição
        """
        election = Election()
        response_ok = election.vote_for("1")
        assert response_ok == "OK"
        assert election.get_candidate("1").get_votes == 1
        response_error = election.vote_for("error")
        assert response_error == "ERROR"

    def test_04_most_voted(self):
        """
        Testa o sistema de mais votado da eleição
        """
        election = Election()
        candidate_1 = {"name": "Angela Pepino", "votes": 1}
        election.vote_for("1")
        most_voted = election.most_voted
        assert most_voted["name"] == candidate_1["name"]
        assert most_voted["votes"] == candidate_1["votes"]
        candidate_2 = {"name": "Gean da Silva", "votes": 1}
        election.vote_for("2")
        new_most_voted = election.most_voted
        assert isinstance(new_most_voted, list)
        assert new_most_voted[0]["name"] == candidate_1["name"]
        assert new_most_voted[0]["votes"] == candidate_1["votes"]
        assert new_most_voted[1]["name"] == candidate_2["name"]
        assert new_most_voted[1]["votes"] == candidate_2["votes"]

    def test_05_end_election(self):
        """
        Testa a finalização da eleição
        """
        election = Election()
        candidate_1 = {"name": "Angela Pepino", "votes": 1}
        election.vote_for("1")
        most_voted = election.end_election
        globed = glob("resultados.csv")
        assert most_voted["name"] == candidate_1["name"]
        assert len(globed) == 1
        assert election.is_active is False
        os.remove(globed[0])
