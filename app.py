from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
  message = "<h1><center> Hello World app! Version  3 {} <center><h1>".format(hostname)
  return message

if __name__ == "__main__":
  
  hostname = os.getenv('HOSTNAME',None)  
  app.run(host='0.0.0.0',port=5000)
  
