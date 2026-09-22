from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"page":"Home"}
@app.get("/about")
def about():
    return{"page":"About","author":"Charan"}
@app.get("/health")
def health():
    return {"Status":"ok"}

#postreq
@app.post("/create")
def create_some():
    return {"messege":"Created"}