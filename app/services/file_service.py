from typing import Dict, List
context: Dict[str, List[str]] = {}

def store_chunks(filename: str, chunks: List[str]) -> None:
    context[filename] = chunks

def get_full_context(sep: str = " ") -> str:
    """
    Return every chunk in every file, joined into one big string.
    `sep` is the separator between chunks (default: a single space).
    """
    # Flatten and join in one line:
    return sep.join(chunk
                    for chunks in context.values()
                    for chunk in chunks)
