from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from farm_database import Base

animal_feeds = Table(
    "animal_feeds",
    Base.metadata,
    Column("animal_id", Integer, ForeignKey("animals.id"), primary_key=True),
    Column("feed_id", Integer, ForeignKey("feeds.id"), primary_key=True)
)

class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    animals = relationship("Animal", secondary=animal_feeds, back_populates="feeds")

    def __repr__(self):
        return f"<Feed(name={self.name})>"
