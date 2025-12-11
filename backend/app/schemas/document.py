# from pydantic import BaseModel
# from datetime import datetime
# from uuid import UUID


# class DocumentResponse(BaseModel):
#     id: UUID
#     filename: str
#     file_size: int
#     uploaded_at: datetime

#     class Config:
#         from_attributes = True


# class DocumentListResponse(BaseModel):
#     documents: list[DocumentResponse]


# class DocumentResponse(BaseModel):
#     id: UUID
#     filename: str
#     message: str

from pydantic import BaseModel
from datetime import datetime

class DocumentListResponse(BaseModel):
    filename: str
    file_size: int

class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_size: int
    created_at: datetime

    class Config:
        from_attributes = True

