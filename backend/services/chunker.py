from typing import List, Dict

CHUNK_SIZE = 500        # characters
CHUNK_OVERLAP = 100     # overlap to preserve context

def chunk_code(files: List[Dict]):
    """
    Takes loader output and splits code into chunks.
    Returns list of dicts: {file_path, chunk_id, text}
    """
    chunks = []

    for file in files:
        content = file["text"]
        file_path = file["file_path"]

        start = 0
        chunk_id = 0

        while start < len(content):
            end = start + CHUNK_SIZE
            chunk_text = content[start:end]

            chunks.append({
                "file_path": file_path,
                "chunk_id": chunk_id,
                "text": chunk_text
            })

            chunk_id += 1
            start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks
