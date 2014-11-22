#Dev Sethi
#CIT 590 HW 4

movieInfo = {}
def createDb():
    '''Imports data from local disk into a dict'''
    global movieInfo
    f = open('movies1.txt')
    for line in f:
        line = line.rstrip()
        movie = line.split(':')[0].lower()
        actors = line.split(':')[1].split(',')
       
        for i in range(0,len(actors)):
                actors[i] = actors[i].lower()
        movieInfo[movie] = actors


        
def insertIntoDb(movieTuple):
    '''Inserts new movie and actors or adds actors to an existing movie'''
    #Check if movie already exists in Db
    lowerActors = list()                    
    lowerMovie = movieTuple[0].lower() 
    actorSet = set()                     
                   
    if(type(movieTuple) == tuple):            
        if movieInfo.has_key(movieTuple[0]):    #if movie name already exists
            print movieInfo[movieTuple[0]]
            actorSet = list2set(movieTuple[0])
                
            for i in range(0,len(movieTuple[1])):
                actorSet.add(movieTuple[1][i].lower())          #add all the user-entered names to the actorSet automatically removing duplicates
               
            movieInfo[movieTuple[0]]=[]                         #empty all the values for the given movie

            for i in range(0,len(actorSet)):
                movieInfo[movieTuple[0]].append(actorSet.pop().lower()) #Populate the movie key with the elements of actorSet
            return 1
        else:                                  #if movie name is new
            for i in range(0,len(movieTuple[1])):
                lowerActors.append(movieTuple[1][i].lower())    #make names lowercase 
            movieInfo[movieTuple[0].lower()]= lowerActors       #assign actor anmes to movie name key
            return 1
    else:
        return -1

def deleteFromDb(movie):
    '''Deletes a movie from database'''
    if movieInfo.has_key(movie):
        del movieInfo[movie]
        return 1
    else:
        return -1

def selectMovieInfo(movie):
    '''Returns the actors of a given movie'''
    if movieInfo.has_key(movie):
        print movieInfo[movie]
        return movieInfo[movie]

    else:
        print movie + " is not in database."
        return []

def selectActorInfo(actorName):
    '''Returns the filmography of a given actor'''
    actorName = actorName.lower()
    movieList =list()
    movieInfoCopy = movieInfo.copy()    #Shallow copy of movieInfo which can iterate through distructively

    for i in range(0,len(movieInfoCopy)): #cycle through all the movies in dictionary
        holder = movieInfoCopy.popitem()    #remove each movie along the way

        for j in range(0,len(holder[1])):      #cycle though all the actors in this movie
            if holder[1][j] == actorName:  
                movieList.append(holder[0]) #movie name to list if match
                break

    print movieList
    return movieList

def getCommonActors(movie1, movie2):
    '''Returns the actors who have starred in two specifed movies'''
    if (movieInfo.has_key(movie1) & movieInfo.has_key(movie2)):
        actorSet1 = list2set(movieInfo[movie1]) 
        actorSet2 = list2set(movieInfo[movie2]) 
        return list(actorSet1.intersection(actorSet2))
    else:
        if movieInfo.has_key(movie1):
            print movie2 + " is not in the database."
        elif movieInfo.has_key(movie2):
            print movie1 + " is not in the database."
        else:
            print "Neither movie is in the database."

def getCoActors(actorName):
    '''Returns list of all a specified actors co-stars'''
    actorSet = set()
    movieList = selectActorInfo(actorName)
    for i in range(len(movieList)):
        actorList = selectMovieInfo(movieList[i])
        actorSet = list2set(actorList)
    actorSet.remove(actorName)
    return list(actorSet)
    
def getLargestEnsembleCast():
    '''Scans through dictionary to find longest value list and returns the key'''
    movieInfoCopy = movieInfo.copy()
    largest = 0
    for i in range(len(movieInfo)):
        holder = movieInfoCopy.popitem()
        size = len(holder[1])
        if (size > largest):
            largest = size
            largestEnsembleCast = holder[0]
    return largestEnsembleCast


def list2set(ls):
    '''converts lists into sets'''
    newSet = set()
    for i in range(len(ls)):
        newSet.add(ls[i])
    return newSet

def getCommonMovie(actor1, actor2):
    '''Returns the movies in which both actors have worked'''
    movieSet1 = list2set(selectActorInfo(actor1))
    movieSet2 = list2set(selectActorInfo(actor2))

    return list(movieSet1.intersection(movieSet2))
    
     
def main():
    createDb()
    entry = str()
    while (entry != 'q'):
        print "\nSelect one:"
        print "a Insert"
        print "b Delete"
        print "c Select movie information"
        print "d Select actor information"
        print "e Find common actors for a given pair of movies"
        print "f Get all co-actors of a given actor"
        print "g Get largest ensemble cast"
        print "h Get common movie"
        print "q Quit"
        entry = raw_input("Entry: ").lower()

        if (entry == 'a'):
            movieName = raw_input("Please enter movie name: ")
            actorList = list()
            actor = str()
            while (actor != 'q'):
               actor = raw_input("Please enter actor name (enter q when finished): ")
               actorList.append(actor)
            movieTuple = (movieName, actorList)
            x = insertIntoDb(movieTuple)
            if (x == 1):
                print "Insertion successful"
            else:
                print "Insertion unsuccessful, please try again and check formatting"

        elif (entry == 'b'):
            movie = raw_input("Enter movie to delete: ")
            x = deleteFromDb(movie.lower())
            if (x == 1):
                print movie + " deleted succesfully."
            else:
                print movie + " not found in database, please try again"
        
        elif (entry == 'c'):
            movie = raw_input("Please enter movie name: ")
            print "Actors in " + movie + ": "
            selectMovieInfo(movie.lower())

        elif (entry == 'd'):
            actorName = raw_input("Enter actor name: ")
            print actorName + " is featured in:"
            selectActorInfo(actorName.lower())

        elif (entry == 'e'):
            movie1 = raw_input("Enter first movie: ")
            movie2 = raw_input("Enter second movie: ")
            print "Common actors in" + movie1 + " and " + movie2 + " are:"
            print getCommonActors(movie1.lower(), movie2.lower())

        elif (entry == 'f'):
            actorName = raw_input("Enter actor name: ")
            print actorName + " has starred alongside:"
            print getCoActors(actorName.lower())

        elif (entry == 'g'):
            print getLargestEnsembleCast() + " has the largest cast"

        elif (entry == 'h'):
            actor1 = raw_input("Enter first actor: ")
            actor2 = raw_input("Enter second actor: ")
            print actor1 + " and " + actor2 + " are in:"
            print getCommonMovie(actor1.lower(), actor2.lower())

        elif (entry == 'q'):
            break
        
        else:
            print "Incorrect entry, please try again."


if __name__ == "__main__":
    main()
