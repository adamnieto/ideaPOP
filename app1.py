from flask import Flask, render_template, request, url_for, Markup
import getString, getImage
app = Flask(__name__)

# setting up the basic route

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/get_data", methods=['POST'])
def handle_data():
    textBox = request.form["ideaBox"]
    # getString.main(textBox)
    indexValues = getString.processString(textBox)
    searchTerms = getString.getSearchValues(indexValues, textBox)
    arrayLinks = getImage.main(searchTerms)
    termCounter = 0
    termInfo = ""
    code = ""
    for linkAddress in arrayLinks:
        code += '<img class="img-circle" src="'+ linkAddress + '">'

    for term in searchTerms:
        if termCounter == 0:
            termInfo += term.strip("\n")
            termInfo += " "
            termCounter += 1
        else:
            termInfo += ", " + term.strip("\n")
            termInfo += " "
    return render_template("product.html",images= Markup(code),termInfo=termInfo,textBox=textBox)

if __name__ == "__main__":
    app.run(debug=True)
