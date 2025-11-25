from fastapi import FastAPI
from pydantic import BaseModel, Field
import random
import re
app = FastAPI()


class PasswordGeneratorRequest(BaseModel):
    length: int = Field(12,ge=8, le=25)
    include_uppercase: bool = True
    include_lowercase: bool = True
    include_digits: bool = True
    include_symbols: bool = True

class PasswordResponse(BaseModel):
    password: str
    strength: str
    score: str
    massage: str | None = None

class PasswordCheckRequest(BaseModel):
    password: str = Field(..., min_length=8)

@app.get("/")
async def root():
    return {"massage": "Welcome to the Password Generator API"}

def check_password_strength(password: str) -> dict():
    scop = 0
    feedback = []

    if len(password) <= 8:
        scop += 1
    else:
        feedback.append('Must be at least 8 characters.')

    if re.search(r'[a-z]', password):
        scop += 1
    else:
        feedback.append('It must have at least one lowercase letter.')

    if re.search(r'[A-Z]', password):
        scop += 1
    else:
        feedback.append('It must have at least one uppercase letter.')

    if re.search(r'/d', password):
        scop += 1
    else:
        feedback.append('It must have at least one digits.')

    if re.search(r'[!@#$%^&*()<>?/\"|}{~:]', password):
        scop += 1
    else:
        feedback.append('It must have at least one special character.')

    if scop == 5:
        strength = 'very_strong'
    elif scop == 4:
        strength = 'strong'
    elif scop == 3:
        strength = 'medium'
    else:
        strength = 'weak'

    return {
        'scop': scop,
        'strength': strength,
        'massage': 'Great! The password is very secure.' if scop == 4 else ( ','.join(feedback)+ 'Add'),
    }



@app.post('/generate')
async def generate(password: str):
    pass

@app.post('/check')
async def check(password: str):
    pass



