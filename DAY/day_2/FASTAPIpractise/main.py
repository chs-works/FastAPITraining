from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"messege":"Hello World","number":27,"is_fun":True}