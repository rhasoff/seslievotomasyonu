from evotomasyon import db
from evotomasyon.models import Service

db.drop_all()
db.create_all()

service1 = Service(service_name='Işık', 
            icon_on='<i class="far fa-lightbulb"></i>',
            icon_off='<i class="fas fa-lightbulb"></i>',
            state=False)

service2 = Service(service_name='Kapı', 
            icon_on='<i class="fas fa-door-open"></i>',
            icon_off='<i class="fas fa-door-closed"></i>',
            state=False)

service3 = Service(service_name='Perde', 
            icon_on='<i class="far fa-window-maximize"></i>',
            icon_off='<i class="fas fa-window-maximize"></i>',
            state=False)

service4 = Service(service_name='Sulama', 
            icon_on='<i class="fas fa-cloud-showers-heavy"></i>',
            icon_off='<i class="fas fa-seedling"></i>',
            state=False)

db.session.add(service1)
db.session.add(service2)
db.session.add(service3)
db.session.add(service4)

db.session.commit()
