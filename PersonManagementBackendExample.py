from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Dict

app = FastAPI()

# Persistent list (global variable)
persons_db: List[Dict[str, int | str]] = [
    {"id": 1, "name": "Pekka", "age": 20},
    {"id": 2, "name": "Kalle", "age": 30},
]

# Separate model for requests (no ID required)
class PersonCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=20)
    age: int = Field(..., ge=18, le=100)

# Model for responses (includes ID)
class Person(PersonCreate):
    id: int

# Dependency function that returns the same persons list
def get_persons_data() -> List[Dict[str, int | str]]:
    return persons_db  # Returns the global list reference

@app.get("/")
def home():
    return {"message": "Welcome to Person management server"}

@app.get("/persons", response_model=List[Person])
def get_persons(persons=Depends(get_persons_data)):
    return [Person(**p) for p in persons]  # Convert list of dicts to Pydantic models

@app.get("/persons/{id}", response_model=Person)
def get_person(id: int, persons=Depends(get_persons_data)):
    person = next((p for p in persons if p["id"] == id), None)
    if person:
        return Person(**person)  # Convert dict to `Person` model
    raise HTTPException(status_code=404, detail=f"No person with id {id}")

@app.post("/persons", response_model=Person, status_code=201)
def add_person(person: PersonCreate, persons=Depends(get_persons_data)):
    if any(p["name"].lower() == person.name.lower() for p in persons):
        raise HTTPException(status_code=400, detail="Person with this name already exists.")

    new_person = {
        "id": max(p["id"] for p in persons) + 1 if persons else 1,  # Auto-increment ID
        "name": person.name,
        "age": person.age,
    }
    persons.append(new_person)  # Modify the global list
    return Person(**new_person)  # Convert dict to `Person` model before returning

@app.delete("/persons/{id}")
def delete_person(id: int, persons=Depends(get_persons_data)):
    global persons_db  # Ensure global reference
    person = next((p for p in persons if p["id"] == id), None)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    persons_db = [p for p in persons if p["id"] != id]  # Reassign to modify the list
    return {"message": "Person deleted"}
