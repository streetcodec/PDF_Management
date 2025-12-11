from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pathlib import Path

from app.core.database import get_db
from app.core.config import settings
from app.schemas.document import DocumentResponse
from app.services import document_service

router = APIRouter()

UPLOAD_DIR = Path(settings.STORAGE_PATH)
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/documents/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    content = await file.read()
    file_size = len(content)

    if file_size > settings.MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    document = document_service.save_document(
        db=db,
        file=file,
        content=content,
        file_size=file_size,
    )

    return DocumentResponse(
        id=document.id,
        filename=document.filename,
        file_size=document.file_size,
        created_at=document.created_at,
    )


@router.get("/documents", response_model=list[DocumentResponse])
def list_documents(db: Session = Depends(get_db)):
    return document_service.list_documents(db)


@router.get("/documents/{document_id}")
def download_document(document_id: int, db: Session = Depends(get_db)):
    document = document_service.get_document(db, document_id)

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    file_path = UPLOAD_DIR / document.filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found on disk")

    return FileResponse(
        path=str(file_path),
        filename=document.filename,
        media_type="application/pdf",
    )


@router.delete("/documents/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    """Delete a specific document"""

    document_service.delete_document(db, document_id)

    return {"message": "Document deleted successfully"}
