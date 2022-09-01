from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User, {username}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)

if __name__ == "__main__":
    app.run()