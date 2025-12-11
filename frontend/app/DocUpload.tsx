'use client';

import { useState } from 'react';

export default function DocUpload({ onSuccess, onError }: any) {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return onError("Please select a PDF");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const res = await fetch("http://localhost:8000/documents/upload", {
        method: "POST",
        body: formData,
      });


const raw = await res.text();


if (!res.ok) {
  onError("Upload failed");
  return;
}

onSuccess("File uploaded successfully");
setFile(null);

    } catch (err) {
      onError("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form 
      onSubmit={handleUpload} 
      className="p-4 border rounded-xl bg-white shadow-sm space-y-3"
    >
      <h2 className="text-xl font-semibold text-black">Upload PDF</h2>

      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        className="block w-full border rounded p-2 text-black/80"
      />

      <button
        type="submit"
        disabled={loading}
        className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded disabled:opacity-50"
      >
        {loading ? "Uploading..." : "Upload"}
      </button>
    </form>
  );
}
