from agno.models.groq import Groq
#from agno.models.openai import OpenAI
from agno.models.message import Message
from dotenv import load_dotenv

load_dotenv()


model = Groq(id="llama-3.3-70b-versatile")

message = Message(
    role="user",
    content=[{'type': 'text', 'text': 'Olá, meu nome é Igor Pinheiro e estou contruindo um aggente de IA com sua base llama 3.3-70b-versatile'}]
    
)

assistant_message = Message(
    role="assistant",
    content=''
)

response = model.invoke(messages=[message], assistant_message=assistant_message )


print(response.content)