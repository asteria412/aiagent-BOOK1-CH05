from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def read_root() :
    obj = {
        "message": "안녕하세요!",
        "user": "KBJ"
    }
    return obj


@app.get("/hello")
def hello(name="hong") :
    print("[GET] name is", name)
    return {
        "name": name
    }
    
@app.post("/hello")
def hello2(name:str=Form(...),password:str=Form(...)) :
    print("[POST] name is", name, "password", password)
    return {
        "name": name,
        "password" : password
    }