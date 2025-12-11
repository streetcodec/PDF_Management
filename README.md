# PDF Portal

A patient portal where users (patients) can upload and manage their medical documents (PDFs).


## Core requirements met

### A. Frontend Application
- Form to upload a PDF file ✅
- List all uploaded files ✅
- Download and delete buttons for each file ✅.
- Display messages on success/failure ✅

### B. Backend API Service
- REST APIs to:
    - Upload a file (PDF only) ✅
    - List all uploaded files ✅
    - Download a specific file ✅
    - Delete a file ✅
- Store uploaded files in a local uploads/ folder ✅
- Save metadata to a database (e.g., filename, upload date, file size) ✅
### C. Database
- Store file metadata in a table (e.g., id, filename, size, created_at) ✅
- Use SQLite, PostgreSQL, or similar ✅.
- No need to implement user login — assume one user for simplicity ✅




## Tech Stack

### Backend 
- FastAPI
- Postgres SQL (Docker)
- SQLAlchemy
- Python

### Frontend
- NextJS 15
- React
- TailwindCSS
- TypeScript

## Local Setup
- Clone the repository
    ```
    git clone https://github.com/streetcodec/PDF_Management.git

    ```
### Backend

- 📦 Install Dependencies
    ```
    cd backend
    pip install -r requirements.txt
    ```
- ▶️ Run FastAPI Server
   ```
   uvicorn app.main:app --reload

   ```
- Backend runs on 8000 port

### Database setup
- Navigate to the Docker file 
    ```
    cd backend
    ```
- Run the file (Ubuntu) 
    ```
    docker pull postgres:15

    docker run -d \
    --name pair_postgres \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=dbname \
    -p 5432:5432 \
    -v pgdata:/var/lib/postgresql/data \
    postgres:15

    ```
- Run the file (Windows)
    ```
    docker run -d --name pair_postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=dbname -p 5432:5432 -v pgdata:/var/lib/postgresql/data postgres:15

    ```
- Run the file (Mac)
    ```
    docker run -d --name pair_postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=dbname -p 5432:5432 -v pgdata:/var/lib/postgresql/data postgres:15
    ```
### Frontend

- 📦 Install dependencies
    ```
    cd frontend
    npm install

    ```
- Run the development server:
    ```
    npm run dev

    ```

