import os

# file extensions we care about
ALLOWED_EXTENSIONS = (
    ".py", ".js", ".ts", ".java", ".cpp", ".c", ".go",
    ".rs", ".php", ".html", ".css", ".json", ".md"
)

# folders we should ignore
IGNORE_DIRS = {
    ".git", "node_modules", "venv", "__pycache__", ".idea", ".vscode"
}

def load_codebase(repo_path: str):
    """
    Reads all code files from the given repository path.
    Returns a list of dicts: {file_path, content}
    """
    code_files = []

    for root, dirs, files in os.walk(repo_path):
        # skip unwanted directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file.endswith(ALLOWED_EXTENSIONS):
                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    code_files.append({
                        "file_path": full_path,
                        "content": content
                    })

                except Exception:
                    # skip files that can't be read
                    continue

    return code_files
