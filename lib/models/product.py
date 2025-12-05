from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from farm_database import Base


animal_products = Table(
    "animal_products",
    Base.metadata,
    Column("animal_id", Integer, ForeignKey("animals.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True)
)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


    animals = relationship("Animal", secondary=animal_products, back_populates="products")

    def __repr__(self):
        return f"<Product(name={self.name})>"
