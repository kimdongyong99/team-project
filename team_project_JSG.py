import hashlib #비밀번호 해싱을 위해서
from pprint import pprint #출력결과 눈에 잘 들어오게

members = []  # 회원정보 보관 리스트
posts = []  # post 보관 리스트
salt = "team14" #해싱을 위한 솔트
class Member:
    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = password



    def display(self):
        print(f'이름 : {self.name}')
        print(f'유저네임 : {self.user_name}')
        # 비밀번호는 보안상의 이유로 안보이게

    def format_register(self):
        for_hashed_pw = str(self.password) + salt
        hashed_pw = hashlib.sha256(for_hashed_pw.encode()).hexdigest()
        #비밀번호 해싱
        return {'이름': self.name, '유저네임': self.user_name, '비밀번호': hashed_pw}
        #해싱된 비밀번호로 저장
        # members 리스트에 추가하기 위해 포맷 만들기

    def register(self):
        members.append(self.format_register())
        # for_register에 작성된 포맷으로 members리스트에 추가하기

# m1 = Member('이상혁', 'faker', 1234)
# m2 = Member('류민석', 'keria', 5678)
# m3 = Member('최우제', 'zeus', 91011)
#         #정보저장을 위한 필요 데이터 입력
# m1.display()
# m1.register()
# m2.register()
# m3.register()
# pprint(members)
# # title, content, author
class Post:
    def __init__(self, title, content, user_name):
        self.title = title
        self.content = content
        self.author = user_name
        # Post의 author를 user_name으로

    def post_display(self):
        print(f'제목 : {self.title}')
        print(f'내용 : {self.content}')

    def p_format_register(self):
        return {'제목': self.title, '내용': self.content, '글쓴이': self.author}
        # posts 리스트에 추가하기 위해 포맷 만들기

    def p_register(self): #p_format_register함수를 통해 만들어진 포맷으로 리스트에 append 하기
        posts.append(self.p_format_register())

# m1_1 = Post('전적','1337전 907승 430패, 승률 67.8%, 총 킬 4725, 총 데스 2845, 총 어시스트 7314, KDA 4.3, 킬 관여율 64.9%','faker')
# m1_2 = Post('성격유형1','MBTI : ENFP','faker')
# m1_3 = Post('솔랭 닉네임','hide on bush. 일명 하온부','faker')
# m2_1 = Post('별명','역천괴 - 역대급 천재 괴물, 울한울 -울어..한없이 울어..','keria' )
# m2_2 = Post('성격유형2','MBTI : ISFP','keria' )
# m2_3 = Post('업적','2022년 1월 1일, 페이커와의 인스타그램 맞팔로우에 성공','keria' )
# m3_1 = Post('오트와 우트','패트와 매트에서 따온, 오너와 함께 불리는 듀오 별명','zeus')
# m3_2 = Post('성격유형3','MBTI : INFP','zeus')
# m3_3 = Post('생년월일','2004년 1월 31일','zeus')
#         # Post 작성
# m1_1.post_display()
# m1_1.p_register()
# m1_2.p_register()
# m1_3.p_register()
# m2_1.p_register()
# m2_2.p_register()
# m2_3.p_register()
# m3_1.p_register()
# m3_2.p_register()
# m3_3.p_register()
# pprint(posts)

# # 특정 유저가 작성한 게시글 제목 프린트
# for p in posts:
#     if p['글쓴이']=='faker':
#         print(p['제목'])
    
    #특정 단어가 content에 포함된 게시글의 제목 프린트
# title_from_word_list=[]
# def find_title(word_needed):
#     for t in posts:
#         if word_needed in t['내용']:
#             title_from_word_list.append(t['제목'])
#     print(title_from_word_list)
# find_title('MBTI')

user_name_list=[]
def use_input():
    while True:
        a = int(input("숫자를 입력하세요(회원등록: 1, 게시글 작성: 2, 회원리스트: 3, 게시글리스트: 4, 종료: 5): "))
        if (a != 1) and (a != 2) and (a != 3) and (a != 4) and (a != 5):
            print("숫자를 다시 입력하세요. (회원등록: 1, 게시글: 2, 회원리스트: 3, 게시글리스트: 4, 종료: 5):")
            continue
        if a == 1:
            mem_name = input("이름을 입력하세요: ")
            mem_user_name = input("UserName을 입력하세요: ")
            mem_password = input("비밀번호를 입력하세요: ")
            mem = Member(mem_name, mem_user_name, mem_password)
            mem.register()
        elif a == 2:
            for_post_title = input("제목을 입력하세요: ")
            for_post_content = input("내용을 입력하세요: ")
            for_post_author = input("UserName을 입력하세요: ")
            for k in members: #맴버리스트에 등록된 유저네임만 모아놓은 새로운 리스트 생성
                    k_user_name = k['유저네임']
                    user_name_list.append(k_user_name)
            if not members: #등록된 회원이 없으면 회원등록 먼저 하고 글쓰러 오게 하기
                print("등록된 회원이 아닙니다. 회원등록을 먼저 해주세요")
                continue
            elif not for_post_author in user_name_list: #등록된 회원이 아니면 회원등록 먼저 하고 글쓰러 오게 하기
                print("등록된 회원이 아닙니다. 회원등록을 먼저 해주세요")
                continue
            for_post = Post(for_post_title, for_post_content, for_post_author)
            for_post.p_register()
        elif a == 3:
            if not members:
                print("등록된 회원이 없습니다")
                #비어있는 리스트의 bool 값은 false
            else:
                for i in members:
                    # i_name = i['이름']
                    # i_user_name = i['유저네임']
                    # print(f'이름: {i_name}  유저네임: {i_user_name}')
                    print(f"이름: {i['이름']}  유저네임: {i['유저네임']}")
                    #비밀번호 표시 x
        elif a == 4:
            if not posts:
                print("등록된 게시물이 없습니다")
            else:
                for j in posts:
                #     j_author = j['글쓴이']
                #     j_title = j['제목']
                #     print(f'작성자: {j_author}  제목: {j_title}')
                    print(f"이름: {j['글쓴이']}  유저네임: {j['제목']}")
        elif a == 5:
            break


use_input()