from flask import Flask, request, render_template #importing this flask class.
from processing import do_calculation #importanting the processing do calculation

app = Flask(__name__)   #creating a app variable using the name of the module
app.config["DEBUG"] = True





@app.route('/',  methods=["GET", "POST"]) #route page of the website.
@app.route('/home') #route page of the website.
def home():
    errors = ""
    text1=""
    #in the case that the page is by POST, get the text from the and process it.
    if request.method == "POST":
        text1 = (request.form["text"])
        text1 = do_calculation(text1)
    #text2 = text1 allows data to send through to the html page as a text2 paramater
    #data is then accessed by {{text2}}
    return render_template('home.html' , text2=text1)

@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
    app.run(debug=True)
    