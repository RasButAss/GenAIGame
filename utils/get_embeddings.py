from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_embedding(text, embedding_model="text-embedding3"):
  text = text.replace("\n", " ")
  embeddings = AzureOpenAIEmbeddings(
    azure_deployment=embedding_model
  )
  response = embeddings.embed_query(text)
  print(f"Embedding model out (OpenAI): {response[0]}")

  return response


#e5 embeddings
def get_e5_embedding(text):
  text = text.replace("\n", " ")
  device = torch.device('cuda' if  torch.cuda.is_available() else 'cpu')
  print(device)
  start=time.time()
  model = SentenceTransformer('intfloat/e5-small').to(device)
  with torch.no_grad():
    embeddings = model.encode(text)
  print(f"Time taken to get embeddings (e5): {time.time()-start}")
  return embeddings

#e5 embeddings
if __name__ == "__main__":
  print(get_embedding("What is the meaning of life?"))