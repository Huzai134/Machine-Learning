# Mock API data for Pakistan car sales
car_sales = [
    {"brand": "Toyota", "model": "Corolla", "price": 4500000},
    {"brand": "Suzuki", "model": "Alto", "price": 2200000},
    {"brand": "Honda", "model": "Civic", "price": 8500000},
    {"brand": "Suzuki", "model": "Cultus", "price": 3800000},
    {"brand": "KIA", "model": "Sportage", "price": 7300000}
]

budget_cars = [car["model"] for car in car_sales if car["price"] < 4000000]

print (budget_cars)