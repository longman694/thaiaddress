from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import thaiaddress
import uvicorn

app = FastAPI(title="Thai Address Parser API", 
              description="API for parsing Thai addresses using thaiaddress library",
              version="1.0.0")

class AddressRequest(BaseModel):
    text: str

class AddressResponse(BaseModel):
    text: str
    name: str
    address: str
    location: str
    subdistrict: str
    district: str
    province: str
    postal_code: str
    phone_number: str
    email: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Thai Address Parser API. Use POST /parse to parse an address."}

@app.post("/parse", response_model=AddressResponse)
def parse_address(request: AddressRequest):
    try:
        result = thaiaddress.parse(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing address: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
