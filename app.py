from fastapi import FastAPI;
from github import GithubApi

app  = FastAPI()
gh =  GithubApi()


@app.get("/home")
def home():
    return {
        "message" : "Server up and Running " , 
        "status" : 200
    }
    
@app.get(gh.baseroute)
async def getAllusers():
    response =  gh.List_Users()
    if(not response):
        return {
            "message" : "Failed To fetch User !",
            "status" : 400
        }
    return {
        "response" : response , 
        "status" : 200
    }
