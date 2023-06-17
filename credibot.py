import openai
import config
from PyPDF2 import PdfReader


# Indica el API Key
openai.api_key = config.api_key 

#Lectura de las politicas
pdf_file_obj = open('POLITICAS.pdf', 'rb')
pdf_reader = PdfReader(pdf_file_obj)
page_obj = pdf_reader.pages[0]
text = page_obj.extract_text()

def run():
    #contexto del asistente
    messages = [{"role": "system",
                 "content": "Eres un experto en politicas internas de una financiera, para saber si los grupos se apruebas o no; las politicas de la financiera son " + text + " me podrias ayudar a contestar dudas"}]
    
    content = input("\n En que te puedo ayudar?: ")
    
    while True:
        if content == "exit":
            break
        
        messages.append({"role": "user", "content": content})
        
        response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
                                                messages= messages)
        
        response_content = response.choices[0].message.content
        
        messages.append({"role":"assistant", "content": response_content})
        
        print(response_content)
        
        content = input("\n")
    

if __name__ == '__main__':
    run()