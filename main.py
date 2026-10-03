 #1) Create two sets `s1` and `s2` with some elements.

# 2) Use `zip(s1, s2)` to pair elements from both sets position-wise:

# a) Convert the zipped pairs into a list using `list(...)`

# b) Store it in `s3`.

# 3) Print the list of zipped pairs `s3` and add a newline.

# 4) Create two lists `list1` and `list2` containing numbers.

# 5) Print paired elements where the second list is reversed:

# a) Use `list2[::-1]` to reverse `list2`.

# b) Use `zip(list1, list2[::-1])` to pair elements.

# c) Loop through each pair as `x, y` and print them one by one.

# 6) Create two lists `stocks` and `prices` to demonstrate zipping into a dictionary.

# 7) Use dictionary comprehension with `zip(stocks, prices)`:

# a) Each stock name becomes a key.

# b) Each corresponding price becomes the value.

# c) Store the result in `new_dict`.

# 8) Print the final dictionary `new_dict` in a formatted way.

s1={1,2,3,4,5}
s2={0,9,8,7,6}
s3=list(zip(s1,s2))
print(s3)
print()
list1=[1,2,3,4,5]
list2=[9,8,7,6,5]
for x,y in zip(list1, list2[::-1]):
    print(x,y)
stocks=["x","y","z"]
prices=[123,134,234]
new_dict={s:p for s,p in zip(stocks,prices)}
print(new_dict)