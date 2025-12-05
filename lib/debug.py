
from farm_database import SessionLocal, Base, engine
from models.category import Category
from models.animal import Animal
from models.feed import Feed


Base.metadata.create_all(engine)


session = SessionLocal()


def get_or_create(session, model, defaults=None, **kwargs):
    """
    Returns existing object or creates a new one.
    `defaults` is a dict of values to set if creating.
    """
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


categories = ["Cow", "Goat", "Chicken"]
for name in categories:
    get_or_create(session, Category, name=name)

animals = [
    {"name": "Bessie", "category_name": "Cow", "gender": "Female"},
    {"name": "Billy", "category_name": "Goat", "gender": "Male"},
    {"name": "Clucky", "category_name": "Chicken", "gender": "Female"}
]

for a in animals:
    category = get_or_create(session, Category, name=a["category_name"])
    get_or_create(
        session,
        Animal,
        defaults={"gender": a["gender"], "category_id": category.id},
        name=a["name"]
    )


feeds = ["Grass", "Grains", "Hay"]
for feed_name in feeds:
    get_or_create(session, Feed, name=feed_name)


print("Database seeded successfully!")
session.close()
