from enum import IntEnum, unique


class BaseIntEnum(IntEnum):

	@classmethod
	def choices(cls):
		return tuple((key.value, key.name) for key in cls)
      
@unique
class QuestionTypes(BaseIntEnum):
    mcq = 1
    descriptive = 2

@unique
class UserTypes(BaseIntEnum):
    admin = 1
    student = 2
    parent = 3