import re


def generate_timetable_response(solution):
    create_file(solution)
    path = "temp/timetable.txt"
    return extract_data_from_txt(path)


def create_file(solution):
    path = "temp/timetable.txt"
    try:
        with open(path, "w") as arquivo:
            arquivo.write(str(solution))
        print("Arquivo salvo com sucesso em:", path)
    except Exception as e:
        print("Ocorreu um erro ao salvar o arquivo:", str(e))


def extract_data_from_txt(txt_file):
    timetable = {
        "timeTable": {
            "timeslot_list": [],
            "lesson_list": [],
            "score": "0hard/0soft"
        }
    }

    with open(txt_file, 'r') as file:
        lines = file.readlines()

    current_section = None

    for line in lines:
        line = line.strip()
        if line.startswith("TimeTable("):
            current_section = "TimeTable"
        elif line.startswith("Timeslot("):
            current_section = "Timeslot"
            timeslot = extract_timeslot(line)
            timetable["timeTable"]["timeslot_list"].append(timeslot)
        elif line.startswith("Lesson("):
            current_section = "Lesson"
            lesson = extract_lesson(line)
            timetable["timeTable"]["lesson_list"].append(lesson)
        elif line.startswith("score="):
            current_section = "score"

    return timetable


def extract_timeslot(timeslot_str):
    parts = re.findall(r"(\w+)=(\w+:\w+:\w+)", timeslot_str)
    timeslot = {}
    for key, value in parts:
        timeslot[key] = value
    return timeslot


def extract_lesson(lesson_str):
    parts = re.findall(r"(\w+)=(\w+:\w+:\w+|\w+)", lesson_str)
    lesson = {}
    for key, value in parts:
        lesson[key] = value
    return lesson
