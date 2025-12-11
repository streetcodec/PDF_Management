import os
import shutil
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.models.document import Document
from app.core.config import settings

def save_document(db: Session, file: UploadFile, content: bytes, file_size: int):
    """
    Save file metadata + file system storage.
    """
    temp_doc = Document(filename="", file_size=file_size)
    db.add(temp_doc)
    db.commit()
    db.refresh(temp_doc)

    base_name = os.path.splitext(file.filename)[0]
    final_filename = f"{base_name}_{temp_doc.id}.pdf"

    file_path = "storage/" + final_filename
    with open(file_path, "wb") as f:
        f.write(content)

    temp_doc.filename = final_filename
    db.commit()
    db.refresh(temp_doc)

    return temp_doc

def list_documents(db: Session):
    return db.query(Document).all()

def get_document(db: Session, doc_id: int):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc


def delete_document(db: Session, doc_id: int):   
    doc = get_document(db, doc_id)
    file_path = os.path.join(settings.STORAGE_PATH, doc.filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    db.delete(doc)
    db.commit()
