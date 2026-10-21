from enum import StrEnum


class UserType(StrEnum):
    HUMAN = "HUMAN"
    AGENT = "AGENT"

class UserRole(StrEnum):
    PARTICIPANT = "PARTICIPANT"
    ADMIN = "ADMIN"