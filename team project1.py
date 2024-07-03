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

class Post:
    # TODO : 코드 구현이 필요합니다.
    pass


# ----- 코드 실행 ------

# TODO : 코드 구현이 필요합니다.