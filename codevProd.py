from msilib.schema import Environment
from flask import Flask
import mysql.connector
import json
import os


api = Flask(__name__)

@api.route('/annualProd', methods=['GET'])
def getAnnualProd():
  cnx = mysql.connector.connect(user=os.getenv('DB_USER'), password=os.getenv('DB_PWD'), host=os.getenv('DB_HOST'), database='codev')
  cursor = cnx.cursor()

  query = ("SELECT * FROM prodannée")
  cursor.execute(query)

  r = cursor.fetchall()
  items = [dict(zip([key[0] for key in cursor.description], row)) for row in r]

  cursor.close()
  cnx.close()
  return json.dumps(items)


@api.route('/annualProd/<year>', methods=['GET'])
def getYearProd(year):
  cnx = mysql.connector.connect(user=os.getenv('DB_USER'), password=os.getenv('DB_PWD'), host=os.getenv('DB_HOST'), database='codev')
  cursor = cnx.cursor()

  query = ("SELECT * FROM prodannée WHERE année = " + year)
  cursor.execute(query)

  r = cursor.fetchall()

  items = [dict(zip([key[0] for key in cursor.description], row)) for row in r]

  cursor.close()
  cnx.close()
  return json.dumps(items)




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    api.run(port=port) 