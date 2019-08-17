import matplotlib.pyplot as plt
import numpy as np
from firebase import firebase
import json


def getDataFirebase(url):
    keys = []
    result = firebase.get(url, None)
    for key in result.keys():
        keys.append(key)

    return (result, keys)


def getElementNode(result):
    keys = []
    for key in result.keys():
        keys.append(key)
    return (result, keys)


# connect to firebase host
firebase = firebase.FirebaseApplication(
    'https://rfid-c0802.firebaseio.com', None)

# create variable list
totalWeightRecycle = []
totalWeightNonRecycle = []
totalWeightBio = []

# get data from path
# return result and keys of path
(result, keys) = getDataFirebase('/waste')

"""
# print result should be
{
    "56a1aefba2":{blabla},
    "47dce83340":{blabla},
    "b6c9b0fb34":{blabla},
    "87d3ee3389":{blabla}
}
# print keys should be
["56a1aefba2", "47dce83340", "b6c9b0fb34", "87d3ee3389"]

So, if you want to access data in result with key
result["56a1aefba2"]
"""

# below will show you how to access data in result variable
for key in keys:
    # access result[key]
    (node, keysNode) = getElementNode(result[key])

    sumRecycle = 0
    sumNonRecycle = 0
    sumBio = 0

    # access result[key][keyNode]["recycle"]
    # access result[key][keyNode]["non-recycle"]
    # access result[key][keyNode]["biodegradable"]
    # key is id truck
    # keyNode is key of data
    for keyNode in keysNode:
        sumRecycle = sumRecycle + node[keyNode]["recycle"]
        sumNonRecycle = sumNonRecycle + node[keyNode]["non-recycle"]
        sumBio = sumBio + node[keyNode]["biodegradable"]

    totalWeightRecycle.append(sumRecycle)
    totalWeightNonRecycle.append(sumNonRecycle)
    totalWeightBio.append(sumBio)


# plot graph
N = len(totalWeightRecycle)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

dataset1 = np.array(totalWeightRecycle)
dataset2 = np.array(totalWeightNonRecycle)
dataset3 = np.array(totalWeightBio)

p1 = plt.bar(ind, dataset1, width, color='g')
p2 = plt.bar(ind, dataset2, width, bottom=dataset1, color='b')
p3 = plt.bar(ind, dataset3, width, bottom=dataset1+dataset2, color='r')

plt.ylabel('Kg.')
plt.title('Total weight')
plt.xticks(ind, keys)
# plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0], p3[0]), ('Recycle', 'Non-Recycle', 'Biodegradable'))

plt.show()
