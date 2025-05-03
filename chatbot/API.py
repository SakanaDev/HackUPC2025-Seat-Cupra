from google import genai
#from google.genai import types
import httpx
import pathlib

client = genai.Client(api_key="AIzaSyCuDpqDuQMslHdR4HbMru2Y9DpE94w5UZg")

doc_url = "https://hackupc2025.slack.com/files/U08NSQU4G1Z/F08QU6K8HKM/cupra_tavascan_owners_manual_11_24_gb.pdf"

# Retrieve and encode the PDF byte
filepath = pathlib.Path('manual_cupra.pdf')

prompt = "eres un asistente virtual experto en ayudar a comprender manuales de usuario para nuevos clientes, responde esto sobre mi CUPRA Tavascan: " + input("¿En que puedo ayudarle?\n")


response = client.models.generate_content(
  model="gemini-2.0-flash",
  contents=[
      genai.types.Part.from_bytes(
        data = filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)

