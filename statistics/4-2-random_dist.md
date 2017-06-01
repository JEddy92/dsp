[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> I upped the number of random draws to 100,000 to smooth out the results / make them more robust. I leveraged the text code pmf, cdf, and plotting methods. As shown below, the resulting distribution is visually indistinguishable from the standard uniform. The pmf fills evenly across the entire range of values, and the cdf appears as a straight line, indicating that all values in the range have equal probability.

```python
import numpy as np
np.random.seed(1)

import thinkstats2
import thinkplot

rand_1000 = np.random.random(100000)
rand_pmf = thinkstats2.Pmf(rand_100000, label='1000 random draws')
rand_cdf = thinkstats2.Cdf(rand_100000, label='1000 random draws')

thinkplot.Pmf(rand_pmf)
thinkplot.Show(xlabel='Random draw value', ylabel='PMF')

thinkplot.Cdf(rand_cdf)
thinkplot.Show(xlabel='Random draw value', ylabel='CDF')
```

![Plot1](https://github.com/JEddy92/dsp/blob/master/statistics/Random_pmf.png)

![Plot2](https://github.com/JEddy92/dsp/blob/master/statistics/Random_cdf.png)
