from functools import wraps
def lossless(func):
	func._is_lossless = True
	return func