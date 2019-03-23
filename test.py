import requests
import base64
from PIL import Image
import numpy as np

#Setup the path to local ip (port = 1234)
path = 'localhost:8888/ecobin'

#Get method (returns a dictionary)
def get_data():
    response = requests.get(path)
    ecobin_dict = response.json()
    return ecobin_dict

#Post/updating the dictionary in the server
def post_data(x):
    #Adjust path
    path = 'localhost:8888/ecobin/'+ x
    #Process picture
    image = Image.open('trash.jpg')
    np_im = np.array(image)
    im = str(np_im).encode()
    new_pic = str(base64.b64encode(im))
    #Specify what to update
    update_key = x
    update_value = new_pic #dummy variable = 'trash'
    response = requests.post(path, json={update_key:update_value})
    ecobin_dict = response.json()
    return ecobin_dict


#Delete method
'''
def delete_data():
    response = requests.delete(path)
'''


#Test Case Get Data
print("GETTING DATA FROM API SERVER")
response = get_data()
class_type = response['class']
object_name = response['object']
pic_data = response['pic']
percentage_data = response['percentage']
print(response)
print(class_type)
print("")

#Test Case Get Data
print("UPDATING DATA FROM API SERVER")
x = 'pic'
response = post_data(x)
class_type = response['class']
object_name = response['object']
pic_data = response['pic']
percentage_data = response['percentage']
print(response)
print(class_type)
print("")
