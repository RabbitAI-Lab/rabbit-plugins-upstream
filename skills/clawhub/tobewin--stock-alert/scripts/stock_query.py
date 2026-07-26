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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python stock_query.py <code1> [code2] ..."}))
        sys.exit(1)
    codes = [normalize_code(c) for c in sys.argv[1:]]
    url = SINA_API.format(codes=",".join(codes))
    req = urllib.request.Request(url, headers={"Referer": "https://finance.sina.com.cn"})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        data = resp.read().decode("gbk")
        results = parse_stock(data)
        print(json.dumps(results, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
