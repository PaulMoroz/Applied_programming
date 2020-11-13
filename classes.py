import json
import copy


class Time():

    def __init__(self, hrs, mins):
        self.hrs = hrs % 24
        self.mins = mins

    def __add__(self, other):
        rezinmins = self.hrs * 60 + self.mins + other.hrs * 60 + other.mins
        hrs = rezinmins // 60
        mins = rezinmins % 60
        return Time(hrs, mins)

    def __sub__(self, other):
        rezinmins = self.hrs * 60 - self.mins + other.hrs * 60 + other.mins
        hrs = rezinmins // 60
        mins = rezinmins % 60
        return Time(hrs, mins)

    def __lt__(self, other):
        return True if self.hrs * 60 + self.mins < other.hrs * 60 + other.mins else False

    def __str__(self):
        return str(self.hrs) + ':' + ('' if self.mins > 10 else '0') + str(self.mins)

    def __dict__(self):
        return {'Hrs': self.hrs, 'Mins': self.mins}

    def __copy__(self):
        return Time(self.hrs,self.mins)
'''
    def __eq__(self, other):
        return other!=None and self.mins==other.mins and self.hrs==other.hrs
'''

'''
    def __lt__(self, other):
        return True if self.hrs * 60 + self.mins < other.hrs * 60 + other.mins else False
'''


class Film:

    def __init__(self, name, duration: Time):
        self.name = name
        self.duration = duration
        self.startTime = None
        self.halls = set()

    def getEnd(self, start: Time):
        return start + self.duration

    def __dict__(self):
        toReturn = {'name': self.name, 'duration': self.duration.__dict__()}
        if self.startTime != None:
            toReturn['begin'] = self.startTime.__dict__()
            toReturn['end'] = self.getEnd(self.startTime).__dict__()
        return toReturn

    def copyFilm(self):
        return Film(self.name,self.duration.__copy__())

class CinemaHall:

    def __init__(self, startTime, endTime, name, numPlaces):
        self.timeTable = []
        self.startTime = startTime
        self.endTime = endTime
        self.name = name
        self.numPlaces = numPlaces
        self.numShows = {}

    def getFilm(self, filmName):
        for elem in self.timeTable:
            if elem.name == filmName:
                return elem
        return None

    def addFilm(self, film: Film, time: Time):
        added = False

        film.startTime = time
        i = 0

        while i < len(self.timeTable) and time > self.timeTable[i].getEnd(self.timeTable[i].startTime):
            i += 1

        if len(self.timeTable) > 0 and (
                self.endTime < time or self.timeTable[i].startTime < time < self.timeTable[i].getEnd()):
            return False
        elif i == len(self.timeTable):
            added = True
            self.timeTable.append(film)
        elif time + Time(0, 10) + film.duration < self.timeTable[i].startTime:
            self.timeTable.insert(i, film)
            added = True
        else:
            added = False

        if added == True:
            try:
                self.numShows[film.name] += 1
            except:
                self.numShows[film.name] = 1

        return added

    def deleteFilm(self, filmName, time=None):
        deleted = False
        i = 0
        while i < len(self.timeTable):
            if self.timeTable[i].name == filmName and (time == None or (
                    self.timeTable[i].startTime.hrs == time.hrs and self.timeTable[i].startTime.mins == time.mins)):
                self.timeTable.pop(i)
                self.numShows[filmName] -= 1
                deleted = True
            i += 1
        return deleted

    def __dict__(self):
        return {'Name': self.name, 'Timetable': list(film.__dict__() for film in self.timeTable),
                'startTime': self.startTime.__dict__(), 'endTime': self.endTime.__dict__(), 'numPlaces': self.numPlaces}


class Cinema:

    def __init__(self):
        self.halls = {}
        self.filmsData = {}
        self.films = {}

    def addHall(self, name, numPlaces):
        if self.halls.get(name) == None:
            self.halls[name] = CinemaHall(Time(8, 0), Time(20, 0), name, numPlaces)
            return True
        return False

    def addFilm(self, film):
        if self.films.get(film) == None:
            self.filmsData[film.name] = film.__dict__()
            self.films[film.name] = film
            return True
        return False

    def addFilmToTheCinemaHall(self, film, hall, time):
        return self.halls[hall].addFilm(self.films[film].copyFilm(), time)

    def moveFilm(self, filmName, hallFrom, timeFrom, hallTo, timeTo):
        if self.films.get(filmName)==None or self.halls.get(hallFrom) == None or self.halls.get(hallTo)==None:
            return False
        filmCopy = self.halls[hallFrom].getFilm(filmName)
        moved = False
        self.halls[hallFrom].deleteFilm(filmName, timeFrom)
        if self.addFilmToTheCinemaHall(filmCopy, hallTo, timeTo) == False:
            moved = False
            self.addFilmToTheCinemaHall(filmCopy, hallFrom, timeFrom)

        return moved

    def getFilmInfo(self, filmName):
        return self.films[filmName]

    def getHallInfo(self, hallName):
        return self.halls[hallName]
        pass

    def deleteFilm(self, filmName, hall=None, time=None):
        if hall == None and time == None:
            self.films.__delitem__(filmName)
        for elem in self.halls:
            if self.halls[elem].numshows[filmName] > 0:
                self.halls[elem].deleteFilm(filmName)
        return True

    def __dict__(self):
        return {'Halls': list(self.halls[hall].__dict__() for hall in self.halls),'Films':list(self.films[film] for film in self.films)}


cinema = Cinema()
cinema.addHall('Marvel',200)
cinema.addFilm(Film('Avengers',Time(2,0)))
cinema.addFilmToTheCinemaHall('Avengers','Marvel',Time(12,0))
print(cinema.__dict__())
