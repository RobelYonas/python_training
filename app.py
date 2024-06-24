from flask import Flask, request

app = Flask(__name__)

# List of stores with their name and items
stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store")
def get_allstore():
    """
    Get all stores.
    ---
    responses:
        200:
            description: A list of stores.
    """
    return {"Store": stores}


@app.get("/store/<string:name>")
def get_store(name):
    """
    Get a store by name.
    ---
    parameters:
        - in: path
          name: name
          schema:
            type: string
          required: true
          description: The name of the store.
    responses:
        200:
            description: The store with the given name.
        404:
            description: No such store can be found.
    """
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "No such store can be found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    """
    Get all items in a store.
    ---
    parameters:
        - in: path
          name: name
          schema:
            type: string
          required: true
          description: The name of the store.
    responses:
        200:
            description: The items in the store.
        404:
            description: No such store can be found.
    """
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "No such store can be found"}, 404


@app.post("/store")
def add_store():
    """
    Add a new store.
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        name:
                            type: string
    responses:
        201:
            description: The new store.
    """
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def add_item(name):
    """
    Add a new item to a store.
    ---
    parameters:
        - in: path
          name: name
          schema:
            type: string
          required: true
          description: The name of the store.
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        name:
                            type: string
                        price:
                            type: number
    responses:
        201:
            description: The new item.
        404:
            description: No store with that name.
    """
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"No store with that name"}, 404

