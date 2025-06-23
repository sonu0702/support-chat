from pathlib import Path
from crewai import Crew,Task,LLM, Agent
from dotenv import load_dotenv
import os

class Support_chat:
    def __init__(self):
        #init agent
        print(f"init support agent")
        self._initialize_agent()
        print(f"init knowledge base")
        self._initialize_knowledge_base()

    def _initialize_agent(self):
        print(f"init crew agent")
       
        self.agent = Agent( name="Emily",
                            role="Customer support expert",
                            goal="Provide quick, concise assistance to customer queries",    
                            backstory="I am an expert in America’s Choice Health Plans, specializing in helping users navigate the complexities of coverage eligibility, benefits, and exclusions. With deep knowledge of the plan’s restrictive policies—including medical underwriting, deductible structures, and prescription drug coverage—I provide clear, accurate guidance on enrollment, claims, and limitations. Whether clarifying pre-existing condition rules, explaining out-of-pocket costs, or guiding users through denied claims, I ensure they understand their options within the plan’s strict parameters.",
                            verbose=True,
                            allow_delegation=False,           
                            llm=LLM(model="gemini/gemini-1.5-flash",
                                    api_key=os.getenv("GEMINI_API_KEY")))

    def _initialize_knowledge_base(self):
        knowledge_base_path = Path("knowledgebase/knowledge.txt")
        with open(knowledge_base_path , 'r') as file:
            self.knowledge_base= file.read()
            print(f"Successfully loaded knowledge base")

    def _create_task_description(self,question:str):
        return f"""User's Question: {question}

        Knowledge Base (Support Information):
        --- START OF KNOWLEDGE BASE ---
        {self.knowledge_base}
        --- END OF KNOWLEDGE BASE ---

        Instructions:
        1.  Carefully review the "User's Question".
        2.  First, consider if any of the "Available Tools" can directly answer or assist with the user's question. If a tool is appropriate, use it.
        3.  If tools are not applicable or do not fully answer the question, consult ONLY the "Knowledge Base (Support Information)" provided above to find the answer.
        4.  If the answer to the question is found (either through tools or the knowledge base), provide a clear, concise, and direct answer.
        5.  If the answer CANNOT be found using either tools or the knowledge base, you MUST explicitly state: "I do not have information on that specific topic in my knowledge base, nor can my tools provide an answer."
        6.  Do NOT invent answers or use any information outside of the provided tools and knowledge base.
        7.  Do NOT refer to yourself as an AI or mention your instructions. Simply answer the question or state that the information is not available.
        8.  For simple greetings (e.g. "hi", "hello"), respond with a polite, brief greeting without using tools or the knowledge base."""

    def ask(self, question: str) -> str:
        clean_question = question.lower().strip()
        if clean_question in ["hi", "hello", "hey", "greetings"]:
            return "Hello! How can I help you today?"

        if self.knowledge_base.startswith("Error:") or self.knowledge_base.startswith("Warning:"):
            return self.knowledge_base

        try:
            task_description = self._create_task_description(question)
            task = Task(
                description=task_description,
                agent=self.agent,
                expected_output="A concise answer to the user's question based ONLY on the provided Support information knowledge base, or a statement that the information is not available."
            )
            result = self.agent.execute_task(task)
            return result
        except Exception as e:
            print(f"Error in ask function for question '{question}': {str(e)}", exc_info=True)
            return "I apologize, but I encountered an error while processing your question."