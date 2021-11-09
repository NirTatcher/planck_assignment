# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import requests
import json

#
x = requests.get('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
arcaffe_content = x.json()['Data']
for i in range(0,len(arcaffe_content['categoriesList'])):
    category=arcaffe_content['categoriesList'][i]['categoryName']
    dishes = arcaffe_content['categoriesList'][i]['dishList']
    output=[]

    for dish in dishes:
        output.append({'id': dish['dishId'],'name':dish['dishName'],'description':dish['dishDescription'],'price':dish['dishPrice'] })
    print(output)

# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}
#
# x = requests.post(url, data = myobj)
#
# print(x)
