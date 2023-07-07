from transformers import AutoTokenizer, BartForConditionalGeneration
import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")


def summary_api(url):
    
   
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


    