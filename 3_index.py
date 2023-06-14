from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

print("Lectura de los datos...")
documents = SimpleDirectoryReader('data').load_data()
print("Vectorización de los datos...")
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist()
print("Vectores guardados en la carpeta ./storage")