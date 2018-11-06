#!/usr/bin/env python
import time
import serial
import mysql.connector


cnx = mysql.connector.connect(user='t7hani00', password='NEwttgtub7h3FHYq',
                              host='mysli.oamk.fi',
                              database='opisk_t7hani00')



ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=10
    )
counter = 0
print(cnx)
dbcursor = cnx.cursor()

#dbcursor.execute("SHOW TABLES")
#for x in dbcursor:
 #   print(x)


while 1:
    x=ser.readline()
    print x
#    sql = "INSERT INTO sensori_data (lampotila, gyro) VALUES (%s, %s)"
    sql = "UPDATE sensori_data SET lampotila = %s WHERE data_id = %s"
#    val = (x, "900.0")
    val = (x, "1")
    dbcursor.execute(sql, val)
    cnx.commit()
    print(dbcursor.rowcount, "record inserted.")
    
