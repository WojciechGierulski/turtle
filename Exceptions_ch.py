
class UnknownCommandError(Exception):
    def __init__(self, message):
        self.message = message
        self.name = 'Command Error'


class UnknownFormatError(Exception):
    def __init__(self, message):
        self.message = message
        self.name = 'Format Error'


class InvalidArgumentError(Exception):
    def __init__(self, message):
        self.message = message
        self.name = 'Argument Error'


class FileDoesNotExistError(Exception):
    def __init__(self, message="Can't find file"):
        self.message = message
        self.name = 'File Error'


class FileOpenError(Exception):
    def __init__(self, message="Can't open file"):
        self.message = message
        self.name = 'File Open Error'
