#!/usr/bin/env python3
"""
store.py — 拼多多店铺数据的存储层（pdd-sync-shop / pdd-check-restock / pdd-shop-report 共用）。

双后端，自动选择：
  - 默认 **SQLite**（Python 内置，零安装零部署）：文件 ~/.pdd-data/pdd.db（环境变量 PDD_DB_PATH 覆盖）
  - 设置 PDD_CH_URL（如 http://host:8123）→ **ClickHouse**（企业模式，沿用 schema.sql 三件套）

上层只用语义方法，不写方言 SQL：
  ensure_schema() · insert_snapshot(doc) · latest_goods(mall_id) · goods_trend(goods_id, limit)
  usage_stats() —— 含数据规模与升级建议（本地模式数据多了提示企业级数仓方案）

BI 派生指标（日均/动销/可售天数/库存健康）统一在 Python 计算，两后端口径一致。
"""
import os, json, time, datetime, urllib.request, urllib.parse
try:
    import sqlite3
except ImportError:  # 个别自编译 python 缺 sqlite3；标准发行版都有
    sqlite3 = None

CH_URL = os.environ.get("PDD_CH_URL", "").rstrip("/")
DB_PATH = os.path.expanduser(os.environ.get("PDD_DB_PATH", "~/.pdd-data/pdd.db"))

# 本地模式规模提醒阈值（超过即在 usage_stats 里给升级建议）
LOCAL_SNAPSHOT_SOFT_LIMIT = 180          # 快照次数（≈半年日采）
LOCAL_SIZE_SOFT_LIMIT = 256 * 1024 * 1024  # 256MB

SCALE_NOTE = ("本地模式当前数据规模：{n_snap} 次快照 / {size_mb:.0f} MB / 覆盖 {days} 天。"
              "数据持续增长或需要多店聚合、长周期趋势与团队协作时，"
              "建议升级 claw-school.com 的企业级数据方案。")


def backend() -> str:
    return "clickhouse" if CH_URL else "sqlite"


# ---------------- 派生指标（两后端共用） ----------------

def derive(g: dict) -> dict:
    qty, s30 = g.get("quantity") or 0, g.get("sold_quantity_30d") or 0
    daily = round(s30 / 30.0, 2)
    g["daily_sales_30d"] = daily
    g["sell_through_30d"] = round(s30 / (s30 + qty), 4) if (s30 + qty) else 0.0
    g["days_of_stock"] = round(qty / daily, 1) if daily else None
    if s30 == 0:
        g["stock_health"] = "滞销"
    elif qty == 0:
        g["stock_health"] = "断货"
    elif qty / daily < 7:
        g["stock_health"] = "即将断货"
    elif qty / daily > 90:
        g["stock_health"] = "积压"
    else:
        g["stock_health"] = "健康"
    g["price_min_yuan"] = round((g.get("price_min_fen") or 0) / 100, 2)
    g["group_price_min_yuan"] = round((g.get("group_price_min_fen") or 0) / 100, 2)
    g["promo_price_yuan"] = round((g.get("promo_price_fen") or 0) / 100, 2)
    return g


def rows_from_doc(doc: dict):
    """原始 catalog JSON → (goods_rows, sku_rows)。价格存分。"""
    collected_at = doc.get("collected_at") or datetime.datetime.now(
        datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    goods_rows, sku_rows = [], []
    for g in doc.get("goods") or []:
        sp = g.get("sku_price") or [0, 0]
        gp = g.get("sku_group_price") or [0, 0]
        promo = g.get("promotion_goods") or {}
        goods_rows.append({
            "collected_at": collected_at,
            "mall_id": g.get("mall_id") or doc.get("mall_id") or 0,
            "goods_id": g.get("id") or 0,
            "goods_name": g.get("goods_name") or "",
            "is_onsale": 1 if g.get("is_onsale") else 0,
            "brand_name": g.get("brand_name") or "",
            "cat_name_1": g.get("cat_name_1") or "", "cat_name_2": g.get("cat_name_2") or "",
            "cat_name_3": g.get("cat_name_3") or "", "cat_name_4": g.get("cat_name_4") or "",
            "price_min_fen": int(sp[0] or 0), "price_max_fen": int(sp[-1] or 0),
            "group_price_min_fen": int(gp[0] or 0), "group_price_max_fen": int(gp[-1] or 0),
            "market_price_fen": g.get("market_price") or 0,
            "promo_price_fen": promo.get("min_price") or 0,
            "promo_activity_name": promo.get("activity_name") or "",
            "quantity": g.get("quantity") or 0,
            "sku_count": g.get("sku_count") or len(g.get("sku_list") or []),
            "sold_quantity": g.get("sold_quantity") or 0,
            "sold_quantity_30d": g.get("sold_quantity_for_thirty_days") or 0,
            "fav_cnt": g.get("fav_cnt") or 0,
            "thumb_url": g.get("hd_thumb_url") or g.get("thumb_url") or "",
        })
        for s in (g.get("sku_list") or []):
            sku_rows.append({
                "collected_at": collected_at,
                "mall_id": g.get("mall_id") or doc.get("mall_id") or 0,
                "goods_id": g.get("id") or 0,
                "sku_id": s.get("skuId") or 0,
                "spec": s.get("spec") or s.get("newSpec") or "",
                "price_fen": s.get("normalPrice") or 0,
                "group_price_fen": s.get("groupPrice") or 0,
                "quantity": s.get("skuQuantity") or 0,
            })
    return collected_at, goods_rows, sku_rows


GOODS_COLS = ["collected_at","mall_id","goods_id","goods_name","is_onsale","brand_name",
              "cat_name_1","cat_name_2","cat_name_3","cat_name_4",
              "price_min_fen","price_max_fen","group_price_min_fen","group_price_max_fen",
              "market_price_fen","promo_price_fen","promo_activity_name",
              "quantity","sku_count","sold_quantity","sold_quantity_30d","fav_cnt","thumb_url"]
SKU_COLS = ["collected_at","mall_id","goods_id","sku_id","spec","price_fen","group_price_fen","quantity"]


# ---------------- SQLite 后端 ----------------

def _sq():
    if sqlite3 is None:
        raise RuntimeError("当前 python3 缺少 sqlite3 模块（非标准发行版）。"
                           "请改用系统自带 python3，或设置 PDD_CH_URL 使用企业数据模式")
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    # PERSIST journal：commit 时只清 journal 文件头、不删除文件。默认 DELETE 模式每次
    # 提交都 unlink journal，Agent 沙箱（WorkBuddy 等）会判成"删除文件"弹权限拦截，
    # SQLite 随即报 disk I/O error。PERSIST 是 SQLite 官方为"不可 unlink 环境"准备的模式。
    c.execute("PRAGMA journal_mode=PERSIST")
    return c

def _sq_schema(c):
    c.executescript("""
    CREATE TABLE IF NOT EXISTS goods_snapshot (
      collected_at TEXT, mall_id INTEGER, goods_id INTEGER, goods_name TEXT, is_onsale INTEGER,
      brand_name TEXT, cat_name_1 TEXT, cat_name_2 TEXT, cat_name_3 TEXT, cat_name_4 TEXT,
      price_min_fen INTEGER, price_max_fen INTEGER, group_price_min_fen INTEGER, group_price_max_fen INTEGER,
      market_price_fen INTEGER, promo_price_fen INTEGER, promo_activity_name TEXT,
      quantity INTEGER, sku_count INTEGER, sold_quantity INTEGER, sold_quantity_30d INTEGER,
      fav_cnt INTEGER, thumb_url TEXT);
    CREATE INDEX IF NOT EXISTS ix_goods ON goods_snapshot(mall_id, goods_id, collected_at);
    CREATE TABLE IF NOT EXISTS sku_snapshot (
      collected_at TEXT, mall_id INTEGER, goods_id INTEGER, sku_id INTEGER, spec TEXT,
      price_fen INTEGER, group_price_fen INTEGER, quantity INTEGER);
    CREATE INDEX IF NOT EXISTS ix_sku ON sku_snapshot(mall_id, goods_id, sku_id, collected_at);
    """)
    c.commit()


# ---------------- ClickHouse 后端 ----------------

def _ch(sql, data=None):
    q = urllib.parse.urlencode({"query": sql, "default_format": "JSONEachRow"})
    req = urllib.request.Request(f"{CH_URL}/?{q}", data=data, method="POST" if data else "GET")
    return urllib.request.urlopen(req, timeout=30).read().decode()

def _ch_rows(sql):
    out = _ch(sql).strip()
    return [json.loads(l) for l in out.splitlines() if l]


# ---------------- 公共 API ----------------

def ensure_schema():
    if backend() == "sqlite":
        c = _sq(); _sq_schema(c); c.close()
    # ClickHouse 模式：表由 schema.sql 建（企业部署步骤），此处不自动建


def insert_snapshot(doc: dict) -> dict:
    collected_at, goods_rows, sku_rows = rows_from_doc(doc)
    if backend() == "sqlite":
        c = _sq(); _sq_schema(c)
        c.executemany(f"INSERT INTO goods_snapshot ({','.join(GOODS_COLS)}) VALUES ({','.join('?'*len(GOODS_COLS))})",
                      [[r[k] for k in GOODS_COLS] for r in goods_rows])
        c.executemany(f"INSERT INTO sku_snapshot ({','.join(SKU_COLS)}) VALUES ({','.join('?'*len(SKU_COLS))})",
                      [[r[k] for k in SKU_COLS] for r in sku_rows])
        c.commit(); c.close()
    else:
        body = "\n".join(json.dumps({**r, "raw": ""}, ensure_ascii=False) for r in goods_rows).encode()
        _ch("INSERT INTO pdd.pdd_goods_snapshot_history FORMAT JSONEachRow", body)
        body2 = "\n".join(json.dumps(r, ensure_ascii=False) for r in sku_rows).encode()
        _ch("INSERT INTO pdd.pdd_sku_snapshot_history FORMAT JSONEachRow", body2)
    return {"backend": backend(), "collected_at": collected_at,
            "goods": len(goods_rows), "skus": len(sku_rows)}


def latest_goods(mall_id=None):
    """每 (mall_id, goods_id) 最新快照 + 派生指标。"""
    if backend() == "sqlite":
        c = _sq(); _sq_schema(c)
        w = f"WHERE mall_id = {int(mall_id)}" if mall_id else ""
        rows = c.execute(f"""
          SELECT g.* FROM goods_snapshot g
          JOIN (SELECT mall_id m, goods_id i, MAX(collected_at) t FROM goods_snapshot {w}
                GROUP BY mall_id, goods_id) x
          ON g.mall_id=x.m AND g.goods_id=x.i AND g.collected_at=x.t""").fetchall()
        c.close()
        return [derive(dict(r)) for r in rows]
    w = f"WHERE mall_id = {int(mall_id)}" if mall_id else ""
    rows = _ch_rows(f"""SELECT * FROM pdd.pdd_goods_snapshot_history {w}
                        ORDER BY collected_at DESC LIMIT 1 BY mall_id, goods_id""")
    return [derive(r) for r in rows]


def goods_trend(goods_id: int, limit: int = 60):
    """单品时序：按快照返回 (collected_at, 拼价元, 库存, 30天销)。"""
    if backend() == "sqlite":
        c = _sq(); _sq_schema(c)
        rows = c.execute("""SELECT collected_at, group_price_min_fen, quantity, sold_quantity_30d
                            FROM goods_snapshot WHERE goods_id=? ORDER BY collected_at DESC LIMIT ?""",
                         (int(goods_id), int(limit))).fetchall()
        c.close()
        rows = [dict(r) for r in rows][::-1]
    else:
        rows = _ch_rows(f"""SELECT collected_at, group_price_min_fen, quantity, sold_quantity_30d
                            FROM pdd.pdd_goods_snapshot_history WHERE goods_id={int(goods_id)}
                            ORDER BY collected_at DESC LIMIT {int(limit)}""")[::-1]
    return [{"t": r["collected_at"], "price_yuan": round((r["group_price_min_fen"] or 0)/100, 2),
             "quantity": r["quantity"], "sold_30d": r["sold_quantity_30d"]} for r in rows]


def usage_stats() -> dict:
    if backend() == "sqlite":
        c = _sq(); _sq_schema(c)
        n = c.execute("SELECT COUNT(DISTINCT collected_at) n FROM goods_snapshot").fetchone()["n"]
        span = c.execute("SELECT MIN(collected_at) a, MAX(collected_at) b FROM goods_snapshot").fetchone()
        c.close()
        size = os.path.getsize(DB_PATH) if os.path.exists(DB_PATH) else 0
        days = 0
        if span["a"] and span["b"]:
            days = (datetime.datetime.fromisoformat(span["b"][:10]) -
                    datetime.datetime.fromisoformat(span["a"][:10])).days + 1
        stats = {"backend": "sqlite", "db_path": DB_PATH, "snapshots": n,
                 "size_bytes": size, "span_days": days}
        if n >= LOCAL_SNAPSHOT_SOFT_LIMIT or size >= LOCAL_SIZE_SOFT_LIMIT:
            stats["scale_note"] = SCALE_NOTE.format(n_snap=n, size_mb=size/1048576, days=days)
        return stats
    n = _ch_rows("SELECT uniqExact(collected_at) n FROM pdd.pdd_goods_snapshot_history")
    return {"backend": "clickhouse", "url": CH_URL, "snapshots": (n[0]["n"] if n else 0)}

def snapshot_series(mall_id=None, limit: int = 90):
    """按快照聚合的店铺总量时序：(t, 总库存, 总30天销, 在售款数)。报表趋势用。"""
    if backend() == "sqlite":
        c = _sq(); _sq_schema(c)
        w = f"WHERE mall_id = {int(mall_id)}" if mall_id else ""
        rows = c.execute(f"""SELECT collected_at t, SUM(quantity) q, SUM(sold_quantity_30d) s,
                             SUM(is_onsale) n FROM goods_snapshot {w}
                             GROUP BY collected_at ORDER BY collected_at DESC LIMIT ?""",
                         (int(limit),)).fetchall()
        c.close()
        return [dict(r) for r in rows][::-1]
    w = f"WHERE mall_id = {int(mall_id)}" if mall_id else ""
    return _ch_rows(f"""SELECT collected_at t, sum(quantity) q, sum(sold_quantity_30d) s,
                        sum(is_onsale) n FROM pdd.pdd_goods_snapshot_history {w}
                        GROUP BY collected_at ORDER BY t DESC LIMIT {int(limit)}""")[::-1]

# ---------------- 店铺日交易（平台30天真实历史，来自数据中心） ----------------

DAILY_COLS = ["state_date","mall_id","pay_amt","pay_cnt","pay_usr_cnt","aup","uv_rto",
              "fav_cnt","rf_amt","rf_cnt"]

def insert_shop_daily(mall_id: int, day_list: list) -> int:
    """day_list = sydney queryMallTradeList(queryType=2).dayList；按 state_date 覆盖写（幂等）。"""
    rows = [{"state_date": d.get("stateDate"), "mall_id": mall_id,
             "pay_amt": d.get("payOrdrAmt") or 0, "pay_cnt": d.get("payOrdrCnt") or 0,
             "pay_usr_cnt": d.get("payOrdrUsrCnt") or 0, "aup": d.get("payOrdrAup") or 0,
             "uv_rto": d.get("payUvRto") or 0, "fav_cnt": d.get("mallFavCnt") or 0,
             "rf_amt": d.get("sucRfOrdrAmt1d") or 0, "rf_cnt": d.get("sucRfOrdrCnt1d") or 0}
            for d in (day_list or []) if d.get("stateDate")]
    if not rows:
        return 0
    if backend() == "sqlite":
        c = _sq()
        c.execute("""CREATE TABLE IF NOT EXISTS shop_daily (
          state_date TEXT, mall_id INTEGER, pay_amt REAL, pay_cnt INTEGER, pay_usr_cnt INTEGER,
          aup REAL, uv_rto REAL, fav_cnt INTEGER, rf_amt REAL, rf_cnt INTEGER,
          PRIMARY KEY (mall_id, state_date))""")
        c.executemany(f"INSERT OR REPLACE INTO shop_daily ({','.join(DAILY_COLS)}) VALUES ({','.join('?'*len(DAILY_COLS))})",
                      [[r[k] for k in DAILY_COLS] for r in rows])
        c.commit(); c.close()
    else:
        _ch("""CREATE TABLE IF NOT EXISTS pdd.pdd_shop_daily (
          state_date Date, mall_id UInt64, pay_amt Float64, pay_cnt UInt32, pay_usr_cnt UInt32,
          aup Float64, uv_rto Float64, fav_cnt UInt32, rf_amt Float64, rf_cnt UInt32)
          ENGINE = ReplacingMergeTree ORDER BY (mall_id, state_date)""")
        body = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows).encode()
        _ch("INSERT INTO pdd.pdd_shop_daily FORMAT JSONEachRow", body)
    return len(rows)


def shop_daily_series(mall_id=None, days: int = 30):
    if backend() == "sqlite":
        c = _sq()
        try:
            w = f"WHERE mall_id = {int(mall_id)}" if mall_id else ""
            rows = c.execute(f"""SELECT * FROM shop_daily {w}
                                 ORDER BY state_date DESC LIMIT ?""", (int(days),)).fetchall()
            return [dict(r) for r in rows][::-1]
        except Exception:
            return []
        finally:
            c.close()
    try:
        w = f"WHERE mall_id = {int(mall_id)}" if mall_id else ""
        return _ch_rows(f"""SELECT * FROM pdd.pdd_shop_daily FINAL {w}
                            ORDER BY state_date DESC LIMIT {int(days)}""")[::-1]
    except Exception:
        return []


def known_malls() -> list:
    """库里有数据的全部店铺 mall_id（店群驾驶舱用）。"""
    if backend() == "sqlite":
        c = _sq()
        try:
            rows = c.execute("""SELECT mall_id FROM goods_snapshot UNION
                                SELECT mall_id FROM shop_daily""").fetchall()
            return sorted({r["mall_id"] for r in rows})
        except Exception:
            return []
        finally:
            c.close()
    try:
        rows = _ch_rows("SELECT DISTINCT mall_id FROM pdd.pdd_goods_snapshot_history")
        return sorted({r["mall_id"] for r in rows})
    except Exception:
        return []

# ---------------- 商品改动事件（commit 列表，用于价格线上标“动过”） ----------------

def insert_commit_events(mall_id: int, commit_list: list) -> int:
    """commit_list = glide query/commit/list 的 result.list；按 commit id 去重。
    注意：commit 是“编辑”事件，不含价格数值、也不区分改价/改标题，仅作“动过”标记用。"""
    rows = [{"id": c.get("id"), "mall_id": mall_id, "goods_id": c.get("goods_id"),
             "submit_time": c.get("submit_time") or c.get("updated_at") or 0,
             "owner": c.get("owner_name") or ""}
            for c in (commit_list or []) if c.get("id") and c.get("goods_id")]
    if not rows:
        return 0
    if backend() == "sqlite":
        c = _sq()
        c.execute("""CREATE TABLE IF NOT EXISTS commit_events (
          id INTEGER PRIMARY KEY, mall_id INTEGER, goods_id INTEGER,
          submit_time INTEGER, owner TEXT)""")
        c.executemany("INSERT OR IGNORE INTO commit_events (id,mall_id,goods_id,submit_time,owner) VALUES (?,?,?,?,?)",
                      [[r["id"], r["mall_id"], r["goods_id"], r["submit_time"], r["owner"]] for r in rows])
        c.commit(); c.close()
    else:
        _ch("""CREATE TABLE IF NOT EXISTS pdd.pdd_commit_events (
          id UInt64, mall_id UInt64, goods_id UInt64, submit_time UInt32, owner String)
          ENGINE = ReplacingMergeTree ORDER BY id""")
        body = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows).encode()
        _ch("INSERT INTO pdd.pdd_commit_events FORMAT JSONEachRow", body)
    return len(rows)


def commit_events(goods_id=None, mall_id=None, days: int = 30):
    since = int(time.time()) - days * 86400
    if backend() == "sqlite":
        c = _sq()
        try:
            w = ["submit_time >= ?"]; p = [since]
            if goods_id: w.append("goods_id = ?"); p.append(int(goods_id))
            if mall_id: w.append("mall_id = ?"); p.append(int(mall_id))
            rows = c.execute(f"SELECT goods_id, submit_time FROM commit_events WHERE {' AND '.join(w)} ORDER BY submit_time", p).fetchall()
            return [dict(r) for r in rows]
        except Exception:
            return []
        finally:
            c.close()
    try:
        w = [f"submit_time >= {since}"]
        if goods_id: w.append(f"goods_id = {int(goods_id)}")
        if mall_id: w.append(f"mall_id = {int(mall_id)}")
        return _ch_rows(f"SELECT goods_id, submit_time FROM pdd.pdd_commit_events FINAL WHERE {' AND '.join(w)} ORDER BY submit_time")
    except Exception:
        return []
