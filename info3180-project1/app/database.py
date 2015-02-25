import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(dbname='infodatabase' user='hevongordon')   
    
    cur = con.cursor()
  
    cur.execute("CREATE TABLE profile (Id INTEGER PRIMARY KEY, Name VARCHAR(20), FirstName INT)")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()