from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

# Criando um agente
agent = Agent(
    name="Researcher",
    tools=[TavilyTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
    debug_mode=True
)

# Executar uma única vez e finalizar a chamada.
agent.print_response('Use suas ferramentas para pesquisar a temperatura de hoje em Natal')

