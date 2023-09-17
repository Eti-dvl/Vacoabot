# import the module
from twython import Twython
from twython import TwythonError, TwythonRateLimitError
import time
import json
import matplotlib.pyplot as plt

dossier=""

politiciens=[
    "n_arthaud",
    "PhilippePoutou",
    "PCF",
    "JLMelenchon",
    "EELV",
    "Anne_Hidalgo",
    "bayrou",
    "enmarchefr",
    "JeanCASTEX",
    "EPhilippe_LH",
    "lesRepublicains",
    "vpecresse",
    "dupontaignan",
    "MLP_officiel",
    "ZemmourEric",
    "jeanlassalle"
]

# set tweepy api
credentials = [{"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},

      {"api_key": "XXX",
      "api_secret_key": "XXX",
      "access_token": "XXX-XXX",
      "access_token_secret": "XXX"},
      ]
def create_api(idx):
    credential=credentials[idx]
    return Twython(credential["api_key"], credential["api_secret_key"], credential["access_token"], credential["access_token_secret"])


def fetch_friends(user_screen_name):
    p=0
    followers=[]
    friends_ids = []
    api_idx=0
    useful_keys=("id", "id_str", "name", "screen_name", "location", "followers_count", "friends_count", "lang", "verified", "profile_image_url_https")
    curseur=-1

    while curseur !=0:
        try :
            api_t=create_api(api_idx)
            print(f"\npage {p}")
            a = api_t.get_friends_list(screen_name=user_screen_name, count=200,cursor=curseur)
            for user in a['users']:
                friends_ids.append(user['id'])
            curseur=a["next_cursor"]
            if (curseur != 0):
                p+=1
        except TwythonRateLimitError as e:
            print(e.retry_after)
            api_idx = (api_idx + 1) % len(credentials)
            print(f"You reached the rate limit. Moving to next api: #{api_idx}")
            if api_idx==0:
                print("We will wait a bit longer this time")
                time.sleep(180)
            else: time.sleep(0.5)
        except TwythonError as e:
            print(e)
            print("curseur : {}".format(curseur))
            with open("commus/temp3.json",'w', encoding='utf-8') as write_file: json.dump(followers+friends, write_file, indent=4)
            time.sleep(900)
        

    print("Found {} friends.".format(len(friends_ids)))

    return friends_ids

def is_in_dicho(arr, x, n):
    lo = 0
    hi = n - 1
    mid = 0

    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return True
    return False


def plot(dico):
    colors=["#bb0000", "#bb0000", "#dd0000", "#cc2443", "#00c000", "#FF8080",
            "#ff9900", "#ffeb00", "#ffeb00", "#ffeb00", "#0066cc", "#0066cc",
            "#0082C4", "#0D378A", "#404040", "#26c4ec"]
    cands = [key for key,value in dico.items()]
    scores = [value for key,value in dico.items()]
    width = 0.35
    fig, ax = plt.subplots()
    ax.barh(cands, scores, width, color=colors)
    
    ax.invert_yaxis()
    ax.set_ylabel('Candidats')
    ax.set_title('pourcentages par candidats')
    ax.legend()
    
    plt.show()
    fig.savefig('plot.png')


def princ(cible):
    dict1={}
    ind=0
    users_ids=fetch_friends(cible)
    coef1=100/len(users_ids)
    for pol in politiciens:
        dict1[pol] = 0
        commu=[]
        with open(dossier+"commu_ids_"+pol+".json", "r", encoding="utf-8") as read_file:
            commu = json.load(read_file)
        le=len(commu)
        for user_id in users_ids:
            if is_in_dicho(commu, user_id, le):
                dict1[pol] += 1
                ind+=1
    dict2={key: round(coef1*elem,2) for key, elem in dict1.items()}
    print(dict1)
    plot(dict2)
    print(dict2)
    print(round(ind*coef1,0))
