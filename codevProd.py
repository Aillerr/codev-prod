from flask import Flask
import mysql.connector
import json


api = Flask(__name__)

@api.route('/annualProd', methods=['GET'])
def getAnnualProd():
  cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='codev')
  cursor = cnx.cursor()

  query = ("SELECT * FROM prodannée")
  cursor.execute(query)

  r = cursor.fetchall()
  cursor.close()
  cnx.close()

  return json.dumps(r)


@api.route('/annualProd/<year>', methods=['GET'])
def getYearProd(year):
  cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='codev')
  cursor = cnx.cursor()

  query = ("SELECT * FROM prodannée WHERE année = " + year)
  cursor.execute(query)

  r = cursor.fetchall()
  cursor.close()
  cnx.close()

  return json.dumps(r)




if __name__ == '__main__':
    api.run() 