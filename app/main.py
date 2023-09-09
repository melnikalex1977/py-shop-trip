import math
import datetime
from app.car import CustomerCar
from app.shop import Shop
from app.customer import customers_and_content


def shop_trip() -> str:
    customers, content, shops, priсe_fuel = customers_and_content()
    for name_customer in customers:
        customer_instance = CustomerCar(name_customer)
        customer_inf = customer_instance.customer_location()
        fuel_consumption_car = customer_inf["fuel_consumption_car"]
        distance_customer_x = customer_inf["distance_customer_x"]
        distance_customer_y = customer_inf["distance_customer_y"]
        quantities = customer_inf["quantities"]
        money = customer_inf["money"]
        product = customer_inf["product"]
        name = customer_inf["name"]
        total_price_list = []
        for element in shops:
            shop_instance = Shop(element)
            shop_inf = shop_instance.shop_location()
            name_shop = shop_inf["name_shop"]
            distance_location_shop_x = shop_inf["distance_location_shop_x"]
            distance_location_shop_y = shop_inf["distance_location_shop_y"]
            product = shop_inf["product"]
            distance = (
                math.sqrt((distance_customer_x
                           - distance_location_shop_x) ** 2
                          + (distance_customer_y
                             - distance_location_shop_y) ** 2)
            )
            priсe_distance = (
                (distance * 2 / 100)
                * fuel_consumption_car
                * priсe_fuel
            )
            distance_priсe = round(priсe_distance, 2)
            total_price = (
                sum(product[items]
                    * quantities.get(items, 0)
                    for items in product)
                + float(distance_priсe)
            )
            print(
                f"{name}'s trip to the "
                f"{name_shop} costs "
                f"{total_price}"
            )
            total_price_list.append(total_price)
            total_price_list.sort()
            total_price_min = total_price_list[0]
            if total_price <= total_price_min:
                total = total_price
                name_cust_min = name_shop
                products_list = product
                total_price_dol = total_price - distance_priсe

        if money >= total:
            print(f"{name} rides to {name_cust_min}\n")
            datetime_form = datetime.datetime.now()
            datetime_print = datetime_form.strftime("%d/%m/%Y %X")
            print(f"Date: {datetime_print}")
            print(
                f"Thanks, {name}, "
                f"for your purchase!\n"
                f"You have bought: "
            )
            for items in product:
                print(
                    f"{quantities[items]} {items}s "
                    f"for {int(products_list[items] * quantities[items])} "
                    f"dollars"
                )
            print(
                f"Total cost is {round(total_price_dol, 2)} dollars\n"
                f"See you again!\n\n"
                f"{name} rides home\n"
                f"{name} now has {money - total} dollars\n"
            )
        else:
            print(
                (f"{name} doesn't have "
                 f"enough money to make a purchase in any shop")
            )
