from carRental import CarRental, Customer

def main():
    shop = CarRental(100)
    customer = Customer()

    while True:
        print("""
        ====== Car Rental Shop =======
        1. Display available cars
        2. Request a car on hourly basis $5
        3. Request a car on daily basis $20
        4. Request a car on weekly basis $60
        5. Return a car
        6. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.displaystock()
        
        elif choice == 2:
            customer.rentalTime = shop.rentCarOnHourlyBasis(customer.requestCar())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.rentCarOnDailyBasis(customer.requestCar())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rentCarOnWeeklyBasis(customer.requestCar())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnCar(customer.returnCar())
            customer.rentalBasis, customer.rentalTime, customer.cars = 0,0,0        
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the car rental system.")


if __name__=="__main__":
    main()
