from sqlalchemy import Column, Integer, String, Float
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    merchant = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
