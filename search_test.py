import chromadb

client = chromadb.Client()
collection = client.create_collection("test")
collection.add(
    ids = ["1", "2", "3", "4"],
    documents= ["netwon has 3 laws", "I play goal keeper",
                "I like pasta", "Python is the most used language"]
)

questions = ["what do u cook","what do u code","do you like soccer"]
results = collection.query(
    query_texts = questions,
    n_results = 4
)
for q, docs, dists in zip(questions, results["documents"], results["distances"]):
    print(f"{q} --> {docs[0]} ({dists[0]:.3f}) | 2nd: {docs[1]} ({dists[1]:.3f})")
