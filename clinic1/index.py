from flask import render_template, request, redirect
from flask_login import login_user
from clinic1 import app, admin, login, dao
from clinic1.decorators import anonymous_user
import cloudinary.uploader


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=['get', 'post'])
def book_now():
    if request.method.__eq__('POST'):
        fullname = request.form.get('fullname')
        date_of_birth = request.form.get('date-of-birth')
        gender = request.form.get('gender')
        address = request.form.get('address')
        phone_number = request.form.get('phone-number')
        dao.booking(fullname, gender, date_of_birth, address, phone_number)
    return render_template('index.html')


@app.route('/login-admin', methods=['post'])
def login_admin():
    username = request.form['username']
    password = request.form['password']

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


# @app.route("/register")
# def register():
#     err_msg = ''
#     if request.method == 'POST':
#         password = request.form['password']
#         confirm = request.form['confirm']
#         if password.__eq__(confirm):
#             avatar = ''
#             if request.files:
#                 res = cloudinary.uploader.upload(request.files['avatar'])
#                 avatar = res['secure_url']
#
#             try:
#                 dao.register(name=request.form['name'],
#                              username=request.form['username'],
#                              password=password,
#                              avatar=avatar)
#
#                 return redirect('/admin')
#             except:
#                 err_msg = 'There is something wrong! Try again later.'
#         else:
#             err_msg = 'Your password does not correct, please reconfirm your password.'
#
#     return render_template('register.html', err_msg=err_msg)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
