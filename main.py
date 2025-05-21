from quart import Quart, request, redirect
import config


app = Quart("Dexmon VPN App Link")


@app.get(config.PATH)
async def index():
    if "Mac" in request.user_agent.string:
        url = config.MAC_URL
    elif "Windows" in request.user_agent.string:
        url = config.WINDOWS_URL
    elif "iPhone" in request.user_agent.string:
        url = config.IOS_URL
    elif "Android" in request.user_agent.string:
        url = config.ANDROID_URL
    else:
        url = config.OTHER_URL
    return redirect(url)


app.run("127.0.0.1", config.PORT)
