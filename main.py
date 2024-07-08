import hashlib
# 해시 함수 알아보기

# 빈리스트 만들기
members = []  # 회원들의 정보를 담고 있는 리스트
posts = []  # 게시글을 담고 있는 리스트


class Member:  # 각각의 회원정보를 담고 있는 클래스다.

    # 생성자
    def __init__(self, name, username, password) -> None:
        self.name = name
        self.username = username
        self.password = password

    # 회원정보출력
    def display(self):
        for_hashed_pw = self.password
        hashed_pw = hashlib.sha256(for_hashed_pw.encode()).hexdigest()
        # 비밀번호 해싱
        # print("sha",hashed_pw)
        # return {'이름': self.name, '유저네임': self.username, '비밀번호': hashed_pw}
        
        print("name :{0}  username: {1} hashed_pw: {2}".format(self.name, self.username,hashed_pw))
        # print("data :", self.password)
    
        # for post in self.posts:
        #     print("title :{} ".format(post.title))
        #     print("content :{} ".format(post.content))


# 각각의게시글 관리
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_post(self):
        print("author :{0}, title :{1}".format(self.author, self.title))
        print("content:{0}".format(self.content))

# 관리
class working():
    def create_post():
        if len(members) > 0:
            author = input("작성자입력\n")
            for member in members:
                if member.name == author:
                    title = input("제목\n")
                    content = input("내용\n")
                    post = Post(title, content, author)
                    posts.append(post)
                    print(f"{post.author}님의 게시글이 작성되었습니다.\n\n\n")
                else:
                    print("작성자가 일치하지 않습니다. 다시 입력하세요\n")
                    working.create_post()
        else:
            print("회원가입을 먼저 해주세요\n")

    # 게시글 검색
    def post_search():
        search_result = []
        search_content = []
        
        if len(posts) > 0:
            # 회원이름, 회원아이디,
            print("1. 게시글제목\n")
            print("2. 게시글내용\n")
            print("3. 작성자\n")
            search_type = input("무엇을 검색하시겠습니까?\n")
            if search_type == "1":
                print("게시글 제목으로 검색합니다.")
                search_word = input("제목을 입력해주세요\n")
                for post in posts:
                    if search_word in post.title:
                        search_result.append(post.title)
                        search_content.append(post.content)
            elif search_type == "2":
                search_word = input("내용을 입력해주세요: \n")
                for post in posts:
                    if search_word in post.content:
                        search_content.append(post.content)
            elif search_type == "3":
                search_word = input("작성자를 입력해주세요: \n")
                for post in posts:
                    if search_word in post.author:
                        search_result.append(post.title)
                        search_content.append(post.content)
            else:
                print("잘못된 입력입니다. 다시 입력해주세요")
                working.post_search()
        else:
            print("작성글이 없습니다.")

        if search_result:
            print("검색결과입니다.")
            for result in search_result:
                print(f'제목:{result}')
                print(f'내용: {post.content}')
                
            # print (result for result in search_result)

    # 회원가입시키기

    def join():
        name = input("이름입력")
        username = input("아이디입력")
        password = input("비밀번호 입력")
        # name 회원이름, username : 회원아이디, password:
        member = Member(name, username, password)
        members.append(member)  # 회원가입추가
        print(f"{member.name}님의 회원가입이 완료되었습니다.\n\n\n")

    def option():
        print("1. 회원가입")
        print("2. 회원정보출력")
        print("3. 게시글작성")
        print("4. 게시글출력")
        print("5. 게시글검색")
        print("6. 종료")

        choice = input("무엇을 하시겠습니까?")

        if choice == "1":
            print("회원가입을 시작합니다.")
            working.join()
            working.option()

        elif choice == "2":
            print("회원정보리스트출력")
            for member in members:
                member.display()
            print("\n\n")
            working.option()

        elif choice == "3":
            print("게시글작성")
            working.create_post()
            working.option()

        elif choice == "4":
            print("게시글출력")
            for i, post in enumerate(posts):
                num = i + 1
                print(f"글번호{num}\n")
                post.display_post()
            print("\n\n")
            working.option()

        elif choice == "5":
            print("게시글검색")
            working.post_search()
            working.option()

        elif choice == "6":
            print("종료합니다")

        else:
            print("잘못된 입력입니다.")
            working.option()


#     for i in range(3):
#         title = input("{}의 게시글 제목 {}".format(name, i+1))
#         content = input("{}의 게시글 내용 {}".format(name, i+1))
#         member.create_post(title, content)

# members.append(member)

if __name__ == '__main__':
    working.option()
