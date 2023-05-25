import os
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from llama_index import LangchainEmbedding
from llama_index.llm_predictor.chatgpt import ChatGPTLLMPredictor
from llama_index import ServiceContext, load_index_from_storage
llm = AzureChatOpenAI(deployment_name=deployment_name,temperature=0.2,
                      openai_api_version=openai_api_version)

llm_predictor = ChatGPTLLMPredictor(llm=llm, retry_on_throttling=False)
embedding_llm = LangchainEmbedding(OpenAIEmbeddings(model="text-embedding-ada-002", chunk_size=1, openai_api_version=openai_api_version))


# Define prompt helper
max_input_size = 3000
num_output = 256
chunk_size_limit = 1000
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size=max_input_size, 
                             num_output=num_output, 
                             max_chunk_overlap=max_chunk_overlap, 
                             chunk_size_limit=chunk_size_limit)

# Define service_context 
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, embed_model=embedding_llm, prompt_helper=prompt_helper)

# Read txt files from data directory
index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
print("storage folder created")
