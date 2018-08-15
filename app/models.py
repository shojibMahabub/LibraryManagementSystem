from django.db import models
from datetime import date, timedelta, datetime


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    depertment_name = models.CharField(max_length=30)
    roll_number = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return self.depertment_name.upper() + ', ' + self.roll_number + ', ' + self.first_name.upper()


class Book(models.Model):
    name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    remaining = models.IntegerField()

    def __str__(self):
        return self.name


class Issue(models.Model):
    issue_id = models.CharField(max_length=10)
    roll = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.issue_id

    def return_date(self):
        return datetime.now()+timedelta(days=3)

    def fine(self):
        return_date = datetime.now() + timedelta(days=3)
        if datetime.now() > return_date:
            return 'Fine'
        else:
            return 'No Fine'

    def clean(self, *args, **kwargs):
        from django.core.exceptions import ValidationError
        super().clean()
        if self.book_name.remaining < 1:
            raise ValidationError("No books available")
        else:
            self.book_name.remaining -= 1
            self.book_name.save()


class Return(models.Model):
    return_id = models.CharField(max_length=10)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.return_id

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.book.remaining += 1
            self.book.save()
            self.issue_id.delete()
        else:
            super().save(*args, **kwargs)
