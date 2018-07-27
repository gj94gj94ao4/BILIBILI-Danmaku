class bilibili_comment():
    user: str()
    sec: float()
    text: str()

    def __init__(self, user, sec, text):
        self.user = user
        self.sec = sec
        self.text = text


    def __str__(self):
        return str.format("user:{0} time:{1} \t {2}", self.user, self.sec, self.text)