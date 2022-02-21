import hashlib

class moderate:

	def kick(user):
		# todo
		return

	def ban(user):
		# todo
		return

	def unban(user):
		# todo
		return

	def mute(user):
		# todo
		return

	def unmute(user):
		# todo
		return

class hash:
	
	def sha256(ptr):

		# encode string to hex, decode with .decode(my_str)
		ptr_byte = str.encode(ptr)

		# digest bytes into sha256
		result = hashlib.sha256(b"" + ptr_byte).hexdigest()
		return result
