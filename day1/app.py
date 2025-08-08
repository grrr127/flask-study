from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  users = [
    {"no": 1, "name": "Minjung"},
    {"no": 2, "name": "Subin"},
    {"no": 3, "name": "Junsun"},
    {"no": 4, "name": "Intae"},
    {"no": 5, "name": "Hyungu"}
  ]
  return render_template('index.html', users=users)

if __name__ == '__main__':
  app.run(debug=True)