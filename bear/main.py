from __future__ import annotations
import random
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

FACTS_FILE = "bear_facts.txt"

app = FastAPI()

class Fact(BaseModel):
    fact: str

with open(FACTS_FILE, "r") as f:
    facts = f.readlines()

@app.get("/")
async def root():
    return {'message': 'Hello World!  Welcome to Bear Facts'}

@app.get("/fact")
async def get_bear_fact(index: str | None = None):
    if index is None:
        index = random.randint(0, len(facts) - 1)
    return {index: facts[int(index)].strip()}

@app.post("/add/")
async def add_a_new_bear_fact(fact: Fact):
    with open(FACTS_FILE, "a") as f:
        f.write("\n")
        f.write(fact.fact)
    return fact


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)





