from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from prompts.rag import TEMPLATE_QUERY_REWRITING


prompt_template = ChatPromptTemplate.from_template(TEMPLATE_QUERY_REWRITING)
generate_queries = (
    prompt_template
    | ChatOpenAI(model="gpt-4o-mini")
    | StrOutputParser()
    | (lambda x: x.split("\n"))
)

generate_queries.invoke({"question": "What is the capital of France?", "num_questions": 5})
# ['1. Which city serves as the capital of France?',
#  "2. Can you tell me the name of France's capital city?",
#  '3. What is the name of the capital city located in France?',
#  '4. Which French city holds the title of the capital?',
#  '5. What city is recognized as the capital of France?']