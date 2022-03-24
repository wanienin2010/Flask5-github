from flask import render_template,flash,url_for,redirect,request
from flask_login import login_required

from application import db
from .import library
from .models import Book, Publication
from .forms import EditForm


@library.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@library.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)

@library.route('/book/delete/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('book deleted successfully')
        return redirect(url_for('library.display_books'))
    return render_template('delete_book.html', book=book, book_id=book.id)

@library.route('/edit/book/<book_id>', methods=['GET','POST'])
@login_required
def edit_book(book_id):
    book=Book.query.get(book_id)
    form=EditForm(obj=book)
    if form.validate_on_submit():
        book.title=form.title.data
        book.format=form.title.data
        book.num_pages=form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash('Book edited sucessfuly!')
        return redirect(url_for('library.display_books'))
    return render_template('edit_book.html',form=form)


