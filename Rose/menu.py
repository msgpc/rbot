from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Rose.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Prime_BotZ"
            ),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/TamilPrime_LinkZz"
            )
        ], 
        [
            InlineKeyboardButton(
                text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/I_m_madhan"
            ),
            InlineKeyboardButton(
                text="ɪɴꜰᴏ", url="https://t.me/Prime_BotZ"
            )
        ], 
        [
            InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data='startcq')
        ]
        ]
)

keyboard =InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="🇱🇷 ᴇɴɢʟɪsʜ", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="🇱🇰 සිංහල", callback_data="languages_si"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            ),
            InlineKeyboardButton(
                text="🇮🇹 ɪᴛᴀʟɪᴀɴᴏ", callback_data="languages_it"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_ta"
            ),
            InlineKeyboardButton(
                text="🇮🇩 ɪɴᴅᴏɴᴇsɪᴀ", callback_data="languages_id"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🇦🇪 عربي", callback_data="languages_ar"
            ),
            InlineKeyboardButton(
                text="🇮🇳 മലയാളം", callback_data="languages_ml"
            ), 
        ],
        [
            InlineKeyboardButton(
                text="🇲🇼 ᴄʜɪᴄʜᴇᴡᴀ", callback_data="languages_ny"
            ), 
            InlineKeyboardButton(
                text="🇩🇪 ɢᴇʀᴍᴀɴ", callback_data="languages_ge"
            ), 
        ], 
        [  
            InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data='startcq')
        ]
    ]
)

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    user = CallbackQuery.message.from_user.mention
    await app.send_message(
        CallbackQuery.message.chat.id,
        text= "The list of available languages:",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()
    
@app.on_callback_query(filters.regex("_about"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=_["menu"],
        reply_markup=fbuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

