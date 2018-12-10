#!/usr/bin/env python

import time
import serial
import mysql.connector

##Konnarelay ver 1.0
##by Saku Huuha

##While-silmukka ja try - except-rakenne lisaa luotettavuutta
ser = None
cnx = None
while True:
    try:
##        Luodaan yhteys tietokantaan, jos yhteytta ei ole
        if cnx == None:
            cnx = mysql.connector.connect(user='t7hani00', password='NEwttgtub7h3FHYq',
                                          host='mysli.oamk.fi',
                                          database='opisk_t7hani00')
            print(cnx)
            dbcursor = cnx.cursor()
##Luodaan sarjaporttiyhteys tiettyyn USB-porttiin(alhaalla vasemmalla Raspissa)
        if ser == None:
            ser = serial.Serial(
                port='/dev/ttyACM0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=10
                )
            

##Luetaan rivi sarjaportilta
        x=ser.readline()
        print x
##Jaetaan lampotila, kulma x ja kulma y listaan
        konnanarvot = x.split(", ")
        if len(konnanarvot)==3:
##Tietokantaoperaatiot
            sql = "UPDATE sensori_data SET lampotila = %s, kulma_x = %s, kulma_y = %s, nalka = nalka + 1 WHERE data_id = %s"
            val = (konnanarvot[0], konnanarvot[1], konnanarvot[2], "1")
            dbcursor.execute(sql, val)
            cnx.commit()
#            print(dbcursor.rowcount, "record inserted.")
    except:
        if not(ser == None):
            ser.close()
            ser = None
            print("Serial Closed")
        if not(cnx == None):
            cnx.close()
            cnx = None
            print("DB Connection Closed")

        

            
