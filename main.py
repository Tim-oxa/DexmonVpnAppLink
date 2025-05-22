from quart import Quart, request, redirect
import os


app = Quart("Dexmon VPN App Link")


@app.get(os.getenv("PATH"))
async def index():
    if "Mac" in request.user_agent.string:
        url = os.getenv("MAC_URL")
    elif "Windows" in request.user_agent.string:
        url = os.getenv("WINDOWS_URL")
    elif "iPhone" in request.user_agent.string:
        url = os.getenv("IOS_URL")
    elif "Android" in request.user_agent.string:
        url = os.getenv("ANDROID_URL")
    else:
        url = os.getenv("OTHER_URL")
    return redirect(url)


app.run("0.0.0.0", int(os.getenv("PORT")))
