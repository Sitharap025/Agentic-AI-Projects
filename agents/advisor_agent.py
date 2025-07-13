import os
from settings import GROQ_API_KEY, OPENAI_API_KEY
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain

def advisor_agent(component, failure_reason, docs):
    # Combine the page contents of relevant documents
    context = "\n\n".join([doc.page_content for doc in docs])

    # Define the prompt template
    prompt = ChatPromptTemplate.from_template("""
You are an experienced maintenance advisor.

Component at risk: {component}
Reason: {reason}

Relevant historical and SOP data:
{context}

Based on this, recommend:
- Specific inspection or replacement steps
- Urgency level
- Timeframe for next checkup

Your answer should be actionable and clear.
""")

    # Use Groq's LLaMA3 model
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="llama3-70b-8192"
    )

    # Build the chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain and return the result
    response = chain.invoke({
        "component": component,
        "reason": failure_reason,
        "context": context
    })

    return response['text']

