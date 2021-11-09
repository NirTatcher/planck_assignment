import time

from flask import Flask,request;
from time import *
import threading
import requests
import json
import schedule
import datetime
# def myInterval():
#     x = requests.get(
#         'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
#
#     print("getting info again...")
#     return x

# def countdown():
#
#     #86400 daily seconds
#     global my_timer
#     my_timer = 10
#     for x in range(10):
#         my_timer=my_timer-1
#         print("1 sec passed")
#         sleep(1)
#     print("Getting info...")


def getDish(dishId):
    res=""
    print(dishId)
    for i in range(0, len(arcaffe_content['categoriesList'])):
            category = arcaffe_content['categoriesList'][i]['categoryName']
            dishes = arcaffe_content['categoriesList'][i]['dishList']
            for dish in dishes:
                if(str(dish['dishId']) == str(dishId) or str(dish['dishName']).upper() == str(dishId).upper()):
                    res = {'id': dish['dishId'], 'name': dish['dishName'], 'description': dish['dishDescription'],
                           'price': dish['dishPrice']}
    return res
                                # all_category.append(
                #     {'id': dish['dishId'], 'name': dish['dishName'], 'description': dish['dishDescription'],
                #      'price': dish['dishPrice']})

def setSchedule():
    schedule.every(86400).seconds.do(myInterval)
    while True:
        schedule.run_pending()
        sleep(1)
def getCategoty(c_name):
    all_category=[]
    for i in range(0, len(arcaffe_content['categoriesList'])):
        category = arcaffe_content['categoriesList'][i]['categoryName']
        dishes = arcaffe_content['categoriesList'][i]['dishList']
        if(category == c_name):
            for dish in dishes:
                all_category.append({'id': dish['dishId'], 'name': dish['dishName'], 'description': dish['dishDescription'],
                           'price': dish['dishPrice']})
    return all_category

def checkDate():
    if(date != datetime.datetime.now()):
        x = requests.get(
            'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
        global arcaffe_content
        arcaffe_content = x.json()['Data']
global x
x = requests.get(
    'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
global arcaffe_content
arcaffe_content= x.json()['Data']

global date
date = datetime.datetime.now()


app = Flask(__name__)

@app.route("/")
def index():
    return "hello and thank you for the challenge :)!"
@app.route("/drinks")
def getDrinks():
    checkDate()
    all_drinks=getCategoty('Drinks')
    return json.dumps(all_drinks)

@app.route('/drinks/<id>')
def getDrink(id):
    checkDate()
    return json.dumps(getDish(id))

@app.route('/pizzas/')
def getPizzas():
    checkDate()
    all_pizzas = getCategoty('Pizzas')
    return json.dumps(all_pizzas)

@app.route('/pizzas/<id>')
def getPizza(id):
    checkDate()
    return json.dumps(getDish(id))

@app.route('/desserts/')
def getDesserts():
    checkDate()
    all_desserts = getCategoty('Desserts')
    return json.dumps(all_desserts)

@app.route('/desserts/<id>')
def getDessert(id):
    checkDate()
    return json.dumps(getDish(id))

##POST!!!

@app.route('/order/',methods=['POST'])
def postOrder():
    checkDate()
    sumPrice=0
    keys=[]
    values=[]
    for i in request.json:
       keys.append(i)
       value = json.loads(json.dumps(request.json))[i]
       for val in value:
           sumPrice+=getDish(val)['price']
    return {"price":sumPrice}


