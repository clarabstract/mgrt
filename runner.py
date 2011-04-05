import pkgutil
import topsort

class Repos(object):
	pass

class MigrationList(object):
	def __init__(self):
		self.migrations = {}
	
	def register(self, migration):
		self.migrations[migration.name] = migration
	
	def sorted(self):
		pairlist = []
		for migration in self.migrations.values():
			for req in migration.requirements:
				pairlist.append((self.migrations[req], migration))
		return topsort.topsort(pairlist)
	

class Migration(object):
	def __init__(self, module):
		self.module  = module
		self.name = module.__name__.split('.')[-1]
		reqs = getattr(module, 'requires', [])
		if not hasattr(reqs, '__iter__'):
			reqs = [reqs]
		self.requirements = reqs
	
	def __repr__(self):
		return "<%s %s>" % (self.__class__.__name__, self.name)

def run(module):
	repositories = Repos()
	migrations = MigrationList()
	for name, repo in getattr(module, 'REPOSITORIES', {}).iteritems():
		setattr(repositories, name, repo)
	for importer, name, ispkg in pkgutil.iter_modules(module.__path__, module.__name__+"."):
		migration_module  = importer.find_module(name, module.__path__).load_module(name)
		migration = Migration(migration_module)
		migrations.register(migration)
	
	print migrations.sorted()



from test import testmgrtns
run(testmgrtns)

