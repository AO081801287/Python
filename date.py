from datetime import datetime as dt # import datetime Module
d1=input('enter date in YY-MM-DD:').strip()
d2=input('enter date in YY-MM-DD:').strip()
format= "%Y-%m-%d" # date format

def datedifference(date1, date2): 
        try:
                d1 = dt .strptime(date1,format)
                d2 = dt.strptime(date2, format)
        except Exception as e:
                print(e)
                return e
        return (d2 - d1)
print(datedifference(d1,d2))



