import address_book

"""
    Test cases for address_book programm
"""


def main():
    book = address_book.AddressBook()

    john_record = address_book.Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = address_book.Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, records in book.data.items():
        print(records)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    john.find_phone("5555555555")

    book.delete("Jane")

    for name, records in book.data.items():
        print(records)


if __name__ == "__main__":
    main()