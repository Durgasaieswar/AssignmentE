from fastapi import FastAPI

from validation import ValidatePayload
from models import AddressBook
from db import db_conn, Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    """Health Check

    Returns:
        dict: Health status
    """
    return {"Health": "Success"}

@app.get("/address")
def read_root():
    """Retrieve addresses

    Returns:
        list: List of addresses from SQLite database
    """
    # db = sess_local()
    ab_rows = db_conn.query(AddressBook).all()
    output = []
    for row in ab_rows:
        response = {"id": "","latitude": "", "longitude": ""}
        response["id"] = row.id
        response["latitude"] = row.lat
        response["longitude"] = row.long
        output.append(response)
    
    return output

@app.post("/address")
def read_item(payload: ValidatePayload):
    """Create address in DB

    Args:
        payload (ValidatePayload): Input with address details

    Returns:
        dict: Status message
    """
    # db = sess_local()
    payload = dict(payload)
    # Write to DB
    ab_data = AddressBook(
        lat=payload["lat"],
        long=payload["long"],
    )

    db_conn.add(ab_data)
    db_conn.commit()

    return {"Status": "Creation of address details is success"}

@app.put("/items/{item_id}")
def update_item(item_id: int, latitude: float, longitude: float):

    """Update address in DB

    Returns:
        dict: Status message
    """
    
    # Query DB with item_id
    ab_row = db_conn.query(AddressBook).filter_by(id=item_id).first()
    # UpdateDB with new values.
    ab_row.long = latitude
    ab_row.lat = longitude
    db_conn.commit()
    return {"Status": "Updation of address is success"}

@app.delete("/items_del/{item_id}")
def delete_item(item_id: int):
    """Delete address in DB

    Args:
        item_id (int): id of address to be deleted

    Returns:
        dict: Status message
    """
    # Delete row in DB where item_id matches
    ab_row = db_conn.query(AddressBook).filter_by(id=item_id).first()
    db_conn.delete(ab_row)
    db_conn.commit()

    return {"Status": "Deletion of address is success"}
