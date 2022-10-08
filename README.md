# Python Programming Problems 

Flexing my puny understanding of **python**. I managed to solve these **leetcode** problems on my own by spending a lot of time smashing bugs! 

## Binary Search 

I ended up having to make an iterative version of this binary search to keep track of the binary tree search depth in the [Merge Two Sorted Lists](#merge-two-sorted-lists) problem. 

```py
# binary search
def search(a, item, start=0, end=-1):
  if end < 0:
    end = len(a)
  if start >= end:
    return -1
  i = (end + start) // 2
  print('searching...')
  if item == a[i]:
    return i
  elif item > a[i]:
    return search(a, item, i + 1, end)
  else:
    return search(a, item, start, i)

print(search(['a', 'b', 'c', 'd'], 'a')) # 0
```

## Merge Two Sorted Lists 

This was a challenging one because I had to implement a form of iterative binary search to even proceed with the other stuff. I had to solve some big brain logarithms, draw binary trees, and discover the geometric series to figure out this one. The other stuff was easy though. 

```py
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
```

## Median of Two Sorted Lists 

This was literally a copy of the [Merge Two Sorted Lists](#merge-two-sorted-lists) problem but with *another* function. 

```py
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
```