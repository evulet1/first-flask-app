from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
posts = {
    0: {
        'post_id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    # return f"Post {post['title']}, content: {post['content']}"
    if not post:
        return render_template('404.html', message=f'A post with id {post_id} was not found.')
    return render_template('post.html', post=post)


@app.route('/post/form')
def form():
    return render_template('create.jinja2')


@app.route('/post/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    post_id = len(posts)
    posts[post_id] = {'id': post_id, 'title': title, 'content': content}

    return redirect(url_for('post', post_id=post_id))


if __name__ == '__main__':
    app.run(debug=True)
