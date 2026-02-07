export default function AnswerBox({ answer }) {
  return (
    <div className="card">
      <h3>AI Response</h3>
      <pre>{answer}</pre>
    </div>
  );
}
