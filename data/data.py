exist_courier = {'login': 'god', 'password': 'password', 'first_name': 'John'}

RESP_LOGIN_COURIER_SUCCESS = {'code': 200, 'body': {"id": "some_id"}}
RESP_LOGIN_COURIER_UNSUCCESS = {'code': 404, 'body': {'code': 404, 'message': 'Учетная запись не найдена'}}
RESP_LOGIN_COURIER_WO_LOGIN = {'code': 400, 'body': {'code': 400, 'message': 'Недостаточно данных для входа'}}
RESP_LOGIN_COURIER_WO_PASSWORD = {'code': 504, 'body': 'Service unavailable'}

RESP_CREATE_COURIER_SUCCESS = {'code': 201, 'body': {"ok": True}}
RESP_CREATE_COURIER_TWICE = {'code': 409, 'body': {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}}
RESP_CREATE_COURIER_UNSUCCESS = {'code': 400, 'body': {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}}