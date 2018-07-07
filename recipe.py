from review import Review
from course import Course

class Recipe:
    _all=[]
    def __init__(self, name):
        self._name=name
        Recipe.all().append(self)

    @property
    def name(self):
        return self._name
    @classmethod
    def all(cls):
        return Recipe._all
    def reviews (self):
        return [review for review in Review.all() if review.recipe == self]
    def ratings(self):
        return[review.rating for review in self.reviews()]
    def avg_rating(self):
        if (len(self.reviews()) > 0):
            num_reviews = len([review for review in self.reviews()])
            total = sum([review.rating for review in self.reviews()])
        return (total/num_reviews)



    @classmethod
    def top_three(cls):
        recipes= [recipe for recipe in Recipe.all() if len(recipe.reviews()) > 0]
        sorted_recipe = sorted(recipes, key=lambda recipe: recipe.avg_rating(), reverse=True)
        return sorted_recipe [0:3]

    @classmethod
    def bottom_three(cls):
        recipes= [recipe for recipe in Recipe.all() if len(recipe.reviews()) > 0]
        sorted_recipe = sorted(recipes, key=lambda recipe: recipe.avg_rating())
        return sorted_recipe[0:3]



    def top_five_reviews(self):
        reviews=[]
        for review in self.reviews():
            reviews.append(review)
        sorted_reviews = sorted(reviews, key=lambda review: review.rating, reverse=True)
        return sorted_reviews[0:5]

    #def top_five_reviews(self):
        #return list_of_sorted_reviews=[review for review in Recipe.sortedreviews()]
        # list_review_rating=[]
        # for review in self.reviews():
        #     list_review_rating.append((review, sorted(review.rating())))
        # list_of_reviews=[]
        # for review in list_review_rating.keys():
        #     list_of_reviews.append(review)

        #sorted_reviews = sorted (list_review_rating, key=lambda q:q[1], reverse=True)
