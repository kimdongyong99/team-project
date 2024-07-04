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

