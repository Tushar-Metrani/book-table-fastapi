from fastapi import FastAPI,Form
from fastapi.responses import RedirectResponse
from scm import send_mail
from generate_id import id_generator
from datetime import datetime
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

origins = [
    "http://localhost:5173",
    #"https://your-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],   
)


@app.get("/")
def default():
    return RedirectResponse("/wakeup")


@app.get("/wakeup")
def wakeup():
    return "server active"


@app.post("/submit")

async def handle_form(
    name : str = Form(...),
    email : str = Form(...),
    phone : int =Form(...),
    date : str = Form(...),
    time : str = Form(...),
    people : int = Form(...),
    requests : Optional[str] = Form(None)
):  
    dt = datetime.strptime(date, "%Y-%m-%d")
    formatted_dt = dt.strftime("%d-%m-%y")
    t = datetime.strptime(time, '%H:%M')
    formatted_t = t.strftime('%I:%M %p')
    booking_id = id_generator()
    code = send_mail(booking_id,name,email,formatted_dt,formatted_t,people)
    if (code==201):
        return JSONResponse(
            status_code=201,
            content={
                "status":"success",
                "message":booking_id
            }
        )
    else:
        return JSONResponse(
            status_code=400,
            content={
                "status":"failure",
                "message":400
            }
        )

