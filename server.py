"""Greeting Flask app."""

from random import choice

from flask import Flask, request, redirect

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html>
              <html>
                <body>Hi! This is the home page. 
                  <a href="http://localhost:5000/hello">Link hello</a>
                </body>
              </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Choose your compliment 
            <select name="compliment">
                <option value="smart">Smart</option>
                <option value="creative">Creative</option>
                <option value="bombass at coding">Bombass At Coding</option>
                <option value="nice">Nice</option>
            </select><br>
          Diss me instead <input type="checkbox" name="diss" value="yes"><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Greet user by name."""
    diss = request.args.get("diss")
    player = request.args.get("person")
    compliment = request.args.get("compliment")
 
    if diss:
        return redirect("/diss")
    else:    
        return """
        <!doctype html>
        <html>
          <head>
            <title>A Compliment</title>
          </head>
          <body>
            Hi, {}! I think you're {}!
          </body>
        </html>
        """.format(player, compliment)

@app.route("/diss")
def diss_person():
    """Insult user by name"""
    
    diss = choice(["crappy person", "stupid", "smelly", "funny looking"])

    return"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, I think you're {}!
      </body>
    </html>
    """.format(diss)




if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
