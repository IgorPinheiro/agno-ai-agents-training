from agno.agent import Agent
# from agno.models.groq import Groq
from agno.models.deepseek import DeepSeek
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Analyst",
    tools=[YFinanceTools()],
    model=DeepSeek(id="deepseek-reasoner"),
    instructions='Use tabelas para mostrar informações finais. Não inclua nenhum outro texto',
)
agent.print_response("Qual a cotação atual da Petrobras?", markdown=True, stream=True)