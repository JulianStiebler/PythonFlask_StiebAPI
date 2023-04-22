from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Yesterday'
    },
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Today'
    }
]

@app.route("/") # -> MAIN ROUTE
def routes_main():
    return render_template('pages/home.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

