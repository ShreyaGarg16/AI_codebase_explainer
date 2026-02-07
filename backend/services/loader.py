"""import os
import shutil
import zipfile
import tempfile
import requests


CODE_EXTENSIONS = {".py", ".js", ".ts", ".java", ".cpp", ".c", ".go", ".rs", ".md"}


# ---------- CORE FILE READER ----------

def _read_code_files(base_path: str):
    files = []

    for root, _, filenames in os.walk(base_path):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext not in CODE_EXTENSIONS:
                continue

            full_path = os.path.join(root, filename)

            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                files.append({
                    "file_path": full_path,
                    "text": content
                })
            except Exception:
                continue

    return files


# ---------- LOCAL FOLDER LOADER ----------

def load_from_folder(folder_path: str):
    if not os.path.exists(folder_path):
        raise ValueError(f"Folder not found: {folder_path}")

    return _read_code_files(folder_path)


# ---------- GITHUB ZIP LOADER ----------

def load_from_github(github_url: str):
    
    Supports URLs like:
    https://github.com/username/repo
    

    if github_url.endswith("/"):
        github_url = github_url[:-1]

    zip_url = github_url + "/archive/refs/heads/main.zip"

    tmp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(tmp_dir, "repo.zip")
    extract_path = os.path.join(tmp_dir, "repo")

    try:
        response = requests.get(zip_url, timeout=30)
        response.raise_for_status()

        with open(zip_path, "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        # GitHub wraps files in a single top-level folder
        extracted_root = os.path.join(extract_path, os.listdir(extract_path)[0])

        return _read_code_files(extracted_root)

    finally:
        # Cleanup AFTER reading
        shutil.rmtree(tmp_dir, ignore_errors=True)
"""
import os
import subprocess
import stat
import shutil

SUPPORTED_EXTENSIONS = (".py", ".js", ".ts", ".java", ".md")

REPO_DIR = "temp_repo"


def load_from_folder(folder_path: str):
    if not os.path.isdir(folder_path):
        raise ValueError(f"Folder not found: {folder_path}")

    files = []

    for root, _, filenames in os.walk(folder_path):
        for name in filenames:
            if name.endswith(SUPPORTED_EXTENSIONS):
                full_path = os.path.join(root, name)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        files.append({
                            "file_path": full_path,
                            "text": f.read()
                        })
                except Exception:
                    pass

    return files


def load_from_github(github_url: str):
    # Clone only once
    if not os.path.exists(REPO_DIR):
        subprocess.run(
            ["git", "clone", github_url, REPO_DIR],
            check=True
        )

    return load_from_folder(REPO_DIR)
