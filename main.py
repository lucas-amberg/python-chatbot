import os
import openai


def main():
  openai.api_key = os.getenv('OPENAI_API_KEY')
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
      break
    response = chat_with_gpt(user_input)
    print(f'AI: {response}')

def chat_with_gpt(prompt):
  response = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": prompt}]
  )

  return response.choices[0].message.content.strip()
  

if __name__ == '__main__':
  main()