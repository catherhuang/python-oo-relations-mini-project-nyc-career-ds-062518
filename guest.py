from review import Review
from invite import Invite

class Guest:
    _all=[]
    def __init__(self, name):
        self._name=name
        Guest.all().append(self)
    @classmethod
    def all(cls):
        return Guest._all
    @property
    def name(self):
        return self._name
    @classmethod
    def most_popular(cls):
        guests=cls.all()
        sorted_invites_guest= sorted(guests, key=lambda guest: guest.number_of_invites(), reverse=True)
        return sorted_invites_guest[0]

    def avg_rating(self):
        reviews = self.reviews()
        total_of_reviews= len(reviews)
        list_of_ratings=[review.rating for review in reviews]
        sum_of_ratings=sum(list_of_ratings)
        return  sum_of_ratings/ total_of_reviews

    @classmethod
    def toughest_critic(cls):
        guests=cls.all()
        sorted_ratings=sorted(guests, key=lambda guest:guest.avg_rating())
        return sorted_ratings[0]

    @classmethod
    def most_active_critic(cls):
        guests=cls.all()
        sorted_reviews= sorted(guests, key=lambda guest:len(guest.reviews()), reverse=True)
        return sorted_reviews[0]

    def invites(self):
        return [invite for invite in Invite.all() if invite.guest ==self]

    def reviews(self):
        return [review for review in Review.all() if review.guest == self]

    def number_of_invites(self):
        return len(self.invites())

    def rsvp(self, invite, status):
        invite.accepted = status
        return invite.accepted

    def review_recipe(self, recipe, rating, comment):
        new_review = Review(self, recipe, rating, comment)
        return recipe.reviews()

    def favorite_recipe(self):
        reviews= self.reviews()
        sorted_reviews= sorted (reviews, key=lambda review:review.rating, reverse=True)
        return sorted_reviews[0].recipe

        #for each guest's rating on recipe, return that guest's recipe that has the highest rating
