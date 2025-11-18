# 1. Kth Largest & Smallest (Without Sort)

arr = [7, 2, 9, 4, 1]
k = 2

largest = arr[:]
smallest = arr[:]

for _ in range(k):
    max_val = max(largest)
    largest.remove(max_val)

for _ in range(k):
    min_val = min(smallest)
    smallest.remove(min_val)

print(max_val, min_val)



# 2. Merge Sort + Quick Sort

arr = [5, 2, 8, 1, 3]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i]); i += 1
        else:
            sorted_arr.append(right[j]); j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

print(merge_sort(arr))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr))



# 3. Valid Palindrome

s = "A man, a plan, a canal: Panama"
clean = ""

for ch in s:
    if ch.isalnum():
        clean += ch.lower()

print(clean == clean[::-1])



# 4. Union & Intersection Without Sets

a = [1, 2, 3]
b = [2, 3, 4]

inter = []
for x in a:
    if x in b and x not in inter:
        inter.append(x)

un = a[:]
for x in b:
    if x not in un:
        un.append(x)

print(inter)
print(un)



# 5. Stack Using Two Queues

from collections import deque

q1 = deque()
q2 = deque()

q2.append(10)
while q1:
    q2.append(q1.popleft())
q1, q2 = q2, q1

q2.append(20)
while q1:
    q2.append(q1.popleft())
q1, q2 = q2, q1

print(q1.popleft())



# 6. Reverse Linked List

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

n1 = Node(1); n2 = Node(2); n3 = Node(3)
n1.next = n2; n2.next = n3

prev = None
curr = n1

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

print(prev.data)



# 7. Recursive Binary Search

arr = [1, 2, 3, 4, 5]
target = 4

def bsearch(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return bsearch(arr, low, mid-1, target)
    return bsearch(arr, mid+1, high, target)

print(bsearch(arr, 0, len(arr)-1, target))



# 8. Kadane's Algorithm

arr = [-2,1,-3,4,-1,2,1,-5,4]

curr = best = arr[0]
for x in arr[1:]:
    curr = max(x, curr + x)
    best = max(best, curr)

print(best)



# 9. Check if Binary Tree is Balanced

class TNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

root = TNode(1)
root.left = TNode(2)
root.right = TNode(3)

def height(node):
    if not node:
        return 0
    left = height(node.left)
    right = height(node.right)
    if left == -1 or right == -1 or abs(left-right) > 1:
        return -1
    return max(left, right)+1

print(height(root) != -1)



# 10. Rotate Array by K

arr = [1,2,3,4,5]
k = 2

k %= len(arr)
print(arr[-k:] + arr[:-k])



# 11. All Permutations of String

def perm(s, ans=""):
    if len(s)==0:
        print(ans)
        return
    for i in range(len(s)):
        perm(s[:i] + s[i+1:], ans + s[i])

perm("abc")



# 12. Count Words in File (Top 5)

# Uncomment if file exists:
# freq = {}
# with open("sample.txt", "r") as f:
#     for w in f.read().lower().split():
#         freq[w] = freq.get(w, 0) + 1
# print(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5])



# 13. Check Anagrams

s1 = "listen"
s2 = "silent"
print(sorted(s1)==sorted(s2))



# 14. Compress String

s = "aaabbccccd"
res = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        res += s[i-1] + str(count)
        count = 1
res += s[-1] + str(count)

print(res)



# 15. Reverse Words, Keep Punctuation

import re

s = "Hello, world! How are you?"

words = re.findall(r'\b\w+\b', s)
punct = re.findall(r'\W+', s)
words.reverse()

result = ""
i = j = 0

while i < len(words) or j < len(punct):
    if i < len(words):
        result += words[i]; i += 1
    if j < len(punct):
        result += punct[j]; j += 1

print(result)



# 16. Fibonacci With Memoization

memo = {}

def fib(n):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1)+fib(n-2)
    return memo[n]

print(fib(10))



# 17. Print All Subsets

arr = [1,2,3]

def subsets(i, curr):
    if i == len(arr):
        print(curr)
        return
    subsets(i+1, curr)
    subsets(i+1, curr+[arr[i]])

subsets(0, [])



# 18. Evaluate Postfix Expression

exp = "5 1 2 + 4 * + 3 -"
stack = []

for ch in exp.split():
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+': stack.append(a+b)
        if ch == '-': stack.append(a-b)
        if ch == '*': stack.append(a*b)
        if ch == '/': stack.append(a/b)

print(stack.pop())



# 19. Find Pairs With Target Sum

arr = [1,2,3,4,5,6]
target = 7

seen = {}
pairs = []

for x in arr:
    y = target - x
    if y in seen:
        pairs.append((y, x))
    seen[x] = True

print(pairs)



# 20. Flatten Nested List

lst = [1, [2, [3,4], 5], 6]

def flatten(x):
    out = []
    for item in x:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

print(flatten(lst))