import yagmail


class Mail(object):
    def __init__(self, cfg):
        self.yag = yagmail.SMTP(user=cfg['username'], 
                                password=cfg['password'], 
                                host=cfg['host'])
        self.to = cfg['to']
    
    def send(self, subject, contents):
        self.yag.send(to=self.to, 
                      subject=subject, 
                      contents=contents)
