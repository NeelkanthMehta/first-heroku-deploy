import os
import wget


data_dir = '/home/nm/PycharmProjects/pythonProject/data'
data_file = 'hiring.csv'

if not data_file in os.listdir(data_dir):
    wget.download(
        url='https://raw.githubusercontent.com/krishnaik06/Deployment-flask/master/hiring.csv',
        out=os.path.join(data_dir, data_file)
    )