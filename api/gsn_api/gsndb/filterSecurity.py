from django.contrib.auth.models import User
from gsndb.models import StudentUserHasAccess, MyStudents

allAccess = "all"
myAccess = "my"

user = User.objects.first()
accessibleStudents = StudentUserHasAccess.objects.filter(user=user).values('student')

myStudentsPk = MyStudents.objects.values('studentUserHasAccess')
myStudents = StudentUserHasAccess.objects.filter(user=user, pk__in=myStudentsPk).values('student')