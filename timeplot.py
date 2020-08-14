from matplotlib import pyplot as plt
from matplotlib import dates as mplt_dates
from datetime import datetime, timedelta
import pandas as pd

# style
plt.style.use('seaborn')
dates = [
    datetime(2020, 8, 8),
    datetime(2020, 8, 9),
    datetime(2019, 8, 10),
    datetime(2020, 8, 11),
    datetime(2020, 8, 12),
    datetime(2020, 5, 22)]
y = [0, 1, 2, 3, 4, 5]
plt.plot_date(dates, y, linestyle='solid')
date_formater = mplt_dates.DateFormatter('%b,%d,%Y')
plt.gca().xaxis.set_major_formatter(date_formater)
plt.gcf().autofmt_xdate()
# show plot
plt.tight_layout()
plt.savefig('./plots/timeplot.png')
plt.show()
