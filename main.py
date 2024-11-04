"""
## Arquivo principal

É o ponto de partida da urna
"""
from fastapi import FastAPI
import uvicorn
from src.models.election import Election
from src.models.candidate import Candidate

app = FastAPI()

election = Election({
            "1": Candidate(name="Angela Pepino", code='1', party="PMDB"),
            "2": Candidate(name="Gean da Silva", code='2', party='PT'),
            "3": Candidate(name='Cesar Souza Neto', code='3', party="DEM")
            })

@app.post("/api/vote/{code}")
async def vote(code: str) -> str:
    """
    Endpoint para votar
    """
    return election.vote_for(code)

@app.get("/candidates")
async def get_all_candidates() -> dict:
    """
    Endpoint para buscar candidatos
    """
    candidates = election.get_candidates.copy()
    for key, value in candidates.items():
        candidates[key] = value.get_dict
    return candidates

@app.get("/candidates/{code}")
async def get_one_candidate(code: str) -> dict:
    """
    Endpoint para retornar apenas um candidato
    """
    response = election.get_candidate(code)
    if response == 404:
        return {"status": response, "message": "Candidato não encontrado"}
    return response.get_dict

@app.get("/api/end")
async def finish_election() -> dict | list[dict]:
    """
    Endpoint para encerrar as eleições
    """
    return election.end_election

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
