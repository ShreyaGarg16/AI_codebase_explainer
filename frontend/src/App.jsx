import "./styles/app.css";
import AskPanel from "./components/AskPanel";

export default function App() {
  return (
    <div className="wrapper">
      <div className="navbar">
        <h1>AI Codebase Explainer & Debug Assistant</h1>
      </div>

      <div className="container">
      <section className="hero">
        <p>
          Ask natural language questions about large codebases.
          This system understands entire repositories and helps
          you explain logic and debug faster.
        </p>

        <div className="ideas">
          <div className="idea">Understand unfamiliar repositories</div>
          <div className="idea">Locate bugs & logical issues</div>
          <div className="idea">Built for real-world GitHub projects</div>
        </div>
      </section>

      <section className="try-box">
        <div className="try-card">
          <AskPanel />
        </div>
      </section>
    </div>
    </div>
  );
}
