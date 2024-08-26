from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1,
    },
    {
        "title": "Favorite Food",
        "content": "I like pizza",
        "id": 2,
    },
]


def findpost(id):
    for i in my_posts:
        if i["id"] == id:
            return i


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello!!!! "}


@app.get("/posts")
def get_posts():
    return {"message": my_posts}


# @app.post("/createposts")
# def create_post(temp : dict = Body(...)):
#     print(temp)
#     return {"new_post": f"title {temp['title']} content: {temp['content']}"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)  # Generate a random ID
    my_posts.append(post_dict)  # Append the new post to the list
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    # print(id)
    post = findpost(int(id))
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No post with id {id} was found",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"No post with id {id} was found"}
    return {"post-details": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} DNE"
        )

    my_posts.pop(index)
    # return {"message": "post was successfully deleted"}
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} DNE"
        )
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}
