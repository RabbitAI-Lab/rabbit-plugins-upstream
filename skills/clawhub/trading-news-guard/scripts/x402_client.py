import json, os, sys, urllib.request, urllib.error
BASE = os.environ.get("X402_BASE", "http://186.240.156.169:8791")
KEY = os.environ.get("X402_API_KEY", "")
def call(endpoint, params=None, method="GET"):
    if not KEY:
        print("❌ Sæt X402_API_KEY (https://github.com/MohamedAbdisamed/x402-api)"); sys.exit(1)
    url = BASE + endpoint
    if params: url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {KEY}"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP {e.code}: {e.read().decode()[:200]}"); sys.exit(1)
