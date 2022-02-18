from fastapi import FastAPI
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

# @app.get("/")
# async def root():
#     return controller.get_items()

@app.get("/{barcode}")
async def read_item(barcode: str):
    return controller.get_item(barcode)