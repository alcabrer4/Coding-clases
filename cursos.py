# import classes
# classes.hello()       
from os import linesep, read


def hello():
    print("Hello world")

#Convert elevator floors 
def floor():
    euf = input('Europe floor?')
    usf = int(euf) + 1
    print('US floor: ', usf)

#Calculates gross pay
def payone():
    hrs = input('Enter hours worked:')
    rate = input('Enter rate per hour:')
    pay = float(hrs)*float(rate)
    print('Pay:', pay)

# classes.es_par()
def es_par():
    print('¿Por o Impar?')
    x = int(input('Ingrese un numero:'))
    if x%2 == 0:
        return True
    else:
        return False

# try and except sample
def trex():
    rawstr = input('enter a number:')
    try:
        ival = int(rawstr)
    except:
        ival = -1
    if ival >= 0:
        print('Good Job')
    else:
        print('Not a number')

def paytwo():
    hrs = input('Enter hours worked:')
    rate = input('Enter rate per hour:')
    try:
        h = float(hrs)
        r = float(rate)
    except:
        print('please enter the number in numerical form')
        quit()
    if hrs <= 40:
        pay = h*r
        ovtm = 0
    else:
        ovtm = (h - 40)*r*1.5
        pay = 40*r
    tp = pay + ovtm
    print('Pay:', tp)

def score():
    score = input('Enter your score:')
    s = float(score)
    if s > 1 or s < 0:
        print('Score should be between 0 and 1')
        quit()
    if s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    elif s < 0.6:
        print('F')

def addtwo(a, b):
    added = a + b
    return added

def test():
    h = float(input('Enter hours worked:'))
    r = float(input('Enter rate per hour:'))
    def computepay(h, r):
        if  h <= 40:
            pay = h*r
            ovtm = 0
        else:
            ovtm = (h - 40)*r*1.5
            pay = 40*r
        tp = pay + ovtm
        return tp
    computepay(h, r)
    print('Pay', computepay(h,r))

def conbreak():
    i = 0
    while i < 10:
        i += 1
        if i == 3:
            continue
        print(i)
        if i == 9:
            break
def largest():
    largest = int(input('give me a number'))
    for i in [10, 39, 67, 3, 5, 88]:
        if i > largest:
            largest = i
        else:
            continue
    print('largest:', largest)

def counloop():
    x = []
    y = 0
    for i in range(5):
        n =  int(input('Dame un numero:'))
        x.append(n)
    for h in x:
        if h == 5:
            f = True
            print ('There is a 5')
        y = y + h
        print(h, y)

def smallest():
    s = None
    x = []
    for i in range(5):
        n =  int(input('Dame un numero:'))
        x.append(n)
    for h in x:
        if s is None:
            s = h
        elif h < s:
            s = h
    print(s)

def smbg():
    s = None
    b = None
    x =[]
    while True:
        n = input('Enter a number:')
        if n == 'done':
            break
        try:
            nn = int(n)
        except:
            print('Invalid input')
        x.append(nn)
        for h in x:
            if s is None:
                s = h
            elif h < s:
                s = h
        for i in x:
            if b is None:
                b = i
            elif i > b:
                b = i
    print('Maximum:', b)
    print('Minimum:', s)

#this counts how many letters are in a word and enters a letter of it
#it also loops through it telling us if there's a letter in it or not
def fruits():
    f = input('tell me a fruit:')
    i = int(input('give me a number:'))
    a = 0
    w = input('give me letter:')
    print('this is the lenght:', len(f))
    print('your letter is:', f[i])
    for l in f:
        print(l, a)
        a += 1
    tf = w in f
    print('your letter is in the word?:', tf)

#Slice a part of a string
def slicing():
    text = "X-DSPAM-Confidence:     0.8475";
    x = int(text.find('0'))
    print(x,type(x))
    y = int(text.find('5'))
    print(y, type(y))
    z = text[x:y+1]
    zz = float(z)
    print(zz)

#read through a file and print the content in upper case
def words():
    fn = input('Enter a file name:')
    f = open(fn)
    fr = f.read()
    fu = fr.upper()
    print(fu)


def word2():
    fn = input('Enter a file name:')
    f = open(fn)
    x = 0
    y = 0
    for i in f:
        if i.startswith('X-DSPAM-Confidence:'):
            x += 1
            a = int(i.find('0'))
            b = int(i.find('\n', a))
            c = i[a:b]
            d = float(c)
            y += d
    z = y/x
    print('Average spam confidence:', z)

#Sorting a list, appending stuff and checking if the stuff is already in
def sorting():
    fn = input('Enter a file name:')
    f = open(fn)
    x = []
    for l in f:
        lrst = l.rstrip()
        lsp = lrst.split()
        for w in lsp:
            if w not in x:
                x.append(w)
    print(x)
    x.sort()
    print(x)

def mail():
    fn = input('Enter a file name:')
    f = open(fn)
    x = 0
    for l in f:
        if l.startswith('From '):
            x += 1
            lsp = l.split()
            print(lsp[1])
    print("There were", x, "lines in the file with From as the first word")
#this is a dictionary
def purse():
    bag = {}
    z = input('Do you want to buy?')
    while  z != 'no':
        x = input('What will you buy?')
        y = int(input("What's the price?"))
        bag[x] = y #this is how you save stuff 
        z = input('Want to buy more?')
    print(bag)

#Counting stuff with dictionaries
def cuenta():
    c = {}
    l = []
    z = None
    while True:
        z = input('what are you buying?')
        if z == ' ':
            break
        l.append(z)
    print(l)
    for stuff in l:
        c[stuff] = c.get(stuff, 0) + 1
    print(c)

#Counting words in a file
def palabra():
    palabras = {}
    bigp = None
    bigcount = None
    finame = input('Enter a file name:')
    try:
        openf = open(finame)
    except:
        print("That's not a file")
        quit()
    for line in openf:
        words = line.split()
        for w in words:
            palabras[w] = palabras.get(w, 0) + 1
    print('Words', palabras)
    print(palabras.keys()) #this gives me a list of the keys
    print(palabras.values()) #this gives me a list of values 
    for p, c in palabras.items(): #this tells me the most used word
        if bigcount is None or c > bigcount:
            bigp = p
            bigcount = c
    print(bigp, bigcount)

def sender():
    palabras = {}
    palabrota = None
    veces = None
    finame = input('Enter a file name:')
    try:
        openf = open(finame)
    except:
        print("That's not a file")
        quit()
    for line in openf:
        if line.startswith('From '):
            lispl = line.split()
            a = lispl[1]
            palabras[a] = palabras.get(a, 0) + 1
    for p, v in palabras.items(): #this tells me the most used word
        if veces is None or v > veces:
            palabrota = p
            veces = v
    print(palabras)
    print(palabrota, veces)

def tupi():
    c = {}
    while True:
        a = input('Want to add?')
        if a == ' ':
            break
        b = input('What will you buy?')
        d = input('How many?')
        c[b] = d
    print( sorted ( [ (v,k) for k,v in c.items() ] ) )

def dnh():
    dh = {}
    finame = input('Enter file name:')
    try:
        openfi = open(finame)
    except:
        print('That is not a file!')
        quit()
    for line in openfi:
        if line.startswith('From '):
            lispl = line.split()
            hour = lispl[5]
            pot = hour.split(':')
            hr = pot[0]
            dh[hr] = dh.get(hr, 0) + 1
    fdh = sorted( [ (k,v) for k,v in dh.items() ] )
    for i in fdh:
        print (*i) # * => unpacking

def regex():
    import re # This is the library for regular expresions
    hand = open('mbox-short.txt')
    for line in hand:
        line =line.rstrip()
        if re.search('^From: ', line):
            b = re.findall('\S+@\S+', line)
            print(b)
            print(line) # ^ => match the start of the line
    x = 'My favorite 2 numbers are 19 and 42'
    y = re.findall('[0-9]+', x)
    print(y)
    z = re.search('From:', x)
    print(z)
    a = re.search('My ', x)
    print(a)
    # . => any character
    # + => one or more times
    # ? => shortest
    # ^F.+?: => first character in the match is F
    # any number of characters, one or more times, the shortest
    #last character in the match is ':'
    #\S => at least one non-white character

def paco():
    p = 'Mexico'
    c = 'America'
    print(p, type(p))
    print(c, type(c))

def white():
    import re
    x = 'From al.cabrer4@gmail.com Abril 21 11:38'
    y = re.findall('\S+@\S+', x)
    print(y)

def lasuma():
    import re
    s = []
    finame = input('Give me the name of the file:')
    try:
        openfi = open(finame)
    except:
        print('That is not a file!')
        exit()
    for line in openfi:
        if re.search('[0-9]+', line):
            numeros = re.findall('[0-9]+', line)
            for numerito in numeros:
                n = int(numerito)
                s.append(n)
    print(sum(s))

# Esta es la manera corta de hacer el ejercicio anterior
#def lasumita():
#import re 
#print( sum( [ ****** *** * in **********('[0-9]+',************.read())]))

def sock():
    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    print(cmd)
    print(type(cmd))
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data)< 1):
            break
        print(data.decode())
    mysock.close()
# import requests
# r = requests.get('http//data.pr4e.org/romeo.txt')
# print(r.txt)
# can also be done like this, but it's more advanced

def beau():
    import urllib
    from bs4 import BeautifulSoup as BS

    x = 0
    url = input('Enter a link:')
    html = urllib.request.urlopen(url).read()
    soup = BS(html, 'html.parser')

    #Retrieve all of the anchor tags
    tags = soup('span')
    for tag in tags:
        x += int(tag.contents[0])
    print(x)
#parts of a tag
#TAG = tag
#URL = tag.get('href', None)
#Contents = tag.contents[0]
#Attributes = tag.attrs

def bello():
    import urllib
    from bs4 import BeautifulSoup as BS
    x = 0
    name = input('Enter a name:')
    #this is easier for this particular work, like a repetitive task
    url = 'http://py4e-data.dr-chuck.net/known_by_' + name + '.html'
    html = urllib.request.urlopen(url).read()
    soup = BS(html, 'html.parser')
    tags = soup.find_all('a')
    for tag in tags:
        x += 1
        print(x, tag.get('href', None))

def arbol():
    from urllib import request as rq
    from urllib import error as er
    import xml.etree.ElementTree as ET
    x = 0
    url = input('Enter a url:')
    html = rq.urlopen(url).read()
    root = ET.fromstring(html)
    for fruta in root.findall('.//count'):
        f = int(fruta.text)
        x += f
    print(x)

#Este es mas pro pero hacen lo mismo
def arbol2():
    from urllib import request as rq
    from urllib import error as er
    import xml.etree.ElementTree as ET
    x = 0
    url = input('Enter a url:')
    html = rq.urlopen(url).read()
    root = ET.fromstring(html)
    for fruta in root.findall('.//comment'):
        f = fruta.find('count').text
        ff = int(f)
        x += ff
    print(x)

def jason():
    import json
#you can also use lists for this
    data = '''
    {
        "name": "Alejandro",
        "phone": {
            "type": "intl",
            "number": "+52 7471500954"
        },
        "email":{
            "hide": "yes"
        }
    }'''
    info = json.loads(data) #this parses through the info
    print(info)
    print('Name:', info["name"])
    print ('Hide:', info ["email"]["hide"])

def jasonito():
    from urllib import request as rq
    from urllib import error
    from json import loads
    y = 0
    url = input('enter a url:')
    html = rq.urlopen(url).read()
    info = loads(html)
    for i in info["comments"]:
        x = int(i["count"])
        y += x
    print(y)

def gg():
    import urllib.request, urllib.parse, urllib.error
    import json
    service = 'http://py4e-data.dr-chuck.net/json?'
    while True:
        direccion = input('Enter an address:')
        if len(direccion) < 1: break
        lapiz = {}
        lapiz['address'] = direccion
        lapiz['key'] = 42
        url = service + urllib.parse.urlencode(lapiz)
        print(url)
        data = urllib.request.urlopen(url).read()
        dd = data.decode()
        jaime = json.loads(dd)
        placeid = jaime["results"][0]["place_id"]
        print(placeid)

class person:
    def __init__(self, name, age): #classes.person(x, y)
        self.name = name
        self.age = age

    def __repr__(self): #x
        return self.name + ' de ' + str(self.age) + ' años'

    def myname(self): #x.myname()
        print('Hello my name is ', self.name)

class job:
    def __init__(self, name):
        self.name = name
        self.workers = []

    def addw(self, worker:person):
        self.workers.append(worker)

    def workers(self):
        for w in self.workers:
            print(w.person)

class player(person): #Esta clase expande sobre la clase:"person".
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def intro(self):
        print('Con el numero ', self.num, ', ', self.name)

#-------------------------------SQL Classes--------------------------------
# In sqlite:
# To create somthing you do: CREATE

# To create a table: 
#CREATE TABLE x(
# y VARCHAR(128) <-- The 128 is the lenght accepted, can be less, no more
# z VARCHAR(128)
#)

# To insert something in the table created:
#INSERT INTO x(y, z) VALUES('abc', 'def')

# To update:
#UPDATE x SET y='ghi' WHERE z='def'

# To delete:
#DELETE FROM x WHERE z='def'

# To retrieve records:
#SELECT * FROM x <-- The "*" means all columns, so it's all
#SELECT * FROM X WHERE z='def' <-- Just one row 
#SELECT * FROM X ORDER BY y <-- That orders them

# To join data:
#SELECT Album.title, Artist.name FROM Album JOIN Artist on Album.artist_id=Artist.id
# The ON clause gives only the combinations that match

def marte():
    import sqlite3
    import re
    conn = sqlite3.connect('mbox.sqlite')
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS Counts''')
    cur.execute('''CREATE TABLE Counts( org TEXT, count INTEGER)''')
    fina = input('Enter a file name:')
    fop = open(fina)
    for linea in fop:
        if re.search('^From: ', linea):
            org = re.findall('@\S+', linea)
            o = org[0][1:]
            cur.execute('''SELECT count FROM Counts WHERE org = ?''', (o,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts(org, count)
                    VALUES(?, 1)''', (o,))
            else:
                cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (o,))
    conn.commit()
    cur.close()

def cancion():
    import sqlite3
    import xml.etree.ElementTree as ET

    conn = sqlite3.connect('canciones.sqlite')
    cur = conn.cursor()
    cur.executescript('''DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Genre;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Track;

        CREATE TABLE Artist(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
            );
        CREATE TABLE Genre(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
            );
        CREATE TABLE Album(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id INTEGER,
            title TEXT UNIQUE
            );
        CREATE TABLE Track(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            artist_id INTEGER,
            album_id INTEGER,
            genre_id INTEGER,
            len INTEGER,
            rating INTEGER,
            count INTEGER
            )''')

    def encontrar(a, x):
        encontrado = False
        for i in a:
            if encontrado:
                return i.text
            if i.text == x:
                encontrado = True
        return None

    tree = ET.parse('Library.xml')
    dicks = tree.findall('dict/dict/dict')
    for dick in dicks:
        title = encontrar(dick, 'Name')
        album = encontrar(dick, 'Album')
        genre = encontrar(dick, 'Genre')
        rating = encontrar(dick, 'Rating')
        artist = encontrar(dick, 'Artist')
        count = encontrar(dick, 'Play Count')
        lenght = encontrar(dick, 'Total Time')

        if title is None or album is None or genre is None or rating is None or artist is None or count is None or lenght is None: continue

        cur.execute('''INSERT OR IGNORE INTO Artist(name)
        VALUES(?)''', (artist,))
        cur.execute('''Select id FROM Artist WHERE name = ?''', (artist,))
        artistid = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album(title, artist_id)
        VALUES(?,?)''', (album, artistid))
        cur.execute('''Select id FROM Album WHERE title = ?''', (album,))
        albumid = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Genre(name)
        VALUES(?)''', (genre,))
        cur.execute('''Select id FROM Genre WHERE name = ?''', (genre,))
        genreid = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track(title, artist_id, album_id, genre_id, len, rating, count)
        VALUES(?, ?, ?, ?, ?, ?, ?)''', (title, artistid, albumid, genreid, lenght, rating, count))


    cur.execute('''SELECT Track.title, Album.title, Artist.name, Genre.name, Track.len, Track.rating, Track.count FROM Album JOIN Artist JOIN Genre JOIN Track ON Track.album_id=Album.id AND Track.genre_id=Genre.id AND Track.artist_id=Artist.id ''')
    conn.commit()

def pollo():
    import json
    import sqlite3

    conn = sqlite3.connect('roster.sqlite')
    cur = conn.cursor()
    cur.executescript('''DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE);
    CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE);
    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id))
        ''')

    fina = input('Enter a file name:')
    if len(fina) < 1:
        fina = 'roster_data.json'
    fop = open(fina).read()
    lock = json.loads(fop)
    from random import randint as rdi
    for i in lock:
        user = i[0]
        course = i[1]
        role = i[2]

        cur.execute('''INSERT OR IGNORE INTO User(name) VALUES(?)''', (user,))
        cur.execute('''SELECT id FROM User WHERE name = ?''', (user,))
        userid = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES(?)''', (course,))
        cur.execute('''SELECT id FROM Course WHERE title = ?''', (course,))
        courseid = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member(user_id, course_id, role) VALUES(?, ?, ?)''', (userid, courseid, role))

        jaja = rdi(0, 50)
        if jaja == 25:
            conn.commit()

#to use this u gotta open localhost:9000 in a web browser
def servicio():
    import socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0):
                print(pieces[0])
            data = 'HTTP/1.1 200 OK\r\n'
            data += ' Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body>Hello World</body></html>\r\n\r\n'
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        print('\nShutting down...\n');
    except Exception as exc:
        print('Error:\n');
        print(exc)
    serversocket.close()




