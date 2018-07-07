class Review:
    _all = []
    def __init__(self, guest, recipe , rating, comment=None):
        self._recipe=recipe
        self._reviewer=guest
        self._rating=rating
        self._comment=comment
        Review.all().append(self)
    @property
    def recipe(self):
        return self._recipe
    @property
    def reviewer(self):
        return self._reviewer
    @property
    def guest(self):
        return self._reviewer
    @property
    def rating(self):
        return self._rating
    @property
    def comment (self):
        return self._comment
    @classmethod
    def all (cls):
        return Review._all
