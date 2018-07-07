class Course:
    _all=[]

    def __init__(self, dinner, recipe):
        self._recipe=recipe
        self._dinner=dinner
        Course.all().append(self)

    @property
    def recipe(self):
        return self._recipe
    @recipe.setter
    def recipe(self, recipe):
        self._recipe = recipe
    @property
    def dinner_party(self):
        return self._dinner
    @dinner_party.setter
    def dinner_party(self, dinner):
        self._dinner=dinner
    @property
    def dinner (self):
        return self._dinner
    @classmethod
    def all(cls):
        return Course._all
