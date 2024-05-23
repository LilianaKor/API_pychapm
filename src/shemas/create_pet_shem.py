from pydantic import BaseModel, Field, field_validator

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel) :
    id: int
    name: str

class CreatePetShema(BaseModel):
    id: int
    name: str
    category: Category
    photoUrls: list[str] = []
    tag: list[Tag] = []
    status: str