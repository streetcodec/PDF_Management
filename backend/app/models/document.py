# from sqlalchemy import Column, String, Integer, DateTime
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from datetime import datetime
# from app.core.database import Base


# class Document(Base):
#     __tablename__ = "documents"

#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
#     filename = Column(String, nullable=False)
#     file_path = Column(String, nullable=False)
#     file_size = Column(Integer, nullable=False)
#     content_type = Column(String, nullable=False)
#     uploaded_at = Column(DateTime, default=datetime.utcnow)
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
