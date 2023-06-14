# Taller: ¿Cómo conectar sus datos a un modelo de lenguaje (LLM)?

# 1. Introducción

## 1.1 ¿Por qué es interesante conectar sus datos a un modelo de lenguaje?

Dar más contexto al modelo puede ayudar a:
- generar respuestas más precisas (?)
- responder a nuevos tipos de preguntas (?)
- adaptarse al vocabulario de un dominio/industria (?)
- ...

## 1.2 Dos enfoques: "LLM finetuning" vs. "Semantic Search + LLM"

**LLM finetuning**:
- Ajustar un modelo preentrenado, reentrenandole con ejemplos adicionales para resolver una tarea más específica.
- Utilizar el modelo con pesos ajustados.

**Semantic Search + LLM**
- Buscar información relevante a partir de una consulta y de colección de documentos.
- Utilizar un modelo pre-entrenado entregandóle un contexto con informacion relevante.

La búsqueda semántica (o Semantic Search) se diferencia de otro concepto similar en Tratamiento Automático del Lenguaje: la Recuperación de Información (o Information Retrieval):
- las técnicas de "Information Retrieval" se basan tradicionalmente en la coincidencia de palabras claves entre las consultas y los documentos, técnicas de ponderación y algoritmos de ranking.
- las técnicas de "Semantic Search" se basan sobre la construcción de vectores matemáticos que representan las dimensions semánticas/el significado de los documentos.

# 2. ¿Qué es LlamaIndex?

Desde marzo 2023, LlamaIndex (inicialmente GPTIndex) es una librería que permite construir aplicaciones que combinan Semantic Search y LLM:
- https://gpt-index.readthedocs.io/en/latest/

¿Qué soluciones aporta?
-   Ofrece conectores de datos (APIs, PDFs, documentos, SQL, etc.)
-   Proporciona formas de estructurar nuestros datos (índices, gráfos)
-   Proporciona una interfaz avanzada para conectarse a cualquier LLM (tipicamente ChatGPT, Falcon, etc.) 

LlamaIndex esta construida arriba de otra nueva librería Langchain (https://python.langchain.com/en/latest/) cuyo objetivo principal es facilitar el desarrollo de aplicaciones que utilizan LLMs.

# 3. Demo

## 3.1 Crearse una cuenta en OpenAI 

- https://platform.openai.com/playground
- crearse una API Key

## 3.2 Configuración del entorno de trabajo

1. Clonear repositorio GitHub: https://github.com/matthieuvernier/Taller-LLM-2023
2. Instalar librerias necesarias 
```pip install -r requirements.txt ```
3. Exportar la API Key como variable de entorno
```export OPENAI_API_KEY="..." ```

## 3.3 Conectarse a OpenAI desde Python 

ver scripts python 1 y 2.

## 3.4 Dataset

Utilizamos un conjunto de aproximadamente 15.000 noticias de prensa sobre Valdivia obtenidas desde el motor de búsqueda Sophia Search.

## 3.5 Uso de LlamaIndex

ver scripts 3, 4, 5 y 6.