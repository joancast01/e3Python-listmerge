def listmerge(list1, list2):
    # creates a new emtpy list, will contain sorted list
    newlist = []
    # Steps through each list, checking to see if the list item is already included in the list
    for item in list1:
        if item in list1:
            newlist.append(item)
    for item in list2:
        if item not in newlist:
            newlist.append(item)
    newlist.sort()
    return newlist


firstlist = ["American Pie", "Respect", "Uptown Girl", "Bohemian Rhapsody", "(Sittin' On) the Dock of the Bay",
             "Heart of Glass"]
secondlist = ["Bohemian Rhapsody", "Hey Jude", "Respect", "Thriller", "Promised Land", "American Pie"]

print(listmerge(firstlist, secondlist))
