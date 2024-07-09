import json

# configuration
def getTOKEN() :
    with open('config.json', 'r') as f:
        json_data = json.load(f)

    return json_data['token']

# menu list
def getMenuList() :
    with open('menu_list.json', 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
    return json_data['list']

def getChannelID() :
    with open('config.json', 'r') as f:
        json_data = json.load(f)
    return json_data['channel_id']


if __name__ == '__main__':

    TOKEN = getTOKEN()
    menu_list = getMenuList()

    print(menu_list)