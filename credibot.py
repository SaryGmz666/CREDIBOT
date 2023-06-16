import openai

# Indica el API Key
openai.api_key = "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"

def run():
    # Uso de ChapGPT en Python
    
    
    while True:
        
        prompt = input("\nEn que te puedo ayudar?: ")
        
        if prompt == "exit":
            break
        
        completion = openai.Completion.create(engine= 'text-davinci-003',
                                              prompt=prompt,
                                              max_tokens=2048)

        print(completion.choices[0].text)
    

if __name__ == '__main__':
    run()