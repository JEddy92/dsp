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

>> The `lambda` keyword allows you to define anonymous functions with the syntax `lambda args: expression`, using any number of arguments and one expression. Anonymous means that the function is not defined in the usual `def name(args):`, syntax that allows it to be called by name later (if you want to use an anonymously defined function repeatedly, you would have to store it in a function variable). This is useful when you don't want to store a function for long term use, and is especially useful when you want to create a function on the fly to be passed as a variable to another function.

>> For example, the built-in `sorted` function takes an optional function-valued argument 'key' that specifies an evaluation function to sort by. Borrowing from the solution to part of question 7, the code below shows how to sort a list of tuples by the last element in the tuple using a lambda keyword function.   

```python
return sorted(tuples, key = lambda tup: tup[-1])
```

>> Other common use cases include passing anonymous functions to `map`, `filter`, and `reduce`. For example, the code below shows how you could extract a sublist of strings starting with 's' from a list of strings, using filter and a lambda function.

```python
return list(filter(lambda s: s[0] == 's',str_list)) 
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a syntax tool for list construction that allow certain code tasks to be both more readable and more efficient. They are designed to closely mirror mathematical set notation in terms of specifying elements -- for example, think along the lines of S = {2x; x in X} or S = {x | xmod2 = 0; x in X} (the set of all elements in X multipled by 2, the set of all elements in X divisible by 2). For the first of these, the list comprehension equivalent would be `S = [2 * x for x in X]`; for the second, the equivalent would be `S = [x for x in X if x % 2 == 0]`. The outer brackets indicate that we are creating a new list, we specify an expression defining the elements of the new list (first clause), we specify a list to iterate over when evaluating the expression (for clause), and we possibly give a conditional expression to filter the list iterated over (if clause). 

>> Some more examples are below: the first line gives code for getting all strings in a list that start with 's' and capitalizing them; the second line gives code for getting the cubes of all numbers from 1 to 10.

```python
return [s.capitalize() for s in str_list if s[0] == 's']
return [i**3 for i in range(1,11)]
```
>> The `map` and `filter` equivalents for these list comprehensions would be:

```python
return list(map(lambda s: s.capitalize(), filter(lambda s: s[0] == 's',str_list)))
return list(map(lambda x: x**3, range(1,11)))
```

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





