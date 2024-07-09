####게시판 속성

import hashlib

# 빈리스트 만들기
members = []  # 회원들의 정보를 담고 있는 리스트
posts = []    # 게시글을 담고 있는 리스트


class Member:
    # 생성자
    def __init__(self, name, username, password) -> None:
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print("name :{0}  username: {1}".format(self.name, self.username))
        # 비밀번호는 출력하지 않게!

# m1 = Member('이상혁', 'faker', 1234)
# m2 = Member('류민석', 'keria', 5678)
# m3 = Member('최우제', 'zeus', 91011)
      # 정보저장을 위한 필요 데이터 입력
# m1.display()

# 각각의 게시글 관리
class Post:
    def __init__(self, title, content, username):
        self.title = title
        self.content = content
        self.author = username
        # username을 받아서 author로 취급

    def display_post(self):
        print("author :{0}, title :{1}".format(self.author, self.title))
        print("content:{0}".format(self.content))

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
# m1_1.display_post()

# 관리
class working():
    def create_post():
        if len(members) > 0:
            while True:
                author = input("유저네임 입력\n")
                for member in members:
                    if member.username == author:
                        title = input("제목\n")
                        content = input("내용\n")
                        post = Post(title, content, author)
                        posts.append(post)
                        print(f"{post.author}님의 게시글이 작성되었습니다.\n\n\n")
                        return
                print("작성자가 일치하지 않습니다. 다시 입력하세요\n")
        else:
            print("회원가입을 먼저 해주세요\n")

    # 게시글 검색
    def post_search():
        search_result = []
        search_content = []

        if len(posts) > 0:
            print("1. 게시글 제목\n")
            print("2. 게시글 내용\n")
            print("3. 유저네임\n")
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
                search_word = input("유저네임을 입력해주세요: \n")
                for post in posts:
                    if search_word in post.author:
                        search_result.append(post.title)
                        search_content.append(post.content)
            else:
                print("잘못된 입력입니다. 다시 입력해주세요")
                working.post_search()
        else:
            print("등록된 게시글이 없습니다.")

        if search_result:
            print("검색결과입니다.")
            for result in search_result:
                print(f'제목:{result}')
                print(f'내용: {post.content}')

            # print (result for result in search_result)

    # 회원가입시키기

    def join():
        name = input("이름입력\n")
        username = input("유저네임 입력\n")
        password = input("비밀번호 입력\n")
        for_hashed_pw =str(password)
        hashed_pw = hashlib.sha256(for_hashed_pw.encode()).hexdigest()
        # name 회원이름, username : 회원아이디, password: hashing된 비밀번호로 전환하여 등록
        member_ = Member(name, username, hashed_pw)
        members.append(member_)  # 회원리스트에 추가
        print(f"{member_.name}님의 회원가입이 완료되었습니다.\n")

    def option():
        while True:
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
                continue

            elif choice == "2":
                print("회원정보리스트 출력")
                if len(members) > 0:
                    for member__ in members:
                        member__.display()
                else:
                    print("등록된 회원이 없습니다.")
                print("\n")
                continue
            
            elif choice == "3":
                print("게시글 작성")
                working.create_post()
                continue

            elif choice == "4":
                print("게시글 출력")
                if len(posts) > 0:
                    for i, post in enumerate(posts):
                        num = i + 1
                        print(f"글번호{num}")
                        post.display_post()
                else:
                    print("등록된 게시글이 없습니다")
                print("\n")
                continue

            elif choice == "5":
                print("게시글 검색")
                working.post_search()
                continue

            elif choice == "6":
                print("종료합니다")
                break

            else:
                print("잘못된 입력입니다.")
                continue


#     for i in range(3):
#         title = input("{}의 게시글 제목 {}".format(name, i+1))
#         content = input("{}의 게시글 내용 {}".format(name, i+1))
#         member.create_post(title, content)

# members.append(member)

if __name__ == '__main__':
    working.option()