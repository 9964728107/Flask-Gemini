# import requests

# # Define the URL of the API endpoint you want to call
# url = "http://127.0.0.1:5000/"

# # Make a GET request to the API
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Print the response content (the data returned by the API)
#     print(response.json())
# else:
#     # If the request was not successful, print the error status code
#     print("Error:", response.status_code)

# import google.generativeai as genai

# genai.configure(api_key="AIzaSyAr6G0NZg0-d75x5LeuoUXpCN1Xu6DcV7A")
# model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)


import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=""

genai.configure(api_key=GOOGLE_API_KEY)

# list of availabe models it seems...
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')    

response = model.generate_content("What is the meaning of life? tell in 5 words")
print(response.text)
to_markdown(response.text)