from farmspersistence.farmdatabase import FarmDatabase

farms = {
    "farms": [
        {
            "_id": "0",
            "name": "Grace Farms",
            "type": ["Vegetables"]
        },
        {
            "_id": "1",
            "name": "Mary Farms",
            "type": ["meatProducts"]
        },
        {
            "_id": "2",
            "name": "Jerry Farms",
            "type": ["Vegetables", "Meat", "Meat Products"]
        }
    ]
}

crops = {
    "crops": [
        {
            "_id": "0",
            "produce": [
                {
                    "name": "onion",
                    "price": "k2",  ## price per kg
                    "priceType": "kg",
                    "available": True
                },
                {
                    "name": "potatoes",
                    "price": "k2",
                    "priceType": "kg",
                    "available": True
                }
            ]
        },
        {
            "_id": "1",
            "produce": [
                {
                    "name": "milk",
                    "price": "k10",
                    "priceType": "quantity",
                    "available": True
                },
                {
                    "name": "cheese",
                    "price": "k10",
                    "priceType": "quantity",
                    "available": True
                },
            ]

        },
        {
            "_id": "2",
            "produce": [
                {
                    "name": "Pork",
                    "price": "k10",
                    "priceType": "kg",
                    "available": True
                },
                {
                    "name": "Beef",
                    "price": "k10",
                    "priceType": "kg",
                    "available": True
                },
            ]
        }
    ]
}


class FakeFarmDB(FarmDatabase):
    def __init__(self):
        self.db = None

    def get_farm(self, farm_id):
        result = None
        result=farms["farms"][farm_id]

        return result

    def get_farm_crops(self, farm_id):
        result = None
        result = crops["crops"][farm_id]
        return result

    def connect_db(self):
        self.db = farms

    def get_all_farms(self):
        return farms["farms"]
