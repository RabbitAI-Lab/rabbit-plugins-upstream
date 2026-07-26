# -*- coding: utf-8 -*-
"""
券商研报工具集 — 5个功能
  1. stock_research_summary(code, days=90)  → 个股研报汇总
  2. rating_wind_today()                    → 今日评级变动风向标
  3. eps_consistency(code, days=180)        → EPS一致性预期
  4. broker_ranking(days=180)               → 券商覆盖统计
  5. daily_research_brief()                 → 今日研报速览
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pyodbc

# ===== 数据库连接 =====
_DEV = "Driver={ODBC Driver 17 for SQL Server};Server=192.168.18.31;Database=ghdata;UID=aiuser;PWD=31415;TrustServerCertificate=yes;"
_PRD = "Driver={ODBC Driver 17 for SQL Server};Server=192.168.18.11;Database=ghdata;UID=Topeasy;PWD=Topeasy;TrustServerCertificate=yes;"

def _get_conn():
    """优先生产库，降级到开发库"""
    try:
        return pyodbc.connect(_PRD)
    except:
        return pyodbc.connect(_DEV)

# ────────────────────────────
# 1. 个股研报汇总
# ────────────────────────────
def stock_research_summary(code: str, days: int = 90) -> str:
    """查询个股近期研报汇总，返回格式化文本"""
    conn = _get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT report_date, org_name, rating, rating_change, researcher, title, page_count,
               eps_this_year, eps_next_year, eps_year_after,
               pe_this_year, pe_next_year, pe_year_after
        FROM research_report
        WHERE stock_code=? AND report_date >= DATEADD(DAY,?,GETDATE())
        ORDER BY report_date DESC, id DESC
    """, code, -days)
    rows = c.fetchall()
    conn.close()

    if not rows:
        return f"近{days}天无券商研报覆盖。"

    lines = [f"📊 券商观点（近{days}天，{len(rows)}篇）"]
    lines.append("=" * 60)

    for r in rows[:10]:  # 最多10条
        rd = str(r[0] or '')[:10]
        org = str(r[1] or '')
        rat = str(r[2] or '') or '-'
        rc  = str(r[3] or '')
        res = str(r[4] or '')
        title = str(r[5] or '')
        pages = int(r[6] or 0)

        eps = []
        for v in [r[7], r[8], r[9]]:
            if v is not None: eps.append(f"{float(v):.2f}")
        eps_str = f"EPS={'→'.join(eps)}" if eps else ""

        pe = []
        for v in [r[10], r[11], r[12]]:
            if v is not None: pe.append(f"{float(v):.1f}x")
        pe_str = f"PE={'→'.join(pe)}" if pe else ""

        rc_mark = {'调高':'↑','调低':'↓','维持':'→'}.get(rc, '')
        rating_str = f"{rat}{rc_mark}" if rc_mark else rat

        lines.append(f"  {rd}  {org[:12]:12s}  {rating_str:8s}  {eps_str}")
        if title:
            lines.append(f"       {title[:40]}（{pages}页）{res}")
        if eps or pe:
            lines.append(f"       {eps_str}  |  {pe_str}")

    if len(rows) > 10:
        lines.append(f"  ... 还有{len(rows)-10}篇")

    return "\n".join(lines)


# ────────────────────────────
# 2. 评级变动风向标
# ────────────────────────────
def rating_wind_today(date_str: str = None) -> str:
    """今日评级变动统计"""
    conn = _get_conn()
    c = conn.cursor()
    today = date_str or __import__('datetime').datetime.now().strftime('%Y-%m-%d')

    # 调高/调低统计
    c.execute("""
        SELECT rating_change, COUNT(*) as cnt
        FROM research_report WHERE report_date=?
        GROUP BY rating_change
    """, today)
    changes = {str(r[0]): r[1] for r in c.fetchall()}

    # 评级分布
    c.execute("""
        SELECT 
            CASE 
                WHEN rating LIKE '%买入%' THEN '买入'
                WHEN rating LIKE '%增持%' THEN '增持'
                WHEN rating LIKE '%中性%' THEN '中性'
                WHEN rating LIKE '%减持%' THEN '减持'
                ELSE '其他'
            END as rgroup,
            COUNT(*) as cnt
        FROM research_report WHERE report_date=?
        GROUP BY 
            CASE 
                WHEN rating LIKE '%买入%' THEN '买入'
                WHEN rating LIKE '%增持%' THEN '增持'
                WHEN rating LIKE '%中性%' THEN '中性'
                WHEN rating LIKE '%减持%' THEN '减持'
                ELSE '其他'
            END
        ORDER BY cnt DESC
    """, today)
    ratings = {str(r[0]): r[1] for r in c.fetchall()}

    # 行业评级变动
    c.execute("""
        SELECT s.industry, rr.rating_change, COUNT(*) as cnt
        FROM research_report rr
        LEFT JOIN stock_info s ON rr.stock_code = s.stock_code
        WHERE rr.report_date=? AND rr.rating_change IN ('调高','调低')
        GROUP BY s.industry, rr.rating_change
        ORDER BY cnt DESC
    """, today)
    industry_rows = c.fetchall()
    conn.close()

    total = sum(ratings.values())
    if total == 0:
        return f"今日({today})无研报数据。"

    up = changes.get('调高', 0)
    down = changes.get('调低', 0)
    keep = changes.get('维持', 0)

    lines = [f"📈 今日({today})研报评级动态"]
    lines.append(f"    总{total}篇 | 调高↑{up} 调低↓{down} 维持→{keep}")
    lines.append("-" * 40)
    lines.append(f"  评级分布:")
    for k in ['买入','增持','中性','减持']:
        v = ratings.get(k, 0)
        if v > 0:
            pct = v / total * 100
            bar = '█' * int(pct / 5) + '░' * (20 - int(pct / 5))
            lines.append(f"    {k:4s}  {v:3d}篇  {bar} {pct:.0f}%")

    # 调高最多行业
    up_industries = [r for r in industry_rows if r[1]=='调高']
    down_industries = [r for r in industry_rows if r[1]=='调低']
    if up_industries:
        lines.append(f"\n  🔺 调高最多行业:")
        for r in up_industries[:5]:
            lines.append(f"    {str(r[0] or '未知'):12s}  {r[2]}家")
    if down_industries:
        lines.append(f"\n  🔻 调低最多行业:")
        for r in down_industries[:5]:
            lines.append(f"    {str(r[0] or '未知'):12s}  {r[2]}家")

    return "\n".join(lines)


# ────────────────────────────
# 3. EPS一致性预期指数
# ────────────────────────────
def eps_consistency(code: str, days: int = 180) -> str:
    """同一只股票多家机构EPS预期的离散度"""
    import statistics
    conn = _get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT eps_this_year, eps_next_year, org_name, report_date
        FROM research_report
        WHERE stock_code=? AND report_date >= DATEADD(DAY,?,GETDATE())
            AND eps_this_year IS NOT NULL
        ORDER BY report_date DESC
    """, code, -days)
    rows = c.fetchall()
    conn.close()

    if not rows:
        return f"{code} 近{days}天无EPS预期数据。"

    eps_vals = [float(r[0]) for r in rows if r[0] is not None]
    if len(eps_vals) < 2:
        return f"{code} 仅{len(eps_vals)}家机构覆盖，不足以计算一致性。"

    mean = statistics.mean(eps_vals)
    stdev = statistics.stdev(eps_vals)
    cv = stdev / abs(mean) if abs(mean) > 0.01 else 0  # 变异系数

    if cv < 0.05:
        level, desc = '低分歧', '高度一致 ✅'
    elif cv < 0.15:
        level, desc = '中等分歧', '基本一致 👍'
    elif cv < 0.3:
        level, desc = '较大分歧', '存在分歧 ⚠️'
    else:
        level, desc = '高度分歧', '严重分歧 ❌'

    lines = [
        f"📐 EPS一致性预期 — {code}",
        f"    覆盖机构: {len(eps_vals)}家",
        f"    平均EPS: {mean:.3f}",
        f"    标准差: {stdev:.3f}",
        f"    变异系数: {cv:.1%}",
        f"    判定: {desc} ({level})",
        f"    预期区间: [{min(eps_vals):.3f} ~ {max(eps_vals):.3f}]",
        "",
        f"  各机构预期:",
    ]
    for r in rows[:8]:
        org = str(r[2] or '未知')[:12]
        dt = str(r[3] or '')[:10]
        ep = float(r[0]) if r[0] else 0
        dev = f"{(ep - mean) / abs(mean) * 100:+.1f}%" if abs(mean) > 0.01 else ""
        lines.append(f"    {org:12s}  {dt}  EPS={ep:.3f}  {dev}")

    return "\n".join(lines)


# ────────────────────────────
# 4. 券商覆盖统计
# ────────────────────────────
def broker_ranking(days: int = 180) -> str:
    """券商研报产量排名"""
    conn = _get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT org_name,
               COUNT(*) as total,
               SUM(CASE WHEN rating LIKE '%买入%' THEN 1 ELSE 0 END) as buy_cnt,
               SUM(CASE WHEN rating_change='调高' THEN 1 ELSE 0 END) as up_cnt,
               SUM(CASE WHEN rating_change='调低' THEN 1 ELSE 0 END) as down_cnt,
               COUNT(DISTINCT stock_code) as stock_cnt
        FROM research_report
        WHERE report_date >= DATEADD(DAY,?,GETDATE())
        GROUP BY org_name
        ORDER BY total DESC
    """, -days)
    rows = c.fetchall()
    conn.close()

    if not rows:
        return f"近{days}天无研报数据。"

    total_reports = sum(r[1] for r in rows)
    lines = [f"🏦 券商研报覆盖统计（近{days}天，共{total_reports}篇）"]
    lines.append("=" * 70)
    lines.append(f"  {'机构':16s} {'篇数':>6s} {'买入率':>7s} {'调高':>4s} 调低  {'覆盖':>5s}")
    lines.append("-" * 70)

    for r in rows[:15]:
        name = str(r[0] or '')[:16]
        total = r[1]
        buy_pct = r[2] / total * 100 if total > 0 else 0
        up = r[3]
        down = r[4]
        stocks = r[5]
        bar_len = int(total / max(r[1] for r in rows) * 20)
        bar = '█' * bar_len + '░' * (20 - bar_len)
        lines.append(f"  {name:16s} {total:5d}篇 {buy_pct:5.0f}%  {bar}  ↑{up} ↓{down}  {stocks}只")

    return "\n".join(lines)


# ────────────────────────────
# 5. 今日研报速览
# ────────────────────────────
def daily_research_brief(date_str: str = None) -> str:
    """今日研报速览（适合嵌入daily_update输出）"""
    conn = _get_conn()
    c = conn.cursor()
    today = date_str or __import__('datetime').datetime.now().strftime('%Y-%m-%d')

    c.execute("SELECT COUNT(*) FROM research_report WHERE report_date=?", today)
    total = c.fetchone()[0]
    if total == 0:
        conn.close()
        return f"📰 {today} 无券商研报"

    c.execute("SELECT COUNT(DISTINCT org_name) FROM research_report WHERE report_date=?", today)
    orgs = c.fetchone()[0]

    c.execute("SELECT COUNT(DISTINCT stock_code) FROM research_report WHERE report_date=?", today)
    stocks = c.fetchone()[0]

    c.execute("""
        SELECT 
            SUM(CASE WHEN rating LIKE '%买入%' THEN 1 ELSE 0 END),
            SUM(CASE WHEN rating LIKE '%增持%' THEN 1 ELSE 0 END),
            SUM(CASE WHEN rating LIKE '%中性%' THEN 1 ELSE 0 END),
            SUM(CASE WHEN rating LIKE '%减持%' OR rating LIKE '%卖出%' THEN 1 ELSE 0 END)
        FROM research_report WHERE report_date=?
    """, today)
    buy, add, neutral, sell = [v or 0 for v in c.fetchone()]

    c.execute("""
        SELECT 
            SUM(CASE WHEN rating_change='调高' THEN 1 ELSE 0 END),
            SUM(CASE WHEN rating_change='维持' THEN 1 ELSE 0 END),
            SUM(CASE WHEN rating_change='调低' THEN 1 ELSE 0 END)
        FROM research_report WHERE report_date=? AND rating_change != ''
    """, today)
    up, keep, down = [v or 0 for v in c.fetchone()]

    conn.close()

    return (
        f"📰 研报速览: {total}条 | {orgs}家机构 | 覆盖{stocks}只股票\n"
        f"   评级: 买入{buy}  增持{add}  中性{neutral}  减持{sell}\n"
        f"   变动: ↑调高{up}  →维持{keep}  ↓调低{down}"
    )


# ────────────────────────────
# 测试入口
# ────────────────────────────
if __name__ == '__main__':
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'brief'
    if cmd == 'stock':
        code = sys.argv[2] if len(sys.argv) > 2 else '601899'
        print(stock_research_summary(code))
    elif cmd == 'wind':
        print(rating_wind_today())
    elif cmd == 'eps':
        code = sys.argv[2] if len(sys.argv) > 2 else '600309'
        print(eps_consistency(code))
    elif cmd == 'rank':
        print(broker_ranking())
    else:
        print(daily_research_brief())
