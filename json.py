import json
'''
READ THE DATABASE README before operating
'''
File = r'''YOUR FILE'''
with open(File,'a') as fileObj:
    data = json.load()
    '''
    YOUR DATA LOGIC GOES IN HERE
    Once the data is changed, to write it to your JSON file use the following command.
    '''
    json.dump(object,File)