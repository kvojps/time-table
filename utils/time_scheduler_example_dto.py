from service.serializers.time_scheduler_dto import TimeSlotDTO, LessonDTO, TimeSchedulerDTO

timeslot_list_data = [{
    "id": 1,
    "day_of_week": "MONDAY",
    "hour_start_time": 8,
    "minute_start_time": 30,
    "hour_end_time": 9,
    "minute_end_time": 30
},
    {
        "id": 2,
        "day_of_week": "MONDAY",
        "hour_start_time": 9,
        "minute_start_time": 30,
        "hour_end_time": 10,
        "minute_end_time": 30
    },
    {
        "id": 3,
        "day_of_week": "MONDAY",
        "hour_start_time": 10,
        "minute_start_time": 30,
        "hour_end_time": 11,
        "minute_end_time": 30
    },
    {
        "id": 4,
        "day_of_week": "MONDAY",
        "hour_start_time": 13,
        "minute_start_time": 30,
        "hour_end_time": 14,
        "minute_end_time": 30
    },
    {
        "id": 5,
        "day_of_week": "MONDAY",
        "hour_start_time": 14,
        "minute_start_time": 30,
        "hour_end_time": 15,
        "minute_end_time": 30
    },
    {
        "id": 6,
        "day_of_week": "TUESDAY",
        "hour_start_time": 8,
        "minute_start_time": 30,
        "hour_end_time": 9,
        "minute_end_time": 30
    },
    {
        "id": 7,
        "day_of_week": "TUESDAY",
        "hour_start_time": 9,
        "minute_start_time": 30,
        "hour_end_time": 10,
        "minute_end_time": 30
    },
    {
        "id": 8,
        "day_of_week": "TUESDAY",
        "hour_start_time": 10,
        "minute_start_time": 30,
        "hour_end_time": 11,
        "minute_end_time": 30
    },
    {
        "id": 9,
        "day_of_week": "TUESDAY",
        "hour_start_time": 13,
        "minute_start_time": 30,
        "hour_end_time": 14,
        "minute_end_time": 30
    },
    {
        "id": 10,
        "day_of_week": "TUESDAY",
        "hour_start_time": 14,
        "minute_start_time": 30,
        "hour_end_time": 15,
        "minute_end_time": 30
    }
]

lesson_list_data = [
    {
        "id": 1,
        "subject": "Math",
        "teacher": "A. Turing",
        "student_group": "9th grade"
    },
    {
        "id": 2,
        "subject": "Math",
        "teacher": "A. Turing",
        "student_group": "9th grade"
    },
    {
        "id": 3,
        "subject": "Physics",
        "teacher": "M. Curie",
        "student_group": "9th grade"
    },
    {
        "id": 4,
        "subject": "Chemistry",
        "teacher": "M. Curie",
        "student_group": "9th grade"
    },
    {
        "id": 5,
        "subject": "Biology",
        "teacher": "C. Darwin",
        "student_group": "9th grade"

    },
    {
        "id": 6,
        "subject": "History",
        "teacher": "I. Jones",
        "student_group": "9th grade"
    },
    {
        "id": 7,
        "subject": "English",
        "teacher": "I. Jones",
        "student_group": "9th grade"
    },
    {
        "id": 8,
        "subject": "English",
        "teacher": "I. Jones",
        "student_group": "9th grade"
    },
    {
        "id": 9,
        "subject": "Spanish",
        "teacher": "P. Cruz",
        "student_group": "9th grade"
    },
    {
        "id": 10,
        "subject": "Spanish",
        "teacher": "P. Cruz",
        "student_group": "9th grade"
    },
    {
        "id": 11,
        "subject": "Math",
        "teacher": "A. Turing",
        "student_group": "10th grade"
    },
    {
        "id": 12,
        "subject": "Math",
        "teacher": "A. Turing",
        "student_group": "10th grade"
    },
    {
        "id": 13,
        "subject": "Math",
        "teacher": "A. Turing",
        "student_group": "10th grade"
    },
    {
        "id": 14,
        "subject": "Physics",
        "teacher": "M. Curie",
        "student_group": "10th grade"
    },
    {
        "id": 15,
        "subject": "Chemistry",
        "teacher": "M. Curie",
        "student_group": "10th grade"
    },
    {
        "id": 16,
        "subject": "French",
        "teacher": "M. Curie",
        "student_group": "10th grade"
    },
    {
        "id": 17,
        "subject": "Geography",
        "teacher": "C. Darwin",
        "student_group": "10th grade"
    },
    {
        "id": 18,
        "subject": "History",
        "teacher": "I. Jones",
        "student_group": "10th grade"
    },
    {
        "id": 19,
        "subject": "English",
        "teacher": "P. Cruz",
        "student_group": "10th grade"
    },
    {
        "id": 20,
        "subject": "Spanish",
        "teacher": "P. Cruz",
        "student_group": "10th grade"
    }
]

timeslot_list = [TimeSlotDTO(**data) for data in timeslot_list_data]

lesson_list = [LessonDTO(**data) for data in lesson_list_data]

time_scheduler_dto = TimeSchedulerDTO(
    timeslot_list=timeslot_list,
    lesson_list=lesson_list
)
