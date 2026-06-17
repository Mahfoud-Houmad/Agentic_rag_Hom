from google import genai
from google.genai import types

INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""

USER_PROMPT_TEMPLATE = """
Question:
{question}

Context:
{context}
"""

gemini_client = genai.Client()

class RAGBase:
  def __init__(self, index, llm_client= gemini_client, instructions = INSTRUCTIONS, prompt_template = USER_PROMPT_TEMPLATE, model = 'gemini-2.5-flash'):
      self.index = index 
      self.instructions = instructions
      self.prompt_template = prompt_template
      self.model = model
      self.llm_client = llm_client
      
  def search(self , query , num_results = 5):
      return self.index.search(
      query, 
      num_results=num_results
    )

  def build_context(self, search_results):
      lines = []

      for doc in search_results:
          lines.append(doc["filename"])
          lines.append("Content: " + doc["content"])
          lines.append("")

      return "\n".join(lines).strip()

  def build_prompt(self, query, search_results):
      context = self.build_context(search_results)
      prompt = self.prompt_template.format(
          question=query,
          context=context
      )
      return prompt.strip()

  def llm(self, query):
      response = self.llm_client.models.generate_content(
          model=self.model,
          contents= query,
          config= types.GenerateContentConfig(
              system_instruction= self.instructions
          )
      )
      return response

  def rag(self, query):
      search_results = self.search(query)
      prompt = self.build_prompt(query, search_results)
      response = self.llm(prompt)
      answer = response.text
      return response,answer