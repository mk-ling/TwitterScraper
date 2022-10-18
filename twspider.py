import re
import os
import requests


def find_all_links(path):
    links_set = set()
    pattern = r'https://pbs.twimg.com/media/.*jpg'
    with open(path, 'r') as f:
        file = f.read()
    links = re.findall(pattern, file)
    append_string = '=jpg&name=large'

    for link in links:
        pic_url = str(link)
        pic_url = pic_url[0: len(pic_url) - 4]
        if len(pic_url) < 100:
            pic_url = pic_url + append_string
            links_set.add(pic_url)
    return links_set

def get_pic(pic_url, proxy):
    max_tries = 5
    if max_tries <= 0 :
        print(" ++++ TIME OUT for 5 times +++++    ")
        print("Max attempts exceeded. Proxy Time Out. Program terminated.")
        exit()
    response = ''
    try:
        response = requests.get(pic_url, proxies=proxy)
    except(requests.exceptions.ProxyError, requests.exceptions.ConnectionError):
        max_tries = max_tries - 1
        get_pic(pic_url, max_tries)
    return response


twitter_id = input("Input twitter id（Format：@ID）")
py_path = os.path.dirname(__file__)
har_path = os.path.join(py_path, 'HAR', twitter_id + '.txt')
save_path = os.path.join(py_path,'Archive', twitter_id)
counter = 1

try:
    os.mkdir(path=save_path)
except FileExistsError as e:
    print('Directory already exists, please use a different directory name')
    exit()

proxy_path = os.path.join(py_path, 'proxy.txt')
proxy_text = open(proxy_path, 'r').read().strip().split(',')
proxy = dict()
proxy['http'] = proxy_text[0]
proxy['socks5'] = proxy_text[1]
print('Save Path ： ' + save_path)
links = find_all_links(har_path)


for link in links:
    pic_name = twitter_id + str(counter) + '.jpg'
    file_name = os.path.join(save_path, pic_name)
    pic_url = str(link)
    print(pic_url)
    response = get_pic(pic_url, proxy=proxy)
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(str(counter) + ' image downloaded')
    counter += 1

print('\n ------ Download Finished ------')
