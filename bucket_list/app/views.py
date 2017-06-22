# views.py
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from User import User
from app import app
from urllib.parse import urlparse
from BucketList import BucketList

# Instantiating objects
event = BucketList()
user = User()


# defining home page route
@app.route('/')
def index():
    return render_template("index.html", data={
        'url': urlparse(request.url)[2]
    })


# defining login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = None
    if 'logged_in' not in session.keys():
        if request.method == "POST":
            email = request.form['email']
            passwd = request.form['passwd']

            res = user.login(email, passwd)
            print(res)
            if email in res.keys():
                session['logged_in'] = {
                    'name': res[email]['name'],
                    'email': email
                }
                return redirect('/')

            elif 'error' in res.keys():

                return render_template("login.html", data={
                    'data': res['error'],
                    'url': urlparse(request.url)[2],
                })
        elif request.method == "GET":
            return render_template("login.html", data={
                'url': urlparse(request.url)[2]
            })
    else:
        return redirect('/')


# defining logout page route
@app.route('/logout')
def logout():
    if 'logged_in' in session.keys():
        session.pop('logged_in', None)

        return redirect('/')
    else:
        return redirect('/login')


# defining sign-up page route
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if 'logged_in' not in session.keys():
        if request.method == "POST":

            name = request.form['name']
            email = request.form['email']
            passwd = request.form['passwd']
            cpasswd = request.form['cpasswd']

            res = user.create_account(name, email, passwd, cpasswd)

            if email in res.keys():
                return redirect('/login')
            elif 'error' in res.keys():
                return render_template("login.html", data={
                    'data': res['error'],
                    'url': urlparse(request.url)[2],
                })

            return redirect('/')

        elif request.method == "GET":

            return render_template("login.html", data={
                'url': urlparse(request.url)[2],
            })
    else:
        return redirect('/')


# defining create-bucketlist page route
@app.route('/create-bucketlist', methods=['GET', 'POST'])
def create_bucket():
    if 'logged_in' in session.keys():
        if request.method == 'POST':
            title = request.form['title']
            location = request.form['location']
            category = request.form['category']
            date = request.form['date']
            desc = request.form['desc']
            user_id = session['logged_in']['name']

            res = event.add_bucket_list(title, category, location, date, desc, user_id)
            if 'success' in res.keys():
                return redirect('/bucket-list')
            return render_template("add-bucket-list.html", data=res)
        elif request.method == "GET":
            return render_template("add-bucket-list.html")
    else:
        return redirect('/login')


# defining bucket-list page route
@app.route('/bucket-list/', methods=['POST', 'GET'])
def bucket_list():
    if 'logged_in' in session.keys():
        if request.method == "POST":
            msg = event.update_bucket_list_status(request.form['title'], 'Completed')
        res = event.get_bucket_list()
        return render_template("bucket-list.html", data=res)
    else:
        return redirect('/login')


# defining route for deleting bucket list item
@app.route('/delete-bucket/<item>')
def delete_bucket(item):
    if 'logged_in' in session.keys():
        msg = event.del_bucket_list(item)
        return redirect('/bucket-list')
    else:
        return redirect('/login')


# defining checklist page route
@app.route('/checklist/<bucket_list>')
def check_list(bucket_list):
    if 'logged_in' in session.keys():
        data = {
            'bucket_list': bucket_list,
            'check_list': event.get_checklist(),
            'bucket_status': event.get_bucket_list()[bucket_list]['status'],
        }

        return render_template("checklist.html", data=data)
    else:
        return redirect('/login')


# defining route for changing checklist status
@app.route('/change-checklist-status', methods=['POST', 'GET'])
def check_list_status():
    if 'logged_in' in session.keys():
        if request.method == "POST":
            bucketlist = request.form['bucket_list']
            checklist = request.form['checklist']
            event.update_step_status(bucketlist, checklist, 'Completed')
            url = '/checklist/' + request.form['bucket_list']
            return redirect(url)
    else:
        return redirect('/login')


# defining add-checklist page route
@app.route('/add-checklist', methods=['POST', 'GET'])
def add_checklist():
    if 'logged_in' in session.keys():
        if request.method == "POST":
            title = request.form['goal']
            bucket_list = request.form['bucket_list']
            res = event.add_step(bucket_list, title)

            return redirect('/checklist/' + bucket_list)

        else:
            return redirect('/bucket-list')
    else:
        return redirect('/login')


# defining delete-checklist page route
@app.route('/delete-checklist/', methods=['GET'])
def del_checklist():
    bucket_list = request.args.get('bucket')
    check_list = request.args.get('checklist')
    msg = event.del_step(bucket_list, check_list)
    print(msg)
    url = '/checklist/' + bucket_list
    return redirect(url)


# defining edit-bucket page route
@app.route('/edit-bucket/<title>')
def edit_bucket(title):
    bucket_list = event.get_bucket_list()[title]
    return render_template('edit_bucket.html', data=bucket_list)


# defining update-bucket page route
@app.route('/update-bucket', methods=['GET', 'POST'])
def update_bucket():
    if 'logged_in' in session.keys():
        if request.method == 'POST':
            title = request.form['title']
            location = request.form['location']
            category = request.form['category']
            date = request.form['date']
            desc = request.form['desc']
            user_id = session['logged_in']['name']

            res = event.update_bucket_list(title, category, location, date, desc, user_id)
            print(res)
            if 'success' in res.keys():
                return redirect('/bucket-list')
            return render_template("add-bucket-list.html", data=res)
        elif request.method == "GET":
            return render_template("add-bucket-list.html")
    else:
        return redirect('/login')
