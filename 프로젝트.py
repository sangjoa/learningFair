import requests
from bs4 import BeautifulSoup
import os

# bs4에서 얻은 값에서 html 값 뽑아오는 방법
# soup.select(selector 표현)
# 텍스트 뽑아오기 : .text
# 속성값을 뽑아오기 : .get(속성명)
# class 하위에 있는 값은 >로 표현

res = requests.get("https://movie.naver.com/movie/running/current.naver")
soup = BeautifulSoup(res.text,"html.parser")


def GetData() : # 필요한 값들 가져오는 함수
    Data = []
    for i in soup.select(".lst_dsc")[:10] :

        # 영화이름, 평점, 평점 참여자수, 예매율, 관련등급
        movieName  = i.select('.tit > a')[0].text
        grades = i.select('.num')[0].text
        participantions = i.select('.num2 > em')[0].text
        ticket_sales = i.select('.num')[1].text
        view_grade = i.select('.tit > span')[0].text

        # 줄거리
        a = i.select('.tit > a')[0].get("href")
        storyline = GetStory(a)
        storyline = delete2(storyline)

        # 상영시간, 개봉날짜, 장르, 감독 
        director = delete(i.select('.info_txt1 > dd')[1].text)
        genre = delete(i.select('.info_txt1 > dd')[0].text).split('|')[0]
        movie_time = delete(i.select('.info_txt1 > dd')[0].text).split('|')[1]
        release_date = delete(i.select('.info_txt1 > dd')[0].text).split('|')[2]
        Data.append([movieName, grades, participantions, ticket_sales, view_grade, director, genre, movie_time, release_date,storyline])
    return Data

def GetStory(storyurl) : # 줄거리 가져오는 함수
     # 실제 html에 적혀있는 url과 실제 url이 달라서 필요한 끝자리 번호만 가져와서 사용
    s = "https://movie.naver.com" + storyurl
    res2 = requests.get(s)
    soup2 = BeautifulSoup(res2.text,"html.parser")
    story = soup2.select(".story_area > .con_tx")[0].text
    lis = []
    lis.append(story)
    return lis

def delete(A) :  # 각 값의 쓸데 없는 부분 제거함수
    for i in '\t\n\r' :
        A = A.replace(i,"")
    return A

def delete2(storyline) : # storyline에 들어가는 쓸모없는 값 제거함수
    for i in "\r\xa0" :
        storyline[0] = storyline[0].replace(i,"")
    return storyline


def Output(lis,num) : # 출력함수
    print(f"영화제목 : {lis[num][0]}")
    print(f"평점 : {lis[num][1]} ")
    print(f"참여자수 : {lis[num][2]} ")
    print(f"예매율 : {lis[num][3]} ")
    print(f"관련등급 : {lis[num][4]} ")
    print(f"감독 : {lis[num][5]} ")
    print(f"장르 : {lis[num][6]} ")
    print(f"상영시간 : {lis[num][7]} ")
    print(f"개봉날짜 : {lis[num][8]} \n")
    print(f"줄거리 : {lis[num][9][0]}")
    print()
     
lis = GetData()

while True : 
    print("="*40)
    print("☆ 현재 상영중인 영화 TOP 10 ☆")
    print("="*40)

    for i in range(10) :
        print(f"{i+1}. {lis[i][0]}")
    print("q(Q). 종료")
    print()
    
    user = input("영화 선택 > ")

    if user.isnumeric() :
        user = int(user)
        if 1 <= user < 11 :
            pass
        else :
            print("1-10까지만 입력해주세요")
    
    if user == 'Q' :
        user = chr(ord(user) + 32)

    # 선택
    if user == 1 :
        Output(lis,user-1)
    elif user == 2 :
        Output(lis,user-1)
    elif user == 3 :
        Output(lis,user-1)
    elif user == 4 :
        Output(lis,user-1)
    elif user == 5 :
        Output(lis,user-1)
    elif user == 6 :
        Output(lis,user-1)
    elif user == 7 :
        Output(lis,user-1)
    elif user == 8 :
        Output(lis,user-1)
    elif user == 9 :
        Output(lis,user-1)
    elif user == 10 :
        Output(lis,user-1)
    elif user == 'q' :
        break
    else :
        print("숫자를 입력해주세요 !!")

    input()
    os.system("cls")