import discord
import command

def check_author_role(message):

	# we dont want the bot to reply to other bots
	# lets grab the roles from both ends and check them later
	role_boteration = discord.utils.get(message.guild.roles, name="Boteration")
	role_member = discord.utils.get(message.author.roles, name="Boteration")

	if role_boteration == role_member:
		return True
	else:
		return False

async def verify_author(message):

	# encode string to hex
	digest_msg = command.hash.sha256(message.author)
	
	if digest_msg == message.content:

		# grab the role id
		role_obj = discord.utils.get(message.guild.roles, name = "verfied")

		# verify user
		await message.author.add_roles(role_obj)

		# TODO: add ping to channel "self-roles"
		print("> verified user: {}".format(message.author))
	else:
		await message.reply("wrong", mention_author = True)