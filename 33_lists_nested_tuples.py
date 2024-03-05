# Working with Lists Nested in Tuples

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post[-1][1])
