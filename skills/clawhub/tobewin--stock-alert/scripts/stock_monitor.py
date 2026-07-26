import urllib.request
import json
import os
import sys

CONFIG_FILE = os.path.expanduser("~/.stock_alert_config.json")
SINA_API = "https://hq.sinajs.cn/list={codes}"

def normalize_code(code):
    code = code.strip().upper()
    if code.startswith(("SH", "SZ", "HK", "US")):
        return code.lower()
    if code.isdigit():
        if len(code) == 6:
            return f"sh{code}" if code.startswith("6") else f"sz{code}"
        if len(code) == 5:
            return f"hk{code}"
    if code.isalpha():
        return f"us{code}"
    return code.lower()

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return []
    with open(CONFIG_FILE) as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def parse_stock(text):
    lines = text.strip().split("\n")
    results = []
    for line in lines:
        if not line.startswith("var hq_str_"):
            continue
        code = line.split("var hq_str_")[1].split("=")[0]
        body = line.split('"')[1]
        if not body or not body.strip():
            continue
        parts = body.split(",")
        market = code[:2]
        if market in ("sh", "sz"):
            name = parts[0]
            prev_close = float(parts[2])
            current = float(parts[3])
        elif market == "hk":
            name = parts[1]
            prev_close = float(parts[2])
            current = float(parts[6])
        elif market == "us":
            name = parts[0]
            prev_close = float(parts[1]) if parts[1] else 0
            current = float(parts[2]) if parts[2] else 0
        else:
            continue
        change = current - prev_close
        change_pct = (change / prev_close * 100) if prev_close else 0
        results.append({"code": code, "name": name, "current": current, "change": round(change, 2), "change_pct": round(change_pct, 2)})
    return results

def check_alerts():
    config = load_config()
    if not config:
        return {"status": "no_config", "message": "No monitoring config found. Use 'add' command first."}
    codes = [normalize_code(item["code"]) for item in config]
    url = SINA_API.format(codes=",".join(codes))
    req = urllib.request.Request(url, headers={"Referer": "https://finance.sina.com.cn"})
    resp = urllib.request.urlopen(req, timeout=10)
    text = resp.read().decode("gbk")
    prices = parse_stock(text)
    price_map = {p["code"]: p for p in prices}
    alerts = []
    for item in config:
        c = normalize_code(item["code"])
        price = price_map.get(c)
        if not price:
            continue
        cur = price["current"]
        cp = price["change_pct"]
        triggered = []
        if item.get("price_high") is not None and cur >= item["price_high"]:
            triggered.append(f"Price {cur} >= threshold {item['price_high']}")
        if item.get("price_low") is not None and cur <= item["price_low"]:
            triggered.append(f"Price {cur} <= threshold {item['price_low']}")
        if item.get("change_pct") is not None and abs(cp) >= item["change_pct"]:
            triggered.append(f"Change {cp}% >= threshold {item['change_pct']}%")
        if triggered:
            alerts.append({"code": c, "name": price["name"], "current": cur, "change_pct": cp, "triggers": triggered})
    return {"status": "ok", "monitored": len(config), "alerts": alerts, "prices": prices}

if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "check"
    if action == "add":
        item = {"code": sys.argv[2], "name": sys.argv[3] if len(sys.argv) > 3 else ""}
        if len(sys.argv) > 4:
            item["price_high"] = float(sys.argv[4]) if sys.argv[4] else None
        if len(sys.argv) > 5:
            item["price_low"] = float(sys.argv[5]) if sys.argv[5] else None
        if len(sys.argv) > 6:
            item["change_pct"] = float(sys.argv[6]) if sys.argv[6] else None
        config = load_config()
        config.append(item)
        save_config(config)
        print(f"Added {item['code']} to monitoring.")
    elif action == "list":
        config = load_config()
        print(json.dumps(config, ensure_ascii=False, indent=2))
    elif action == "remove":
        code = normalize_code(sys.argv[2])
        config = load_config()
        config = [c for c in config if normalize_code(c["code"]) != code]
        save_config(config)
        print(f"Removed {code} from monitoring.")
    elif action == "check":
        result = check_alerts()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Usage: python stock_monitor.py <add|remove|list|check> [params...]")
