from doctest import debug
from agno.agent import Agent
from agno.models.groq import Groq
# from agno.models.deepseek import DeepSeek
from agno.tools.yfinance import YFinanceTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
import os

load_dotenv()

# Configurando o meu database em PostgresSQL
db = SqliteDb(db_file='tmp/agno_storage_conversation.db')


agent = Agent(
    name="Analista Petrobras",
    # session_id='petrobras_session', # Serve para dar mais inteligência ao agente que estamos criando, passando referência sobre o assunto.  
    # user_id='analista_petrobras', # Serve para dar mais inteligência ao agente que estamos criando.
    tools=[YFinanceTools(),
           TavilyTools()],
    # model=DeepSeek(id="deepseek-reasoner"),
    model=Groq(id="llama-3.3-70b-versatile"),
    db=db, # Configurando o meu agente com o database.
    enable_user_memories=True,
    debug_mode=False,
    
    instructions='Você é um analista e tem diferentes clientes. Lembre-se de cada cliente, suas informações e preferências',
    # instructions='Faça uma pesquisa pela pessoa e mostre todo o histórico de vida dele, sendo nome completo, idade, ano, dia e mês que ele nasceu, tudo isso em uma tabela',
    add_history_to_context=True, # Historiar o contexto da conversa.
    num_history_runs=7,
    
)
agent.print_response("Qual a cotação da Apple?", session_id='apple_session', user_id='analista_apple')
agent.print_response("Qual a cotação da Vale?", session_id='vale_session', user_id='analista_vale')
agent.print_response("Qual a cotação da Petrobrás?", session_id='petrobras_session', user_id='analista_petrobras')
agent.print_response("Qual a cotação da Nvidia?", session_id='nvidia_session', user_id='analista_nvidia')
agent.print_response("Quais empresas já consultamos a cotação?", session_id='petrobras_session', user_id='analista_empresa')
# agent.print_response('Quais empresas que solicitei cotação anteriormente?')