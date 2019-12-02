import unittest
from datetime import datetime, timedelta
from carRental import CarRental, Customer


class CarRentalTest(unittest.TestCase):

    def test_Car_Rental_diplays_correct_stock(self):

        shop1 = CarRental()
        shop2 = CarRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)
        
    def test_rentCarOnHourlyBasis_for_negative_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnHourlyBasis(-1), None)

    def test_rentCarOnHourlyBasis_for_zero_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnHourlyBasis(0), None)

    def test_rentCarOnHourlyBasis_for_valid_positive_number_of_cars(self):
        shop = CarRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentCarOnHourlyBasis(2).hour, hour)

    def test_rentCarOnHourlyBasis_for_invalid_positive_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnHourlyBasis(11), None)



    def test_rentCarOnDailyBasis_for_negative_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnDailyBasis(-1), None)

    def test_rentCarOnDailyBasis_for_zero_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnDailyBasis(0), None)

    def test_rentCarOnDailyBasis_for_valid_positive_number_of_cars(self):
        shop = CarRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentCarOnDailyBasis(2).hour, hour)

    def test_rentCarOnDailyBasis_for_invalid_positive_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnDailyBasis(11), None)
     


    def test_rentCarOnWeeklyBasis_for_negative_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnWeeklyBasis(-1), None)

    def test_rentCarOnWeeklyBasis_for_zero_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnWeeklyBasis(0), None)

    def test_rentCarOnWeeklyBasis_for_valid_positive_number_of_cars(self):
        shop = CarRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentCarOnWeeklyBasis(2).hour, hour)

    def test_rentCarOnWeeklyBasis_for_invalid_positive_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnWeeklyBasis(11), None)

    
    def test_returnCar_for_invalid_rentalTime(self):
        # create a shop and a customer
        shop = CarRental(10)
        customer = Customer()

        # let the customer not rent a car a try to return one.
        request = customer.returnCar()
        self.assertIsNone(shop.returnCar(request))

        # manually check return function with error values
        self.assertIsNone(shop.returnCar((0,0,0)))
        
    def test_returnCar_for_invalid_rentalBasis(self):
        # create a shop and a customer
        shop = CarRental(10)
        customer = Customer()
        
        # create valid rentalTime and cars
        customer.rentalTime = datetime.now()
        customer.cars = 3

        # create invalid rentalbasis
        customer.rentalBasis = 7

        request = customer.returnCar()
        self.assertEqual(shop.returnCar(request), 0)

    def test_returnCar_for_invalid_numOfCars(self):
     
        # create a shop and a customer
        shop = CarRental(10)
        customer = Customer()
        
        # create valid rentalTime and rentalBasis
        customer.rentalTime = datetime.now()
        customer.rentalBasis = 1

        # create invalid cars
        customer.cars = 0

        request = customer.returnCar()
        self.assertIsNone(shop.returnCar(request))


    def test_returnCar_for_valid_credentials(self):
     
        # create a shop and a various customers
        shop = CarRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()
        
        # create valid rentalBasis for each customer
        customer1.rentalBasis = 1 # hourly
        customer2.rentalBasis = 1 # hourly
        customer3.rentalBasis = 2 # daily
        customer4.rentalBasis = 2 # daily
        customer5.rentalBasis = 3 # weekly
        customer6.rentalBasis = 3 # weekly

        # create valid bikes for each customer
        customer1.cars = 1
        customer2.cars = 5 # eligible for family discount 30%
        customer3.cars = 2
        customer4.cars = 8 
        customer5.cars = 15
        customer6.cars = 30

        # create past valid rental times for each customer
        
        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer2.rentalTime = datetime.now() + timedelta(hours=-23)
        customer3.rentalTime = datetime.now() + timedelta(days=-4)
        customer4.rentalTime = datetime.now() + timedelta(days=-13)
        customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
        customer6.rentalTime = datetime.now() + timedelta(weeks=-12)

        # make all customers return their bikes
        request1 = customer1.returnCar()
        request2 = customer2.returnCar()
        request3 = customer3.returnCar()
        request4 = customer4.returnCar()
        request5 = customer5.returnCar()
        request6 = customer6.returnCar()

        # check if all of them get correct bill
        self.assertEqual(shop.returnCar(request1), 20)
        self.assertEqual(shop.returnCar(request2), 402.5)
        self.assertEqual(shop.returnCar(request3), 160)
        self.assertEqual(shop.returnCar(request4), 2080)
        self.assertEqual(shop.returnCar(request5), 5400)
        self.assertEqual(shop.returnCar(request6), 21600)


class CustomerTest(unittest.TestCase):
    
    def test_return_Car_with_valid_input(self):
        # create a customer
        customer = Customer()
        
        # create valid rentalTime, rentalBasis, bikes
        now = datetime.now()
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.cars= 4

        self.assertEqual(customer.returnCar(),(now,1, 4))


    def test_return_Car_with_invalid_input(self):
        # create a customer
        customer = Customer()
        
        # create valid rentalBasis and Car
               
        customer.rentalBasis = 1
        customer.cars = 0

        # create invalid rentalTime
        customer.rentalTime =  0
        self.assertEqual(customer.returnCar(),(0,0,0))

if __name__ == '__main__':
    unittest.main()
