from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb+srv://sproutsai:O7X8tgRfJjgmnWZa@nlpcluster.oh532d5.mongodb.net/")
db = client["linkgrabberlinkedinurl"]
collection = db["urls"]

class LinksData(BaseModel):
    links: List[str]

@app.post("/storeLinks_from_customized_linkgrabber")
async def store_links(data: LinksData):
    try:
        links = data.links
        # Store links in MongoDB
        print(links)
        for link in links:
            # Insert the link into MongoDB
            result = collection.insert_one({"link": link})

        return {'success': True, 'message': 'Links stored successfully'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
