from transformers import AutoTokenizer,T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
#model = AutoModelForSeq2SeqLM.from_pretrained("grammarly/coedit-large")

#gram='helo this was wonderfull event organising tommorrow'
#input_ids = tokenizer(gram, return_tensors="pt").input_ids

model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")
#input_text = 'Fix grammatical errors in this sentence: When I grew up, I start to undersand what he said  quite is right and you shloud learn that to told her about ur feeelings on her but carefullly you had to tell. im very trieard from working night and day in officee so make my mood today a cup of caffe please'

def grammar(text):
    e_text=''
    #for i in range(0, (len(text)//100)+1):
        #input_ids = tokenizer([text[i*100:(i+1)*100]],return_tensors="pt").input_ids
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=256)
    edited_text = tokenizer.decode(outputs[0],skip_special_tokens=True)#, 
    e_text=e_text+edited_text+ ' '

    return e_text

#labels = tokenizer("<extra_id_0> cute dog <extra_id_1> the <extra_id_2>", return_tensors="pt").input_ids
#outputs = model.generate(input_ids,early_stopping=True)
#print(outputs)
# Decode the generated summary
#summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

# inference
# input_ids = tokenizer(
#     "summarize: studies have shown that owning a dog is good for you", return_tensors="pt").input_ids  # Batch size 1outputs = model.generate(input_ids)
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))


#gram='helo this was wonderfull event organised tommorrow'

#print(grammar(input_text))
