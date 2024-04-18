from flask import Flask, render_template, make_response,redirect
from flask import request
from pymongo import MongoClient
import pickle
from datetime import datetime

# gemini
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro') 


# MONGODB
from bson.objectid import ObjectId
cluster=MongoClient("")

db=cluster["test"]
collection=db["test"]
users=db["users"]
chats=db["chats"]

# collection.insert_one({"_id":1,"name":"Sayeem","password":"password"})
# collection.insert_many([post1,post2])

res=collection.find({"name":"sayeem"})

for re in res:
      print(re)
app = Flask(__name__)

@app.route('/')
def home():
    data = ['Item 1', 'Item 2', 'Item 3']
    return render_template('home.html', logged=request.cookies.get('logged'))


class CustomObject:
    def __init__(self, data):
        self.data = data

@app.route('/test')
def test():
    res= collection.find({"name":"Sayeem"})


    # res=list(res)
    # for re in res:
    #      print(re)
    # print("that was cookie")
    return request.cookies.get('nameD')

@app.get('/login')
def login_get():
    return render_template('login.html', logged=request.cookies.get('logged'))

# @app.route('/login', methods=['POST'])
# def login_post():
#     if request.method == 'POST':
#         username = request.form['Username']
#         password = request.form['Password']
#         print(username, password)
#         return "done"
#     else:
#         return "Invalid request method"
@app.route('/signUp', methods=['POST'])
def SignUp():
    
        usernameF = request.form['username']
        passwordF = request.form['password']
        print(usernameF, passwordF)
        users.insert_one({"username":usernameF,"password":passwordF})

        return render_template("home.html",logged=request.cookies.get("logged"))
        

@app.route('/signUp')
def signShow():
     return render_template('signup.html')

@app.route('/logout')
def logout():
        response = make_response(render_template("home.html", logged=False))
        
        # Set cookies
        response.set_cookie("nameD", "", expires=0)
        response.set_cookie("passwordD", "", expires=0)
        response.set_cookie("id", "", expires=0)
        response.set_cookie("logged", "", expires=0)
        return render_template("home.html",logged=request.cookies.get("logged"))



@app.route('/login', methods=['POST'])
def handle_post():
    
        usernameF = request.form['username']
        passwordF = request.form['password']
        print(usernameF, passwordF)
        

        res = users.find_one({"username": usernameF})
        if res:
                # Extract details from MongoDB response
                nameD = res.get("username")
                passwordD = res.get("password")
                id=str(res.get("_id"))
                
                # Create response object
                response = make_response("Cookies set successfully")
                
                # Set cookies
                response.set_cookie("nameD", nameD)
                response.set_cookie("passwordD", passwordD)
                response.set_cookie("id", id)
                 
                if (passwordF==passwordD):
                     response.set_cookie("logged","True")
                else:
                      response.set_cookie("logged","False")

                
                return response 
        else:
                return "No document found"
        
    
@app.route('/chat')
def chat():
      
    data=""
    chatHistory= chats.find({"userId":request.cookies.get('id')})
    return render_template('chat.html',data=data, logged=request.cookies.get('logged'),chatHistory=chatHistory)
    

@app.route('/chat', methods=['POST'])
def handle_chat():
     prompt = request.form['prompt']
     response = model.generate_content(prompt)
     chats.insert_one({"userId":request.cookies.get('id'),"question":prompt,"answer":response.text,"date":datetime.now()})

     chatHistory= chats.find({"userId":request.cookies.get('id')})
     return  render_template('chat.html',data=response.text,chatHistory=chatHistory, logged=request.cookies.get('logged'))
     
@app.route('/delete/<string:id>', methods=['POST'])
def delete_document(id):
    try:
        # Convert the string id to ObjectId
        document_id = ObjectId(id)
        
        # Delete the document from the collection based on its _id
        result = chats.delete_one({'_id': document_id})
        
        # Check if document is deleted successfully
        if result.deleted_count == 1:
            return redirect('/chat')  # Redirect to success page or some other route
        else:
            return "Document not found or already deleted"
    except Exception as e:
        return str(e)     

if __name__ == '__main__':
    app.run(debug=True)
