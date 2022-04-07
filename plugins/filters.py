#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import re
import pyrogram

from pyrogram import (
    filters,
    Client
)

from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)

from bot import Bot
from script import script
from database.mdb import searchquery, searchquery_link, searchquery_sub
from plugins.channel import deleteallfilters
from config import AUTH_USERS, SM_ADMIN, WEB_SITE_URL, ADMIN_ALIVE

BUTTONS = {}
 
@Client.on_message(filters.group & filters.text)
async def filter(client: Bot, message: Message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    try:
        otherUserId = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    except:
        otherUserId = message.from_user.id
        first_name = message.from_user.first_name
        
    if 2 < len(message.text) < 50:    
        btn = []
        btnss = "" 
    
        group_id = message.chat.id
        name = message.text
        name = name.replace("-", " ").replace(":", " ").replace(" tg", "")
        try:
            if name.index("sub")>0:
                filenames, links = await searchquery_sub(group_id, name)
                replyText = "Subtitle"

                if filenames and links:
                    for filename, link in zip(filenames, links):
                        btn.append(
                            [InlineKeyboardButton(text=f"{filename}",url=f"{link}")]
                        )
                else:
                    clicked = message.from_user.id
                    if (clicked in AUTH_USERS) or (clicked in SM_ADMIN) or (ADMIN_ALIVE == "no"):
                        return
                    else:
                        try:
                            if message.text.index("http")> 0:
                                return
                        except:
                            try:
                                if message.text.index("chat")> 0:
                                    return
                            except:
                                keybuoard = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("👮‍♂️ Mention Admin", callback_data="i_am_correct"),
                                        InlineKeyboardButton("🗑 Delete this Msg", callback_data="delete_msg")],
                                    [InlineKeyboardButton(text="♻️ Translate above Msg to English",callback_data="i_am_forighn")]
                                ])
                                await message.reply_text(
                                    f"ඔයා හොයන <code>{message.text}</code> නම් දැනට මගෙ DataBase එකේ නෑ.\n🙁 පොඩ්ඩක් Google Search කරල බලන්න ඔයා නම හරියටම දාල තියනවද කියල.\n👽ඔයා නම හරියට දාලත් Film එක ලැබුන් නැත්තම් පහළ Button එකෙන් Admin Mention කරන්න",
                                    reply_markup=keybuoard,
                                    disable_web_page_preview=True
                                )
                                return

                if not btn:
                    return

                if len(btn) > 10: 
                    btns = list(split_list(btn, 10)) 
                    keyword = f"{message.chat.id}-{message.message_id}"
                    BUTTONS[keyword] = {
                        "total" : len(btns),
                        "buttons" : btns
                    }
                else:
                    buttons = btn
                    userTEXT = message.text.replace(" tg", "").replace(" sub", "")
                    buttons.append(
                        [InlineKeyboardButton(text="😎 Pages 1/1",callback_data="pages"),
                            InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")]
                    )
                    await message.reply_text(
                        f"🔗 මෙන්න <a href='tg://user?id={otherUserId}'>{first_name}</a> හොයන <code>{message.text}</code> {replyText} 👇🏾\n\n📌 Join our Channels 👇🏻\n<b>@IruPC_NET ‖ @MoIndex</b>",
                        reply_markup=InlineKeyboardMarkup(buttons)
                    )
                    return

                data = BUTTONS[keyword]
                buttons = data['buttons'][0].copy()

                buttons.append(
                    [InlineKeyboardButton(text="NEXT ➡️",callback_data=f"next_0_{keyword}")]
                )    
                buttons.append(
                    [InlineKeyboardButton(text=f"📚 Pages 1/{data['total']}",callback_data="pages"),
                        InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")]
                )

                await message.reply_text(
                        f"🔗 මෙන්න <a href='tg://user?id={otherUserId}'>{first_name}</a> හොයන <code>{message.text}</code> {replyText} 👇🏾\n\n📌 Join our Channels 👇🏻\n<b>@IruPC_NET ‖ @MoIndex</b>",
                        reply_markup=InlineKeyboardMarkup(buttons)
                    )    
        except:
            filenames, links = await searchquery_link(group_id, name)
            if filenames and links:
                keybuoard = InlineKeyboardMarkup([
                    [InlineKeyboardButton("📥 Download Links 🔗", callback_data=f"dlLinks_bar_{name}"),
                            InlineKeyboardButton("📂 TG Files 📥", callback_data=f"tgFiles_bar_{name}")],
                    [InlineKeyboardButton(text="♻️ Translate above Msg to English",callback_data="i_am_forighn_links")]
                ])
                await message.reply_text(
                    f"🥳<a href='tg://user?id={otherUserId}'>{first_name}</a> හොයන <code>{message.text}</code> මගෙ Data Base එකේ තියනව. 🔗 Download Linksද, 📂TG Filesද ඕනි...\n⭕️පහල Button Click කරන්න 👇\n<b>@IruPC_NET ‖ @MoIndex</b>",
                    reply_markup=keybuoard,
                    disable_web_page_preview=True
                )
                return
            else:
                clicked = message.from_user.id
                if (clicked in AUTH_USERS) or (clicked in SM_ADMIN) or (ADMIN_ALIVE == "no"):
                    return
                else:
                    try:
                        if message.text.index("http")> 0:
                            return
                    except:
                        try:
                            if message.text.index("chat")> 0:
                                return
                        except:
                            keybuoard = InlineKeyboardMarkup([
                                [InlineKeyboardButton("👮‍♂️ Mention Admin", callback_data="i_am_correct"),
                                    InlineKeyboardButton("🗑 Delete this Msg", callback_data="delete_msg")],
                                [InlineKeyboardButton(text="♻️ Translate above Msg to English",callback_data="i_am_forighn")]
                            ])
                            await message.reply_text(
                                f"ඔයා හොයන <code>{message.text}</code> නම් දැනට මගෙ DataBase එකේ නෑ.\n🙁 පොඩ්ඩක් Google Search කරල බලන්න ඔයා නම හරියටම දාල තියනවද කියල.\n👽ඔයා නම හරියට දාලත් Film එක ලැබුන් නැත්තම් පහළ Button එකෙන් Admin Mention කරන්න",
                                reply_markup=keybuoard,
                                disable_web_page_preview=True
                            )
                            return

            
@Client.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    clicked = query.from_user.id
    typed = query.message.reply_to_message.from_user.id
    try:
        specialUser = query.message.entities[0].user.id
    except:
        specialUser = 1697481598
    if (clicked == typed) or (clicked in AUTH_USERS) or (clicked == specialUser):

        if query.data.startswith("next"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword]

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⬅️ BACK", callback_data=f"back_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📚 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                        InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⬅️ BACK", callback_data=f"back_{int(index)+1}_{keyword}"),InlineKeyboardButton("NEXT ➡️", callback_data=f"next_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📚 Pages {int(index)+2}/{data['total']}", callback_data="pages"),
                        InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data.startswith("back"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword] 

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("NEXT ➡️", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📚 Pages {int(index)}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("⬅️ BACK", callback_data=f"back_{int(index)-1}_{keyword}"),InlineKeyboardButton("NEXT ➡️", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📚 Pages {int(index)}/{data['total']}", callback_data="pages"),
                        InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data == "pages":
            await query.answer()


        elif query.data == "delete_msg":
            await query.message.delete()


        elif query.data.startswith("dlLinks"):
            await query.answer()
            keyword = query.data.split("_bar_")[1]
            btn = []
            btnss = "" 
            group_id = query.message.chat.id
            try:
                inputTexT = query.message.text.split("හොයන ")[1].split(" මගෙ")[0]
            except:
                inputTexT = query.message.text.split("🙈")[1].split(" ")[0]
            name = keyword
            try:
                otherUserId = query.message.entities[0].user.id
                first_name = query.message.entities[0].user.first_name
            except:
                otherUserId = query.message.from_user.id
                first_name = query.message.from_user.first_name
            filenames, links = await searchquery_link(group_id, keyword)
            if filenames and links:
                for filename, link in zip(filenames, links):
                    btn.append(
                        [InlineKeyboardButton(text=f"{filename}",url=f"{link}")]
                    )
            else:
                return

            if not btn:
                return

            if len(btn) > 10: 
                btns = list(split_list(btn, 10)) 
                keyword = f"{query.message.chat.id}-{query.message.message_id}"
                BUTTONS[keyword] = {
                    "total" : len(btns),
                    "buttons" : btns
                }
            else:
                buttons = btn
                buttons.append(
                    [InlineKeyboardButton(text="😎 Pages 1/1",callback_data="pages"),
                        InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")],
                )
                await query.message.edit_text(
                    f"🔗 මෙන්න <a href='tg://user?id={otherUserId}'>{first_name}</a> ඉල්ලුව <code>{inputTexT}</code> #Direct_Links 👇\n\n📌 Join our Channels 👇🏻\n<b>@IruPC_NET ‖ @MoIndex</b>",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

            data = BUTTONS[keyword]
            buttons = data['buttons'][0].copy()

            buttons.append(
                [InlineKeyboardButton(text="NEXT ➡️",callback_data=f"next_0_{keyword}")]
            )    
            buttons.append(
                [InlineKeyboardButton(text=f"📚 Pages 1/{data['total']}",callback_data="pages"),
                    InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")],
            )

            await query.message.edit_text(
                    f"🔗 මෙන්න <a href='tg://user?id={otherUserId}'>{first_name}</a> ඉල්ලුව <code>{inputTexT}</code> #Direct_Links 👇\n\n📌 Join our Channels 👇🏻\n<b>@IruPC_NET ‖ @MoIndex</b>",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )


        elif query.data.startswith("tgFiles"):
            await query.answer()
            keyword = query.data.split("_bar_")[1]
            btn = []
            btnss = "" 
            group_id = query.message.chat.id
            name = keyword
            try:
                inputTexT = query.message.text.split("හොයන ")[1].split(" මගෙ")[0]
            except:
                inputTexT = query.message.text.split("🙈")[1].split(" ")[0]
            try:
                otherUserId = query.message.entities[0].user.id
                first_name = query.message.entities[0].user.first_name
            except:
                otherUserId = query.message.from_user.id
                first_name = query.message.from_user.first_name
            filenames, links = await searchquery(group_id, keyword)
            if filenames and links:
                for filename, link in zip(filenames, links):
                    btn.append(
                        [InlineKeyboardButton(text=f"{filename}",url=f"{link}")]
                    )
            else:
                return

            if not btn:
                return

            if len(btn) > 10: 
                btns = list(split_list(btn, 10)) 
                keyword = f"{query.message.chat.id}-{query.message.message_id}"
                BUTTONS[keyword] = {
                    "total" : len(btns),
                    "buttons" : btns
                }
            else:
                buttons = btn
                buttons.append(
                    [InlineKeyboardButton(text="😎 Pages 1/1",callback_data="pages"),
                        InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")],
                )
                await query.message.edit_text(
                    f"🔗 මෙන්න <a href='tg://user?id={otherUserId}'>{first_name}</a> ඉල්ලුව <code>{inputTexT}</code> #TG_Files 👇🏾\n\n📌 Join our Channels 👇🏻\n<b>@IruPC_NET ‖ @MoIndex</b>",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

            data = BUTTONS[keyword]
            buttons = data['buttons'][0].copy()

            buttons.append(
                [InlineKeyboardButton(text="NEXT ➡️",callback_data=f"next_0_{keyword}")]
            )    
            buttons.append(
                [InlineKeyboardButton(text=f"📚 Pages 1/{data['total']}",callback_data="pages"),
                    InlineKeyboardButton("🎬 Join Our Channel", url="https://t.me/irupc_net")],
            )
            await query.message.edit_text(
                    f"🔗 මෙන්න <a href='tg://user?id={otherUserId}'>{first_name}</a> ඉල්ලුව <code>{inputTexT}</code> #TG_Files 👇🏾\n\n📌 Join our Channels 👇🏻\n<b>@IruPC_NET ‖ @MoIndex</b>",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )

        elif query.data == "start_data":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("HELP", callback_data="help_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data")],
                [InlineKeyboardButton("⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/irupc_net")]
            ])

            await query.message.edit_text(
                script.START_MSG.format(query.from_user.mention),
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "help_data":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("BACK", callback_data="start_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data")],
                [InlineKeyboardButton("⭕️ SUPPORT ⭕️", url="https://t.me/irupc_net")]
            ])

            await query.message.edit_text(
                script.HELP_MSG,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "i_am_correct":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("☑️ Done", callback_data="i_done_that"),
                    InlineKeyboardButton("🗑 Delete this Msg", callback_data="delete_msg")]
            ])

            await query.message.edit_text(
                script.ADMIN_MENTION,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "i_am_wrong":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("🇱🇰 Share Our Group", url="https://telegram.me/share/url?url=https://Top_movie_Links"),
                    InlineKeyboardButton("🗑 Delete this Msg", callback_data="delete_msg")]
            ])

            await query.message.edit_text(
                script.USER_INCORRECT,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "i_am_forighn":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("☑️ Done", callback_data="i_done_that"),
                    InlineKeyboardButton("🗑 Delete this Msg", callback_data="delete_msg")]
            ])

            await query.message.edit_text(
                script.FOR_FORIGHN,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "i_am_forighn_links":
            await query.answer()
            try:
                otherUserId = query.message.reply_to_message.from_user.id
                first_name = query.message.reply_to_message.from_user.first_name
            except:
                otherUserId = query.message.from_user.id
                first_name = query.message.from_user.first_name
            try:
                inputTexT = query.message.text.split("හොයන ")[1].split(" මගෙ")[0]
            except:
                inputTexT = query.message.text.split("🙈")[1].split(" ")[0]
            keybuoard = InlineKeyboardMarkup([
                [InlineKeyboardButton("📥 Download Links 🔗", callback_data=f"dlLinks_bar_{inputTexT}"),
                        InlineKeyboardButton("📂 TG Files 📥", callback_data=f"tgFiles_bar_{inputTexT}")]
            ])
            await query.message.edit_text(
                f"🙈{inputTexT} requested by <a href='tg://user?id={otherUserId}'>{first_name}</a> is Available on my Data Base. Do you want 🔗 Download Links or 📂TG Files?\nClick on Following Buttons",
                reply_markup=keybuoard,
                disable_web_page_preview=True
            )


        elif query.data == "about_data":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("BACK", callback_data="help_data"),
                    InlineKeyboardButton("START", callback_data="start_data")],
                [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Auto-Filter-Bot-V2")]
            ])

            await query.message.edit_text(
                script.ABOUT_MSG,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "delallconfirm":
            await query.message.delete()
            await deleteallfilters(client, query.message)
        
        elif query.data == "delallcancel":
            await query.message.reply_to_message.delete()
            await query.message.delete()
    else:
        await query.answer("😂 Thats not for you ❗️\n😂 ඒක ඔයාට දැම්ම Msg එකක් නෙවෙයිනේ❗️\n😉ඔයාට ඒක ඕනි නම් ඔයත් එයා දැම්ම Msg එක Group එකට දාන්න.",show_alert=True)
    if (clicked in AUTH_USERS) or (clicked in SM_ADMIN):
        if query.data == "i_done_that":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("🇱🇰 Share Our Group", url="https://telegram.me/share/url?url=https://Top_movie_Links")]
            ])

            await query.message.edit_text(
                script.TEXT_AFTER_DONE,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )
    else:
        await query.answer("😂 Thats only for Admins ❗️\n😂 ඒක Click කරන්න පුලුවන් Adminට විතරයි\n😉ඔයාට Movie එක ලැබුන නම් Delete Button එක Click කරල ඒ Msg එක Delete කරන්න",show_alert=True)
        

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
