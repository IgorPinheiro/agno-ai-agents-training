from doctest import debug
from agno.agent import Agent
from agno.models.groq import Groq
# from agno.models.deepseek import DeepSeek
from agno.tools.yfinance import YFinanceTools
from agno.tools.tavily import TavilyTools
from agno.db.postgres import PostgresDb
from dotenv import load_dotenv
import os

load_dotenv()

# user = os.getenv(DB_USER)
# password = os.getenv(DB_PASSWORD)

# Configurando o meu database em PostgresSQL
db = PostgresDb(
    db_url=(
        f"postgresql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    ),
    session_table="agents_session_tables" # Especifique oa tabela que deseja guardar as seções.
)


agent = Agent(
    name="Analyst",
    tools=[YFinanceTools(),
           TavilyTools()],
    # model=DeepSeek(id="deepseek-reasoner"),
    model=Groq(id="llama-3.3-70b-versatile"),
    db=db, # Configurando o meu agente com o database.
    debug_mode=False,
    
    instructions='Use tabelas para mostrar informações finais. inclua apenas o nome da empresa, data da solicitação o simbolo e o valor da cotação.',
    # instructions='Faça uma pesquisa pela pessoa e mostre todo o histórico de vida dele, sendo nome completo, idade, ano, dia e mês que ele nasceu, tudo isso em uma tabela',
    add_history_to_context=True, # Historiar o contexto da conversa.
    num_history_runs=7,
    
)
agent.print_response("Qual a cotação da Apple?", markdown=True, stream=True)
agent.print_response("Qual a cotação da Vale?", markdown=True, stream=True)
agent.print_response("Qual a cotação da Petrobrás?", markdown=True, stream=True)
agent.print_response("Qual a cotação da Nvidia?", markdown=True, stream=True)
agent.print_response("Quais empresas já consultamos a cotação?", markdown=True, stream=True)
# agent.print_response('Quais empresas que solicitei cotação anteriormente?')