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
#    ser.flushInput()
    print x
#    x = "25.2 120.2 66.6 17.9"
    konnanarvot = x.split(", ")
    
    print x
#    sql = "INSERT INTO sensori_data (lampotila, gyro) VALUES (%s, %s)"
    sql = "UPDATE sensori_data SET lampotila = %s, kulma_x = %s, kulma_y = %s WHERE data_id = %s"
#    val = (x, "900.0")
    val = (konnanarvot[0], konnanarvot[1], konnanarvot[2], "1")
    dbcursor.execute(sql, val)
    cnx.commit()
    print(dbcursor.rowcount, "record inserted.")
#    time.sleep(0.2)
    
