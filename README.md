# Crawling me Beautifulsoup
Detyra e tretë nga Lënda “Siguria në Internet”. Grupi i 20

# Rreth këtij aplikacioni

Cka është crawling?
Crawling është marrja automatike e të dhënave duke përdorur ndonjë software ose ndonjë aplikacion. Në rastin tonë ne kemi pasur të ndërtojmë një aplikacion i cili i merr të dhënat nga ndonjë web-faqe (në rastin tonë IMDB), edhe me i nxjerr të dhënat prej asaj web-faqe dhe i ruan ato të dhënat në një spreadsheet.
# Kërkesat

Që ky aplikacion të punojë duheni t’i instaloni këto libraritë duke përdorur [pip](https://pip.pypa.io/en/stable/) package installer

```bash
from tkinter import *
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
import matplotlib.pyplot as plt
```

# Startimi i aplikacionit

Për me e startu aplikacionin veq hyni te [DataCrawling-tkinter.py] edhe ekzekutoni kodin. Nëse keni të instaluar [Visual Studio Code]( https://code.visualstudio.com/) veq shtypni butonin [F5]

![executing the code](https://media.giphy.com/media/01cTq1eJHnR8Sq1GWQ/giphy.gif) 

# Rezultatet

**Fillimi i ekzekutimit**

![Fillimi i ekzekutimit]( https://media.giphy.com/media/pUilZYce1cPpQSE3UV/giphy.gif)

**Fundi i ekzekutimit**

![Fundi i ekzekutimit]( https://media.giphy.com/media/DDC8InLGHLbvS8r0P9/giphy.gif)

**Rezultati në Excel:**

![](Images/resultExcel.PNG)

**Rezultati nga Chart-i:**

![](Images/resultChart.PNG)

**Printojmë disa informacione në DataFrame me anë të librarisë Panda:**

![](Images/resultPanda.PNG)

# Konkludimi
Si konkludim ne kemi arritur me sukses të marrim rreth 2862 filma me emrat e tyre, imdb-rating të tyre, vitin kur kanë dalë, etj. një web-faqe(IMDB), t’i paraqesim të dhënat në një graf, si dhe t’i paraqesim të gjitha të dhënat e marrura nga web-faqja në një Excel spreadsheet. Si dhe kemi mësuar qysh përdoren libraritë si: tkinter. Panda, matplotlib dhe BeautifulSoup.


Për shkak të dhënave të mëdhaja të cilat ekstraktohen nga web-sajti, ekzekutimi i kodit mund të zgjas prej 20 deri në 30 minuta, varësisht prej fuqisë procesorike të llaptopit apo kompjuterit juaj.

Nëse doni që ekzekutimi i kodit të zgjasë më pak, shkoni te rreshti i 27 (**years_url = [str(i) for i in range(2010, 2021)]**) edhe ndrroni range qysh e doni, sa ma pak vite aq më shpejt ekzekutohet kodi

# Referencat

* https://www.youtube.com/watch?v=YXPyB4XeYLA&ab_channel=freeCodeCamp.org
* https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer
* https://matplotlib.org/3.2.1/tutorials/introductory/sample_plots.html
* https://www.python-course.eu/python_tkinter.php
