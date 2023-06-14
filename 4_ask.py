from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
print("Lectura de los vectores...")
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

#Acceso al LLM
query_engine = index.as_query_engine()

pregunta="""
Explicame en detalles cuáles fueron las principales problemáticas ambientales el año pasado en la ciudad de Valdivia. 
Dame fechas precisas y descripción de algunos eventos vinculados a problemáticas ambientales occuridos en 2022 o 2023. 
Idealmente, por cada evento agrega la URL de una noticia que habla de este evento. Organiza tu respuesta con bullet points.

Finalmente, actúa como la alcaldesa de Valdivia y propone tres medidas para ayudar a resolver la problemática 
de la calidad ambiental en la ciudad. Explica tus medidas con argumentos y datos concretos sobre Valdivia.

Elabora una respuesta en aproximadamente 1.000 palabras.
"""
print(pregunta)

response = query_engine.query(pregunta)
print(response)
