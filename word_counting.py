import ray

ray.init()
def count_words(document):
    words = document.split()
    return len(words)

@ray.remote
def count_words_parallel(documents):
    results = [count_words(doc) for doc in documents]
    return results

documents = [
    "This is a sample document.",
    "Ray is a powerful framework for parallel and distributed computing.",
    "Word counting example with Ray cluster."
]

results = ray.get(count_words_parallel.remote(documents))

for i, result in enumerate(results):
    print(f"Document {i + 1}: {result} words")

ray.shutdown()
