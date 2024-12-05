from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    time = Column(DateTime, default=datetime.utcnow)

# Создание базы данных
engine = create_engine('sqlite:///tasks.db')  # Замените на вашу базу данных
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Пример добавления задачи
new_task = Task(task_name='Пример задачи')
session.add(new_task)
session.commit()
