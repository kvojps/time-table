from model.time_scheduler import Lesson
from optapy import constraint_provider, get_class
from optapy.constraint import Joiners
from optapy.score import HardSoftScore

LessonClass = get_class(Lesson)


@constraint_provider
def define_constraints(constraint_factory):
    return [
        teacher_conflict(constraint_factory),
        student_group_conflict(constraint_factory),
    ]


def teacher_conflict(constraint_factory):
    return constraint_factory \
        .forEach(LessonClass)\
        .join(LessonClass,
              [
                  Joiners.equal(lambda lesson: lesson.timeslot),
                  Joiners.equal(lambda lesson: lesson.teacher),
                  Joiners.lessThan(lambda lesson: lesson.id)
              ]) \
        .penalize("Teacher conflict", HardSoftScore.ONE_HARD)


def student_group_conflict(constraint_factory):
    return constraint_factory \
        .forEach(LessonClass) \
        .join(LessonClass,
              [
                  Joiners.equal(lambda lesson: lesson.timeslot),
                  Joiners.equal(lambda lesson: lesson.student_group),
                  Joiners.lessThan(lambda lesson: lesson.id)
              ]) \
        .penalize("Student group conflict", HardSoftScore.ONE_HARD)
