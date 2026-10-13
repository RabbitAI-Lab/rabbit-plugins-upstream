#!/usr/bin/env python3
"""
拼多多商品采集器（脚本化 CDP）。连已登录 Chrome，复用页面请求客户端 window.__mms.fetch
（自动带 anti-content 风控签名）拉数据。所有端点经 resilience 健壮层：失败分型 + 退避 +
熔断，接口改版/频率限制时少打慢打早停，绝不重试成风暴。

用法: python3 cdp_collect.py [--port 9222] [--out catalog.json]
输出: {collected, mall_id, collected_at, goods:[...], day_list:[...], commit_list:[...]}
退出码: 0 成功 / 2 没找到已登录 PDD 页 / 3 采集受阻（熔断/改版/频率/登录），stdout 带 action
"""
import sys, os, json, time, datetime
import urllib.request

# 零第三方依赖设计：HTTP 走标准库 urllib；websocket 优先用 websocket-client（装了就用），
# 没装自动落到随技能分发的纯标准库实现 _miniws——"什么都没有"的业务电脑也能跑。
try:
    from websocket import create_connection
except ImportError:
    from _miniws import create_connection  # 纯标准库兜底，接口兼容
try:
    import sqlite3  # noqa: F401
except ImportError:
    sqlite3 = None


def _http_json(url, timeout=5):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read().decode())


def _dep_guard():
    """启动即检。零第三方依赖后唯一可能缺的是 sqlite3（Python 内置，但 pyenv 自编译
    版可能没带）——缺了按操作系统给对修复命令，而不是 ModuleNotFoundError 乱码裸崩。"""
    if sqlite3 is None:
        fix = ("请改用 python.org 官方安装包的 Python（自带 sqlite3）运行，如：py scripts\\run.py"
               if os.name == "nt" else
               "请改用系统自带 Python 运行：/usr/bin/python3 scripts/run.py ...")
        print(json.dumps({
            "ok": False, "reason": "missing_dependency", "missing": ["sqlite3(python内置)"],
            "action": {"type": "notify_user",
                       "message": "当前 Python 缺少内置模块 sqlite3（精简编译版）。" + fix +
                                  "。装好后重试本技能。"}}, ensure_ascii=False))
        sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resilience as R  # noqa: E402
import chrome_manager as CM  # noqa: E402

INTER_CALL_SLEEP = 0.6   # 端点间礼貌间隔（秒）——低频、不猛打


def find_pdd_page(port):
    for t in _http_json(f"http://localhost:{port}/json", timeout=5):
        if t.get("type") == "page" and "mms.pinduoduo.com" in t.get("url", ""):
            return t
    return None


class CDP:
    def __init__(self, ws_url):
        self.ws = create_connection(ws_url, max_size=None, timeout=60, suppress_origin=True)
        self.i = 0
    def raw(self, method, params=None):
        """任意 CDP 命令（如 Network.getCookies，可读 httpOnly）。"""
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.i:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                return msg.get("result", {})
    def eval(self, expr):
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": "Runtime.evaluate", "params": {
            "expression": expr, "awaitPromise": True, "returnByValue": True, "userGesture": True}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.i:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                r = msg["result"]
                if r.get("exceptionDetails"):
                    raise RuntimeError(json.dumps(r["exceptionDetails"])[:300])
                return r["result"].get("value")
    def close(self):
        try: self.ws.close()
        except Exception: pass


def _mms_call(cdp, path, body):
    """在页面内用 __mms.fetch.post 调一个端点，返回原始 mms 响应（dict）。"""
    js = """(async () => {
      if (!(window.__mms && window.__mms.fetch && window.__mms.fetch.post))
        return {__no_client: true};
      try { return await window.__mms.fetch.post(%s, %s); }
      catch(e) {
        // __mms 在业务失败时 reject 的是响应体本身；原样回传给 Python 分型
        if (e && (e.error_code || e.errorCode || e.error_msg)) return e;
        return {__exc: String(e).slice(0,160)};
      }
    })()""" % (json.dumps(path), json.dumps(body))
    resp = cdp.eval(js)
    if isinstance(resp, dict) and resp.get("__no_client"):
        raise RuntimeError("no_mms_client")
    if isinstance(resp, dict) and resp.get("__exc"):
        raise RuntimeError(resp["__exc"])
    return resp


def collect_goods(cdp, shop=None):
    """分页拉全量在售商品，逐页过熔断器（店维度独立）+ 页间礼貌间隔。"""
    all_goods, page, total = [], 1, None
    while page <= 60:
        body = {"page": page, "size": 50, "is_onsale": 1, "sold_out": 0,
                "pre_sale_type": 4, "shipment_time_type": 3, "out_goods_sn_gray_flag": True}
        ok, resp, err = R.run("goodsList", lambda: _mms_call(cdp, "/vodka/v2/mms/query/display/mall/goodsList", body),
                              validate=R.v_nonempty_list("goods_list"), shop=shop)
        if not ok:
            return None, err
        r = resp.get("result") if isinstance(resp.get("result"), dict) else resp
        lst = r.get("goods_list") or []
        all_goods.extend(lst)
        total = r.get("total") or 0
        if len(lst) < 50 or len(all_goods) >= total:
            break
        page += 1
        time.sleep(INTER_CALL_SLEEP)
    return all_goods, None


def pass_id_hours_left(cdp):
    """PASS_ID 剩余寿命（小时）。PDD 登录短票实测 3 天固定到期——提前预警重登。
    PASS_ID 是 httpOnly，页面 JS 读不到，走 CDP Network.getCookies。"""
    try:
        r = cdp.raw("Network.getCookies", {"urls": ["https://mms.pinduoduo.com"]})
        for c in r.get("cookies", []):
            if c.get("name") == "PASS_ID" and c.get("expires", -1) > 0:
                return round((c["expires"] - time.time()) / 3600, 1)
    except Exception:
        pass
    return None


def main():
    _dep_guard()
    port, out, shop_name = 9222, "catalog.json", None
    shutdown_after = "--shutdown" in sys.argv
    a = sys.argv
    if "--port" in a: port = int(a[a.index("--port") + 1])
    if "--out" in a: out = a[a.index("--out") + 1]
    if "--shop" in a: shop_name = a[a.index("--shop") + 1]

    launched = False
    if shop_name:
        shop = CM.find_shop(shop_name)
        if not shop:
            print(json.dumps({"ok": False, "reason": "unknown_shop", "shop": shop_name,
                              "action": {"type": "notify_user",
                                         "message": f"店铺 {shop_name} 未登记。让用户运行登记流程：python3 chrome_manager.py add {shop_name}"}},
                             ensure_ascii=False)); sys.exit(2)
        port = shop["cdp_port"]
        if not CM._has_mms_logged_in(port):
            # 按需拉起该店专属 Chrome（登录态在独立 profile 磁盘里，拉起即恢复）
            try:
                CM.ensure_chrome(shop)
                launched = True
                time.sleep(2)
            except RuntimeError as e:
                print(json.dumps({"ok": False, "reason": str(e), "shop": shop["name"],
                                  "action": {"type": "notify_user",
                                             "message": f"店铺 {shop['name']} 的浏览器启动失败或登录过期，请先登录一次该店铺。"}},
                                 ensure_ascii=False)); sys.exit(2)

    pg = find_pdd_page(port)
    if not pg:
        print(json.dumps({"ok": False, "reason": "no_pdd_page",
                          "action": {"type": "notify_user",
                                     "message": "在已登录的 Chrome 打开 mms.pinduoduo.com 商家后台再重试"}},
                         ensure_ascii=False)); sys.exit(2)

    cdp = CDP(pg["webSocketDebuggerUrl"])
    try:
        cdp.eval("1")  # Runtime 预热
        pid_hours = pass_id_hours_left(cdp)  # 登录保鲜：短票剩多久
        # 1) 商品（主数据，必需）
        goods, err = collect_goods(cdp, shop=shop_name)
        if err:
            print(json.dumps({"ok": False, "stage": "goods", **err}, ensure_ascii=False))
            sys.exit(3)

        # 2) 平台日交易历史（增强，失败不阻塞主采集）
        day_list = []
        time.sleep(INTER_CALL_SLEEP)
        ok, resp, derr = R.run("mallTradeList",
                               lambda: _mms_call(cdp, "/sydney/api/mallTrade/queryMallTradeList",
                                                 {"queryType": 2, "queryDate": datetime.date.today().isoformat()}),
                               validate=R.v_has_keys("dayList"), shop=shop_name)
        if ok:
            _r = resp.get("result") if isinstance(resp.get("result"), dict) else resp
            day_list = _r.get("dayList") or []

        # 3) 商品改动事件（增强，1 次调用，失败不阻塞）
        commit_list = []
        time.sleep(INTER_CALL_SLEEP)
        ok, resp, cerr = R.run("commitList",
                               lambda: _mms_call(cdp, "/glide/v2/mms/query/commit/list",
                                                 {"check_status": 2, "start": 0, "length": 50}),
                               validate=R.v_has_keys("list"), shop=shop_name)
        if ok:
            _r = resp.get("result") if isinstance(resp.get("result"), dict) else resp
            commit_list = _r.get("list") or []
    finally:
        cdp.close()
        if launched and shutdown_after:
            CM.shutdown_chrome(port)  # 优雅关闭（cookie 落盘）；复用的存量实例不动

    res = {"ok": True, "collected": len(goods),
           "mall_id": goods[0]["mall_id"] if goods else None,
           "collected_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
           "goods": goods, "day_list": day_list, "commit_list": commit_list}
    json.dump(res, open(out, "w"), ensure_ascii=False)
    out_line = {"ok": True, "collected": res["collected"], "mall_id": res["mall_id"],
                "collected_at": res["collected_at"], "out": out,
                "daily_days": len(day_list), "commit_events": len(commit_list),
                "pass_id_hours": pid_hours,
                "health": R.health_summary()}
    if pid_hours is not None and pid_hours < 24:
        shop_disp = f"店铺 {shop_name or '当前'} 的"
        out_line["action"] = {
            "type": "notify_user",
            "message": (f"{shop_disp}登录凭证还剩约 {pid_hours:.0f} 小时过期（拼多多登录票固定 3 天）。"
                        "如不确认自动续期，请在到期前重新登录一次该店铺，避免采集中断。")}
    print(json.dumps(out_line, ensure_ascii=False))


if __name__ == "__main__":
    main()
