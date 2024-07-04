class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        pass

    def display(self):
        print(f"이름: {self.name}")
        print(f"아이디: {self.username}")


members = []
members.append(Member("이상혁", "faker", "0000"))
members.append(Member("김건부", "canyon", "0002"))
members.append(Member("김혁규", "deft", "0001"))

print("회원 이름")
for member in members:
    print(member.name)


class Post:
    def __init__(self, title, content, author) :
        self.title = title 
        self.content = content
        self.author = author
        pass        



posts = []

for member in members:

    posts.append(Post(f"{member.name}의 첫 번째 글", "첫 번째 게시물 내용", member.username))
    posts.append(Post(f"{member.name}의 두 번째 글", "두 번째 게시물 내용", member.username))
    posts.append(Post(f"{member.name}의 세 번째 글", "세 번째 게시물 내용", member.username))

for post in posts:
    print(post.title, post.content, post.author)   

for post in posts:
    if "두 번째" in post.content:
        print(post.title)


        

members = [] #회원정보 보관 리스트
posts = []
class member:
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
m1 = member('정순겸','gyum9779',1234) #정보저장을 위한 필요 데이터 입력
m1.display()
m1.register()
print(members)


# ----- 코드 실행 ------

# TODO : 코드 구현이 필요합니다.
