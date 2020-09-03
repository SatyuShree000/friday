"""COMMAND : .lovestory"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="lovestory"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lovestory":

    await event.edit("Starting asf")

    animation_chars = [

            "Your Request was registered",
            "Trying to download the movie.......📥",    
            "Download Started\n(●○○○○○○○○○○)10%",    
            "Download Started\n(●●○○○○○○○○○)20%",    
            "Download Started\n(●●●○○○○○○○○)30%",    
            "Download Started\n(●●●●○○○○○○○)40%",    
            "Download Started\n(●●●●●○○○○○○)50%",    
            "Download Started\n(●●●●●●○○○○○)60%",    
            "Download Started\n(●●●●●●●○○○○)70%",    
            "Download Started\n(●●●●●●●●○○○)80%",    
            "Download Started\n(●●●●●●●●●○○)90%",    
            "Download Started\n(●●●●●●●●●●○)100%",
            "Trying to upload to telegram.....📤",
            "Upload Started\n[",
            "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
            "  😘   😊 \n /👕\/👗\ \n   👖   /|",
            " 😳  😁 \n /|\ /👙\ \n /     / |",    
            "😈    /😰\ \n<|\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
            "The End 😂..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])

