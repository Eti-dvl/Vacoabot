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
credentials = [{"api_key": "H2Kb9lqJO9hs4Vjuy4gW4vzBc",
      "api_secret_key": "udbvouAs06VcnaecOBeHohVPXoXIOl6WE8mgc9BgA0IJtyqFPT",
      "access_token": "1114921866559410176-wpu5Vn7ylv0vUFW87KerYXSJp7ng6P",
      "access_token_secret": "1lA3UMQ3u0i7d7W6riAUfZlDMKh740FQjFuMiHijTQIGF"},

      {"api_key": "9mWZwOUFHyvkv7LlJB9FqIlo2",
      "api_secret_key": "6FXhs6IXl615UW5iPPY5xaHdtHERKlr05qPeDdPwduAz89zJr6",
      "access_token": "1114921866559410176-lYDInajnRb0qpNtaPEFjWR7Ba3nnLY",
      "access_token_secret": "Dh22jBCTa5OmRf9WD2qxo5Emx8yf1kvpru4HDam8QFfO4"},

      {"api_key": "F5265WboXvHH4rjQsZjRLgQvG",
      "api_secret_key": "wyGbGdxE6m8eTmAZoGuQs0ZahxfY2M06bUojOyLqgTYpoNtQFN",
      "access_token": "1114921866559410176-E2o8t6OwOa7Fv6IZYsBZebTDj91ysr",
      "access_token_secret": "S6b1mNUw9l53SUTwEmnEmrBBiWsLb3uF7UJWSuOFZFBeO"},

      {"api_key": "NjFB01rpT0UUarjCljDSRXUTp",
      "api_secret_key": "5Ox2I1r2sSiGPrJNa7cu3s8Sbk9LR5BHJAKP0YDuGDYKLUV0n7",
      "access_token": "1114921866559410176-X5zyAP3AgJ8UI10aZnHUHIPoBHEQ5Y",
      "access_token_secret": "78jiBKZnfH6KfcWnjs31BVCHtlRNvulJj1mrCNnn72dv8"},

      {"api_key": "6ejPpqpxzucPhtk0xmYGlWIbE",
      "api_secret_key": "6r11psBbG25jrdQMpbCa5M3BJmBQIbyHiihwgVOxl5stOGkgl6",
      "access_token": "1114921866559410176-3fQgxNvTfAgLwMge1MAqo8cluVEDqS",
      "access_token_secret": "a95WfZIhWfOqRrcNraid29IZW9HH220z3R5DWknKPufY1"},

      {"api_key": "AdGZqFOyG23UpHxyXDCV7VU1w",
      "api_secret_key": "kKkVO139pKBxDJZavRD9KQWt2IlaShS1PCHw0xCtc3wf0UL87b",
      "access_token": "1114921866559410176-8zGm5QsmE6QcqHH569pl1hRQon4cIO",
      "access_token_secret": "wk1HO41oJWzsNFlRyuciLf8WEZUR7LS8OdfZvjqdgBfRN"},

      {"api_key": "8AUZZRP0QuA8IHOXyHLZNfJbM",
      "api_secret_key": "Pvy0ZrOMzpVs95uIZu8cLj3MOXa6crI3K8b2b0RCXFJ3XgtU2S",
      "access_token": "1114921866559410176-fmhEkrcXGeiuHC4DiIrV8ylAUqkZnE",
      "access_token_secret": "2kFhjsRwPcNOZcrwdm9s9ImcatH8Qv2CrMOIcO5R3xypK"},

      {"api_key": "7TgXeaRd7Ozq11qpcPHSdfLxX",
      "api_secret_key": "r9Dcb8wJr7SwVUF03HObBUxohtjB3Oqdi9u4pqSrttCV0OxzZm",
      "access_token": "1114921866559410176-HjU360sSqaV5zGdlwYnBPrRWYhsR8h",
      "access_token_secret": "CiGbKvgCwjg8e8BcePMjnhAAqNQ4RJQIkr1aHKK8YJIqi"},

      {"api_key": "9aI5ifh4kEsumKDCuLuCQgqxu",
      "api_secret_key": "iFBHqTbUOixyHqPs73cT2roL8YTUxZ1uTfwebkGBDmMSvJNOpY",
      "access_token": "1114921866559410176-3Bii8ap2xg74emfJaGBjZVfAoc0l3I",
      "access_token_secret": "Z2MUA9RxoyitRVITG1OKXRoqX7FIyvPiLciOgAQIvyINX"},

      {"api_key": "PfYuhZtxCortmFDEHIJ7IKzRl",
      "api_secret_key": "hlNIvKHqUnqmVyt3FO261pUD8GvRvSY3YcVZBKOxEPyTkv6GUp",
      "access_token": "1114921866559410176-S7XLsAKrzx11ReygwXDPYFdvNzimUu",
      "access_token_secret": "qMScULlnGV8L7v294TXFBVcKN1qKQfwKukXNQaE1RX064"},
      ]
def create_api(idx):
    credential=credentials[idx]
    return Twython(credential["api_key"], credential["api_secret_key"], credential["access_token"], credential["access_token_secret"])


def fetch_friends(user_screen_name):
    p=0
    friends_ids = []
    api_idx=0
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
    fig, ax = plt.subplots(tight_layout=True)
    fig.layout='constrained'
    ax.barh(cands, scores, width, color=colors)
    
    ax.invert_yaxis()
    ax.set_title('pourcentages par compte politique')
    
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
