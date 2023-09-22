import requests as req
from bs4 import BeautifulSoup


def get_req(myurl, somthing_to_search):
    if somthing_to_search:
        RESPONSE = req.get(url=myurl, params=somthing_to_search)
    else:
        RESPONSE = req.get(url=myurl)
        
    data = BeautifulSoup(RESPONSE.content, 'html.parser')
    return data
    # return API.json()
    
def post_req(myurl, myjson):
    RESPONSE = req.post(myurl, json = myjson)
    data = BeautifulSoup(RESPONSE.content, 'html.parser')
    
    print(data)
    print(RESPONSE.status_code)

def delete_req(myurl, somthing_to_delete):
    RESPONSE = req.delete(url=myurl, params=somthing_to_delete)
    data = BeautifulSoup(RESPONSE.content, 'html.parser')
    
    print(data)
    print(RESPONSE.status_code)


""" Main Menu """
def menu():    
    URL1 = 'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies'
    URL2 = 'https://my-json-server.typicode.com/typicode/demo/posts'
    data_for_add = {
            'Title': 'just do it',
            'Year': '2023',
            'Runtime': 'while 1==True',
            'Poster': 'wait for it...'
        }

    data_for_delete = {
        "id": 1,
        "title": "Post 1"
        } 

    cmd = input('what do you want to do with this API?[read,add,remove]>>> ')
    title = None # search and show all result
    # title = 'The Lion King' # search just this title
    search_somthing = {'Title': title}

    if cmd.lower() == 'read':
        print(get_req(URL1, search_somthing))
    elif cmd.lower() == 'add':
        post_req(URL2, data_for_add)
    elif cmd.lower() == 'remove':
        delete_req(URL2, data_for_delete)
    else:
        print('this command is not exist!!!')
    menu()
menu()
