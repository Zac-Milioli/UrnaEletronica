"""
Testes unitários para Candidate
"""
from src.models.candidate import Candidate

class TestCandidate:
    """
    Classe para testes de Candidate
    """
    def test_01_create_candidate(self):
        """
        Testa se o candidato é instanciado adequadamente
        """
        candidate = Candidate(name="test", code="test", party="test")
        assert candidate.name == "test"
        assert candidate.code == "test"
        assert candidate.party == "test"
        assert candidate.get_votes == 0

    def test_02_get_candidate_dict(self):
        """
        Testa se o dict retornado pela classe está sendo construído corretamente
        """
        candidate = Candidate(name="test", code="test", party="test")
        candidate_dict = candidate.get_dict
        assert candidate_dict["name"] == candidate.name
        assert candidate_dict["code"] == candidate.code
        assert candidate_dict["party"] == candidate.party
        assert candidate_dict["votes"] == candidate.get_votes

    def test_03_vote_for_candidate(self):
        """
        Testa o sistema de votação do candidato
        """
        candidate = Candidate(name="test", code="test", party="test")
        candidate.vote_for()
        assert candidate.get_votes == 1
        candidate.vote_for()
        assert candidate.get_votes == 2
