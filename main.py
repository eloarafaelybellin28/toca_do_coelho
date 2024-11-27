from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inical():
      return render_template("index.html")

@app.route("/paginainicial")
def paginainical():
      return render_template("paginainicial.html")

@app.route("/sobrenos")
def sobrenos():
      return render_template("sobrenos.html")

@app.route("/menu")
def menu():
      return render_template("menu.html")
@app.route("/Livros")
def Livros():
      return render_template("Livros.html")
@app.route("/Blog")
def Blog():
      return render_template("Blog.html")



if __name__ == '__main__':
      app.run(debug=True)