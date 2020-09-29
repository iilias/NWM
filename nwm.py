def InitMatrix(CostMatrix, Supplier, Consumer):
    while True:
        userInput = input("Введите матрицу стоимостей: ")
        if userInput == "":
            for i in CostMatrix[0]:
                Consumer.append(int(input("Потребитель: ")))
            break
        CostMatrix.append(userInput.split(" "))
        Supplier.append(int(input("Количество поставок: ")))


def NorthWestMethod(CostMatrix, Supplier, Consumer):
    consLen = len(Consumer)
    suplLen = len(Supplier)
    ResMatrix = [[0] * consLen for i in range(suplLen)]
    for supl in range(suplLen):
        for cons in range(consLen):
            if Consumer[cons] == 0 or Supplier[supl] == 0:
                continue

            if Consumer[cons] > Supplier[supl]:
                # Отнять от потребности тек кол-во запасов
                Consumer[cons] -= Supplier[supl]
                # Записать в матрицу маршрута
                ResMatrix[supl][cons] = Supplier[supl]
                # Аннулировать запасы
                Supplier[supl] = 0
                continue
            elif Consumer[cons] < Supplier[supl]:
                # Отнять от запаса тек кол-во потребности
                Supplier[supl] -= Consumer[cons]
                # Записать в матрицу маршрута
                ResMatrix[supl][cons] = Consumer[cons]
                # Аннулировать потребность
                Consumer[cons] = 0
                continue
            else:
                ResMatrix[supl][cons] = Supplier[supl]
                Supplier[supl] = 0
                Consumer[cons] = 0

    return ResMatrix


def Solve(Route, CostMatrix):
    sum = 0
    for i in range(len(CostMatrix)):
        for j in range(len(CostMatrix[0])):
            if Route[i][j] == 0:
                continue
            sum += int(Route[i][j]) * int(CostMatrix[i][j])
    return sum


def main():
    CostMatrix = []
    Supplier = []
    Consumer = []
    InitMatrix(CostMatrix, Supplier, Consumer)
    Route = NorthWestMethod(CostMatrix, Supplier, Consumer)
    print(Solve(Route, CostMatrix), "ден. ед.")


if __name__ == "__main__":
    main()
