from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_route():
    """Basic API"""
    return {"message": "Hey, It is me Ash"}
