from pydantic import BaseModel
from typing import List


class TimeSlotDTO(BaseModel):
    id: int
    day_of_week: str
    hour_start_time: int
    minute_start_time: int
    hour_end_time: int
    minute_end_time: int


class LessonDTO(BaseModel):
    id: int
    subject: str
    teacher: str
    student_group: str


class TimeSchedulerDTO(BaseModel):
    timeslot_list: List[TimeSlotDTO]
    lesson_list: List[LessonDTO]
