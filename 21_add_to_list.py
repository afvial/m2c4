# How to Add to a List in Python with Both In Place and Copy Processes

tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming'

# In Place
#tags.extend('Programming')
#tags.extend(['Programming'])

# New List
new_tags = tags + ['Programming']

print(new_tags)

print(tags)
