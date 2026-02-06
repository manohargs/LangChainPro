from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "BT is the capital of Slovakia",
    "Vienna is the capital of Austria",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(str(vector))