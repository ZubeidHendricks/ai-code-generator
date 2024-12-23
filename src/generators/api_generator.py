class APIGenerator:
   def __init__(self, llm):
       self.llm = llm

   def generate_endpoint(self, specs):
       prompt = f'''
Create API endpoint:
- Method: {specs.get('method')}
- Path: {specs.get('path')}
- Params: {specs.get('params', [])}
Include validation, error handling, tests'''
       return self.llm(prompt)

   def generate_model(self, specs):
       prompt = f'''
Create database model:
- Name: {specs.get('name')}
- Fields: {specs.get('fields', [])}
Include validation, relations, migrations'''
       return self.llm(prompt)
