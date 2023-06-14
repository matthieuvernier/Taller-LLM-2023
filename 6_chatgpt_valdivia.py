from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
print("Lectura de los vectores, por favor esperar...")
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

#Acceso al LLM
query_engine = index.as_query_engine()


while True:
    # Solicitar al usuario ingresar una cadena
    pregunta = input("Ingresa una pregunta ('stop' para terminar): ")

    # Verificar si el usuario quiere detener el programa
    if pregunta.lower() == "stop":
        break

    print("Pregunta:", pregunta)

    #Solicita respuesta a ChatGPT
    response = query_engine.query(pregunta)
    print(response)

