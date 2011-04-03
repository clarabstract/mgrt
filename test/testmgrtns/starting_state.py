from . import repositories

initialzes = repositories.defaultdb

@lossless
def do():
    if file.exists(outftfile):
        etc
    repositories.defaultdb.sql("""
    CREATE DATABASE `foo`;
    CREATE TABLE `foodata`;
    """)

def undo():
    repositories.defaultdb.sql("""
    DROP DATASE `foo`;
    """)

def lossless_undo():
    repositories.defaultdb.sql("SELET INTO OUTFILE ...")
    undo()
