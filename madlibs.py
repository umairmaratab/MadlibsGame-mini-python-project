# string concatenation (aka how to put strings together)
# suppose we want to create strings that says "Hello '_______'"
# name = "Umair"

# a few ways to do this
# print("Hello to " + name)
# print("Hello to {}".format(name))
# print(f"Hello to {name}")

# 3rd method is preffered Most
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay tuned and {verb2} Like you are {famous_person}!"

print(madlib)
