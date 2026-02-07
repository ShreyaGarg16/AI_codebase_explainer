import { useState } from "react";
import { askCodebase } from "../api";

export default function AskPanel() {
  const [repo, setRepo] = useState("backend");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleAsk() {
    setLoading(true);
    setAnswer("");
    const res = await askCodebase(repo, question);
    setAnswer(res.answer);
    setLoading(false);
  }

  return (
    <>
      <label>Repository / Folder</label>
      <input value={repo} onChange={(e) => setRepo(e.target.value)} />

      <label>Question</label>
      <textarea
        rows={4}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={handleAsk}>
        {loading ? "Analyzing…" : "Ask AI"}
      </button>

      {answer && (
        <div className="answer">
          <h3>AI Response</h3>
          <pre>{answer}</pre>
        </div>
      )}
    </>
  );
}
