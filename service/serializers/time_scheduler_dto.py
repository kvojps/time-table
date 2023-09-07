from pydantic import BaseModel


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
    timeslot_list: [TimeSlotDTO]
    lesson_list: [LessonDTO]
