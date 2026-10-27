# Second Brain

The goal of this project is to use my own notes and build a program in Python with Claude that lets me ask questions about my documents and get answers with sources.

## How it works
- **Stage 1 – Load:** `load_notes` reads every note in the `Notes` folder (with UTF-8 encoding) and stores each one as a record with its source and text.
- **Stage 2 – Chunk:** `chunk_notes` splits each note into smaller chunks with overlap, so ideas that fall at the edge of a chunk still appear whole in the next one, and nothing gets lost. Each chunk keeps track of which file it came from.

## Status
- Loading and chunking are finished
- Next: search with embeddings (ChromaDB)
- Then: answering questions with Claude, and a Streamlit app

## What I learned
- Nested loops, and writing functions with different parameters
- Passing data between functions with `return` instead of `print`
- A UTF-8 encoding bug: Python on Windows guessed the wrong encoding when reading my notes, so special characters like the apostrophe in "Newton's" showed up as junk (`â€™`). Fixed by reading files with `encoding="utf-8"`.
- Silent bugs: code that runs without errors but produces wrong data (like losing text between chunks)