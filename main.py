# external library
import discord
import hashlib
import json

# local library
import author
import command

prefix = "!"

# legend for console: 
# ">" info
# "#" error

class bot(discord.Client):

	async def on_ready(self):
		print("> logged on as {}".format(self.user))
		print("> self.user.id = {}".format(self.user.id))

	async def on_message(self, message):

		# ignore bots messages
		if author.check_author_role(message) == True:
			return

		# verify users automatically
		if message.channel.id == 910195064951697429 and len(message.content) == 64:
			await author.verify_author(message)

		# reply only when message starts with the prefix
		if message.content[0] == prefix:

			# lets split the message into arrays
			# TODO: concatenate all strings after hash selection, into a single string
			argv = message.content.split()

			# string[array][index : end_index]
			cmd = argv[0][1:]

			if cmd == "hash":

				try:
					check_error = argv[1] in globals()
				except:
					await message.channel.send("Specify which hash algorithm to use:\nex. `... sha256 your_string`")
					print("# error '{0.content}': something went wrong".format(message))
					return
				else:

					try:
						check_error = argv[2] in globals()
					except:
						await message.channel.send("Specify the string to hash:\nex. `... your_string`")
						print("# error '{0.content}': something went wrong".format(message))
						return

				if argv[1] == "sha256":

					print("> message from {0.author} from {0.channel.id}: {0.content}".format(message))

					buffer = command.hash.sha256(argv[2])
					await message.channel.send("sha256 {}".format(buffer))
		else:
			return


# initial client runtime
client = bot()

# grab file from directory tree
auth = open("auth.json")
data = json.load(auth)

# populate string with token
client.run(data["token"])