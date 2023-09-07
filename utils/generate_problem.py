from model.time_scheduler import Timeslot, Lesson, TimeTable
from datetime import time


def generate_problem(time_scheduler_dto):
    timeslot_list = generate_time_slot_list(time_scheduler_dto)
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


def generate_time_slot_list(time_scheduler_dto):
    timeslot_list = []
    for time_slot in time_scheduler_dto["timeslot_list"]:
        time_slot_add = Timeslot(time_slot["id"], time_slot["day_of_week"],
                                 time(hour=time_slot["hour_start_time"], minute=time_slot["minute_start_time"]),
                                 time(hour=time_slot["hour_end_time"], minute=time_slot["minute_end_time"]))
        timeslot_list.append(time_slot_add)

    return timeslot_list
