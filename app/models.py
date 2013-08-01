from hashlib import md5
from app import db
from flask import url_for

#association table that links Course and Category
course_categories = db.Table('course_categories',
                          db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
                          db.Column('category_id', db.Integer, db.ForeignKey('category.id'))

                    )

#association table that links Professor and Course
course_professors = db.Table('course_professors',
                           db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key= True),
                           db.Column('professor_id', db.Integer, db.ForeignKey('professor.id'), primary_key = True)

                          )



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    net_id = db.Column(db.String(10))
    user_reviews = db.relationship('Review', backref = 'user', lazy = 'dynamic')
    user_likes = db.relationship('Like', backref = 'user', lazy ='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
    
    def avatar(self, size):
        #Should provide a hardcoded url for the default image as "url_for('static',filename='avatar.png')" seems not to work
        default_image = 'http://nyuad.nyu.edu/content/nyuad/en/configuration/header/_jcr_content/logoConfig/image.img.gif/1343285483773.gif'
        return 'http://www.gravatar.com/avatar/' + md5(self.net_id+'@nyu.edu').hexdigest() + '?d='+default_image+'&s=' + str(size) #+ '&f=y'


    def __repr__(self):
        return '< User %r>'%self.net_id
    
     
class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    course_name =db.Column(db.String(120))
    course_description = db.Column(db.Text)
    course_reviews = db.relationship('Review', backref ='course', lazy ='dynamic')
    categories = db.relationship('Category', secondary=course_categories, backref = 'courses', lazy='dynamic')
    
    def totalreviews(self):
        return len(self.course_reviews.all())
    
    def __repr__(self):
        return '< Course %r >'%(self.course_name)
    



class Professor(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    professor_name = db.Column (db.String(80))
    courses = db.relationship('Course', secondary = course_professors , backref ='professor')
     
    def __repr__(self):
        return '< Professor %r>'%self.professor_name



    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    category_name = db.Column(db.String(40))

    def courses_count(self):
        return Course.query.with_parent(self,'courses').count() 

    def __repr__(self):
        return '< Category %r>'%self.category_name

     



class Review(db.Model):
    __table_args__ = ( db.UniqueConstraint('course_id', 'user_id'), { } )
    id = db.Column(db.Integer, primary_key = True )
    review_date = db.Column(db.DateTime)#default=db.func.now()
    review_comment = db.Column(db.Text)
    rating = db.Column(db.SmallInteger)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id') )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    review_likes = db.relationship('Like', backref = 'review', lazy = 'dynamic')
    
         
    def __repr__(self):
        return '< Review %r>'%self.id




class Like(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    like = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
 
    def __repr__(self):
        return '< Like value %r>'%self.like



    
