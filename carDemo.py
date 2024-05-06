from car import Car

myHybrid = Car(50)
myHybrid.addGasLevel(20)
myHybrid.drive(100)
print(f"The gas level is {myHybrid.getGasLevel()}")