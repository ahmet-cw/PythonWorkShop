from flask import Flask, redirect, url_for, render_template

# creating application
app =  Flask(__name__)

# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>'
# and assign route of no path ('/')
@app.route('/')
def home():
    return '<h1> Welcome to Clarusway </h1>'
@app.route('/about')
def about():
    return '<h1> This is my about page...</h1>'
@app.route('/error')
def error():
    return '''<h1> Sorry, something went wrong.
              You are not auhtorized to see this page</h1>'''
@app.route('/hello')
def hello():
    return '<h1> Hello from Ahmet </h1>'
@app.route('/admin', methods=['GET'])
def admin():
    authorized=False
    if authorized:
        return 'This is the admin page'
    else:
        return redirect(url_for('error'))
# @app.route('/<name>')
# def greet(name):
#     greet_format=f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Greeting Page</title>
#     </head>
#     <body>
#         <h1>Hello, { name }!</h1>
#         <h1>Welcome to my Greeting Page</h1>
#     </body>
#     </html>
#     """
#     return greet_format

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name='Master Admin!!!'))


@app.route('/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@app.route('/list10')
def list10():
    return render_template('list10.html')

    
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

