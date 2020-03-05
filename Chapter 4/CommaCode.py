# Function that reads the contents of a list and returns it as a readble string 
def list_to_string(someList):
    resString = ''  # Stores what the resulting value is.

    if(someList == []): # Checks if list is empty.
        return(reSstring)
    else:               # Other wise proceed to loop through list.
        for i in someList:
            if(i != someList[-1]):
                resString += (i + ', ')
            else:
                resString += ('and ' + i)

    return(resString)
