from enum import Enum


class RequestType(Enum):
    batch_message = 1
    single_message = 2
    routes = 3
    login = 4