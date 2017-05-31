[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> On average, first babies are lighter than others, with a Cohen's D statistic of approximately -0.089. This shows a larger effect size than the difference in pregnancy length between first babies and others, where the Cohen's D statistic is approximately 0.029.

>> The block of code below follows the textbook for setup, then compares mean weights for first babies vs. others, showing that the mean weight of first babies is less than the mean weight of others. 

```python
import numpy as np
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

print(np.mean(firsts['totalwgt_lb']),';', np.mean(others['totalwgt_lb']))
print(np.mean(firsts['totalwgt_lb']) - np.mean(others['totalwgt_lb']))
```

>> This second block of code defines a cohenD function using numpy functions, then runs the function for the series we're interested in. From this we get the Cohen's D results stated above.

```python
def cohenD(group1, group2):
    
    m1, m2 = np.mean(group1), np.mean(group2)
    
    vars = [np.var(group1), np.var(group2)]
    weights = [len(group1), len(group2)]
    pooled_var = np.dot(vars, weights) / np.sum(weights)
    
    return (m1 - m2) / np.sqrt(pooled_var)
    
print(cohenD(firsts['totalwgt_lb'], others['totalwgt_lb']))
print(cohenD(firsts['prglngth'], others['prglngth']))
```
