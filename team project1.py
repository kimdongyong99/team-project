import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # def _hash_password(self, password):
    #     # SHA-256 해시 객체 생성
    #     sha256 = hashlib.sha256()
    #     # 비밀번호를 UTF-8 인코딩으로 변환하여 해시 객체에 추가
    #     sha256.update(password.encode('utf-8'))
    #     # 해시화된 비밀번호 반환
    #     return sha256.hexdigest()  



    def display(self):
        print(f"Name: {self.name}, Username: {self.username}")

# members = []
# members.append(Member("이상혁", "faker", "0000"))
# members.append(Member("김건부", "canyon", "0002"))
# members.append(Member("김혁규", "deft", "0001"))

# print("회원 이름")
# for member in members:
#     print(member.name)

def create_member_from_input():
    print("\n새로운 회원 정보를 입력하세요:")
    name = input("이름을 입력하세요: ")
    username = input("사용자명을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    
    

    member = Member(name, username, password)
    return member

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

# posts = []

# for member in members:

#     posts.append(Post(f"{member.name}의 첫 번째 글", "첫 번째 게시물 내용", member.username))
#     posts.append(Post(f"{member.name}의 두 번째 글", "두 번째 게시물 내용", member.username))
#     posts.append(Post(f"{member.name}의 세 번째 글", "세 번째 게시물 내용", member.username))

# for post in posts:
#     print(post.title, post.content, post.author)   

# for post in posts:
#     if "두 번째" in post.content:
#         print(post.title)        

def create_post_from_input(author):
    print(f"\n{author}님의 새로운 게시글 정보를 입력하세요:")
    title = input("게시물 제목을 입력하세요: ")
    content = input("게시물 내용을 입력하세요: ")

    post = Post(title, content, author)
    return post

# 회원 인스턴스 생성 및 리스트에 저장
members = []

for _ in range(3):
    member = create_member_from_input()
    members.append(member)

# 회원들의 이름 출력
print("\n회원들의 이름:")
for member in members:
    print(member.name)

# 게시글 인스턴스 생성 및 리스트에 저장
posts = []
for member in members:
    for _ in range(3):
        post = create_post_from_input(member.username)
        posts.append(post)




# # 특정 유저가 작성한 게시글 제목 출력
# print("\n각 회원이 작성한 게시글 제목:")
# for member in members:
#     print(f"{member.name}님이 작성한 게시글 제목:")
#     for post in posts:
#         if post.author == member.username:
#             print(post.title)

# # 특정 단어가 포함된 게시글 제목 출력
# keyword = input("\n찾고자 하는 단어를 입력하세요: ")
# print(f"\n'{keyword}'가 포함된 게시글 제목:")
# for post in posts:
#     if keyword in post.content:
#         print(post.title)





