from pprint import pprint
members = [] #회원정보 보관 리스트
posts = [] #post 보관 리스트
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
        return {'이름': self.name, '유저네임': self.user_name, '비밀번호': self.password}
        # members 리스트에 추가하기 위해 포맷 만들기
    def register(self):
        members.append(self.format_register())
        #for_register에 작성된 포맷으로 members리스트에 추가하기

# m1 = Member('이상혁','faker',1234) 
# m2 = Member('류민석', 'keria',5678)
# m3 = Member('최우제','Zeus',9101)
# #         #정보저장을 위한 필요 데이터 입력
# m1.display()
# m1.register()
# m2.register()
# m3.register()
# pprint(members)
# title, content, author
class Post:
    def __init__(self,title, content,user_name):
        self.title = title
        self.content = content
        self.author =  user_name
        # Post의 author를 user_name으로
    def post_display(self):
        print(f'제목 : {self.title}')
        print(f'내용 : {self.content}')
    
    def p_format_register(self):
        return {'제목': self.title, '내용': self.content, '글쓴이': self.author}
        # posts 리스트에 추가하기 위해 포맷 만들기
    def p_register(self):
        posts.append(self.p_format_register())
#         # 코드실행
# m1_1 = Post('전적','1337전 907승 430패, 승률 67.8%, 총 킬 4725, 총 데스 2845, 총 어시스트 7314, KDA 4.3, 킬 관여율 64.9%','faker')
# m1_2 = Post('대회 경력','월즈 우승 4회, MSI 우승 2회, LCK 우승 10회, IEM 우승 1회, 리프트 라이벌즈 우승 1회, 리그 오브 레전드 올스타전 우승 5회, NLB 우승 1회, 아시안 게임 금메달','faker')
# m1_3 = Post('개인 업적','Worlds MVP 1회, MSI MVP 1회, LCK 통합 MVP 2회, LCK 포스트시즌 MVP 1회, LCK All-Pro First team 2회','faker')
# m2_2 = Post('전적',)
#         # Post 작성
# m1_1.post_display()
# m1_1.p_register()
# m1_2.p_register()
# m1_3.p_register()
# pprint(posts)
cnt = 0
def use_input():
    while True:
        a = int(input("숫자를 입력하세요(회원등록: 1, 게시글 작성: 2, 회원리스트: 3, 게시글리스트: 4, 종료: 5): "))
        if (a !=1) and (a !=2) and (a !=3) and (a != 4) and (a !=5):
            print("다시 입력하세요(회원등록: 1, 게시글 작성: 2, 회원리스트: 3, 게시글리스트: 4, 종료: 5):")
            continue
        if a == 1:
            mem_name = input("이름을 입력하세요: ")
            mem_user_name = input("UserName을 입력하세요: ")
            mem_password = input("비밀번호를 입력하세요: ")
            mem = Member(mem_name,mem_user_name,mem_password)
            mem.register()
        elif a == 2:
            for_post_title = input("제목을 입력하세요: ")
            for_post_content = input("내용을 입력하세요: ")
            for_post_author = input("UserName을 입력하세요: ")
            for_post = Post(for_post_title,for_post_content,for_post_author)
            for_post.p_register()
        elif a == 3:
            pprint(members)
        elif a ==4:
            pprint(posts)
        elif a == 5:
            break
use_input()