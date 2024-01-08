from Assignment4 import db_access

films = db_access.list_of_all_films()
stores = db_access.list_of_all_stores()

customers = db_access.list_all_customers()

template = "{:>5} {:15} {:15} {:45}"
template2 = "{:>5} {:15} {:15} {:45} {:5}"
row = template.format("ID", "Last Name", "First Name", "Address")
row2 = template2.format("ID", "Last Name", "First Name", "Address", "# Rentals")


print("*** Customer Report ***")
print(row)
for customer in customers:
    customer_id = customer['customer_id']
    fName = customer['first_name']
    lName = customer['last_name']
    addr = customer['address']
    row = template.format(customer_id, lName, fName, addr)
    print(row)

print("\n\n*** Customer Rental Report ***")
print(row2)
for customer in customers:
    customer_id = customer['customer_id']
    fName = customer['first_name']
    lName = customer['last_name']
    addr = customer['address']
    row2 = template2.format(customer_id, lName, fName, addr, db_access.get_num_customer_rentals(customer_id)[0]['cnt'])
    print(row2)