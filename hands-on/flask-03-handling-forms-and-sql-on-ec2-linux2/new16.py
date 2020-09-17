from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('greet.html', name='Ahmet')


@app.route('/greet', methods=['GET'])
def greet():
    if 'name' in request.args:
        usr = request.args['name']
        return render_template('greet.html', name=usr)
    else:
        return render_template('greet.html', name='Send your user name with "name" parameter in query string')
if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)