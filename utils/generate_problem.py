from model.time_scheduler import Timeslot, Lesson, TimeTable
from datetime import time


def generate_problem():
    timeslot_list = [
        Timeslot(1, "MONDAY", time(hour=8, minute=30),
                 time(hour=9, minute=30)),
        Timeslot(2, "MONDAY", time(hour=9, minute=30),
                 time(hour=10, minute=30)),
        Timeslot(3, "MONDAY", time(hour=10, minute=30),
                 time(hour=11, minute=30)),
        Timeslot(4, "MONDAY", time(hour=13, minute=30),
                 time(hour=14, minute=30)),
        Timeslot(5, "MONDAY", time(hour=14, minute=30),
                 time(hour=15, minute=30)),
        Timeslot(6, "TUESDAY", time(hour=8, minute=30),
                 time(hour=9, minute=30)),
        Timeslot(7, "TUESDAY", time(hour=9, minute=30),
                 time(hour=10, minute=30)),
        Timeslot(8, "TUESDAY", time(hour=10, minute=30),
                 time(hour=11, minute=30)),
        Timeslot(9, "TUESDAY", time(hour=13, minute=30),
                 time(hour=14, minute=30)),
        Timeslot(10, "TUESDAY", time(hour=14, minute=30),
                 time(hour=15, minute=30)),
    ]
    lesson_list = [
        Lesson(1, "Math", "A. Turing", "9th grade"),
        Lesson(2, "Math", "A. Turing", "9th grade"),
        Lesson(3, "Physics", "M. Curie", "9th grade"),
        Lesson(4, "Chemistry", "M. Curie", "9th grade"),
        Lesson(5, "Biology", "C. Darwin", "9th grade"),
        Lesson(6, "History", "I. Jones", "9th grade"),
        Lesson(7, "English", "I. Jones", "9th grade"),
        Lesson(8, "English", "I. Jones", "9th grade"),
        Lesson(9, "Spanish", "P. Cruz", "9th grade"),
        Lesson(10, "Spanish", "P. Cruz", "9th grade"),
        Lesson(11, "Math", "A. Turing", "10th grade"),
        Lesson(12, "Math", "A. Turing", "10th grade"),
        Lesson(13, "Math", "A. Turing", "10th grade"),
        Lesson(14, "Physics", "M. Curie", "10th grade"),
        Lesson(15, "Chemistry", "M. Curie", "10th grade"),
        Lesson(16, "French", "M. Curie", "10th grade"),
        Lesson(17, "Geography", "C. Darwin", "10th grade"),
        Lesson(18, "History", "I. Jones", "10th grade"),
        Lesson(19, "English", "P. Cruz", "10th grade"),
        Lesson(20, "Spanish", "P. Cruz", "10th grade"),
    ]
    lesson = lesson_list[0]
    lesson.set_timeslot(timeslot_list[0])

    return TimeTable(timeslot_list, lesson_list)
