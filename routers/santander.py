from fastapi import APIRouter , Depends, Request
from fastapi import Body , Path , Query , HTTPException
from pydantic import BaseModel , Field
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle 
import cloudpickle 
from fastapi import APIRouter , Depends, Form, Request
import numpy as np 
from sklearn.preprocessing import StandardScaler 

from sklearn.preprocessing import StandardScaler


filename = r"routers\lgbmlightnew.pkl"
filename2 = r'routers\logestic_for_tran.pkl'
filename3 = r'routers\naive_for_tran.pkl'



router = APIRouter()

templates =  Jinja2Templates(directory= "templates")
standard =  StandardScaler()



with open( filename, "rb") as pickle_light:
    model_light = cloudpickle.load(pickle_light)

with open( filename2, 'rb') as pickle_logestic:
    model_logestic = pickle.load(pickle_logestic)

with open( filename3, 'rb') as pickle_naive:
    model_naive = pickle.load(pickle_naive)



class modelrequest(BaseModel):
    VAR_1: float 
    VAR_2: float
    VAR_3: float
    VAR_4: float  
    VAR_5: float 
    VAR_6: float  
    VAR_7: float 
    VAR_8: float 
    VAR_9: float 
    VAR_10: float






@router.get("/", response_class=HTMLResponse)
def test_model(request:Request):
    return templates.TemplateResponse("santander_templates.html", {"request":request})

@router.post("/", response_class= HTMLResponse)
def test_model( request: Request, 
              VAR_1: float= Form(...),
              VAR_2: float= Form(...),
              VAR_3: float= Form(...),
              VAR_4: float= Form(...),
              VAR_5: float= Form(...),
              VAR_6: float= Form(...),
              VAR_7: float= Form(...),
              VAR_8: float= Form(...),
              VAR_9: float= Form(...),
              VAR_10: float= Form(...),
              
                ):
    
    re = np.array([VAR_1, VAR_2, VAR_3, VAR_4, VAR_5,VAR_6,VAR_7,VAR_8,VAR_9,VAR_10]).reshape(-1,1)
    push = standard.fit_transform(re).transpose()
    
   
    light = model_light.predict_proba(push)[: , 1][0]
    naive = model_naive.predict_proba(push)[: , 1][0]
    arr= np.array([light, naive ])
    pred_name = model_logestic.predict([arr])[0]



    if pred_name ==0:
        return "CUSTOMER MIGHT NOT DO THE TRANSCATION"
    else:
        return "CUSTOMER MIGHT TRANSACT"
    
    

