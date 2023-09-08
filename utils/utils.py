def create_file(solution):
    path = "temp/timetable.txt"
    try:
        with open(path, "w") as arquivo:
            arquivo.write(str(solution))
        print("Arquivo salvo com sucesso em:", path)
    except Exception as e:
        print("Ocorreu um erro ao salvar o arquivo:", str(e))