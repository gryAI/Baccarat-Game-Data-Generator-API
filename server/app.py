from fastapi import FastAPI, Query, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
from dataclasses import dataclass
from game import simulate_baccarat
from game import dataclass_to_dict


# Instantiate limiter
limiter = Limiter(key_func=get_remote_address)

# Instantiate FastAPI with rate limiter
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# FastAPI routing with number of records exception handling
@app.get("/baccarat")
@limiter.limit("5/minute") 
async def get_baccarat(request: Request, num_records: int = Query(1, le=100)):
    if num_records <= 100:
        records = simulate_baccarat(num_records)
        return [dataclass_to_dict(record) for record in records]
        
    else:
        raise HTTPException(
            status_code=400,
            detail="The number of records requested exceeds the limit of 100."
        )