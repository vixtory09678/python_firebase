import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from firebase import firebase
import json


def stackedBarChart():

    result = firebase.get('waste/', None)
    y = json.dumps(result)
    df = pd.read_json(y)
    df = df.T
    df.set_index('date', inplace=True)

    truck1 = df.loc[df['id'] == 'b6c9b0fb34', [
        'recycle', 'non-recycle', 'biodegradable']].sum()
    truck2 = df.loc[df['id'] == '56a1aefba2', [
        'recycle', 'non-recycle', 'biodegradable']].sum()
    truck3 = df.loc[df['id'] == '47dce83340', [
        'recycle', 'non-recycle', 'biodegradable']].sum()
    truck4 = df.loc[df['id'] == '972bf0337f', [
        'recycle', 'non-recycle', 'biodegradable']].sum()
    truck5 = df.loc[df['id'] == '87d3ee3389', [
        'recycle', 'non-recycle', 'biodegradable']].sum()

    truckChart = pd.DataFrame({
        'Truck 1': truck1,
        'Truck 2': truck2,
        'Truck 3': truck3,
        'Truck 4': truck4,
        'Truck 5': truck5
    })
    truckChart = truckChart.T
    print(truckChart)
    truckChart.plot(kind='bar', stacked=True, figsize=(10, 7))
    plt.xticks(rotation='horizontal')
    plt.show()


def lineChart():

    result = firebase.get('waste/', None)

    y = json.dumps(result)
    df = pd.read_json(y)
    # print(df)
    df = df.T

    df.set_index('date', inplace=True)

    zoneA = df.loc[df['zone'] == 'A']
    zoneB = df.loc[df['zone'] == 'B']
    zoneC = df.loc[df['zone'] == 'C']

    ax1 = plt.subplot(311)
    plt.setp(ax1.get_xticklabels(), fontsize=6)
    plt.ylabel('Weight zone A')
    zoneA.plot(kind="line", ax=ax1)

    ax2 = plt.subplot(312)
    plt.setp(ax2.get_xticklabels(), fontsize=6)
    plt.ylabel('Weight zone B')
    zoneB.plot(kind="line", ax=ax2)

    ax3 = plt.subplot(313)
    plt.setp(ax3.get_xticklabels(), fontsize=6)
    plt.ylabel('Weight zone C')
    zoneC.plot(kind="line", ax=ax3)
    plt.show()


if __name__ == "__main__":
    # connect to firebase host
    firebase = firebase.FirebaseApplication(
        'https://rfid-c0802.firebaseio.com', None)

    stackedBarChart()
