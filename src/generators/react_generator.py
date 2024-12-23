class ReactGenerator:
   def __init__(self, llm):
       self.llm = llm

   def generate_component(self, specs):
       prompt = f'''
Create React component:
- Name: {specs.get('name', 'Component')}
- Props: {specs.get('props', [])}
- Features: {specs.get('features', [])}
Include TypeScript, error handling, tests'''
       return self.llm(prompt)

   def generate_hook(self, specs):
       prompt = f'''
Create React hook:
- Name: {specs.get('name')}
- Functionality: {specs.get('functionality')}
Include types, error handling, example'''
       return self.llm(prompt)
