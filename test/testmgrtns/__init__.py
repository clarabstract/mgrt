from repos import SQLRepository
import sqlite3

REPOSITORIES = {
	'maindb': SQLRepository(sqlite3.connect(':memory:'))
}
