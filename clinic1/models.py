from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref
from clinic1 import db, app
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin
import hashlib


class UserRole(UserEnum):
    NURSE = 1
    DOCTOR = 2
    ADMIN = 3


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


schedule_patient = db.Table('schedule_patient',
                            Column('schedule_id', ForeignKey('schedule.id'), nullable=False, primary_key=True),
                            Column('patient_id', ForeignKey('patient.id'), nullable=False, primary_key=True))


class Medicine(BaseModel):
    __tablename__ = 'medicine'
    name = Column(String(50), nullable=False)
    unit = Column(String(10), nullable=False)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    record_details = relationship('RecordDetail', backref='medicine', lazy=True)


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.ADMIN)

    def __str__(self):
        return self.name


class Patient(BaseModel):
    full_name = Column(String(100), nullable=False)
    gender = Column(String(10), nullable=False)
    date_of_birth = Column(DateTime, default=datetime.now())
    address = Column(String(50))
    phone_number = Column(String(10))
    record = relationship('Record', backref='patient', lazy=True)
    schedule = relationship('Schedule', backref='patient', lazy=True)


class Record(BaseModel):
    date_of_examination = Column(DateTime, default=datetime.now())
    price_of_examination = Column(Float, default=100000)
    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)
    details = relationship('RecordDetail', backref='record', lazy=True)


class RecordDetail(BaseModel):
    quantity_medicine = Column(Integer, default=0)
    price = Column(Float, default=0)
    medicine_id = Column(Integer, ForeignKey(Medicine.id), nullable=False)
    record_id = Column(Integer, ForeignKey(Record.id), nullable=False)


class Schedule(BaseModel):
    date = Column(DateTime, default=datetime.now())
    quantity_patient = Column(Integer, default=0)
    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # password = str(hashlib.md5('Hydra@123'.encode('utf-8')).hexdigest())
        # u1 = User(name='Tran Quoc Hy', username='nurse', password=password, user_role=UserRole.NURSE)
        # u2 = User(name='Truong Trong Nghia', username='doctor', password=password, user_role=UserRole.DOCTOR)
        # u3 = User(name='Hydra', username='admin', password=password, user_role=UserRole.ADMIN)
        # db.session.add_all([u1, u2, u3])
        # db.session.commit()

        # m1 = Medicine(name='Acetazolamid', unit='pill', price=1150)
        # m2 = Medicine(name='Actrapid HM', unit='jar', price=70619)
        # m3 = Medicine(name='Aciclovir', unit='pill', price=4400)
        # m4 = Medicine(name='Acepron', unit='pack', price=351)
        # m5 = Medicine(name='Otrivin', unit='jar', price=37128)
        # m6 = Medicine(name='Agiclovir', unit='pill', price=379)
        # m7 = Medicine(name='Acuvail', unit='pack', price=7917)
        # m8 = Medicine(name='Acyclovir', unit='pack', price=4730)
        # m9 = Medicine(name='Aerius', unit='pill', price=10168)
        # m10 = Medicine(name='Agifuros', unit='pill', price=118)
        # m11 = Medicine(name='Aikido', unit='pack', price=14623)
        # m12 = Medicine(name='Alegysal', unit='jar', price=82132)
        # m13 = Medicine(name='Alcool 70', unit='jar', price=3903)
        # m14 = Medicine(name='Alcain', unit='jar', price=42135)
        # m15 = Medicine(name='Alfasept handrub', unit='pack', price=78645)
        # m16 = Medicine(name='Algotra', unit='pill', price=9414)
        # m17 = Medicine(name='Alfasept handgel', unit='pack', price=78645)
        # m18 = Medicine(name='Albuglucan', unit='pill', price=28364)
        # m19 = Medicine(name='Alpha_SK', unit='pill', price=3190)
        # m20 = Medicine(name='Alphachymotrypsin', unit='pill', price=839)
        # m21 = Medicine(name='Alverin', unit='pill', price=149)
        # m22 = Medicine(name='Bambec', unit='pill', price=6033)
        # m23 = Medicine(name='Baribit', unit='pack', price=48150)
        # m24 = Medicine(name='Batimed', unit='pill', price=4180)
        # m25 = Medicine(name='Betaloc Zok', unit='pill', price=4827)
        # m26 = Medicine(name='Benita', unit='jar', price=96299)
        # m27 = Medicine(name='Cammic', unit='pill', price=1980)
        # m28 = Medicine(name='Caricin', unit='pill', price=13910)
        # m29 = Medicine(name='Licotan', unit='pill', price=5885)
        # m30 = Medicine(name='Paracetamol', unit='pack', price=20000)
        #
        # db.session.add_all([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10,
        #                     m11, m12, m13, m13, m14, m15, m16, m17, m18, m19, m20,
        #                     m21, m22, m23, m24, m25, m26, m27, m28, m29, m30])
        # db.session.commit()
