from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[BigInteger] = mapped_column(primary_key=True)
    username = Column(String(100), unique=True)
    name = Column(String(100))
    surname = Column(String(100))
    age = Column(Integer)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    orders = relationship("Order", back_populates="user")
    addresses = relationship("Address", secondary="user_addresses", back_populates="users")


class UserAddress(Base):
    __tablename__ = "user_addresses"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    address_id = Column(BigInteger, ForeignKey("addresses.id"))

    user = relationship("User", back_populates="addresses")
    address = relationship("Address", back_populates="users")


class Address(Base):
    __tablename__ = "addresses"
    id = Column(BigInteger, primary_key=True)
    zipcode = Column(String(6))
    street = Column(String(100))
    number = Column(String(100))
    apartment = Column(String(100))
    city = Column(String(100))
    country = Column(String(100))
    users = relationship("User", secondary="user_addresses", back_populates="addresses")


class Group(Base):
    __tablename__ = "groups"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    products = relationship("Product", back_populates="group")


class Product(Base):
    __tablename__ = "products"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    group = Column(BigInteger, ForeignKey("groups.id"), delete="CASCADE")
    description = Column(String(100))
    price = Column(Float)
    group = relationship("Group", back_populates="products")


class OrderUser(Base):
    __tablename__ = "order_users"
    id = Column(BigInteger, primary_key=True)
    user = Column(BigInteger, ForeignKey("users.id"), delete="CASCADE")
    order = Column(BigInteger, ForeignKey("orders.id"), delete="CASCADE")

    user = relationship("User", back_populates="orders")
    order = relationship("Order", back_populates="users")


class Order(Base):
    __tablename__ = "orders"
    id = Column(BigInteger, primary_key=True)
    user = Column(BigInteger, ForeignKey("users.id"), delete="CASCADE")
    product = Column(BigInteger, ForeignKey("products.id"), delete="CASCADE")
    quantity = Column(Integer)
    total_cost = Column(Float)

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")
