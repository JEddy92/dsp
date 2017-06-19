[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> The first step is to standardize our units, so let's convert inches to cms (2.54 cm / inch).

```python
cm_per_inch = 2.54
cm_lower = cm_per_inch * (5 * 12 + 10)
cm_upper = cm_per_inch * (6 * 12 + 1)
```

>> Next we want to find the density of male population heights that fall in the range defined by lower and upper. To do this, we can take the difference cdf(upper) - cdf(lower). Since we are approximating the distribution of heights as normal with the parameters specified in the exercise, we can use the normal cdf to perform this calculation, as in the code below.

```python
import scipy.stats
density = scipy.stats.norm.cdf(cm_upper, loc=178, scale=7.7) \
        - scipy.stats.norm.cdf(cm_lower, loc=178, scale=7.7)
print("The percentage of the male population in the Blue Man Group range is: %.2f%%" % (density * 100))
```

```
The percentage of the male population in the Blue Man Group range is: 34.27%
```
