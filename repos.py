class SQLRepository(object):
	def __init__(self, connection):
		self.connection = connection
		self.cursor = connection.cursor()