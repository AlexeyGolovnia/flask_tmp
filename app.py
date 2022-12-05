from market import app

if __name__ == '__main__':
    app.run()


#with app.app_context():
#    db.create_all()
    

#from sqlalchemy import create_engine
#engine = create_engine('postgresql://admin:admin@host.docker.internal:5432/market')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@host.docker.internal:5432/market'
#db = SQLAlchemy(app)

    
#item1 = Item(name="IPhone 10", price=500, barcode="35698745", description="something about iphone")
#db.session.add(item1)

#engine.execute('''
#	create table courses(
#		c_no text primary key,
#		title text,
#		hours integer
#	);
#''')

#engine.execute('''
#	insert into courses(c_no, title, hours)
#		values ('cs301', 'bases', 30),
#		       ('cs305', 'nets', 60);
#''')

#engine.execute('drop table courses')



    

