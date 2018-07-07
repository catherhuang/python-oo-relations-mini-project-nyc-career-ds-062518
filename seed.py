#Test code in this space. Record the tests and report on bugs
from environment import *

testGuest = Guest('Timmy')
testGuest2 = Guest('Jimmy')
testGuest3 = Guest('Pam')
testGuest4 = Guest('Creed')
testGuest5 = Guest('Mike')
testGuest6 = Guest('Oscar')
testGuest7 = Guest('Meredith')
testGuest8 = Guest('James')
testGuest9 = Guest('Olivia')
testGuest0 = Guest('Erin')
testGuest01 = Guest('Mimi')
testGuest02 = Guest('Gigi')
testGuest03 = Guest('Bella')

list_guests = [testGuest, testGuest2, testGuest3, testGuest4, testGuest5, testGuest6,
               testGuest7, testGuest8, testGuest9, testGuest0]

testDinner_Party = DinnerParty('theoffice')
testDinner_Party2 = DinnerParty('thebuds')
testDinner_Party3 = DinnerParty('theDinnerParty')

list_dinner_party = [testDinner_Party, testDinner_Party2, testDinner_Party3]

testRecipe = Recipe('chickensoup')
testRecipe2 = Recipe('fries')
testRecipe3 = Recipe('pizza')
testRecipe4 = Recipe('ramen')
testRecipe5 = Recipe('burgers')
testRecipe6 = Recipe('hotdots')

list_recipe = [testRecipe, testRecipe2, testRecipe3, testRecipe4, testRecipe5, testRecipe6]

list_invites = [Invite(dinner_party,party_guest) for dinner_party in list_dinner_party for party_guest in list_guests ]

list_course = [Course(dinner_party,recipe_review) for dinner_party in list_dinner_party for recipe_review in list_recipe ]

list_reviews = [Review(list_guests[dinner_guest], (list_recipe)[recipe] , dinner_guest+recipe , ' ') for dinner_guest in range(0, len(list_guests)) for recipe in range(0, len(list_recipe))]
