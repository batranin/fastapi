import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import controller as controller

tags_metadata = [
    {
        'name': 'goods',
        'description': 'goods',
    }
]

app = FastAPI(
    title='Mini api',
    description='This is database of goods barcodes',
    version='1.0.0',
    openapi_tags=tags_metadata
)

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "newton")
    correct_password = secrets.compare_digest(credentials.password, "newton")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}

# @app.get("/")
# async def root():
#     return controller.get_items()

@app.get("/{barcode}")
async def read_item(barcode: str):
    return controller.get_item(barcode)