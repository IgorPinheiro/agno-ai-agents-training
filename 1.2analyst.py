from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Analyst",
    tools=[YFinanceTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions='Use tabelas para mostrar a informação final. Não inclua nenhum outro texto',
)
agent.print_response("Qual a cotação atual da APPLE?", markdown=True, stream=True)