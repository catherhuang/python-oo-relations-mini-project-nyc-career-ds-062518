from course import Course
from invite import Invite

class DinnerParty:
    _all=[]
    def __init__(self, name):
        self._name=name
        DinnerParty.all().append(self)

    @classmethod
    def all(cls):
        return DinnerParty._all

    def invites(self):
        return [invite for invite in Invite.all() if invite.dinner_party == self]

    def guests(self):
        return [invite.guest for invite in self.invite()]

    def number_of_attendees(self):
        accepted = [invite.accepted for invite in self.invites()]
        return len(accepted)


    def courses(self):
        return [dinner for dinner in Course.all() if dinner.dinner == self ]

    def recipes(self):
        return [course.recipe for course in self.courses()]

    def recipe_count(self):
        return len(self.recipes())

    def reviews(self):
        list_of_reviews = [recipe.reviews() for recipe in self.recipes()]
        flattened_list=[]
        for lists in list_of_reviews:
            flattened_list = flattened_list + lists
        return flattened_list

    def highest_rated_recipe(self):
        reviews = self.reviews()
        sorted_reviews=sorted(reviews, key=lambda review: review.rating, reverse=True)
        top_recipe_for_top_review=sorted_reviews[0].recipe
        return top_recipe_for_top_review
