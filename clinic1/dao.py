from clinic1.models import User, Medicine, Patient, Schedule
from clinic1 import db, app
from sqlalchemy import func
import hashlib


def load_medicines():
    return Medicine.query.all()


def get_medicine_by_id(medicine_id):
    return Medicine.query.get(medicine_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def booking(fullname, gender, date_of_birth, address, phone_number):
    u = Patient(full_name=fullname.strip(),
                date_of_birth=date_of_birth,
                gender=gender,
                address=address,
                phone_number=phone_number)
    db.session.add(u)
    db.session.commit()


def search_date(date=None):
    query = db.session.query(Patient.id, Patient.full_name, Patient.gender,
                             Patient.date_of_birth, Patient.address, Patient.phone_number) \
        .join(Schedule, Schedule.date.__eq__(Schedule.date))

    if date:
        query = query.filter(Schedule.date.__eq__(date))

    return query.group_by(Patient.id).all()


# if __name__ == "__main__":
#     with app.app_context():
#        print(search_date())
