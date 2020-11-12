import json

class Time():

    def __init__(self, hrs,mins):
        self.hrs = hrs%24
        self.mins = mins

    def __add__(self,other):
        rezinmins = self.hrs*60+self.mins+other.hrs*60+other.mins
        hrs = rezinmins//60
        mins = rezinmins%60
        return Time(hrs,mins)

    def __sub__(self,other):
        rezinmins = self.hrs*60-self.mins+other.hrs*60+other.mins
        hrs = rezinmins // 60
        mins = rezinmins % 60
        return Time(hrs , mins)

    def __lt__(self,other):
        return True if self.hrs*60+self.mins<other.hrs*60+other.mins else False

    def __str__(self):
        return str(self.hrs)+':'+ ('' if self.mins>10 else '0')+str(self.mins)

'''
    def __lt__(self, other):
        return True if self.hrs * 60 + self.mins < other.hrs * 60 + other.mins else False
'''

class Film:

    def __init__(self,name,duration:Time):
        self.name = name
        self.duration = duration
        self.startTime = None

    def getEnd(self,start:Time):
        return start+self.duration




class CinemaHall:

    def __init__(self,startTime,endTime,name,numPlaces):
        self.timeTable = []
        self.startTime = startTime
        self.endTime = endTime
        self.name = name
        self.numPlaces = numPlaces

    def addFilm(self,film:Film,time:Time):
        added = False
        film.startTime = time
        i = 0
        while i<len(self.timeTable) and time<self.timeTable[i].getEnd():
            i+=1

        if time<self.startTime or self.endTime<time or self.timeTable[i].startTime<time<self.timeTable[i].getEnd():
            return False
        elif i==len(self.timeTable):
            added = True
            self.timeTable.append(film)
        elif time+Time(0,10)+film.duration<self.timeTable[i]:
            self.timeTable.insert(i,film)
            added = True
        else:
            added = False


        return added

    def deleteFilm(self,filmName):
        deleted = False
        i = 0
        while i < len(self.timeTable):
            if self.timeTable[i].name == filmName:
                self.timeTable.pop(i)
                deleted = True
            if deleted:
                break
            i+=1
        return deleted


class Cinema:

    def __init__(self):
        self.halls = {}
        self.films = {}

    def addHall(self,name,numPlaces):
        self.halls[name] = CinemaHall(Time(8,0),Time(20,0),name,numPlaces)

    def addFilm(self,film,hall,time):
        self[film.name] = film
        return self.halls[hall].addFilm(film,time)

    def getFilmInfo(self,filmName):
        return self.films[filmName]

    def getHallInfo(self,hallName):
        return self.halls[hallName]
        pass

    def deleteFilm(self,filmName):
        for elem in self.halls:
            self.halls[elem].deleteFilm(filmName)
        return True

cinema = Cinema()
cinema.addHall('Marvel',200)
