from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()
app.title = "First FastAPI App"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime, Drama",
    },
    {
        "id": 2,
        "title": "Avengers: Endgame",
        "director": "Francis Ford Coppola",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "year": 2019,
        "rating": 9.8,
        "category": "Crime, Drama",
    },
]


@app.get("/", tags=["Home Page"])
def message():
    return HTMLResponse(content="<h1>Home Page</h1>", status_code=200)


@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies


@app.get("/movies/{id}", tags=["Movies by ID"])
def get_movie(movies_id: int):
    if movies_id < 1:
        # if the movie id is less than 1, return an error and status code 400
        return JSONResponse(content={"error": "Invalid ID."}, status_code=400)
    movie = next((movie for movie in movies if movie["id"] == movies_id), None)
    if movie is None:
        # if the movie id is not found, return an error and status code 404
        return JSONResponse(content={"error": "Movie not found."}, status_code=404)
    return movie
