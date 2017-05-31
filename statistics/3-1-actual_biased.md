[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> I leveraged the code in the text to create and plot pmf objects for the actual and biased distributions of number of children in a family. The text includes a BiasPmf function that I use -- this works by scaling the probability of each item in the pmf by its size to capture the effect of observer bias and then renormalizing the pmf. In this case, if we choose randomly we are more likely to survey a child in a larger family than if we survey by family, and it is no longer possible for the observed number of children to be 0. So the biased pmf adjusts numbers of children above 1 to make them more probable, and makes 0 children have probability 0.


```python
%matplotlib inline

import numpy as np

import nsfg
import thinkstats2
import thinkplot

resp = nsfg.ReadFemResp()

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

pmf_actual = thinkstats2.Pmf(resp['numkdhh'], label='actual')
pmf_biased = BiasPmf(pmf_actual, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_actual, pmf_biased])
thinkplot.Show(xlabel='Children in family',ylabel='Probability mass',axis=[-1, 7, 0, 0.6])
```


![Plot](https://github.com/JEddy92/dsp/blob/master/statistics/ex3.1_plot.png)


>> Finally, I compute the means of the actual and biased pmfs. It turns out that the biased mean is nearly 1.4 children in the family higher than the unbiased mean, showing the distortionary effect of observer bias.


```python
print('Actual distribution mean: %f' % pmf_actual.Mean())
print('Biased distribution mean: %f' % pmf_biased.Mean())
print('Biased mean - actual mean: %f' % (pmf_biased.Mean() - pmf_actual.Mean()))
```

```
Actual distribution mean: 1.024205
Biased distribution mean: 2.403679
Biased mean - actual mean: 1.379474
```
