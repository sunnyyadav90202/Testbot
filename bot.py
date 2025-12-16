import os
import requests
from pyrogram import Client, filters

API_ID = int(os.getenv("21629245"))
API_HASH = os.getenv("21678b79dd7741264131705ca6563e59")
BOT_TOKEN = os.getenv("7959412624:AAErK_sglNT94I-S13DYJbtBO0zCpIWZooA")

app = Client(
    "insta_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply(
        "Send any Instagram Reel/Post link.\n\nI will download it for you."
    )

@app.on_message(filters.text & filters.private)
async def download(_, msg):
    url = msg.text.strip()

    if "instagram.com" not in url:
        await msg.reply("Please send a valid Instagram link.")
        return

    await msg.reply("Downloading... Please wait.")

    try:
        api_url = f"https://your-api-endpoint.example/?url={url}"
        r = requests.get(api_url, timeout=20)
        data = r.json()

        video_url = data["medias"][0]["url"]

        await msg.reply_video(
            video=video_url,
            caption="Downloaded successfully"
        )

    except Exception as e:
        await msg.reply("Failed to download. Try another link.")

app.run()
