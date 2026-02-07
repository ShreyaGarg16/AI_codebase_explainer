const API_BASE = "http://127.0.0.1:8000";

export async function askCodebase(folderPath, question) {
  const response = await fetch(`${API_BASE}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      folder_path: folderPath,
      question: question
    })
  });

  return response.json();
}
