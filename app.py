import time

from flask import Flask,request;
import requests
import json
import datetime

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
    global date
    print(str(date) +" = " + str(datetime.datetime.now().date()))
    dateNow = datetime.datetime.now().date()
    if(date != dateNow):
        x = requests.get(
            'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
        global arcaffe_content
        arcaffe_content = x.json()['Data']
        date = dateNow

global x
x = requests.get(
    'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
global arcaffe_content
arcaffe_content= x.json()['Data']

global date
date = datetime.datetime.now().date()


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


