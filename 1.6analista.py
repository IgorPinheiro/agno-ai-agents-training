from doctest import debug
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
# from agno.models.deepseek import DeepSeek
from agno.tools.yfinance import YFinanceTools
from agno.tools.tavily import TavilyTools
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.semantic import SemanticChunking
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.vectordb.chroma import ChromaDb
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
import os

from openai import api_key

load_dotenv()

# STORAGE ================================================
# Setup the SQLite database
db = SqliteDb(db_file='tmp/agno_storage_conversation.db')


# RAG =====================================================
# Inicialize ChromaDB
vector_db = ChromaDb(
    collection='empresas_relatorios',
    path='tmp/chromadb',
    embedder=OpenAIEmbedder(id='text-embedding-3-small', api_key=os.getenv('OPENAI_API_KEY')),
    persistent_client=True
)

# Create Knwledge base
knowledge = Knowledge(
    vector_db=vector_db,
)

# Create a path of file knoledge to Petrobras
knowledge.add_content(
    path='files/PETR/',
    reader=PDFReader(
        chunking_strategy=SemanticChunking()
    ),
    metadata={
        "company": "Petrobras",
        "sector": "Petróleo e Gás",
        "country": "Brazil",
    },
    skip_if_exists=True # Jump to the vectorial database if exists.
)

# Create a path of file knoledge to Vale
knowledge.add_content(
    path='files/VALE/',
    reader=PDFReader(
        chunking_strategy=SemanticChunking()
    ),
    metadata={
        "company": "Vale",
        "sector": "Mineração",
        "country": "Brazil",
    },
    skip_if_exists=True # Jump to the vectorial database if exists.
)

# AGENT =========================================================================

agent = Agent(
    name="Analista_financeiro",
    model=OpenAIChat(id="gpt-5-nano", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[YFinanceTools(),
           TavilyTools()],
    instructions='Você é um analista e tem diferentes clientes. Lembre-se de cada cliente, suas informações e preferências',
    db=db, # Configurando o database para historiar as conversas. 
    debug_mode=False,
    add_history_to_context=True, # adicionar o histórico ao contexto. 
    num_history_runs=7,
    enable_user_memories=True,
    add_memories_to_context=True,
    enable_agentic_memory=True,
    knowledge=knowledge,
    add_knowledge_to_context=True,
     
)
# agent.print_response("Qual a cotação da Apple?", session_id='apple_session', user_id='analista_apple')
agent.print_response("Olá, qual foi o lucro liquido da petrobras em 2T25?", session_id='petrobras_session_4', user_id='analista_petrobras')
agent.print_response("Olá, o que foi comentado sobre o CAPEx da vale no 2T25?", session_id='vale_session_4', user_id='analista_vale')
# agent.print_response("Qual a cotação da Nvidia?", session_id='nvidia_session', user_id='analista_nvidia')
# agent.print_response("Quais empresas já consultamos a cotação?", session_id='petrobras_session', user_id='analista_empresa')
# agent.print_response('Quais empresas que solicitei cotação anteriormente?')