from django.shortcuts import render
import openai

openai.api_key = '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'

def chat(message):
    response = openai.Completion.create(engine='text-davinci-003', prompt = message,max_tokens = 4000)
    return response

def image(message):
    response = openai.Image.create(prompt = message,
    size = '256x256',
    n = 1,
    response_format = 'url')

    return response

def index(request):
    if request.method == "GET":
        message = request.GET.get('message')
        # if "image" in message:
        #     img_response = image(message).data[0]['url']
        #     return render(request, 'index.html', {'image':img_response})
        # else:
        if message:
            if "image" in message:
                img_response = image(message).data[0]['url']
                return render(request, 'index.html', {'image':img_response})
            else:
                chat_response = chat(message).choices[0].text
                return render(request, 'index.html', {'chat': chat_response})
        else:
            return render(request, 'index.html')
    else:
        return render(request,'index.html')
