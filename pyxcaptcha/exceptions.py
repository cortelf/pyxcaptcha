class ServerBadCodeResponseException(Exception):
    def __init__(self, code):
        self.code = code
        self.message = f"Web server return bad code: {self.code}"
        super().__init__(self.message)


class ServerProcessingException(Exception):
    def __init__(self, message="Server processing error"):
        self.message = message
        super().__init__(self.message)


class InvalidAPIKeyException(ServerProcessingException):
    def __init__(self, message="Invalid or incorrect API key."):
        self.message = message
        super().__init__(self.message)


class ZeroBalanceException(ServerProcessingException):
    def __init__(self, message="There is not enough money in your account."):
        self.message = message
        super().__init__(self.message)


class InvalidCaptchaParamsException(ServerProcessingException):
    def __init__(self, message="No google key or pageurl specified."):
        self.message = message
        super().__init__(self.message)


class NoWorkersException(ServerProcessingException):
    def __init__(self, message="There are no workers on the server at the moment."):
        self.message = message
        super().__init__(self.message)


class NotEnoughWorkersException(ServerProcessingException):
    def __init__(self, message="There are not enough workers, the decision of captcha goes in order of turn, "
                               "make a request a little later."):
        self.message = message
        super().__init__(self.message)


class ServerPreventionException(ServerProcessingException):
    def __init__(self, message="The server is on prevention."):
        self.message = message
        super().__init__(self.message)


class CaptchaNotReadyException(ServerProcessingException):
    def __init__(self, message="Captcha is still being decided or in line."):
        self.message = message
        super().__init__(self.message)


class WorkerMistakeException(ServerProcessingException):
    def __init__(self, message="When solving the captcha, the employee made a mistake, the funds were returned."):
        self.message = message
        super().__init__(self.message)


class WorkerTimeoutException(ServerProcessingException):
    def __init__(self, message="During the allotted time, the captcha was not solved, the funds were returned."):
        self.message = message
        super().__init__(self.message)


class WrongCaptchaIDException(ServerProcessingException):
    def __init__(self, message="Captcha with the specified ID is not found or the ID is not correct."):
        self.message = message
        super().__init__(self.message)