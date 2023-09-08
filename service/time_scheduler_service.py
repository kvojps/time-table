from model.time_scheduler import Lesson, TimeTable
from .serializers.time_scheduler_dto import TimeSchedulerDTO
from config.generate_problem import generate_problem
from config.constraints import define_constraints
from utils.utils import create_file
from optapy import get_class
import optapy.config
from optapy.types import Duration
from optapy import solver_factory_create


class TimeSchedulerService:
    def __init__(self):
        self.solver_config = optapy.config.solver.SolverConfig() \
            .withEntityClasses(get_class(Lesson)) \
            .withSolutionClass(get_class(TimeTable)) \
            .withConstraintProviderClass(
            get_class(define_constraints)) \
            .withTerminationSpentLimit(Duration.ofSeconds(30))

    def create_time_table(self, time_scheduler_dto: TimeSchedulerDTO):
        solution = solver_factory_create(self.solver_config) \
            .buildSolver() \
            .solve(generate_problem(time_scheduler_dto))

        create_file(solution)

