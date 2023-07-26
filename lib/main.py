from GetRequester import GetRequester

def main(): 
    get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
    print(get_requester.load_json())
main()