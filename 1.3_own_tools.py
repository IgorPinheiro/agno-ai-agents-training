from doctest import debug
from agno.agent import Agent
from agno.models.groq import Groq
# from agno.models.deepseek import DeepSeek
from agno.tools.yfinance import YFinanceTools
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()


def celsius_to_fh(temperatura_celsius: float):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
        temperatura_celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (temperatura_celsius * 9/5) + 32

agent = Agent(
    name="Analyst",
    tools=[YFinanceTools(),
           TavilyTools(),
           celsius_to_fh],
    # model=DeepSeek(id="deepseek-reasoner"),
    model=Groq(id="llama-3.3-70b-versatile"),
    debug_mode=True,
    instructions='Use tabelas para mostrar informações finais. Não inclua nenhum outro texto a não ser o graus celcius e sua conversão em Fahrenheit ao lado na tablea',
)
agent.print_response("Preciso ganhar dinheiro com automatização de whats-app com agno, como faço para começar.", markdown=True, stream=True)