import urllib.request
import json
import sys

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
            open_p = float(parts[1])
            prev_close = float(parts[2])
            current = float(parts[3])
            high = float(parts[4])
            low = float(parts[5])
        elif market == "hk":
            name = parts[1]
            prev_close = float(parts[2])
            open_p = float(parts[3])
            high = float(parts[4])
            low = float(parts[5])
            current = float(parts[6])
        elif market == "us":
            name = parts[0]
            prev_close = float(parts[1]) if parts[1] else 0
            current = float(parts[2]) if parts[2] else 0
            high = float(parts[3]) if parts[3] else 0
            low = float(parts[4]) if parts[4] else 0
            open_p = float(parts[5]) if parts[5] else 0
        else:
            continue
        change = current - prev_close
        change_pct = (change / prev_close * 100) if prev_close else 0
        results.append({
            "code": code,
            "name": name,
            "open": open_p,
            "prev_close": prev_close,
            "current": current,
            "high": high,
            "low": low,
            "change": round(change, 2),
            "change_pct": round(change_pct, 2)
        })
    return results

def analyze(prices):
    if not prices:
        return {"error": "No data"}
    for p in prices:
        rng = p["high"] - p["low"]
        if rng > 0:
            p["range_position"] = round((p["current"] - p["low"]) / rng * 100, 1)
        else:
            p["range_position"] = 50.0
        p["gap"] = round(p["current"] - p["open"], 2)
        p["gap_pct"] = round((p["gap"] / p["open"] * 100) if p["open"] else 0, 2)
        p["volatility"] = round(rng / p["prev_close"] * 100 if p["prev_close"] else 0, 2)
    total = len(prices)
    up = sum(1 for p in prices if p["change"] > 0)
    down = sum(1 for p in prices if p["change"] < 0)
    flat = total - up - down
    sorted_p = sorted(prices, key=lambda x: x["change_pct"])
    worst = sorted_p[0] if sorted_p else None
    best = sorted_p[-1] if sorted_p else None
    most_volatile = max(prices, key=lambda x: x["volatility"])
    extremes = [p for p in prices if p["range_position"] >= 90 or p["range_position"] <= 10]
    return {
        "stocks": prices,
        "summary": {"total": total, "up": up, "down": down, "flat": flat},
        "best": {"code": best["code"], "name": best["name"], "change_pct": best["change_pct"]} if best else None,
        "worst": {"code": worst["code"], "name": worst["name"], "change_pct": worst["change_pct"]} if worst else None,
        "most_volatile": {"code": most_volatile["code"], "name": most_volatile["name"], "volatility": most_volatile["volatility"]},
        "near_extremes": [{"code": p["code"], "name": p["name"], "range_position": p["range_position"]} for p in extremes]
    }

if __name__ == "__main__":
    codes = sys.argv[1:] if len(sys.argv) > 1 else []
    if not codes:
        print(json.dumps({"error": "Usage: python stock_analysis.py <code1> [code2] ..."}))
        sys.exit(1)
    codes = [normalize_code(c) for c in codes]
    url = SINA_API.format(codes=",".join(codes))
    req = urllib.request.Request(url, headers={"Referer": "https://finance.sina.com.cn"})
    resp = urllib.request.urlopen(req, timeout=10)
    text = resp.read().decode("gbk")
    prices = parse_stock(text)
    result = analyze(prices)
    print(json.dumps(result, ensure_ascii=False, indent=2))
