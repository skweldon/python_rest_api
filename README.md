Directions for starting application.

1. Run the tabledef.py file to set up the sqlite3 database.
2. Run the app.py file to run the server and have the APIs running.
3. Run the APIs based off of what request you want to make.

Example /:
URL: http://localhost:4000/
Method: Any
Result 1: Should give "Hello World" if not authenticated.

Example /user:
URL: http://localhost:4000/user
Method: POST
Data: {
        "username": "yourusername",
        "password": "yourpassword",
        "email": "youremail",
        "address": "youraddress",
        "phone": "yourphone"
}
Result: Returns JSON of data.

Example /user/<username>:
URL: http://localhost:4000/user/<exampleuser>
Method: GET
Result: Returns JSON of specified username.

Example /user/<username>:
URL: http://localhost:4000/user/<exampleuser>
Method: PUT
Data: {
        "email": "newemail",
        "address": "newaddress",
        "phone": "newphone"
}
Result: Returns JSON of new user details.

Example /user/<username>:
URL: http://localhost:4000/user/<exampleuser>
Method: Delete
Result: Deletes the exampleuser.
