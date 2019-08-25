# ตัวอย่างโปรแกรมดึงค่าจาก Firebase แล้ว plot graph ด้วย matplotlib และ pandas

โปรเจคนี้ใช้ **Python 2.7.16**

### require install python-firebase

`pip install python-firebase`

### require install matplotlib

`pip install matplotlib`

### require install numpy

`pip install numpy`

### require install pandas

`pip install pandas`

---

### lineChart() Function

```Python
def lineChart():
    # ดึงข้อมูลจาก Firebase โดยเลือกข้อมูลจาก path 'waste/'
    result = firebase.get('waste/', None)
    # ข้อมูลจะอยู่ในรูปของ json object
    """
    result = {
        key : {
            date : ""
            bio : ""
            recycle : ""
            non-recycle : ""
            ...
        }
    }
    """

    y = json.dumps(result)
    # แปลงข้อมูลของ result ที่เป็น json object ให้อยู่ในรูปของ json string
    # y = "{key : {date : "",bio : "",recycle : "",non-recycle : ""}}"

    df = pd.read_json(y)
    # แปลง json string ให้อยู่ในรูปของ data frame เพื่อเอามาใช้ plot graph

    # print(df)
    df = df.T  # transpose data frame (สลับ row กับ column)

    df.set_index('date', inplace=True)  # set column แรก ให้เป็น date

    zoneA = df.loc[df['zone'] == 'A']  # ดึงข้อมูลเฉพาะ zone = A
    zoneB = df.loc[df['zone'] == 'B']  # ดึงข้อมูลเฉพาะ zone = B
    zoneC = df.loc[df['zone'] == 'C']  # ดึงข้อมูลเฉพาะ zone = C

    # plot graph
    zoneA.plot(kind='line', title="Total weight zone A")
    plt.xticks(rotation='vertical')

    zoneB.plot(kind='line', title="Total weight zone B")
    plt.xticks(rotation='vertical')

    zoneC.plot(kind='line', title="Total weight zone C")
    plt.xticks(rotation='vertical')
    plt.show()
```

### stackedBarChart() Function

```Python
def stackedBarChart():
    # ดึงข้อมูลจาก Firebase โดยเลือกข้อมูลจาก path 'waste/'
    result = firebase.get('waste/', None)
    # ข้อมูลจะอยู่ในรูปของ json object
    """
    result = {
        key : {
            date : ""
            bio : ""
            recycle : ""
            non-recycle : ""
            ...
        }
    }
    """

    y = json.dumps(result)
    # แปลงข้อมูลของ result ที่เป็น json object ให้อยู่ในรูปของ json string
    # y = "{key : {date : "",bio : "",recycle : "",non-recycle : ""}}"

    df = pd.read_json(y)
    # แปลง json string ให้อยู่ในรูปของ data frame เพื่อเอามาใช้ plot graph

    # print(df)
    df = df.T  # transpose data frame (สลับ row กับ column)
    df.set_index('date', inplace=True)  # set column แรก ให้เป็น date

    # ดึงข้อมูลเฉพาะ zone = A
    zoneA = df.loc[df['zone'] == 'A', [
        'recycle', 'non-recycle', 'biodegradable']]
    # ดึงข้อมูลเฉพาะ zone = B
    zoneB = df.loc[df['zone'] == 'B', [
        'recycle', 'non-recycle', 'biodegradable']]
    # ดึงข้อมูลเฉพาะ zone = C
    zoneC = df.loc[df['zone'] == 'C', [
        'recycle', 'non-recycle', 'biodegradable']]

    # plot graph โดยดึงข้อมูลเฉพาะของ ['recycle', 'non-recycle', 'biodegradable']
    zoneA.loc[:, ['recycle', 'non-recycle', 'biodegradable']].plot(
        kind='bar', title='Zone A', stacked=True, figsize=(10, 7))
    zoneB.loc[:, ['recycle', 'non-recycle', 'biodegradable']].plot(
        kind='bar', title='Zone B', stacked=True, figsize=(10, 7))
    zoneC.loc[:, ['recycle', 'non-recycle', 'biodegradable']].plot(
        kind='bar', title='Zone C', stacked=True, figsize=(10, 7))
    plt.show()
```

---

1. Import library

```
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd
import numpy as np
from firebase import firebase
import json
```

2. Connect to Firebase HOST

```python
if __name__ == "__main__":
    # connect to firebase host
    firebase = firebase.FirebaseApplication(
        'https://rfid-c0802.firebaseio.com', None)
```

3. Call function

```python
stackedBarChart()
#lineChart()
```
