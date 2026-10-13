#!/usr/bin/env python3
"""
pdd-sync-shop 入口：采集店铺在售商品 → 写入本地/企业数据存储。只提数，不出报表
（报表是 pdd-shop-report 技能的职责）。支持多店铺（店群模式）。

用法: python3 run.py [--port 9222] [--shop <店名>] [--all] [--shutdown]
  无参数    ：默认单店模式（9222 端口第一个已登录页，兼容旧行为）
  --shop X  ：按注册表寻址店铺 X（别名/mall_id 均可），实例不在则按需拉起
  --all     ：循环采集注册表全部店铺（店间 8s 间隔，单店失败不影响其余店）
  --shutdown：按需拉起的实例采集完优雅关闭（复用中的存量实例不动）

店铺登记（一次性）：python3 chrome_manager.py add <店名> [--label 显示名]
存储: 默认 SQLite（零部署，~/.pdd-data/pdd.db，PDD_DB_PATH 可改）；
      设置 PDD_CH_URL 时写 ClickHouse（企业模式）。所有表按 mall_id 隔离多店。
输出: 单行 JSON。失败含 action 字段（notify_user/retry），agent 按它处理。
"""
import sys, os, json, subprocess, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import store  # noqa: E402

INTER_SHOP_SLEEP = 8  # --all 模式店间间隔（秒）——不同账号身份，礼貌缓冲即可


def sync_one(port=None, shop=None):
    """采一个店并落库。返回 (ok, result_dict)。"""
    catalog = catalog_path()
    cmd = [sys.executable, os.path.join(HERE, "cdp_collect.py"), "--out", catalog]
    if port:
        cmd += ["--port", str(port)]
    if shop:
        cmd += ["--shop", shop, "--shutdown"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        col = json.loads(p.stdout.strip())
    except Exception:
        col = {"ok": False, "reason": "collect_bad_output", "raw": (p.stdout or p.stderr)[-200:]}
    if not col.get("ok"):
        return False, col

    doc = json.load(open(catalog))  # 固定路径覆盖写，用完不删（避免沙箱把 unlink 判成删除弹权限）
    doc["collected_at"] = col.get("collected_at")
    try:
        store.ensure_schema()
        res = store.insert_snapshot(doc)
        res["daily_days"] = store.insert_shop_daily(col["mall_id"], doc.get("day_list"))
        res["commit_events"] = store.insert_commit_events(col["mall_id"], doc.get("commit_list"))
    except Exception as e:
        det = str(e)
        # 沙箱写拦截分型：Agent 沙箱把数据目录的 unlink/rename 判为"删除"拦下时，
        # SQLite 会报 disk I/O error / readonly——给出明确出路而非让用户看到技术报错
        sandbox = any(k in det for k in ("disk I/O error", "readonly", "read-only",
                                         "Permission denied", "unable to open database file"))
        return False, {"ok": False, "stage": "store",
                       "reason": "sandbox_write_blocked" if sandbox else "store_failed",
                       "detail": det[:200],
                       "action": ({"type": "notify_user",
                                   "message": "数据目录被当前运行环境保护，写入被拦。"
                                              "两条出路：① 在终端直接运行本技能；"
                                              "② 设 PDD_DB_PATH 和 PDD_HEALTH_PATH 指到当前工作区后重试。"}
                                  if sandbox else
                                  {"type": "retry",
                                   "message": "数据写入失败。本地模式请检查磁盘；企业模式请检查 PDD_CH_URL 可达后重试"})}
    out = {"ok": True, "mall_id": col["mall_id"], "shop": shop,
           "collected": col["collected"], "collected_at": col["collected_at"],
           "daily_days": res.get("daily_days"), "commit_events": res.get("commit_events"),
           "pass_id_hours": col.get("pass_id_hours"), "health": col.get("health", {})}
    if col.get("action"):  # 登录保鲜预警等采集层提醒
        out["action"] = col["action"]
    backfill_mall_id(shop, col["mall_id"])
    return True, out


def catalog_path():
    """固定路径 + 每次覆盖写（写完不删）：临时文件 unlink 会被 Agent 沙箱判成
    "删除文件"弹权限。同一进程内串行复用，覆盖即失效，无残留风险。"""
    return os.path.join(tempfile.gettempdir(), f"pdd_catalog_{os.getpid()}.json")


def backfill_mall_id(shop_name, mall_id):
    """注册表里该店还没记 mall_id 的话，首次采集后回填。"""
    if not shop_name or not mall_id:
        return
    try:
        import chrome_manager as CM
        shops = CM.load_shops()
        for s in shops:
            if s["name"] == shop_name and not s.get("mall_id"):
                s["mall_id"] = int(mall_id)
                CM.save_shops(shops)
                return
    except Exception:
        pass  # 回填失败不影响主流程


def main():
    a = sys.argv
    do_all = "--all" in a
    shop = a[a.index("--shop") + 1] if "--shop" in a else None
    port = a[a.index("--port") + 1] if "--port" in a else None

    if do_all:
        import chrome_manager as CM
        shops = CM.load_shops()
        if not shops:
            print(json.dumps({"ok": False, "reason": "no_shops_registered",
                              "action": {"type": "notify_user",
                                         "message": "还没有登记任何店铺。先运行登记：python3 chrome_manager.py add <店名>，每店登录一次即可。"}},
                             ensure_ascii=False)); sys.exit(1)
        results, fails = [], 0
        for i, s in enumerate(shops):
            if i:
                time.sleep(INTER_SHOP_SLEEP)
            ok, r = sync_one(shop=s["name"])
            r.pop("stored", None)  # 汇总里瘦身
            results.append({k: r.get(k) for k in ("ok", "shop", "mall_id", "collected",
                                                  "daily_days", "pass_id_hours", "reason", "kind", "action")})
            if not ok:
                fails += 1
        out = {"ok": fails == 0, "mode": "all", "shops": len(shops), "failed": fails,
               "results": results, "usage": store.usage_stats()}
        expiring = [f"{r['shop']}（约{r['pass_id_hours']:.0f}小时后）" for r in results
                    if r.get("ok") and r.get("pass_id_hours") is not None and r["pass_id_hours"] < 24]
        note = out["usage"].pop("scale_note", None)
        if fails or expiring:
            msg = []
            if fails:
                msg.append(f"{fails}/{len(shops)} 家店铺本次未采成（多为登录过期），其余已入库。")
            if expiring:
                msg.append("登录凭证 24 小时内到期的店铺：" + "、".join(expiring) + "——请到期前重登一次，避免下次采集中断。")
            out["action"] = {"type": "notify_user", "message": " ".join(msg)}
        elif note:
            out["action"] = {"type": "notify_user", "message": note}
        print(json.dumps(out, ensure_ascii=False))
        sys.exit(0 if fails == 0 else 1)

    # 单店模式（默认兼容旧行为 / --shop 寻址）
    ok, out = sync_one(port=port, shop=shop)
    if not ok:
        print(json.dumps({"ok": False, "stage": out.get("stage", "collect"),
                          "reason": out.get("reason"),
                          "action": out.get("action") or {
                              "type": "notify_user",
                              "message": "采集失败：请确认 Chrome 已登录拼多多商家后台"}},
                         ensure_ascii=False))
        sys.exit(1)
    usage = out.pop("usage", None) or store.usage_stats()
    note = usage.pop("scale_note", None)
    if note:
        out["action"] = {"type": "notify_user", "message": note}
    out["usage"] = usage
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
