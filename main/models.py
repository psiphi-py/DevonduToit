from django.db import models

class Homepage(models.Model):
    h_name = models.CharField(max_length=200)
    h_desc = models.TextField()
    h_image = models.FileField(upload_to='homepage_image', blank=True)
    h_icon = models.FileField(upload_to='homepage_image', blank=True)

    def __str__(self):
        return self.h_name

class Skillset(models.Model):
    s_name = models.CharField(max_length=100)
    s_desc = models.TextField()
    s_image = models.FileField(upload_to='skills_image', blank=True)

    def __str__(self):
        return self.s_name

class Learning(models.Model):
    l_name = models.CharField(max_length=100)
    l_desc = models.TextField()
    l_image = models.FileField(upload_to='learning_image', blank=True)

    def __str__(self):
        return self.l_name

class Alternative(models.Model):
    a_name = models.CharField(max_length=100)
    a_desc = models.TextField()
    a_image = models.FileField(upload_to='alternative_image', blank=True)

    def __str__(self):
        return self.a_name

class Second_Profile(models.Model):
    sec_name = models.CharField(max_length=100)
    sec_desc = models.TextField()
    sec_image = models.FileField(upload_to='second_image', blank=True)

    def __str__(self):
        return self.sec_name

class Projects(models.Model):
    p_name = models.CharField(max_length=100)
    p_desc = models.TextField()
    p_image = models.FileField(upload_to='project_image', blank=True)
    p_url = models.CharField(max_length=200)

    def __str__(self):
        return self.p_name