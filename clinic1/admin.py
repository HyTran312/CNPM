from clinic1 import app, db, dao
from clinic1.models import UserRole
from flask_admin import Admin, BaseView, expose
from clinic1.models import Medicine, Patient
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask import redirect, request

admin = Admin(app=app, name='Page of administrator', template_mode='bootstrap4')


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MedicineView(AuthenticatedModelView):
    can_view_details = True
    column_searchable_list = ['name', 'unit']


class PatientView(AuthenticatedView):
    @expose('/')
    def index(self):
        patients = dao.search_date(date=request.args.get('date'))
        return self.render('admin/patients.html', patients=patients)


class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(AuthenticatedModelView(Medicine, db.session))
admin.add_view(PatientView(name='Patients'))
admin.add_view(LogoutView(name='Log out'))
