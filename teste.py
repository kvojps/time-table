from domain import Lesson, TimeTable, generate_problem
from constraints import define_constraints
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
    .solve(generate_problem())

path = "adapter/temp/timetable.txt"
try:
    with open(path, "w") as arquivo:
        arquivo.write(str(solution))
    print("Arquivo salvo com sucesso em:", path)
except Exception as e:
    print("Ocorreu um erro ao salvar o arquivo:", str(e))
