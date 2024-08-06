from fastapi import FastAPI, Query
from game import simulate_baccarat
from dataclasses import asdict
from typing import Dict, Any

app = FastAPI()

@app.get("/baccarat")
def get_baccarat_single():
    return asdict(simulate_baccarat())