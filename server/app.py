from fastapi import FastAPI, HTTPException
from game import simulate_baccarat
from game import dataclass_to_dict
from dataclasses import asdict
from typing import Dict, Any

app = FastAPI()

@app.get("/baccarat")
def get_baccarat(num_records = 1):
    if int(num_records) <= 100:
        records = simulate_baccarat(int(num_records))
        return [dataclass_to_dict(record) for record in records]
    else:
        raise HTTPException(
            status_code = 400,
            detail = 'The number of records requested exceeds the limit of 100.'
        )