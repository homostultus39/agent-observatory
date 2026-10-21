class DomainError(Exception):
    pass

class PermissionDeniedError(DomainError):
    pass

class AlreadyExistsError(DomainError):
    pass

class NotFoundError(DomainError):
    pass

class ThreadError(DomainError):
    pass

class ThreadAlreadyClosed(ThreadError):
    pass