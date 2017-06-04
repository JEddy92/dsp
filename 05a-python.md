# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

>> How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences, hence can store collections of objects/values and support sequence operations like indexing, slicing, enumeration, and len(). However, lists are mutable while tuples are immutable. This changes their behavior when passed as function arguments and also means that only tuples can work as keys in dictionaries. Dictionary keys must be hashable because dictionaries use hashtables for key-value storage/lookup, and immutable types are hashable while mutable types are not.

>> Another interesting semantic difference is that lists are typically meant to be homogenous and have order, while tuples are meant to be heterogenous and have structure. For example, the position of a value in a tuple could convey meaning on what that value represents, whereas position should not really convey meaning in a list. A concrete example would be that it makes more sense to represent a point (x,y) as a tuple than a list, because the position of the x and y values inform you about the relevant axis. I found [this post](http://news.e-scribe.com/397) helpful for discussing this.  

---

### Q2. Lists &amp; Sets

>> How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are collections of elements. However, they have a bunch of differences -- lists are ordered while sets are unordered, lists allow duplicate elements while sets only collect unique elements, and list elements can be mutable while set elements must be immutable. Because of the latter requirement for sets, the elements they hold are all hashable, allowing sets to use hashtable lookup: set lookup is then more efficient because it is nearly constant time vs. list lookup which is linear in the number of elements (sets have O(1) lookup vs. O(n) for lists).

>> Suppose that I'm monitoring activity on a specific webpage, and want to answer 2 questions: 1) for some hour long period, how many visitors were there in each minute? 2) what were all the distinct usernames that visited the page? 

>> For 1), I could store a list of length 60. This would allow me to order number of visitors per minute over time and store duplicate values in number of visitors. However, for 2) I don't care about order and have no reason to track duplicate values, so a set would be a more efficient form of storage.  

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





