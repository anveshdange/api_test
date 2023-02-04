# importing the required packages 
from fastapi import FastAPI 

# Instancing the Application 
test = FastAPI()

@test.get("/name")
async def getNames():
    return [
        {
            "name": "Anvesh Dange",
            "username":"anveshdange",
            "password": "12345"
        },
        {
            "name": "Utkarsh Sinha",
            "username":"utkarshsinha",
            "password":"123456"
        },
        {
            "name": "Aditya Mourya",
            "username":"adityamourya",
            "password":"1234567"
        }
    ]

