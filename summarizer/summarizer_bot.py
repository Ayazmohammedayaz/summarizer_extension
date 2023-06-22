#from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import AutoTokenizer, BartForConditionalGeneration
import youtube_transcript_api
#from transformers import AutoTokenizer,T5ForConditionalGeneration
from youtube_transcript_api import YouTubeTranscriptApi
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
# mname = "facebook/blenderbot-400M-distill"
# model = BlenderbotForConditionalGeneration.from_pretrained(mname)
# tokenizer = BlenderbotTokenizer.from_pretrained(mname)
#from transformers import T5ForConditionalGeneration, T5Tokenizer
#model_name = 't5-base'
#model = T5ForConditionalGeneration.from_pretrained(model_name)
#tokenizer = T5Tokenizer.from_pretrained(model_name)
#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
#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
import openai
openai.api_key="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"

# with open("C:/Users/afree/Desktop/etxt_summ.txt",'r',encoding='utf-8') as f:
#     file=f.read()
#print('hello')



def chat(uinput):
    inputs = tokenizer([uinput], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    chat_resp=tokenizer.batch_decode(reply_ids)
    #print(tokenizer.batch_decode(reply_ids))
    #chat_resp.encoding
    return chat_resp


def chatt5(file):
    inputs = tokenizer.encode("summarize: " +file, return_tensors="pt", max_length=1000, truncation=True)
    #print(inputs)
# Generate the summary
    outputs = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)
#print(outputs)
# Decode the generated summary
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

def summary_api(url):
    
    #url = request.args.get('url', '')
    video_id = url.split('.be/')[1]
   #video_id='https://youtu.be/vzLmRomOP4Q'
    summary = summarizer(get_transcript(video_id))
    return summary
    #return summary, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript
    
    
def summarizer(file):
    summary = ''
    for i in range(0, (len(file)//1000)+1):
        inputs = tokenizer([file[i*1000:(i+1)*1000]], max_length=1024, return_tensors="pt",truncation=True)
        summary_ids = model.generate(inputs["input_ids"], num_beams=4,min_length=0, max_length=30)
        summary_text=tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        summary = summary + summary_text + ' '
        
    return summary

def sum_gpt(file):
    response = openai.Completion.create(
    engine='text-davinci-003',
    prompt='Summarize the following text in 5 lines:' +str(file),
    max_tokens=120)

    summary = response.choices[0].text.strip()
    return summary
    

    


# while 1:
#      uinput= input()
#      if uinput=='quit':
#          exit(0)
#      y=chat(uinput)
#      print(type(y))
#      print(y)  

#  chat nakko question answers ka daalo
#  aur grammarly T5ForConditionalGeneration
#  yetta hua to iske baad zara text additons karna starting 
#  final allah ke naam po extension bana dalna
#  chalya to khushi ke ansoon 
#  last mein traing ka ek test baakhi rehta kaisa karna seekna lekin capable hai kya from django.utils.translation import ugettext_lazy as _
