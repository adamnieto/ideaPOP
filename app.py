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
    getString.main(textBox)
    indexValues = getString.processString(textBox)
    searchTerms= getString.getSearchValues(indexValues, textBox)
    getImage.main(searchTerms)
    termInfo = ""
    inFile = open("linkdir.txt","r")
    code = ""
    link = ""
    for i in inFile:
        if i != "\n":
            link += i
        code += '<img class="img-circle" src="'+ link + '">'
        link = ""
    counter = 0
    for term in searchTerms:
        if counter == 0:
            termInfo += term.strip("\n")
            termInfo += " "
            counter += 1
        else:
            termInfo += ", " + term.strip("\n")
            termInfo += " "
    return render_template("product.html",images= Markup(code),termInfo=termInfo,textBox=textBox)

if __name__ == "__main__":
    app.run(debug=True)
