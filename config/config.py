import os
base = "cargosend"
config   = {
            "db":
                {"url": os.getenv('DB_URL', "127.0.0.1:27017"),
                 "user": os.getenv('DB_USER', "test"),
                 "password":  os.getenv('DB_PASSWORD', "test")
                },
            "collections": {
                 "drivers": os.getenv('COL_DRIVERS', "drivers"),
                 "city_cords": os.getenv('COL_CITY', "city"),
                 "geohash": os.getenv('COL_GEOHASH', "geohash"),
                 "werehouse": os.getenv('COL_WERE', "werehouse"),
                 "cargo": os.getenv('COL_CARGO', "cargo"),
                 }
            }