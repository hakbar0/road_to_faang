class Cookie:
    def __init__(self, color: str):
        self.color = color

cookie: Cookie = Cookie('green')
print(cookie.color)