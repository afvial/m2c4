# Working with the slice Class in Python to Store Slices

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])
