from flask import Flask, render_template, request, redirect, url_for
import list_actions as la

app = Flask(__name__)
wish_list = []


def list_append(item):
    global wish_list
    wish_list.append(item)


def list_delete(item):
    global wish_list
    wish_list.remove(item)


@app.route('/', methods=['GET','POST'])
def index():
    global wish_list
    if request.method == 'POST':
        if request.form['add_Button'] == 'Add':
            item_added = request.form['item']
            list_append(item_added)
    return render_template('index.html', wish_list=wish_list)


@app.route('/delete/<item>')
def delete(item):
    list_delete(item)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug = True)
