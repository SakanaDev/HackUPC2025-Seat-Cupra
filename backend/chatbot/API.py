from google import genai
#from google.genai import types
import httpx
import pathlib
import json

client = genai.Client(api_key = "AIzaSyCuDpqDuQMslHdR4HbMru2Y9DpE94w5UZg")

#doc_url = "https://hackupc2025.slack.com/files/U08NSQU4G1Z/F08QU6K8HKM/cupra_tavascan_owners_manual_11_24_gb.pdf"

# Retrieve and encode the PDF byte
script_dir = pathlib.Path(__file__).parent
filepath = script_dir / 'manual_cupra.pdf'

### Entrada ###
prompt = """You're a virtual asisstant specialised in helping new customers understand the owner's manual, 
            so help me with my new Cupra TAVASCAN: """ + input("¿Hello! How can I help you?\n>")

### Procesamiento de la respuesta ###
response = client.models.generate_content(
  model = "gemini-2.0-flash",
  contents = [
      genai.types.Part.from_bytes(
        data = filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])


### Devolucion ###
print(response.text)
messagge = {}
messagge['chatbot'] = response.text
with open('chatbot/data.json', 'w') as f :
    archivo = json.dump(messagge, f) # creacion y guardado del json