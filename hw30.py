from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Session




class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "Student"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    last_name:Mapped[str] = mapped_column()
    name:Mapped[str] = mapped_column()
    rait:Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Students ( id={self.id!r}, last_name={self.last_name!r}, name={self.name!r}, rait={self.rait!r})"


engine = create_engine("sqlite:///my_orm_db.db")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    student1 = Student(last_name="Ярошкін", name="Сергій", rait=539)
    student2 = Student(last_name="Таран", name="Андрій", rait=536)
    student3 = Student(last_name="Бєлоусов", name="Юрій",  rait=490)
    student4 = Student(last_name="Марченко", name="Ілля",  rait=433)
    student5 = Student(last_name="Зайченко", name="Михайло",  rait=428)
    student6 = Student(last_name="Діденко", name="Нікіта", rait=303)
    student7 = Student(last_name="Лозовий", name="Олексій",  rait=298)
    student8 = Student(last_name="Ахмедов", name="Ахмед",  rait=263)
    student9 = Student(last_name="Рыжков", name="Владислав",  rait=227)
    student10 = Student(last_name="Каштаєв", name="Артур",  rait=225)
    student11 = Student(last_name="Тараканов", name="Сергій",  rait=200)
    student12 = Student(last_name="Стрельченко", name="Дмитро",  rait=164)

session.add_all((student1, student2, student3, student4, student5, student6, student7, student8, student9, student10, student11, student12))
session.commit()


#Увеличить в своей записи рейтинг на 5 ед.
student1.rait = 544
print(student1)
session.commit()

#Вывести всех студентов у которых рейтинг больше чем у вас.
students = session.query(Student).filter(Student.id < 1).limit(5).all()
print(students)
session.commit()

#Удалить студентов у которых рейтинг рейтинг меньше заданного значения (любое число)
studen = session.query(Student).filter(Student.rait<400).delete()
print(studen)
session.commit()