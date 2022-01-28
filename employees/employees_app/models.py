from django.db import models


# Create your models here.

class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    # не може директно да се онаследят, за да ги има в другите класове -
    # това става с Meta класа, чрез Meta/abstract

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = 'Soft-Uni'
    GOOGLE = 'Google'
    AUDI = 'Audi'
    COMPANIES = (
        SOFT_UNI,
        GOOGLE,
        AUDI,
    )

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        default='NO NAME',
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )
    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),  # (стойност в базата, как изглежда там)
            (QA_ENGINEER, 'QA Eng'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist'),
        )
    )

    company = models.CharField(
        # динамично задаване на max_length
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('company', '-first_name',)
        # - прави DESC




class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    # ManyToManyField може да или тук или в Employee класа
    employees = models.ManyToManyField(
        to=Employee
    )


class User(models.Model):
    # EmailField е CharField с валидация и default max_length=254
    email = models.EmailField()

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )
