import re
from django.utils import timezone
def datadifference(articles):
    #pattern = re.compile(r'(\d{4})|(\d{2})')
    dates=list()
    for article in articles:
        #print(article.reserve_date)
        #print(re.findall(pattern , article.reserve_date))
        dates.append(re.split('(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})', article.reserve_date))
        #time=
    
    now=datetime.datetime.now()
    print(now)

                
    for i in range(len(dates)):
        for j in range(1,6):
            print(int(dates[i][j]),end="-")
            dates[i][j]=int(dates[i][j])
        
        print()

    for i in range(len(dates)-1):
        pass
