exist_courier = {'login': 'login', 'password': 'password', 'first_name': 'first_name'}



RESP_CREATE_COURIER_SUCCESS = {'code': 201, 'content': {"ok": True}}
RESP_CREATE_COURIER_TWICE = {'code': 409, 'content': {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}}
RESP_CREATE_COURIER_UNSUCCESS = {'code': 400, 'content': {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}}