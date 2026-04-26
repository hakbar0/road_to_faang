class Cookie:
    def __init__(self, color:str):
        self.color: str = color
    
    def get_color(self):
        return self.color


cookie_one = Cookie('green')
print(cookie_one.get_color())