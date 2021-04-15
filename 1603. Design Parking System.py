class ParkingSystem:
    """
    Design a parking system for a parking lot.
    The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

    Constraints
    0 <= big, medium, small <= 1000
    carType is 1, 2, or 3
    At most 1000 calls will be made to addCar


    Input
    ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    [[1, 1, 0], [1], [2], [3], [1]]
    Output
    [null, true, true, false, false]
    """

    def __init__(self, big: int, medium: int, small: int):
        """
        Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
        """
        # should use a mapping from size:slots

        # simple (faster)
        # use an array of size 4 and just index straight into it on calls to addCar

        self.slots = [0, big, medium, small]

        # more extensible
        # using a dict/map
        # self.slotz = {1:big,2:medium,3:small}

    def addCar(self, carType: int) -> bool:
        """
        Checks whether there is a parking space of carType for the car that wants to get into the parking lot.
        carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
        A car can only park in a parking space of its carType.
        If there is no space available, return false, else park the car in that size space and return true.
        """
        # check then decrement

        if self.slots[carType] != 0:
            self.slots[carType] -= 1
            return True

        return False

        # dict/map
        """
        slots = self.slotz[carType]
        if slots != 0: # we know it's always >= 0
            self.slotz[carType] -=1
            return True
        return False
        """


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)