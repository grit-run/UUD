from pydantic import BaseModel
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column

class CreateUser(BaseModel):
    username = Column(String(100), unique=True)
    name = Column(String(100))
    surname = Column(String(100))
    age = Column(Integer)
    email = Column(String(100), unique=True)
    password = Column(String(100))

class CreateAddress(BaseModel):
    zipcode = Column(String(6))
    street = Column(String(100))
    number = Column(String(100))
    apartment = Column(String(100))
    city = Column(String(100))
    country = Column(String(100))

class CreateUserAddress(BaseModel):
    user = Column(BigInteger, ForeignKey("users.id"))
    address = Column(BigInteger, ForeignKey("addresses.id"))

class CreateProduct(BaseModel):
    name = Column(String(100))
    group = Column(BigInteger, ForeignKey("groups.id"))
    description = Column(String(100))
    price = Column(Float)

class CreateGroup(BaseModel):
    name = Column(String(100))

class CreateOrder(BaseModel):
    user = Column(BigInteger, ForeignKey("users.id"))
    product = Column(BigInteger, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_cost = Column(Float)

class UpdateUser(BaseModel):
    name = Column(String(100))
    surname = Column(String(100))
    age = Column(Integer)
    email = Column(String(100))
    password = Column(String(100))

class UpdateAddress(BaseModel):
    zipcode = Column(String(6))
    street = Column(String(100))
    number = Column(String(100))
    apartment = Column(String(100))
    city = Column(String(100))
    country = Column(String(100))

class UpdateProduct(BaseModel):
    name = Column(String(100))
    description = Column(String(100))
    price = Column(Float)

class UpdateGroup(BaseModel):
    name = Column(String(100))