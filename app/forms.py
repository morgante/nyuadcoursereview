from flask.ext.wtf import Form, SelectField, TextAreaField, HiddenField
from flask.ext.wtf import Required

class reviewSubmissionForm(Form):
    rating = SelectField('rating', choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators = [Required('Please select a rating out of 5')])
    comment = TextAreaField('comment',validators = [Required('Please write a review')])



class searchForm(Form):
    pass

    
