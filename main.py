from flask import Flask , render_template

app = Flask(__name__) #create a flask app named app


@app.route("/")
def home() :
      return  '''My name is Demilade Adegbemile. This is my CA2 work.
      My Github URL is https://github.com/DemiladeSystems '''
      # In the return statement above, Use your own name and Github URL

@app.route("/mysite")
def site() :
    return render_template("index.html")

if __name__ == "__main__":
      app.run(port=5005)
