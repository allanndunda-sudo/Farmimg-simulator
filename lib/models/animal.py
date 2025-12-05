
from farm_database import SessionLocal
from models.category import Category
from models.animal import Animal
from models.feed import Feed

session = SessionLocal()

def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    params = {**kwargs}
    if defaults:
        params.update(defaults)
    instance = model(**params)
    session.add(instance)
    session.commit()
    return instance

name = input("Animal name: ")
gender = input("Gender (Male/Female): ")
category_name = input("Category: ")
feed_names = input("Feeds (comma separated): ").split(",")


category = get_or_create(session, Category, name=category_name.strip())


animal = get_or_create(
    session,
    Animal,
    defaults={"gender": gender.strip(), "category_id": category.id},
    name=name.strip()
)


for f in feed_names:
    feed = get_or_create(session, Feed, name=f.strip())
    if feed not in animal.feeds:  
        animal.feeds.append(feed)

session.commit()
print(f"Animal '{name}' added successfully!")
session.close()
