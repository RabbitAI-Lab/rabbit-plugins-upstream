#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""深圳全市预售证/项目全量采集器（基本盘，2026-08-19）

真实列表 API: POST /ysf/publicity/getYsfYsPublicity?cuyGLa6e=TOKEN
请求体: {"pageIndex":N,"pageSize":200,"total":0,"zone":""}
响应: data.total / data.list[] (id,sypId,sypeId,zone,strpreprojectid,project,name,siteaddress,passdate)
字段映射: ysProjectId=sypId, preSellId=sypeId, presell_no=strpreprojectid,
          project=项目名, organ=开发企业, zone=区, siteaddress=地址, passdate=发证日期

策略：全量翻页（无过滤），增量落盘 + 断点续跑（每页覆盖写 JSON）。
"""
import asyncio
import json
import os
from pathlib import Path

BASE = "https://fdc.zjj.sz.gov.cn/szfdcscjy"
OUT_DIR = Path(__file__).parent / "output_cross" / "shenzhen_data"
OUT_JSON = OUT_DIR / "shenzhen_presell_all.json"


async def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    from playwright.async_api import async_playwright
    tok = {"v": None}
    all_rows = []

    # 断点续跑：已有落盘则加载
    if OUT_JSON.exists():
        try:
            old = json.loads(OUT_JSON.read_text(encoding="utf-8"))
            all_rows = old.get("presells", [])
            print(f"[INFO] 断点恢复: 已有 {len(all_rows)} 条")
        except Exception:
            all_rows = []

    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True)
        ctx = await b.new_context(
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36"))
        pg = await ctx.new_page()

        def on_req(r):
            if "cuyGLa6e=" in r.url:
                tok["v"] = r.url.split("cuyGLa6e=")[1].split("&")[0]

        pg.on("request", on_req)
        await pg.goto(f"{BASE}/#/foreignPublic/listApartmentHunting/"
                      f"listApartmentHuntingSj?ysProjectId=35246",
                      wait_until="domcontentloaded", timeout=30000)
        try:
            await pg.wait_for_event(
                "request", lambda r: "cuyGLa6e=" in r.url, timeout=20000)
        except Exception:
            pass
        await pg.wait_for_timeout(2000)
        if not tok["v"]:
            print("[ERR] 未拿到 token")
            await b.close()
            return

        api = f"{BASE}/ysf/publicity/getYsfYsPublicity?cuyGLa6e={tok['v']}"

        # 取第一页拿 total
        first = await pg.evaluate(
            """async(p)=>{const r=await fetch(p.api,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({pageIndex:1,pageSize:200,total:0,zone:''})});return await r.text();}""",
            {"api": api})
        d = json.loads(first)
        total = d.get("data", {}).get("total", 0)
        print(f"[INFO] 深圳全库预售证总数={total}")

        seen_ids = set(r.get("sypeId") for r in all_rows)
        page = 1
        while True:
            resp = await pg.evaluate(
                """async(p)=>{const r=await fetch(p.api,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({pageIndex:p.page,pageSize:200,total:0,zone:''})});return await r.text();}""",
                {"api": api, "page": page})
            dd = json.loads(resp)
            lst = dd.get("data", {}).get("list", []) or []
            if not lst:
                break
            new_cnt = 0
            for it in lst:
                key = it.get("sypeId")
                if key in seen_ids:
                    continue
                seen_ids.add(key)
                all_rows.append(it)
                new_cnt += 1
            print(f"  [页 {page}] 累计 {len(all_rows)} 条 (+{new_cnt})")
            # 每页覆盖写（断点续跑）
            save(all_rows, total)
            if len(all_rows) >= total or len(lst) < 200:
                break
            page += 1
            await pg.wait_for_timeout(300)  # 轻限速
        await b.close()

    save(all_rows, total)
    print(f"\n[结果] 深圳全库 {len(all_rows)} 条（recordCount={total}）")
    # 精简统计
    from collections import Counter
    zones = Counter(r.get("zone") for r in all_rows)
    print("按区:", dict(sorted(zones.items(), key=lambda x: -x[1])))
    devs = Counter(r.get("name") for r in all_rows)
    print("开发商 TOP10:")
    for k, v in devs.most_common(10):
        print(f"  {v:4d}  {k}")
    projs = Counter(r.get("project") for r in all_rows)
    print(f"去重项目数(按项目名): {len(projs)}")
    print("项目 TOP10(证数):")
    for k, v in projs.most_common(10):
        print(f"  {v:4d}  {k}")


def save(rows, total):
    out = {
        "_meta": {
            "city": "深圳",
            "source": "深圳市房地产信息平台 fdc.zjj.sz.gov.cn",
            "api": "POST /ysf/publicity/getYsfYsPublicity (pageSize=200 翻页全量)",
            "captured_at": "2026-08-19",
            "recordCount": total,
            "actual_count": len(rows),
            "note": "深圳全市预售证级全量（基本盘特例，用户批准）；字段=sypId/sypeId/strpreprojectid/project/name/zone/siteaddress/passdate",
        },
        "presells": rows,
    }
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  [SAVE] {len(rows)} 条 -> {OUT_JSON.name} ({os.path.getsize(OUT_JSON)} B)")


if __name__ == "__main__":
    asyncio.run(main())
