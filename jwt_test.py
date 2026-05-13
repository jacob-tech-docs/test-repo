import time
import jwt
import requests

CLIENT_ID = "3MVG9JJwBBbcN47Ll95pgu1a4yv7wymkG9pH95ETyu1YSmp.PU.ZxGTZSpeFhR.NG5i0VJSc8dzY.RVf6LXNJ"
USERNAME = "novatech.integration@cpqadmin.org"
LOGIN_URL = "https://login.salesforce.com"

with open("server.key", "r") as key_file:
    private_key = key_file.read()

payload = {
    "iss": CLIENT_ID,
    "sub": USERNAME,
    "aud": LOGIN_URL,
    "exp": int(time.time()) + 300
}

assertion = jwt.encode(payload, private_key, algorithm="RS256")

response = requests.post(
    f"{LOGIN_URL}/services/oauth2/token",
    data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": assertion
    }
)

print(response.status_code)
print(response.json())
