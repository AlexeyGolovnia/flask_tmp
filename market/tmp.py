from market import app
a = app.app_context()
a.push()
from market.models import db, User, Item
db.drop_all()
db.create_all()
i1 = Item(name='Iphone 10', price=800, barcode='45661187', description='desc1')
i2 = Item(name='Laptop', price=1000, barcode='68884701', description='desc2')
u1 = User(username='a11', password_hash='123456', email_address='a11@a11.com')
u2 = User(username='a12', password_hash='123', email_address='a12@a12.com')
db.session.add(i1)
db.session.add(i2)
db.session.add(u1)
db.session.add(u2)
db.session.commit()





for i in Item.query.all():
    i.name
    i.barcode