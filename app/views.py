from flask import Flask, render_template, request, make_response, redirect, url_for, g, flash, session, abort
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from flask.ext.login import login_user, logout_user, login_required, current_user
from app import app, lm, db, models
from forms import reviewSubmissionForm
from app import oauthLogin
from models import User, Review, Category, Course, Like, Professor
from config import POST_PER_PAGE, SUPERUSERS
from sqlalchemy.sql import func


# Instantiate Authomatic.
authomatic = Authomatic(oauthLogin.oauthconfig, '\x00\x18}{\x9b\xa4(\xaa\xf7[4\xd5Ko\x07S\x03#%_cM\xf2y.\xf6\xf00Kr', report_errors=False)

lm.login_view = "landing"
lm.login_message = "You must be logged in to view the requested page."
lm.login_message_category = "error"

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/reviews/<int:courseid>')
@app.route('/reviews/<int:courseid>/<int:page>')
@login_required
def reviews(courseid, page = 1):
    if courseid < 1:
        abort(404)
    course= Course.query.get_or_404(courseid)
    reviews = Review.query.filter_by(course_id=course.id).order_by(Review.review_date.desc()).paginate(page, POST_PER_PAGE, False)
    avgrating = (db.session.query(func.avg(models.Review.rating)).filter_by(course_id = course.id)[0])[0]
    totalreviews= reviews.total
    return render_template('course-reviews-list.html', user = g.user, reviews= reviews, course =course, totalreviews=totalreviews, avgrating =avgrating)

@app.route('/reviewposted')
@login_required
def reviewposted():
    mockuser={'netID':'JJ1347'}
    return render_template('reviewposted.html', user=mockuser)

@app.route('/search')
@login_required
def search():
    return render_template('searchresults.html')

@app.route('/<int:catid>/courses')
@login_required
def coursesbymajor(catid):
    page = 1
    if catid < 1:
        abort(404)
    category = Category.query.get_or_404(catid)
    categories = Category.query.order_by(Category.category_name)
    
    courses = db.session.query(models.Review, func.count(models.Review.course_id)).group_by(models.Review.course_id).\
              order_by(func.count(models.Review.course_id).desc()).all()
    
    latest_reviews = Review.query.order_by(Review.review_date.desc()).all()[0:2]

    return render_template('courses-by-major.html', category = category, categories = categories, courses = courses, reviews = latest_reviews )

@app.route('/home')
@login_required
def home():
    categories = Category.query.order_by(Category.category_name)
    
    most_rated_courses = db.session.query(models.Review, func.count(models.Review.course_id)).group_by(models.Review.course_id).\
              order_by(func.count(models.Review.course_id).desc()).all()[0:30]
    
    latest_reviews = Review.query.order_by(Review.review_date.desc()).all()[0:2]

    return render_template('home.html', categories = categories, courses=most_rated_courses, reviews= latest_reviews )

@app.route('/write/<int:courseid>', methods=['GET', 'POST'])
@login_required
def write(courseid):
    if courseid < 0:
        abort(404)
    course = Course.query.get_or_404(courseid)
    professor = Professor.query.get_or_404(course.professor[0].id)
    
    from datetime import datetime
    
    form = reviewSubmissionForm()
    if form.validate_on_submit():
        try:
            
            review = models.Review(review_date= datetime.utcnow(), review_comment=form.comment.data, rating =int(form.rating.data), course_id=course.id, user_id =g.user.id)
            db.session.add(review)
            db.session.commit()
            flash("Review posted successfully","success")
            return redirect('home')
        except:
            flash("Sorry you can't post more than one review for a single course", "error")
            db.session.rollback()
            return redirect('home')
            
    return render_template('write.html',form = form, professor = professor, course=course)

@app.route('/user/<netID>/')
@app.route('/user/<netID>/<int:page>')
@login_required
def user(netID, page = 1):
    
    netID = netID.lower()
    user = User.query.filter_by(net_id = netID).first()
    if user == None:
        abort(404)
    elif user!=g.user and g.user.net_id not in SUPERUSERS:
        flash("Sorry, You can't see someone else's profile", "error")
        return redirect('home')

    reviews = Review.query.filter_by(user_id=user.id).order_by(Review.review_date.desc()).paginate(page, POST_PER_PAGE, False)
    
    return render_template('userprofile.html',user = user,reviews = reviews)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    db.session.rollback()
    return render_template('500.html'),500

@app.route ('/logout')
def logout():
    logout_user() #logout with flask-login
    return redirect('http://passport.sg.nyuad.org/auth/logout')#logout with passport


@app.route('/login', methods=['GET', 'POST'])     
@app.route('/login/<provider_name>/', methods=['GET', 'POST'])    
def login(provider_name='nyuad'):
    """
    Login handler, must accept both GET and POST to be able to use OpenID.
    """
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('home'))
    
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)
   
    
    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
            #check if the user is in the database already
            user = User.query.filter_by(net_id = result.user.NetID).first()
            if user is None:
                user = User(net_id = result.user.NetID)
                db.session.add(user)
                db.session.commit()
            
            login_user(user)
            flash("You were logged in successfully.", "success")
        # The rest happens inside the template.
        return redirect(request.args.get('next') or url_for('home'))
    
    # Don't forget to return the response.
    return response



