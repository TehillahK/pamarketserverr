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
                    "_id": 0,
                    "name": "onion",
                    "price": "k2",  ## price per kg
                    "priceType": "kg",
                    "available": True
                },
                {
                    "_id":1,
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
                    "_id":0,
                    "name": "milk",
                    "price": "k10",
                    "priceType": "quantity",
                    "available": True
                },
                {
                    "_id":1,
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
                    "_id": 0,
                    "name": "Pork",
                    "price": "k10",
                    "priceType": "kg",
                    "available": True
                },
                {
                    "_id":1,
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
        result = crops["crops"][int(farm_id)]
        return result

    def connect_db(self):
        self.db = farms

    def get_all_farms(self):
        return farms["farms"]
