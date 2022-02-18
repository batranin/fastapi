import database_scripts as db_scripts

#def get_items():
#   return db_scripts.select_items()

def get_item(barcode: str):
    results = db_scripts.select_items(barcode)
    return results