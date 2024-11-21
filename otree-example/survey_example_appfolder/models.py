from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Krispin Krüger'
doc = 'This is a test survey to try out oTree for the Seminar: Designing and Implementing Online-Survey Experiments'

class Constants(BaseConstants):
    name_in_url = 'Survey-for-your-favorite-food'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    pass


class Player(BasePlayer):
#The Variables are structured on the base of pages
    entry_question = models.StringField(label="Hi how are you doing?", blank=True)
    name_question = models.StringField(label="What's the name your grandmother called you growing up?", blank=True)
    age_question = models.IntegerField(label="How old do you feel today? (And now be honest to yourself and type in your actual age:)):", max= 100, min=1, blank=True)
    food_question = models.StringField(label="What is the food you think of when you want to feel good?", blank=True)
    goodness_indicator = models.IntegerField(
        label="How good does the food make you feel when you eat it?",
        choices=[
            [1, '1 (Not good at all)'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10 (I could die after eating this)'],
        ],
        widget=widgets.RadioSelect,blank=True)                      