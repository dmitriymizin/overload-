

class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

residential_building = Building(5, 'жилое здание')
workshop = Building(2, 'промышленное здание')
res_build_frunze15 = Building(9, 'жилое здание')
rez_build_frunze17 = Building(9, 'жилое здание')
print(residential_building == workshop)
print(res_build_frunze15 == rez_build_frunze17)




