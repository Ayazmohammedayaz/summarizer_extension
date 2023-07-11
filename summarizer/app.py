from flask import Flask,render_template,request,jsonify
from summarizer_bot import summary_api,summarizer
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
        response="I can summarize lengthy texts, give it a try"
        
    response=str(response)
    clean_text = response.replace('<s>', "").replace('[','').replace(']','').replace("'","").replace("'","")
    response=clean_text
     
    message={"answer":response}
    return jsonify(message)



if __name__=="__main__":
    app.run(debug=True)
    
