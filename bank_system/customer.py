class Customer:
    def __init__(self, name, address=None, phone_number=None):
        self.__customer_id = str(id(self))  # Using memory address as the customer ID
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        print(f"Name updated for customer {self.__customer_id}.")

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
        print(f"Address updated for customer {self.__customer_id}.")

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
        print(f"Phone number updated for customer {self.__customer_id}.")

    def get_customer_info(self):
        """Get customer information."""
        return {
            'customer_id': self.__customer_id,
            'name': self.__name,
            'address': self.__address,
            'phone_number': self.__phone_number
        }

    def __str__(self):
        """String representation of the customer."""
        return (f"Customer ID: {self.__customer_id}, Name: {self.__name}, "
                f"Address: {self.__address}, Phone Number: {self.__phone_number}")
