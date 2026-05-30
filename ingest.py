#Describtion : This is a file which is used to load a document into the chromadb database. It uses the chromadb library to create a client and a collection, and then adds documents to the collection with associated metadata and ids.
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. Load the PDF
def read_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    return pages

# 2. split the PDF into chunks
def split_into_chunks(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    )
    chunks = splitter.split_text(pages)
    return chunks
# 3. convert the chunks into vectors
def convert_to_vectors(chunks):
    # Initialize the embedding model
    embedding_model = chromadb.EasyEmbed()
    vectors = embedding_model.embed_documents(chunks)
    return vectors
# 4. store the vectors in the chromadb database
def store_in_chromadb(vectors):
    pass