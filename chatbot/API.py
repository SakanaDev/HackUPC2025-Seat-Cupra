from google import genai
#from google.genai import types
import httpx
import pathlib

client = genai.Client(api_key="AIzaSyCuDpqDuQMslHdR4HbMru2Y9DpE94w5UZg")

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

# Retrieve and encode the PDF byte
filepath = pathlib.Path('chatbot/manual_cupra.pdf')
filepath.write_bytes(httpx.get(doc_url).content)

prompt = "eres un asistente virtual experto en ayudar a comprender manuales de usuario para nuevos clientes, responde esto: " + input("Pregunta puta: ")


response = client.models.generate_content(
  model="gemini-2.0-flash",
  contents=[
      genai.types.Part.from_bytes(
        data = filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)

