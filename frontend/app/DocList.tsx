'use client';

import { Document } from "./types";

interface Props {
  documents: Document[];
  refresh: () => void;
  onError: (msg: string) => void;
}

export default function DocList({ documents, refresh, onError }: Props) {

  const downloadFile = (id: number) => {
    window.open(`http://localhost:8000/documents/${id}`, "_blank");
  };

  const deleteFile = async (id: number) => {
    try {
      const res = await fetch(`http://localhost:8000/documents/${id}`, {
        method: "DELETE",
      });

      if (!res.ok) throw new Error();
      refresh();
    } catch {
      onError("Delete failed");
    }
  };

  return (
    <div className="mt-6 p-4 border rounded-xl bg-white shadow-sm">
      <h2 className="text-xl font-semibold mb-3 text-black">Uploaded Files</h2>

      {documents.length === 0 && (
        <p className="text-gray-500">No files uploaded.</p>
      )}

      <ul className="space-y-3">
        {documents.map(doc => (
          <li
            key={doc.id}
            className="flex justify-between items-center p-3 border rounded"
          >
            <div>
              <p className="font-medium text-black/90">{doc.filename}</p>
              <p className="text-xs text-gray-500">
                {new Date(doc.created_at).toLocaleString()}
              </p>
            </div>

            <div className="flex gap-2">
              <button
                onClick={() => downloadFile(doc.id)}
                className="px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700"
              >
                Download
              </button>

              <button
                onClick={() => deleteFile(doc.id)}
                className="px-3 py-1 bg-red-600 text-white rounded hover:bg-red-700"
              >
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
