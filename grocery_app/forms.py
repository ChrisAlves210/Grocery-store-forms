from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

from grocery_app.models import GroceryStore, ItemCategory

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    address = StringField('Address', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField('Name', validators=[DataRequired(), Length(max=80)])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=[(c, c.value) for c in ItemCategory], coerce=ItemCategory, validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[URL(), Length(max=500)])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query.all(), get_label='title', allow_blank=False, validators=[DataRequired()])
    submit = SubmitField('Submit')