import math


def is_simple(value):
    result = True
    if value == 1:
        result = False
    else:
        result = True
        for i in range(2, round(math.sqrt(value)) + 1):
            if value % i == 0:
                result = False

    return result


intSet = {0, 1, 4, 8, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
          101, 103, 107,
          109, 113}
simpleSet = set()
otherSet = set()
for i in intSet:
    if not is_simple(i):
        otherSet.add(i)
    else:
        simpleSet.add(i)

print("Множество простых чисел: ", simpleSet)
print("Множество других чисел: ", otherSet)

GermanyCar = {"Mercedes", "BMW", "Porsche", "Opel"}

RussiaImports = {"BMW", "Mercedes"}
UAImports = {"BMW", "Mercedes", "Honda"}
USAImports = {"Dodge", "Camaro", "KIA", "BMW"}

CarImports = [RussiaImports, UAImports, USAImports]

for carName in GermanyCar:
    importCount = 0
    for carImport in CarImports:
        if carName in carImport:
            importCount += 1
    if importCount == 0:
        print("Марка ", carName, "не была доставленна не в одну страну")
    elif importCount == len(CarImports):
        print("Марка ", carName, "была доставленна во все страны")
    else:
        print("Марка ", carName, "была доставленна в некотрые страны")
