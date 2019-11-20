from django.db import transaction
from rest_framework import serializers
from books.models import (Book, Genre, Author, BookAuthor)


# class BookAuthorSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.ReadOnlyField(source="author.id")
#     name = serializers.ReadOnlyField(source="author.name")

#     class Meta:
#         model = BookAuthor

#         fields = ('id', 'name', 'role')


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = (
            'id', 'name', 'authors', 'description',
            'genre', 'genre_name', 'created'
        )
    
    @transaction.atomic
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        if "authors" in self.initial_data:
            authors = self.initial_data.get("authors")
            for author in authors:
                author_id = author.get("author")
                role = author.get("role")
                author_instance = Author.objects.get(pk=author_id)
                BookAuthor(book=book, author=author_instance, role=role).save()
        book.save()
        return book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'middle_name', 'last_name')