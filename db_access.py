from Assignment4.db import do_command

def list_of_all_stores():
    return do_command("select * from store")

def list_of_all_films():
    return do_command("select * from film order by title")

def list_of_all_inventory():
    return do_command("select * from inventory")

def inventory_for_film(film_id):
    return do_command("select * from inventory where film_id = ?", [film_id])

def inventory_for_film_from_store(film_id, store_id):
    return do_command("select * from inventory where film_id = ? and store_id = ?", [film_id, store_id])

def list_all_customers():
    return do_command("select customer.customer_id, customer.first_name, customer.last_name, address.address "
                      "from customer "
                      "left join address "
                      "on customer.address_id = address.address_id")

def get_num_customer_rentals(customer_id):
    return do_command("select count(all) as cnt from rental where customer_id = ?", [customer_id])

def count_rentals_for_film(film_id):
    invent = inventory_for_film(film_id)
    rentals = 0
    for inv in invent:
        rnt = do_command("select count(all) as cnt from rental where inventory_id = ?", [inv['inventory_id']])
        rentals += rnt[0]['cnt']
    return rentals