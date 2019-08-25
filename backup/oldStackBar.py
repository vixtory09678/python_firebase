def stackBar():
    (result, keys) = getDataFirebase('waste/')
    # create variable list
    totalWeightRecycle = []
    totalWeightNonRecycle = []
    totalWeightBio = []

    # below will show you how to access data in result variable
    for key in keys:
        # access result[key]
        (node, keysNode) = getElementNode(result[key])

        sumRecycle = 0
        sumNonRecycle = 0
        sumBio = 0

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
    plt.xticks(ind, ["truck1", "truck2", "truck3", "truck4", "truck5"])
    # plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0], p3[0]),
               ('Recycle', 'Non-Recycle', 'Biodegradable'))

    plt.show()
