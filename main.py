from fastapi import APIRouter , Depends, Form, Request
from fastapi import Body , Path , Query , HTTPException


from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles


import santander


app = FastAPI()
templates = Jinja2Templates(directory= "templates")

app.mount("/static", StaticFiles(directory="static"), name = "static")

@app.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("santander_templates.html", {"request": request})


# Santander transaction prediction 
app.include_router(santander.router)

 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

    
    


    
    
     



























