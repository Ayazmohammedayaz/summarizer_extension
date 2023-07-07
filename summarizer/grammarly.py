from transformers import AutoTokenizer,T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")


model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")


def grammar(text):
    e_text=''
    #for i in range(0, (len(text)//100)+1):
        #input_ids = tokenizer([text[i*100:(i+1)*100]],return_tensors="pt").input_ids
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=256)
    edited_text = tokenizer.decode(outputs[0],skip_special_tokens=True)#, 
    e_text=e_text+edited_text+ ' '

    return e_text

