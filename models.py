def ReadModelJson():
    import json
    with open("data.json", "rb") as fileObj:
        Database = json.load(fileObj)
    return Database


def WriteModelJson(data):
    import json
    Database = ReadModelJson()
    with open("data.json", "w") as fileObj:
        Database.extend([data])
        json.dump(Database, fileObj, ensure_ascii=False, indent=4, sort_keys=True)

def PatchModelJson(data):
    import json
    Database = ReadModelJson()
    flag = False

    for i in Database:
        if i["Id"] == data["Id"]:
            Database.insert(Database.index(i),data)
            Database.pop(Database.index(data)+1)
            flag = True
        else:
            flag = False
        
    if flag:
        with open("data.json", "w") as fileObj:
            json.dump(Database, fileObj, ensure_ascii = False, indent = 4, sort_keys = True)
        return "The data was PATCHed and was a part of the Database"

    else: 
        return "The data wasn't PATCHed because wasn't a part of the Database"

def DeleteJsonModel(data):
    import json
    Database = ReadModelJson()
    flag = False
    
    for i in Database:
        if "Id" in (i.keys() and data.keys()) and (data["Id"] == i["Id"]):
            Database.remove(data)
            flag = True
    if flag:
        with open("data.json", "w") as fileObj:
            json.dump(Database, fileObj, ensure_ascii = False, indent = 4, sort_keys = True)
        return "The data was deleted."
    else:
        return "No such data was found."

def PutModelJson(data):
    import json
    flag = False
    Database = ReadModelJson()
    for i in Database:
            if i['Id'] == data['Id']:
                Database.insert(Database.index(i),data)
                Database.pop(Database.index(data)+1)
                flag = True

    if flag:
        with open("data.json", "w") as fileObj:
            json.dump(Database, fileObj, ensure_ascii = False, indent = 4, sort_keys = True)

        return "The data was PUT through and was a part of the Database"

    else: 
        Database.append(data)
        with open("data.json", "w") as fileObj:
            json.dump(Database, fileObj, ensure_ascii = False, indent = 4, sort_keys = True)
        return "The data was PUT through and wasn't a part of the Database"
        