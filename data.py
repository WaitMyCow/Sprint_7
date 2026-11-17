
class Codes:
    SUCCESS_CODE = 200
    CREATED_CODE = 201
    INSUFFICIENT_DATA_CODE = 400
    NOT_FOUND_CODE = 404
    LOGIN_ALREADY_TAKEN_CODE = 409

class JsonResponses:
    INSUFFICIENT_DATA_CREATE_RESPONSE = 'Недостаточно данных для создания учетной записи'
    INSUFFICIENT_DATA_LOGIN_RESPONSE = 'Недостаточно данных для входа'
    NOT_FOUND_RESPONSE = 'Учетная запись не найдена'
    LOGIN_ALREADY_TAKEN_RESPONSE = 'Этот логин уже используется. Попробуйте другой.'