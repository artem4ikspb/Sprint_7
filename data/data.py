exist_courier = {'login': 'courier_wo_orders', 'password': 'password', 'first_name': 'John'}
exist_courier_for_del = {'login': 'courier_for_del', 'password': 'password', 'first_name': 'John'}

exist_courier_w_orders = {'login': 'courier_w_orders', 'password': 'password', 'first_name': 'John'}

orders = [
    {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY"
        ]
    },
    {
        "firstName": "Enakin",
        "lastName": "Skywalker",
        "address": " Galactic Empire, Star Dreadnought 'Executor'",
        "metroStation": 0,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Luke, I am your father!",
        "color": [
            "BLACK"
        ]
    },
    {
        "firstName": "Bart",
        "lastName": "Simpson",
        "address": "Springfield, 80 apt.",
        "metroStation": 0,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2001-06-06",
        "comment": "I hate to do my homework",
        "color": [
            "BLACK", "GREY"
        ]
    }
]


RESP_LOGIN_COURIER_SUCCESS = {'code': 200, 'body': {"id": "some_id"}}
RESP_LOGIN_COURIER_UNSUCCESS = {'code': 404, 'body': {'code': 404, 'message': 'Учетная запись не найдена'}}
RESP_LOGIN_COURIER_WO_LOGIN = {'code': 400, 'body': {'code': 400, 'message': 'Недостаточно данных для входа'}}
RESP_LOGIN_COURIER_WO_PASSWORD = {'code': 504, 'body': 'Service unavailable'}

RESP_CREATE_COURIER_SUCCESS = {'code': 201, 'body': {"ok": True}}
RESP_CREATE_COURIER_TWICE = {'code': 409, 'body': {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}}
RESP_CREATE_COURIER_UNSUCCESS = {'code': 400, 'body': {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}}