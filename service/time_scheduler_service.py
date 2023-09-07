from model.time_scheduler import Lesson, TimeTable
from utils.generate_problem import generate_problem
from utils.example_dto import example_dto
from config.constraints import define_constraints
from optapy import get_class
import optapy.config
from optapy.types import Duration
from optapy import solver_factory_create

solver_config = optapy.config.solver.SolverConfig() \
    .withEntityClasses(get_class(Lesson)) \
    .withSolutionClass(get_class(TimeTable)) \
    .withConstraintProviderClass(get_class(define_constraints)) \
    .withTerminationSpentLimit(Duration.ofSeconds(30))

solution = solver_factory_create(solver_config)\
    .buildSolver()\
    .solve(generate_problem(example_dto))

path = "../temp/timetable.txt"
try:
    with open(path, "w") as arquivo:
        arquivo.write(str(solution))
    print("Arquivo salvo com sucesso em:", path)
except Exception as e:
    print("Ocorreu um erro ao salvar o arquivo:", str(e))
