# python websockets for humidity sensor imitation

So the goal is to read the data from the humidity sensor and display it on the website, IN REAL TIME.

Getting data to the terminal in real time is one thing, but to display it on the website - it's another.

So let's look at `app.py` file.

It's job is to run flask server, which hosts a website and has a route to `/` which is a home page.

Whenever the home page is loaded - it makes a request to the server to get the data from the sensor (aka read the data from the `log.json` file).

And then it sends this data to the website.

And then the website displays the data.

Inside of the `index.html` file, we can see that there is a placeholder for humidity and temperature.

And there is a script, that updates the data every second. The update happens with a `setInterval` function. Every second it says EMIT xsomethingx to the server with a name of "request_update". Surprise surprise, `app.py` has a function called `handle_update_request` that gets triggered by this "request_update" event. And this `handle_update_request` function simply calls the `get_sensor_data` function results and sends it back to the website.

And then the website updates the data.

And that's it.

Inspiration from - https://www.youtube.com/watch?v=nDgdldBPoE0
