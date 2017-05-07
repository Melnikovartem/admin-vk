from urllib.request import urlopen
from json import loads

def get_online(_id):
    url_1 = "https://api.vk.com/method/groups.getMembers?group_id=" + _id
    data1 = loads(urlopen(url_1).read().decode('utf8'))
    offset = 0
    ans = []
    users = int(data1["response"]["count"])
    while users > offset:
        url_ = "https://api.vk.com/method/groups.getMembers?fields=online&offset=" + str(offset) + "&group_id=" + _id
        data = loads(urlopen(url_).read().decode('utf8'))
        for i in data["response"]["users"]:
            if i["online"] == 1:
                ans.append(i)
        offset += 1000
    return ans
def get_posts(_id):
    url_ = "https://api.vk.com/method/wall.get?filter=owner&owner_id=-" + _id# + "&access_token=" config.access_token
    data = loads(urlopen(url_).read().decode('utf8'))
    return data["response"][0]

if __name__ == "__main__":
    _id = "146496931"
    print(get_online(_id))
