# #Setup 

# # PROJECT~/mgrtns/__init__.py
# from mgrt.sources import SQLSource, FileSource
# from mgrt.django import SOURCES

# SOURCES += {
#     'sqlitehelper': SQLSource(connection),
#     'rrds': FileSource(settings.RRD_LOCATION),
#     'memcached': MemcachedSource()
# } 

# # Migration file
# source = ('mysql','rrds', 'oracle')
# requires = ('initial')

# def do(options):
#     if options.safe:
#         # etc

# def undo(options):
#     pass


# #initial:
# require = 'empty'

# #ch1
# require = 'initial'

# """
# mysql, rrds -> oracle, netapp

# start with huge mysql data set

# detect empty... do that at the source level

# ok not empty? no marker? -> mark as initial

# empty and no marker? -> initialize

# right - then we make some changes

# now we switch to oracle

# first oracle needs an initial

# then we want to migrate data into it from sql

# require = ('lastsqlch', 'setup_oracles')
# retires = 'mysql'

# yeah ok we're good

# - now what about safety and reversibility

# add a column
# -> good
# <- needs backup

# always going to have destructive actions that have difficult recovery steps

# mgrt --data-recoverable-only (default)

# mgrt --prompt (default)



# """
# # migrate from mysql to oracle
# # start with a huge mysql data
# # -> mark schema and initial data needed for blank 'new deploys' 
