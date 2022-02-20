import hashlib
import main

class moderate:

	def kick(user):
		# todo

	def ban(user):
		# todo

	def unban(user):
		# todo

	def mute(user):
		# todo

	def unmute(user):
		# todo

class hash:
	
	def sha256(ptr):

		# encode string to hex, decode with .decode(my_str)
		ptr_byte = str.encode(ptr)

		# digest bytes into sha256
		result = hashlib.sha256(b"" + ptr_byte).hexdigest()
		return result
