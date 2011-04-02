====
mgrt
====

Overview
========

``mgrt`` is a small and dumb (just like the name!) migration library for any python apps, with some baked-in niceties for django (which can safely be ignored).

``mgrt`` doesn't know anything about how databases work, in fact it can  be used to migrate data that isn't in a database at all, though a small handful of convenience methods are provided for executing SQL over any PEP-249 compliant connection.

The flip side of this is, naturally, that you will have to handle a great deal of logic in your migration on your own. Embrace it! Data migration is either trivial enough that writing the raw SQL for it is no problem at all, or really quite complicated in which case any automated tooling will either make a great mess of things or, at best, not really be of any help. 

Raw SQL?? What if I want to switch from sqlite to Oracle??
----------------------------------------------------------

Then you have *quite* a migration task up your hands and you need ``mgrt`` more then ever!


Installation
============


Usage
=====


Django Niceties
===============

