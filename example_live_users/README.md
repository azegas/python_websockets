Launch server with `python app.py`

The counter value will be read from `test.txt` file.

The counter value will be updated whenever a new user opens a browser ("connect" event) and decreased when a user closes the browser ("disconnect" event) - BECAUSE we are emitting the 'user' event with the new counter value!

Then in `index.html`, we are listening for the 'user' event and updating the counter value on the page.

The counter value is stored in `test.txt` file.