import math

print('Python File Loaded!')


# binary search
def search(a, item, start=0, end=-1):
  if end < 0:
    end = len(a)
  if start >= end:
    return -1
  i = (end + start) // 2
  if item == a[i]:
    return i
  elif item > a[i]:
    return search(a, item, i + 1, end)
  else:
    return search(a, item, start, i)

print(search(['a', 'b', 'c', 'd'], 'a')) # 0

# merge sorted lists
def deep(a, item):
  start = 0
  end = len(a)
  depth = math.log(len(a) + 1, 2)
  i = 0
  while i <= math.ceil(depth):
    mid = (start + end) // 2
    if start >= end:
      break
    if item == a[mid]:
      return [mid]
    elif item > a[mid]:
      start = mid + 1
    else:
      end = mid
    i += 1
  return [mid, i]

def merge(a: list, b: list):
  for i in range(len(a)):
    b.insert(deep(b, a[i])[0], a[i])
  return b

print(merge([0, 2], [1, 3])) # [0, 1, 2, 3]

# median
def median(a):
  if len(a) % 2:
    return a[len(a) // 2]
  else:
    return (a[len(a) // 2] + a[len(a) // 2 - 1]) / 2

print(median([0, 1, 2])) # 1
print(median([0, 1, 2, 3])) # 1.5

print(median(merge([0, 2], [1, 3]))) # 1.5
print(median(merge([0, 2, 4], [1, 3]))) # 2