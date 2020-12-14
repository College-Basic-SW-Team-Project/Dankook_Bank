import json
from tkinter import *

window = Tk()
window.title("단국뱅킹")
Label(window, fg="blue", text="ID 입력").grid(row=0)
Label(window, fg="blue", text="PASSWORD 입력").grid(row=1)


user_file_path = "./user.json"
product_file_path = "./product.json"

user_data = {}
user_data['user_name'] = []
user_data['user_name'].append({

})
