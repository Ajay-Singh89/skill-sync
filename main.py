from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class SkillCreate(BaseModel):
    name: str
    level: str

@app.post("/add-skill")
def add_skill(skill: SkillCreate):
    db = SessionLocal()
    db_skill = models.Skill(name=skill.name, level=skill.level)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    db.close()
    return db_skill

@app.get("/skills")
def get_skills():
    db = SessionLocal()
    skills = db.query(models.Skill).all()
    db.close()
    return skills