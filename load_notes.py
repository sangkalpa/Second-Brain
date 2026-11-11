from pathlib import Path
import chromadb

def load_notes(folder):
    notes = []
    for file in Path(folder).rglob("*"):
        notes.append({"source":str(file), "text":file.read_text(encoding = "utf-8").strip()})
    return notes

def print_summary(notes):
    for note in notes:
        print(f"{note['source']} - {len(note['text'])} characters")

def chunk_text(text, size, overlap):
    chunks = []
    for i in range(0,len(text), size - overlap):
        chunks.append(text[i:i + size])
    return chunks

def chunk_notes(notes, size, overlap):
    chunks = []
    for note in notes:
        pieces =  chunk_text(note["text"], size, overlap)
        for piece in pieces:
            chunks.append({"source":note["source"], "text": piece})
    return chunks


    

notes = load_notes("Notes")
print_summary(notes)
all_chunks = chunk_notes(notes, 500, 100)
print(f"{len(all_chunks)} total chunks")

ids = []
documents = []
metadatas = []

for i in range(len(all_chunks)):
    documents.append(all_chunks[i]["text"])
    metadatas.append({"source":all_chunks[i]["source"]})
    ids.append(f"chunk-{i}")

print(len(ids), len(documents), len(metadatas))
print(ids[0])
print(documents[0])
print(metadatas[0])

client = chromadb.Client()
collection = client.create_collection("notes")
collection.add(
    ids = ids,
    documents = documents,
    metadatas = metadatas
)

print(collection.count())