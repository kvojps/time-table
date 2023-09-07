from model.time_scheduler import Timeslot, Lesson, TimeTable
from service.serializers.time_scheduler_dto import TimeSchedulerDTO
from datetime import time


def generate_problem(time_scheduler_dto: TimeSchedulerDTO):
    timeslot_list = generate_time_slot_list(time_scheduler_dto)
    lesson_list = generate_lesson_list(time_scheduler_dto)
    lesson = lesson_list[0]
    lesson.set_timeslot(timeslot_list[0])

    return TimeTable(timeslot_list, lesson_list)


def generate_time_slot_list(time_scheduler_dto: TimeSchedulerDTO):
    timeslot_list = []
    for time_slot in time_scheduler_dto.timeslot_list:
        time_slot_add = Timeslot(time_slot.id, time_slot.day_of_week,
                                 time(hour=time_slot.hour_start_time, minute=time_slot.minute_start_time),
                                 time(hour=time_slot.hour_end_time, minute=time_slot.minute_end_time))
        timeslot_list.append(time_slot_add)

    return timeslot_list


def generate_lesson_list(time_scheduler_dto: TimeSchedulerDTO):
    lesson_list = []
    for lesson in time_scheduler_dto.lesson_list:
        lesson_add = Lesson(lesson.id, lesson.subject, lesson.teacher, lesson.student_group)
        lesson_list.append(lesson_add)

    return lesson_list
