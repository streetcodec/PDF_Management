from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.routers.documents import router as doc_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Heathcare BE")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(doc_router)

@app.get("/")
def root():
    return {"message": "Backend is running"}
