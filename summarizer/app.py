from flask import Flask,render_template,request,jsonify
#from chat import get_response
#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
from summarizer_bot import chat,summary_api,chatt5,summarizer,sum_gpt
#from summ_pipe import summarizer1,summary_api1
from grammarly import grammar
from flask_cors import CORS
import json

app=Flask(__name__)


response=''
@app.get('/')
def index_get():
    return render_template("popup.html")

@app.post("/predict")
def predict():
    j=request.get_json()#input from user
    text=j.get("message")
    #todo: check if text is valid
    if text.startswith("check grammar:"):
        response=grammar(text)
    elif len(text)>200:  
        response=summarizer(text)
    elif text.startswith("https"):
        response=summary_api(text)
    else:
        response=sum_gpt(text)
        
    response=str(response)
    clean_text = response.replace('<s>', "").replace('[','').replace(']','').replace("'","").replace("'","")
    response=clean_text
        #clean_text=str(clean_text)
    #response=get_response(text)
    message={"answer":response}
    return jsonify(message)#output giving to js 



if __name__=="__main__":
    app.run(debug=True)
    
