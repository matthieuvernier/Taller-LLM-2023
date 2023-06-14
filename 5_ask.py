from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
print("Lectura de los vectores...")
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

#Acceso al LLM
query_engine = index.as_query_engine()

pregunta="""
Actúa como un periodista, escribe una noticia de aproximadamente 1.000 palabras que describe los logros obtenidos
en la ciudad de Valdivia en tema de seguridad en 2022 y 2023, mencionando los principales desafios aun no resueltos.
Da datos y ejemplos precisos en tu articulo.
"""
print(pregunta)

response = query_engine.query(pregunta)
print(response)
