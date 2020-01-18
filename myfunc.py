#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[15]:


#파일을 읽고 필요한 정보 데이터만 가져오기
def read_file(file):
    data = pd.read_excel(file)
    text = data["text"]
    label = data['label']
    new_data = pd.DataFrame({"Text" : text,"Label" : label})
    return new_data


# In[16]:


if __name__ == "__main__":
    data = read_file("data_sample.xlsx")
    print(data.head())


# In[4]:


def split_all_sentence(text_data):
    result = []
    count = 0
    for idx,text in enumerate(list(text_data)):
        #print(idx,text)
        temp = text.split(sep = " ")
        result.append(temp)
    return result


# In[5]:


if __name__ == "__main__":
    print(split_all_sentence(data["Text"][:5]))
    #type(a)


# In[12]:


#data에 있는 text 데이터에 대해 url을 다 없애주는 함수
def remove_url(text_data):
    result = []
    for line in text_data:
        new_line = []
        for text in line:
            if ("http" not in text) and ("pic" not in text):
                new_line.append(text)
        result.append(new_line)
    return result


# In[15]:


if __name__ == "__main__":
    a = remove_url(split_all_sentence(data["Text"][:10]))
    print(a[:10])


# In[38]:


#특수문자를 모두 제거하는 함수
def change(otl):
    result = []
    for line in otl:
        result_text = ""
        for word in line:
            if word.isalpha() :
                #new_word = remove_dan(word)
                result_text += word
            else:
                for t in word: #remove_dan(word) 
                    if t.isalpha():
                        result_text += t
                    else:
                        result_text += " "
            result_text += " "
        result.append(result_text)
    return result


# In[39]:


if __name__ == "__main__":
    print(change([['#얼음활용법\n#얼음', '#아이스\n#생활꿀팁\n#경기도경제과학진흥원', '#GBSA\n\n집에', '보관해둔', '얼음을', '생활', '곳곳에서', '알뜰하게', '활용하는', '방법을']]))


# In[51]:


"#경기도".isalpha()


# In[78]:


" ".isalpha()


# In[36]:


#이모티콘/ 오타 제거
#"빵" 같은 하나의 문자같은 경우는 처리 XXX /단, 해쉬태그가 붙어 있는 경우엔 예외
#ㅇㅏㅇㅣㅅㅡ 같은 경우엔 다 없애버림 ( 방법 생각중) --> 작업중 #input : string / output : "string"
def remove_dan(word):
    result = ""
    han = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅍㅎㄲㄸㅃㅆㅉㅏㅑㅓㅕㅜㅠㅗㅛㅐㅒㅔㅖㅡㅣㆍ"
    if len(word) < 2:
        pass
    else:
        for text in word:
            if text not in han:
                result+=text
            else:
                result+= " "
    return result


# In[77]:


if __name__ == "__main__":
    print(remove_dan("먹어보세요ㅠ유유ㅠㅠㅠ"))
    print(remove_dan("ㄷㅗㅅㅓ관"))


# In[85]:


#중간에 들어있는 여러 공백을 다 없애주는 함수
def re_sent(text):
    text_list = text.split(" ")
    new_sent = []
    for i in text_list:
        if i.isalpha() :
            new_sent.append(i)
    return new_sent


# In[32]:


#길이가 10 이상인 경우, 형태소 분석기로 나눠주는 함수
import MeCab
# custom_list = ["NNP","NNG","VV","VA","XR", "UNKNOWN"]
def kimchi(text, custom_list =  ["NNP","NNG","VV","VA","XR", "UNKNOWN"]):
    tagger = MeCab.Tagger()
    real = tagger.parse(text)
    separate_text = real.split()
    real_text = separate_text[:-1]
    words = []
    types = []
    #print(real_text)
    for i in range(len(real_text)):
        if i%2 == 0 :
            words.append(real_text[i])
        else:
            #istype = real_text[i].split(sep = ",")[0]
            types.append(real_text[i].split(sep = ",")[0])
            #if istype in custom_list :
                #types.append(real_text[i].split(sep = ",")[0])
    ans = list(zip(words,types))
    return ans


# In[33]:


if __name__ == "__main__":
    print(kimchi(["NNP","NNG","VV","VA","XR"],"아버지가방에들어가신다."))


# In[90]:


if __name__ == "__main__":
    print(a)
    print("-"*100)
    a1 = change(a)
    print(a1)
    print("-"*100)
    s = []
    for test1 in a1:
        s1= []
        for test2 in test1.split():
            if test2 != " ":
                s1.append(test2)
        s.append(" ".join(s1))
    print(s)


# In[2]:


import hgtk


# In[20]:


if __name__ == "__main__":
    a = hgtk.text.decompose("ㅇㅏㅇㅣㅅㅡ")
    print(a.replace("ᴥ",""))
    print(a)


# In[42]:


def decompose_text(text_list):
    new_list = []
    for text in text_list:
        decomposed = hgtk.text.decompose(text)
        new_list.append(decomposed.replace("ᴥ",""))
    return new_list


# In[27]:


def remove_alpha(text_list):
    new_list = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for text in text_list:
        one = ""
        for m in text.lower():
            if m not in alpha :
                one += m
        new_list.append(one)
    return new_list


# In[43]:


if __name__ == "__main__":
    test = ['사람들이 모르는데 진짜 유명해졌으면 하는 일본 편의점 음식 일본 미니스톱 아이스 果実いちご氷 세상사람들 이것 먹어보세요 유유 위에는 달달한 바닐라 아이스고 밑에는 얼린 딸기에 연유가 뿌려져', '아이스의오락시간 아이스 오락시간 과연 누가 아이스의 유연성 왕일지', '오 오랫만에 아이스 돌체라떼 맛있겠다 Starbucks in 부산광역시 Busan', '맛집탐험대 나를 놀라게한 커피 TERAROSA TERAROSA 테라로사 날씨 냉커피 덥다 맛 맛집 사장님 서정점 아메리카노 아이스 아이스커피 양평 좋다 카페 커피 커피향 커피향기 향기 홍보', '로렉스 아이스 다이아 고씨쥬얼리 명품시계 금 화이트 골드 화이트골드', '새벽까지 비가 오더니 아침이 되니 또다시 무더위 아침부터 아아로 마셔요 늦더위 아이스 커피향 태안펜션그람피하우스', '얼음활용법 얼음 아이스 생활꿀팁 경기도경제과학진흥원 GBSA 집에 보관해둔 얼음을 생활 곳곳에서 알뜰하게 활용하는 방법을', '광주 낮보단 더운 하늘마당 어디간거니 이 밤분위기 비타 아이스 들이마시고 있음 광주광역시 문화전당 문화전당하늘공원 여행스타그램 광주여행 그래도 덥다그램 gwangju tripstagram hanulmadang 하늘 마당', '월 주차 신상 입고되었습니다 카메라 안경 빵 튜브잔 토끼 아이스 햄스터 물개 병아리 모찌 포켓몬스터 디즈니프린세스 짱구 스밋코구라시 케이프 맥주잔 게임기 도검난무 건담 가챠폰 피규어 미니어쳐 홍대 상수역 로렌스길', '집에서도 만들 있는 나만의 아이스크림 제조법']
    a = decompose_text(test)
    print(a)
    #print("가나다ABc 으음...EHshldk".lower())
    b = remove_alpha(a)
    print(b)

