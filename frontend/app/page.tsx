'use client';

import { useEffect, useState } from "react";
import DocUpload from "./DocUpload";
import DocList from "./DocList";
import { Document } from "./types";

export default function DocumentsPage() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const getDocuments = async () => {
    try {
      const res = await fetch("http://localhost:8000/documents");
      const data = await res.json();
      setDocuments(data);
    } catch {
      setMessage("Failed to load documents");
    }
  };

  useEffect(() => {
    getDocuments();
  }, []);

  const showSuccess = (msg: string) => {
    setMessage(msg);
    getDocuments();
  };

  const showError = (msg: string) => setMessage(msg);

  return (
    <div className="max-w-2xl mx-auto py-10 space-y-6">
      <h1 className="text-3xl font-bold">Document Manager</h1>

      {message && (
        <div className="p-3 bg-blue-100 border border-blue-300 rounded text-blue-700">
          {message}
        </div>
      )}

      <DocUpload 
        onSuccess={showSuccess} 
        onError={showError} 
      />

      <DocList 
        documents={documents} 
        refresh={getDocuments} 
        onError={showError}
      />
    </div>
  );
}
