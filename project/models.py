from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    p1_name = models.CharField(max_length=100)
    p1_email = models.CharField(max_length=100)
    mob1 = models.CharField(max_length=12)
    p2_name = models.CharField(max_length=100, default="a")
    p2_email = models.CharField(max_length=100, default="a@a.com")
    mob2 = models.CharField(max_length=12, default="9999999999")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    login_time = models.DateTimeField(null=True, max_length=100)
    logout_time = models.DateTimeField(max_length=100, null=True)
    score = models.IntegerField(default=0)
    incr = models.IntegerField(default=4)
    decr = models.IntegerField(default=2)
    counter = models.IntegerField(default=4)
    lifeline1 = models.IntegerField(default=0)

    FE = 'FE'
    SE = 'SE'

    CHOICES = [
        (FE, 'Freshman'),
        (SE, 'Senior'),

    ]
    year = models.CharField(
        max_length=2,
        choices=CHOICES,
        default=FE,
    )

    def __str__(self):
        return self.p1_name


class Questions(models.Model):
    question = models.CharField(max_length=500, default="")
    option1 = models.CharField(max_length=100, default="")
    option2 = models.CharField(max_length=100, default="")
    option3 = models.CharField(max_length=100, default="")
    option4 = models.CharField(max_length=100, default="")
    answer = models.CharField(max_length=100, default="")
    level = models.CharField(max_length=2, default="")

    def __str__(self):
        return self.question


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ques = models.ForeignKey(Questions, on_delete=models.CASCADE)
    resp = models.CharField(max_length=100, default="")
