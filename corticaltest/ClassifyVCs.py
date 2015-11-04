import cortipy
import os
import mysql.connector as msc
import time
<<<<<<< HEAD
import sys
from textblob import TextBlob
=======
>>>>>>> af68d94688cf028245d405a30dbaa7ee6d9bdf62

# Init API client
apiKey = os.environ.get('CORTICAL_API_KEY')
client = cortipy.CorticalClient(apiKey)


MYSQL_GSJ_USER = 'root'
MYSQL_GSJ_PASSWORD = 'nycdsa1!'
MYSQL_GSJ_HOST = '173.194.225.231'
MYSQL_GSJ_DB = 'test'

config = {
   'user': 'root',
   'password': 'uLFZ2WoB',
   'host': '130.211.154.93',
   'database': 'test',
   'charset': 'utf8'
}
<<<<<<< HEAD
print "usage = python ClassifyVCs.py vctest4 (VC scraper) -or- python ClassifyVCs.py crunchbase_startups (startup capital scraper)"

#dbtable = "vctest4"
dbtable = sys.argv[1]
print "dbtable = " + dbtable

#Need to put this into an infinite loop
# while 1:
con = msc.connect(**config)
cur = con.cursor()
#con.autocommit(True)
time.sleep(1)

cur.execute("select siteurl, text from "+dbtable+" where cortical_io is null and text <> '' limit 100")
test = cur.fetchall()
#partnerfunds.com
for i in range(0, len(test)):
    siteurl = str(test[i][0])
    text = str(test[i][1])

    #Cortical.io
    termKeyWords = client.extractKeywords(text)
    termBitmap = client.getTextBitmap(text)['fingerprint']['positions']

    #TextBlob
    blob = TextBlob(text)
    blob.sentiment

    MySqlKeyWordDat = (','.join(termKeyWords), siteurl)
    MySqlBitMapDat = (str(termBitmap), siteurl)
    MySqlTextBlobDat = (str(blob.sentiment), siteurl)
    print "---For "+siteurl+" keywords = " + ",".join(termKeyWords) + " sentiment = " + blob.sentiment

    MySqlKeyWordDatQ = """UPDATE """+dbtable+""" SET cortical_io_keywords = %s WHERE siteurl = %s"""
    MySqlBitMapDatQ = """UPDATE """+dbtable+""" SET cortical_io = %s WHERE siteurl = %s"""
    MySqBlobDatQ = """UPDATE """+dbtable+""" SET opencalais = %s WHERE siteurl = %s"""
=======

#Need to put this into an infinite loop
while 1:
    con = msc.connect(**config)
    cur = con.cursor()
    #con.autocommit(True)
    time.sleep(1)

    cur.execute("select siteurl, text from vctest where cortical_io is null limit 1")
    test = cur.fetchall()

    siteurl = str(test[0][0])
    text = str(test[0][1])
    #programmingCategory = client.createClassification(categoryName, pos, neg)

    if(text == ''):
        continue

    termKeyWords = client.extractKeywords(text)
    termBitmap = client.getTextBitmap(text)['fingerprint']['positions']

    MySqlKeyWordDat = (','.join(termKeyWords), siteurl)
    MySqlBitMapDat = (str(termBitmap), siteurl)

    MySqlKeyWordDatQ = """UPDATE vctest SET cortical_io_keywords = %s WHERE siteurl = %s"""
    MySqlBitMapDatQ = """UPDATE vctest SET cortical_io = %s WHERE siteurl = %s"""
>>>>>>> af68d94688cf028245d405a30dbaa7ee6d9bdf62

    #upload keywords and bitmap to database
    cur.execute(MySqlKeyWordDatQ, MySqlKeyWordDat)
    cur.execute(MySqlBitMapDatQ, MySqlBitMapDat)
<<<<<<< HEAD
    cur.execute(MySqBlobDatQ, MySqlTextBlobDat)
    con.commit()

#programmingCategory = client.createClassification(categoryName, pos, neg)
#if(text == ''):
#    continue

con.close()
=======
    con.commit()

    con.close()
>>>>>>> af68d94688cf028245d405a30dbaa7ee6d9bdf62

#bitmapTerms = client.bitmapToTerms(termBitmap['fingerprint'])






######  sample code bleow.
# Evaluate how close a new term is to the category.
#termBitmap = client.getBitmap("Python")['fingerprint']['positions']
#distances = client.compare(termBitmap, programmingCategory['positions'])
#print distances['euclideanDistance']

# Try a block of text.
#textBitmap = client.getTextBitmap("The Zen of Python >>>import this")['fingerprint']['positions']
#distances = client.compare(textBitmap, programmingCategory['positions'])
#print distances['euclideanDistance']
