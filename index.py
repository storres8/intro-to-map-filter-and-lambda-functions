def square(num):
 return num**2

my_nums = [1,2,3,4,5]

print(
  list(
    map(square,my_nums)
  )
)

#prints out [1, 4, 9, 16, 25]

# could also write the above function as:

def square(num):
    return num**2

my_nums = [6,7,8,9]

for item in map(square, my_nums):
    print(item)

# this way does not print a list however
# 1
# 4
# 9
# 16
# 25

def splicer(string):
  if len(string)%2==0:
    return "EVEN"
  else:
   return string[0]

names=["steve", "kevin", "adrian"]

print(
  list(map(splicer, names))
)
# this functions returns ['s', 'k', 'EVEN']
# by mapping over the names string and applying the splicer function
# onto each of the names in the names list

def even(num):
  if num %2 ==0:
    return True
  else:
    False

my_nums=[1,2,3,4,5,6,7,8,9]

print(
  list(filter(even,my_nums))
)
# for item in filter(even, my_nums):
#   print(item)
# could also get the results this way but would be in a list
# results: [2,4,6,8]
