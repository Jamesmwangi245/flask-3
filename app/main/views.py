from os import abort
from urllib.robotparser import RequestRate
from wsgiref.util import request_uri
from flask import render_template,redirect,url_for
from . import main
from .. import db,photos
from ..models import Pitches,User,Comments
from .forms import PitchForm,CommentForm,updateProfile
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename


#views
@main.route('/')
def index():

    message= "Hello"
    title= 'Pitch It Ip!'
    return render_template('index.html', message=message,title=title)

@main.route('/pitch/', methods = ['GET', 'POST'])
@login_required
def new_pitch():

     form = PitchForm()

     if form.validate_on_submit():
          category = form.category.data
          pitch = form.pitch.data
          comment = form.comment.data

          new_pitch = Pitches(title = title, category = category, pitch = pitch, user_id=current_user,comment=comment)

          title = 'New Pitch'

          new_pitch.save_pitch()

          return redirect(url_for('main.index'))
     return render_template('pitch.html', pitch_entry = form)

@main.route('/user/<uname>')
def category(cate):
     '''
     returns pitches byt category
     '''
     category = Pitches.get_pitches(cate)
     title = f'{cate}'
     return render_template('categories.html',title = title, category = category)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = updateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in RequestRate .files:
        filename = photos.save(request_uri.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comments.get_comment(id)
    print(comm)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title)

@main.route('/new_comment/<int:pitches_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitches_id):
    pitches = Pitches.query.filter_by(id = pitches_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment,user_id=current_user.id, pitches_id=pitches_id)


        new_comment.save_comment()


        return redirect(url_for('main.index'))
    title='New Pitch'
    return render_template('new_comment.html',title=title,comment_form = form,pitches_id=pitches_id)



