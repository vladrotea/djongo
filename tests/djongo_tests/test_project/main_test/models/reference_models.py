from djongo import models


class ReferenceAuthor(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ReferenceEntry(models.Model):
    _id = models.ObjectIdField()
    headline = models.CharField(max_length=255)
    authors = models.ArrayReferenceField(ReferenceAuthor)

    def __str__(self):
        return self.headline

