#!/usr/bin/env python3
"""
拼多多改价器（脚本化 CDP）：对单个商品的 SKU 改拼单价/单买价。
走已登录 Chrome 页面的 __mms.fetch 客户端调 /glide/v2/mms/price/adjust/adjust_in_list（自动带风控签名）。

安全护栏:
  - 改前先读当前价，全程记审计日志（本目录 price_audit.jsonl，含 before/after/commit_id，可回滚）
  - 默认涨跌幅 >30% 拒绝（--max-change-pct 调整，--force 跳过）
  - --dry-run 只打印计划不执行
  - 改后自动复读验证

用法:
  python3 update_price.py --goods <id> --delta +0.13           # 全部SKU 拼/单价同加减(元)
  python3 update_price.py --goods <id> --set 499.13:500.13     # 全部SKU 设为 拼:单(元)
  python3 update_price.py --goods <id> --sku <skuId>:499.13:500.13 [--sku ...]  # 指定SKU
  python3 update_price.py --goods <id> --revert                # 回滚到审计日志里最近一次 before
  附加: [--port 9222] [--execute] [--max-change-pct 30] [--force]
  ⚠️ 默认 DRY-RUN（只出计划不执行）。真实改价必须显式加 --execute（含 --revert）。
输出: 单行 JSON（ok / action）
"""
import sys, os, json, time, datetime
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# 零第三方依赖：HTTP 走标准库；websocket 没装时用随技能分发的纯标准库 _miniws 兜底
try:
    from websocket import create_connection
except ImportError:
    from _miniws import create_connection
# 审计日志放数据目录而非技能目录：技能目录会被打包分发，绝不能混入商户数据
AUDIT = os.path.expanduser(os.environ.get("PDD_AUDIT_PATH",
                                          "~/.pdd-data/price_audit.jsonl"))

def find_pdd_page(port):
    with urllib.request.urlopen(f"http://localhost:{port}/json", timeout=5) as _r:
        tabs = json.loads(_r.read().decode())
    for t in tabs:
        if t.get("type") == "page" and "mms.pinduoduo.com" in t.get("url", ""):
            return t
    return None

class CDP:
    def __init__(self, ws_url):
        self.ws = create_connection(ws_url, max_size=None, timeout=90, suppress_origin=True)
        self.i = 0
    def eval(self, expr):
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": "Runtime.evaluate", "params": {
            "expression": expr, "awaitPromise": True, "returnByValue": True, "userGesture": True}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.i:
                if "error" in msg: raise RuntimeError(msg["error"])
                r = msg["result"]
                if r.get("exceptionDetails"): raise RuntimeError(json.dumps(r["exceptionDetails"])[:300])
                return r["result"].get("value")
    def close(self):
        try: self.ws.close()
        except Exception: pass

def emit(obj, code=0):
    print(json.dumps(obj, ensure_ascii=False)); sys.exit(code)

def read_goods(cdp, goods_id):
    return cdp.eval("""(async () => {
      const r = await window.__mms.fetch.post('/vodka/v2/mms/query/display/mall/goodsList',
        {page:1,size:100,is_onsale:1,sold_out:0,pre_sale_type:4,shipment_time_type:3,out_goods_sn_gray_flag:true});
      const g = (r.goods_list||[]).find(x=>x.id===%d);
      if (!g) return null;
      return {goods_id:g.id, market_price:g.market_price,
        skus:(g.sku_list||[]).map(s=>({sku_id:s.skuId, multi:s.groupPrice, single:s.normalPrice}))};
    })()""" % goods_id)

def fire_adjust(cdp, goods_id, market_price, sku_prices):
    payload = {"goods_id": goods_id,
               "market_price_in_yuan": f"{market_price/100:.2f}", "market_price": market_price,
               "sku_prices": [{"sku_id": s["sku_id"],
                               "multi_price_in_yuan": f"{s['multi']/100:.2f}",
                               "single_price_in_yuan": f"{s['single']/100:.2f}",
                               "multi_price": s["multi"], "single_price": s["single"]} for s in sku_prices],
               "need_delete_goods_commit": True}
    return cdp.eval("""(async () => {
      try { return {ok:true, result: await window.__mms.fetch.post('/glide/v2/mms/price/adjust/adjust_in_list', %s)}; }
      catch(e) { return {ok:false, err:String(e).slice(0,300)}; }
    })()""" % json.dumps(payload)), payload

def main():
    a = sys.argv
    def arg(k, d=None): return a[a.index(k)+1] if k in a else d
    port = int(arg("--port", 9222))
    goods_id = int(arg("--goods", 0))
    max_pct = float(arg("--max-change-pct", 30))
    execute = "--execute" in a
    dry = not execute  # 生产店纪律(2026-10-10)：默认 dry-run，必须显式 --execute
    force, revert = "--force" in a, "--revert" in a
    if not goods_id:
        emit({"ok": False, "reason": "missing --goods",
              "action": {"type": "notify_user", "message": "需要指定商品ID"}}, 2)

    pg = find_pdd_page(port)
    if not pg:
        emit({"ok": False, "reason": "no_pdd_page",
              "action": {"type": "notify_user", "message": "请在已登录 Chrome 打开 mms.pinduoduo.com 商品列表后重试"}}, 2)
    cdp = CDP(pg["webSocketDebuggerUrl"])
    try:
        cur = read_goods(cdp, goods_id)
        if not cur:
            emit({"ok": False, "reason": "goods_not_found",
                  "action": {"type": "notify_user", "message": f"在售列表未找到商品 {goods_id}"}}, 2)

        # 计算目标价
        targets = []
        if revert:
            last = None
            if os.path.exists(AUDIT):
                for line in open(AUDIT):
                    try:
                        j = json.loads(line)
                        if j.get("goods_id") == goods_id and j.get("applied"): last = j
                    except Exception: pass
            if not last:
                emit({"ok": False, "reason": "no_audit_to_revert",
                      "action": {"type": "notify_user", "message": "审计日志里没有该商品可回滚的记录"}}, 2)
            targets = last["before"]["skus"]
        elif arg("--delta"):
            d_fen = round(float(arg("--delta")) * 100)
            targets = [{"sku_id": s["sku_id"], "multi": s["multi"] + d_fen, "single": s["single"] + d_fen}
                       for s in cur["skus"]]
        elif arg("--set"):
            m, s_ = arg("--set").split(":")
            targets = [{"sku_id": s["sku_id"], "multi": round(float(m)*100), "single": round(float(s_)*100)}
                       for s in cur["skus"]]
        elif "--sku" in a:
            spec = {}
            for i, t in enumerate(a):
                if t == "--sku":
                    sid, m, s_ = a[i+1].split(":")
                    spec[int(sid)] = (round(float(m)*100), round(float(s_)*100))
            targets = [{"sku_id": s["sku_id"],
                        "multi": spec.get(s["sku_id"], (s["multi"], s["single"]))[0],
                        "single": spec.get(s["sku_id"], (s["multi"], s["single"]))[1]}
                       for s in cur["skus"]]
        else:
            emit({"ok": False, "reason": "no_price_args",
                  "action": {"type": "notify_user", "message": "需要 --delta / --set / --sku / --revert 之一"}}, 2)

        # 护栏：涨跌幅
        if not force:
            for s, t in zip(cur["skus"], targets):
                for k in ("multi", "single"):
                    if s[k] and abs(t[k] - s[k]) / s[k] * 100 > max_pct:
                        emit({"ok": False, "reason": "change_exceeds_limit",
                              "detail": f"sku {s['sku_id']} {k} {s[k]}→{t[k]} 超过 {max_pct}%",
                              "action": {"type": "notify_user",
                                         "message": f"改价幅度超过护栏({max_pct}%)，如确认请人工复核后用 --force"}}, 3)
                    if t[k] <= 0:
                        emit({"ok": False, "reason": "invalid_price", "detail": f"sku {s['sku_id']} {k}={t[k]}"}, 3)

        plan = {"goods_id": goods_id, "before": cur,
                "after_target": targets, "mode": "revert" if revert else "change"}
        if dry:
            emit({"ok": True, "dry_run": True, **plan,
                  "action": {"type": "notify_user",
                             "message": "以上是改价计划（未执行）。请店主确认后，加 --execute 参数执行。"}})

        res, payload = fire_adjust(cdp, goods_id, cur["market_price"], targets)
        applied = bool(res and res.get("ok"))
        commit_id = res.get("result", {}).get("goods_commit_id") if applied else None

        # 改价走 commit 流，生效有 3~15s 传播延迟：轮询验证最多 20s
        after, verified = None, False
        for _ in range(7):
            time.sleep(3)
            after = read_goods(cdp, goods_id)
            verified = bool(after) and all(
                t["multi"] == s["multi"] and t["single"] == s["single"]
                for t, s in zip(targets, after["skus"]))
            if verified:
                break

        with open(AUDIT, "a") as f:
            f.write(json.dumps({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                "goods_id": goods_id, "mode": plan["mode"], "before": cur,
                                "target": targets, "applied": applied, "commit_id": commit_id,
                                "verified": verified}, ensure_ascii=False) + "\n")

        if not applied:
            emit({"ok": False, "reason": "adjust_failed", "detail": res.get("err") if res else None,
                  "action": {"type": "retry", "message": "改价接口调用失败，可重试；连续失败则刷新页面/检查登录"}}, 1)
        emit({"ok": True, "goods_id": goods_id, "mode": plan["mode"], "commit_id": commit_id,
              "verified": verified,
              "note": None if verified else "提交成功但3秒内未见生效，改价走commit流可能稍有延迟，稍后可用 --dry-run 复读确认",
              "after": after})
    finally:
        cdp.close()

if __name__ == "__main__":
    main()
