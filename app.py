from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

data=[{"name": "Lukman Ibrahim", "track": "AI Developr"},
      {"name": "bayo wealth", "track": "AI Developr"},
      {"name": "Lukman Ibrahim", "track": "AI Developr"},]

class Item(BaseModel):
    name: str = Field(..., example="Lukman")
    age: int = Field(..., example=20)
    track: str = Field(..., example="Backend Dev")

@app.get("/", description="This endpoint just returns a welcome message")
def root():
    return {"Message": "Welcom to my FastAPI APplication"}

@app.get("/get_data")
def get_data():
    return data


@app.post("/post_data")
def post_data(req: Item):
    data.append(req.dict())
    print(data)
    return {"Message": "Submitted successfully", "Data": data}

@app.put("/update_data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)
    return {"Message": "Updated successfully", "Data": data}

@app.delete("/del{id}")
def delete_data(id:int):
    for item in data:
        if item["id"] == data:
            data.pop(item)   
            return {"Message": "Deleted successfuly ", "Data":data}
    

@app.delete("/delete_data/{id}")
def delete_data(id: int):
    for index, item in enumerate(data):
        if item["id"] == id:
            deleted = data.pop(index)
            return {"Message": "Deleted successfully", "Deleted": deleted}
    raise HTTPException(status_code=404, detail="Item not found")


# ✅ PATCH endpoint (for partial updates)
@app.patch("/patch_data/{id}")
def patch_data(id: int, req: dict):
    for item in data:
        if item["id"] == id:
            item.update(req)
            return {"Message": "Partially updated successfully", "Data": item}
    raise HTTPException(status_code=404, detail="Item not found")







if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
    