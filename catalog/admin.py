from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]

    inlines = [BookInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")

    # This allows inline adding/deleting of isntances.
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # These appear on the top level list of book instances
    list_display = ("id", "book__title", "due_back", "status")
    list_filter = ("status", "due_back")

    # These appear for a specific instance
    # #   fields = ['id', 'book', 'imprint', ('status', 'due_back')]
    fieldsets = (
        (
            "Book Details",
            {"fields": ("book", "imprint", "id")},
        ),  # Section for the status of this book instance
        ("Availability", {"fields": ("status", "due_back")}),
    )
