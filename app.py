from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data analyst",
        "location": "Bengaluru, India",
        "Salary": "Rs. 10,00,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        # "Salary": "Rs. 15,00,000"
    },
    {
        "id": 3,
        "title": "Backend Engineer",
        "location": "Bengaluru, India",
        "Salary": "Rs. 10,00,000"
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)

@app.route("/api /jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)