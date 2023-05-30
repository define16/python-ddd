from abc import ABC


class ValidationNotificationHandler(ABC):
    def handle_error(self, message: str):
        raise Exception(message)

    def handle_warped(self):
        raise NotImplementedError


class Validator:
    __validation_notification_handler: ValidationNotificationHandler

    def __init__(self, validation_notification_handler: ValidationNotificationHandler):
        self.set_validation_notification_handler(validation_notification_handler)

    def validate(self):
        raise NotImplementedError

    def set_validation_notification_handler(self, validation_notification_handler: ValidationNotificationHandler):
        self.__validation_notification_handler = validation_notification_handler
