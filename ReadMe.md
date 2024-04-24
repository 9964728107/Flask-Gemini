Project Title - AI chatBot (gemini+flask+mongoDB)
      

# OUTPUT: 
  refer *folder output-images*

# TECH STACK:
   1. flask: for routing and rendering  [https://flask.palletsprojects.com/en/3.0.x/quickstart/]
 
   2. gemini_api: for answering prompts [https://ai.google.dev/gemini-api/docs/get-started/python]

   3. mongoDB(pymongo): to keep track of conversation history of each user   [https://pymongo.readthedocs.io/en/stable/api/pymongo/index.html]


# HOW TO USE
 1. "cd MiniProject"
 2. add GOOGLE_API_KEY and MONGO_DB_URL in [server.py]   
 3. command: "flask --app server run" 
 4. open the link from the terminal eg.[http://127.0.0.1:5000/] 


# CODE STRUCTURE
  [templates]-directory, has all the html files to be shown in the site
  [server.py]-takes care of routing of pages and dealing with mongodb and gemini
  

#  ROUTES
    1. get- [http://127.0.0.1:5000/login]
    2. get- [http://127.0.0.1:5000/signUp]
    3. post-[http://127.0.0.1:5000/login]
    4. get- [http://127.0.0.1:5000/chat]
    5. post-[http://127.0.0.1:5000/chat]
    6. post-[http://127.0.0.1:5000/delete/<:id>]
    

