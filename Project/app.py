from flask import Flask, render_template, request               # Flask is kind of like a python-based version of React (JS) that's more focused on the app side of things.
from chatbot import predict_class, get_response, intents

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

response_list = []                                  # An empty array where we can store out chat log.

@app.route("/")
def home():
    global response_list                            # This stores all the chat messages.
    response_list.clear()                           # This will clear that list to be empty again.
    return render_template("index.html")            # This renders the home page. 

@app.route("/chatbot", methods=["GET", "POST"])     # This gets the route, whilst also stating that we are allowing the GET and POST methods.
def chatbot():
    global response_list
    if request.method == "POST":                    # When a message is sent, run the code below.
        message = request.form['message']           # This will link to a HTML input box.
        ints = predict_class(message.lower())       # Here I convert the user input to lowercas.
        res = get_response(ints, intents)           # ints are the individual inputs and responses, whilst intents is the whole data.json file. This pushes them into an array.
        response_list.append(res)
        return render_template("chatbot.html", message=message, response_list=response_list)        # This essentially updates the page by re-rendering the component.
    return render_template("chatbot.html", message="", response_list=response_list)                 # We do it again here just to make sure it renders if the user accesses the page another way.

if __name__ == "__main__":
    app.run(debug=True)         # This gives me a way to enable debugging if it is run with the right name.
