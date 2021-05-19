from datetime import datetime
from evotomasyon import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(64), unique=True, nullable=False)
    icon_on = db.Column(db.String(64))
    icon_off = db.Column(db.String(64))
    state = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        status =""
        if self.state:
            status="Açık"
        else:
            status="Kapalı"
        return f"{self.service_name} {status}"

    def change_state(self):
        if self.state ==True:
            self.state=False
        else:
            self.state=True
    
    
    # def get_status(self):
    #     status =""
    #     if self.state:
    #         status="Açık"
    #     else:
    #         status="Kapalı"
    #     return f"{self.service_name} {status}"

