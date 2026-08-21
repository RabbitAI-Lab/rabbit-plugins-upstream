#!/usr/bin/env python3
import os

import sys
import json
import argparse
import subprocess
from datetime import datetime
from typing import Dict, Any, Tuple
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))
from reliability import retry_subprocess

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))  # T4-4: 添加项目根以支持mcps.shared导入
from mcps.shared.db_logger import get_logger

import logging
logger = get_logger("system", source="skills/content-analytics/scripts/content_closed_loop.py")
logger = get_logger("_lazy", source="skills/content-analytics/scripts/content_closed_loop.py(v25.0合并)")

_CONTAINER = os.environ.get("JUEJIN_PG_CONTAINER", "juejin-postgres")
_DB_USER = os.environ.get("PG_APP_USER", "juejin_app")
_DB_NAME = os.environ.get("PG_DATABASE", "juejin")

_PROJECT_DIR = Path(__file__).resolve().parent
while _PROJECT_DIR.name != "JueJin" and _PROJECT_DIR != _PROJECT_DIR.parent:
    _PROJECT_DIR = _PROJECT_DIR.parent
_GROWTH_SCRIPT = _PROJECT_DIR / "skills" / "_lazy" / "self-growth" / "scripts" / "self_growth_engine.py"  # BUG-349修复: 路径添加_lazy

def _update_tenant_analytics(tenant_id: str, metrics: dict) -> None:
    """将反馈数据更新到tenant_analytics表(来源:06文档CP-17 多租户素材管理闭环)
    按tenant_id+metric_date+platform聚合更新，不存在则INSERT
    """
    if not tenant_id:
        return
    today = datetime.now().strftime("%Y-%m-%d")
    platform = metrics.get("platform", "unknown")
    views = int(metrics.get("views", 0))
    likes = int(metrics.get("likes", 0))
    comments = int(metrics.get("comments", 0))
    shares = int(metrics.get("shares", 0))
    click_rate = float(metrics.get("click_rate", 0))
    meta = json.dumps({"click_rate": click_rate, "source": metrics.get("data_source", "feedback")}, ensure_ascii=False)
    sql = ("INSERT INTO tenant_analytics (tenant_id, metric_date, platform, views, likes, comments, shares, followers_gained, revenue, metadata) "
           "VALUES (:'tid', :'md', :'plat', :views, :likes, :comments, :shares, 0, 0, :'meta') "
           "ON CONFLICT (tenant_id, metric_date, platform) DO UPDATE SET "
           "views = tenant_analytics.views + EXCLUDED.views, "
           "likes = tenant_analytics.likes + EXCLUDED.likes, "
           "comments = tenant_analytics.comments + EXCLUDED.comments, "
           "shares = tenant_analytics.shares + EXCLUDED.shares;")
    _exec_sql(sql, {"tid": tenant_id, "md": today, "plat": platform,
                    "views": str(views), "likes": str(likes), "comments": str(comments),
                    "shares": str(shares), "meta": meta})

def _esc(val: str) -> str:
    """
    SQL值转义（V5-H9修复：加强防御SQL注入）

    V5-H9: 原实现仅转义单引号，不足以防御：
    - NULL字节注入 (\x00)
    - Unicode混淆 (fullwidth characters)
    - 换行符注入 (\\n in string)
    - 反斜杠逃逸 (\\')
    - 注释符号注入 (-- / /**/)
    """
    if not isinstance(val, str):
        val = str(val)
    
    # 1. 移除NULL字节和不可打印控制字符（保留\\n\\t）
    val = ''.join(c for c in val if c >= ' ' or c in '\n\t\r')
    
    # 2. 转义单引号（PostgreSQL标准方式：''）
    val = val.replace("'", "''")
    
    # 3. 转义反斜杠（防止\\'逃逸）
    val = val.replace("\\", "\\\\")
    
    # 4. 长度限制（防止超长字符串DoS）
    if len(val) > 500:
        logger.warning(f"[content-closed-loop] _esc截断超长值(原长{len(val)}→500)")
        val = val[:500]
    
    return val

def _validate_content_id(cid: str) -> bool:
    """
    V5-H9新增: content_id格式验证
    
    只允许安全的字符集：字母、数字、连字符、下划线
    拒绝包含SQL特殊字符的ID
    """
    import re
    if not cid or not isinstance(cid, str):
        return False
    # 允许: UUID格式、slug格式、纯数字ID
    allowed_pattern = re.compile(r'^[a-zA-Z0-9_\-:.]+$')
    if not allowed_pattern.match(cid):
        logger.error(f"[content-closed-loop] 不安全content_id被拒绝: {cid[:50]}... 包含非法字符")
        return False
    if len(cid) > 100:
        logger.warning(f"[content-closed-loop] content_id过长({len(cid)}字符)，可能异常")
    return True

def _parse_step_output(output: str, step_name: str) -> dict:
    """
    解析步骤输出（V4修复：不再将解析失败包装为成功）

    V4-C1修复: 原实现所有分支都返回success=True，
    导致即使步骤完全失败，整体闭环仍报告overall_success=True
    现在正确区分成功/失败状态
    """
    if not output or not isinstance(output, str):
        return {"success": False, "error": f"{step_name}无输出或输出类型错误", "code": "EMPTY_OUTPUT", "step": step_name}
    try:
        data = json.loads(output)
        if isinstance(data, dict):
            # 保留原始success字段，但默认改为False
            return {
                "success": data.get("success", False),
                "data": data.get("data"),
                "error": data.get("error"),
                "code": data.get("code"),
                "step": step_name
            }
        return {"success": False, "error": f"{step_name}输出非JSON对象(dict)", "code": "INVALID_TYPE", "step": step_name}
    except (json.JSONDecodeError, TypeError) as e:
        return {"success": False, "error": f"{step_name}JSON解析失败: {e}", "code": "PARSE_ERROR", "step": step_name}

def _exec_sql(sql: str, pg_vars: dict = None, tenant_id: str = "", admin_mode: bool = False) -> Tuple[bool, str]:
    """执行SQL（支持psql变量参数化，防御SQL注入）

    pg_vars: {var_name: value} → psql -v var_name=value
    SQL中使用 :'var_name' (字符串) 或 :var_name (数值) 引用变量

    R4修复: 添加psycopg2降级方案(Docker不可用时自动切换到db_pool直连PG)
    根因: Python subprocess可能无法访问Docker daemon(开发环境PATH/socket限制)

    R8修复(P0): 添加tenant_id参数,设置RLS上下文(SET app.current_tenant)
    根因: content_publish_log等表已启用RLS+FORCED,不设置app.current_tenant时
    查询返回0行(tenant_id::text = '' 不匹配任何行),导致自生长引擎读取不到数据
    优化: 自动从pg_vars提取tid/tenant_id,避免20+调用方逐一修改

    R9修复(P0): 添加admin_mode参数,用于跨租户批量操作(如_sync_recent_content)
    根因: _sync_recent_content需要SELECT FROM tenant_publish_records(有RLS)并INSERT INTO
    content_publish_log(有RLS),但这是系统级跨租户操作,不能设置单一租户的RLS上下文
    方案: admin_mode=True时使用postgres超级用户(自动绕过RLS)
    """
    # R8优化: 自动从pg_vars提取tenant_id(大多数调用方已在pg_vars中传入tid)
    if not tenant_id and pg_vars:
        tenant_id = str(pg_vars.get("tid", "") or pg_vars.get("tenant_id", "") or "")
    # 方案1: docker exec psql (生产环境首选,支持psql变量语法)
    # R9: admin_mode使用postgres超级用户绕过RLS(跨租户批量操作)
    _db_user = "postgres" if admin_mode else _DB_USER
    try:
        cmd = ["docker", "exec", _CONTAINER, "psql", "-U", _db_user, "-d", _DB_NAME, "-t", "-A"]
        if pg_vars:
            for k, v in pg_vars.items():
                cmd.extend(["-v", f"{k}={v}"])
        # R8修复: 设置RLS上下文(在主查询前执行,同一psql session内生效)
        if tenant_id:
            cmd.extend(["-v", f"tenant_ctx={tenant_id}", "-c", "SET app.current_tenant = :'tenant_ctx'"])
        cmd.extend(["-c", sql])
        result = retry_subprocess(cmd, timeout=30, service="content-closed-loop-sql", encoding="utf-8", errors="ignore")
        return result.returncode == 0, result.stdout.strip()
    except Exception as e:
        logger.warning(f"content closed loop docker exec失败,降级psycopg2: {e}")

    # 方案2: psycopg2直连PG降级方案(R4修复: Docker不可用时使用db_pool)
    try:
        import re
        import psycopg2.extras
        from mcps.shared.db_pool import get_connection, return_connection

        # 转换psql变量语法为psycopg2参数化查询
        # :'var_name' → %s (字符串), :var_name → %s (数值)
        params = []
        converted_sql = sql
        if pg_vars:
            for k, v in pg_vars.items():
                # 先替换 :'var_name' (带引号,字符串)
                converted_sql = converted_sql.replace(f":'{k}'", "%s")
                # 再替换 :var_name (不带引号,数值)
                converted_sql = converted_sql.replace(f":{k}", "%s")
                params.append(v)

        conn = get_connection()
        try:
            with conn.cursor() as cur:
                # R9修复: admin_mode时关闭行级安全(跨租户批量操作)
                # R8修复: 非admin_mode时设置RLS上下文(在主查询前执行,同一连接内生效)
                if admin_mode:
                    try:
                        cur.execute("SET row_security = off")
                    except Exception as e:
                        logger.debug(f"SET row_security=off失败(非超级用户),降级为普通查询: {e}")
                elif tenant_id:
                    cur.execute("SET app.current_tenant = %s", (tenant_id,))
                cur.execute(converted_sql, params if params else None)
                if converted_sql.strip().upper().startswith("SELECT") or "RETURNING" in converted_sql.upper():
                    rows = cur.fetchall()
                    output = "\n".join("|".join(str(c) for c in row) for row in rows) if rows else ""
                else:
                    output = f"INSERT 0 {cur.rowcount}" if converted_sql.strip().upper().startswith("INSERT") else ""
                conn.commit()
                return True, output
        finally:
            return_connection(conn)
    except Exception as e2:
        logger.error(f"content closed loop psycopg2降级也失败: {e2}", exc_info=True)
        return False, str(e2)

def _ensure_table() -> bool:
    sql = (
        "CREATE TABLE IF NOT EXISTS content_publish_log ("
        "id SERIAL PRIMARY KEY, content_id VARCHAR(100) UNIQUE NOT NULL, "
        "title VARCHAR(500), content_type VARCHAR(50), topic VARCHAR(200), "
        "platforms TEXT[], publish_time TIMESTAMPTZ DEFAULT NOW(), status VARCHAR(20) DEFAULT 'published', "
        "recommended_friends INT DEFAULT 0, target_segments TEXT[], "
        "views INT DEFAULT 0, likes INT DEFAULT 0, comments INT DEFAULT 0, shares INT DEFAULT 0, click_rate FLOAT DEFAULT 0, "
        "engagement_score FLOAT DEFAULT 0, conversion_rate FLOAT DEFAULT 0, roi_score FLOAT DEFAULT 0, "
        "optimization_notes TEXT, next_action VARCHAR(200), "
        "created_at TIMESTAMPTZ DEFAULT NOW(), updated_at TIMESTAMPTZ DEFAULT NOW());"
    )
    ok, _ = _exec_sql(sql)
    _exec_sql("CREATE INDEX IF NOT EXISTS idx_cpl_content_id ON content_publish_log(content_id);")
    _exec_sql("CREATE INDEX IF NOT EXISTS idx_cpl_status ON content_publish_log(status);")
    # R4修复: 新增tenant_id列(同步tenant_publish_records时保留租户标识,供自生长引擎按租户存储经验)
    _exec_sql("ALTER TABLE content_publish_log ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(100) DEFAULT '';")
    _exec_sql("CREATE INDEX IF NOT EXISTS idx_cpl_tenant ON content_publish_log(tenant_id);")
    return ok

def _sync_recent_content(days: int = 7) -> list:
    """Fix-B根因修复: 从tenant_publish_records同步最近发布内容到content_publish_log

    根因: do_full_loop原创建fake content_id(daily_YYYYMMDD),但真实发布数据在
    tenant_publish_records表中(含真实互动指标view_count/like_count等)。
    本函数将最近N天的真实发布数据同步到content_publish_log,使闭环分析基于真实数据。

    UPSERT策略:
    - 新记录: INSERT(含真实指标)
    - 已存在但views=0: UPDATE(补充真实指标)
    - 已存在且views>0: 保留(不覆盖已采集数据)

    遵循: 修复提示词R1(运行时证据)/R31(不降级优化)/R43(全局影响分析)/R74(反敷衍修复)
    """
    if not _ensure_table():
        logger.error("[content-closed-loop] _ensure_table失败,无法同步")
        return []

    # R4修复: 3个根因修正
    # 1. publish_status 'success'→'published'(真实发布代码写入'published',非'success')
    # 2. content_id NULL→COALESCE生成fallback ID 'tpr_{id}'(tenant_publish_records.content_id列未被INSERT填充)
    # 3. 新增tenant_id同步(自生长引擎需按租户存储经验,避免跨租户数据泄露)
    sync_sql = (
        "INSERT INTO content_publish_log (content_id, title, content_type, platforms, publish_time, status, views, likes, comments, shares, tenant_id) "
        "SELECT COALESCE(NULLIF(content_id, ''), CONCAT('tpr_', id::text)), COALESCE(NULLIF(content_title, ''), title, '未命名'), "
        "COALESCE(content_type, 'video'), ARRAY[COALESCE(platform, 'unknown')], COALESCE(published_at, NOW()), 'published', "
        "COALESCE(view_count, 0), COALESCE(like_count, 0), COALESCE(comment_count, 0), COALESCE(share_count, 0), tenant_id "
        "FROM tenant_publish_records "
        f"WHERE publish_status = 'published' AND published_at >= NOW() - INTERVAL '{days} days' "
        "ON CONFLICT (content_id) DO UPDATE SET "
        "title = CASE WHEN content_publish_log.title IS NULL OR content_publish_log.title = '' THEN EXCLUDED.title ELSE content_publish_log.title END, "
        "views = CASE WHEN content_publish_log.views = 0 THEN EXCLUDED.views ELSE content_publish_log.views END, "
        "likes = CASE WHEN content_publish_log.likes = 0 THEN EXCLUDED.likes ELSE content_publish_log.likes END, "
        "comments = CASE WHEN content_publish_log.comments = 0 THEN EXCLUDED.comments ELSE content_publish_log.comments END, "
        "shares = CASE WHEN content_publish_log.shares = 0 THEN EXCLUDED.shares ELSE content_publish_log.shares END, "
        "tenant_id = CASE WHEN content_publish_log.tenant_id IS NULL OR content_publish_log.tenant_id = '' THEN EXCLUDED.tenant_id ELSE content_publish_log.tenant_id END, "
        "updated_at = NOW() "
        "RETURNING content_id;"
    )
    ok, output = _exec_sql(sync_sql, admin_mode=True)  # R9修复(P0): 跨租户同步使用admin_mode绕过RLS
    if not ok:
        logger.error(f"[content-closed-loop] 同步SQL执行失败: {output}")
        return []
    if not output or not output.strip():
        logger.info(f"[content-closed-loop] 同步完成,无新增/更新记录(days={days})")
        return []

    synced_ids = [line.strip() for line in output.strip().split("\n") if line.strip()]
    logger.info(f"[content-closed-loop] 同步{len(synced_ids)}条真实发布内容到content_publish_log: {synced_ids[:5]}")
    return synced_ids

def _out(success: bool, data: Any, error: str = None, code: str = None) -> None:
    print(json.dumps({"success": success, "data": data, "error": error, "code": code}, ensure_ascii=False))

def do_publish(args) -> None:
    if not _ensure_table():
        _out(False, {}, "无法创建内容表", "TABLE_ERROR")
        return
    if not _validate_content_id(args.content_id):
        _out(False, {}, f"不安全的content_id: {args.content_id[:50]}", "INVALID_CONTENT_ID")
        return
    title = args.title or ""
    ctype = args.content_type or "video"
    topic = args.topic or "日常"
    plats = args.platforms or ["douyin", "xiaohongshu"]
    plats_pg = "{" + ",".join(plats) + "}"
    _tid = getattr(args, 'tenant_id', '') or ''
    # R5修复(扩展性): INSERT添加tenant_id列(避免发布记录缺失租户标识)
    sql = ("INSERT INTO content_publish_log (content_id, title, content_type, topic, platforms, status, publish_time, tenant_id) "
           "VALUES (:'cid', :'title', :'ctype', :'topic', :'plats'::text[], 'published', NOW(), :'tid') "
           "ON CONFLICT (content_id) DO UPDATE SET title = EXCLUDED.title, "
           "tenant_id = COALESCE(NULLIF(content_publish_log.tenant_id, ''), EXCLUDED.tenant_id), "
           "updated_at = NOW() "
           "RETURNING id, content_id, publish_time;")
    ok, output = _exec_sql(sql, {"cid": args.content_id, "title": title, "ctype": ctype, "topic": topic, "plats": plats_pg, "tid": _tid})
    if ok and output:
        parts = output.split("|")
        _out(True, {"id": parts[0] if len(parts) > 0 else None, "content_id": parts[1] if len(parts) > 1 else args.content_id,
                     "publish_time": parts[2] if len(parts) > 2 else None, "title": args.title, "platforms": plats,
                     "status": "published"})
    else:
        _out(False, {}, "发布记录失败", "PUBLISH_ERROR")

def do_recommend(args) -> None:
    if not _validate_content_id(args.content_id):
        _out(False, {}, f"不安全的content_id: {args.content_id[:50]}", "INVALID_CONTENT_ID")
        return
    top_k = min(args.top_k, 50)
    _tid = getattr(args, 'tenant_id', '') or ''
    # R5修复(扩展性): 添加tenant_id过滤(防止跨租户好友数据泄露)
    _tf = "AND (:'tid' = '' OR tenant_id = :'tid')" if _tid else ""
    sql = ("WITH target_friends AS (SELECT friend_id, nickname, intimacy_level, tags, "
           "CASE WHEN intimacy_level>=4 THEN 'VIP' WHEN intimacy_level>=3 THEN '高价值' "
           "WHEN intimacy_level>=2 THEN '普通' ELSE '新朋友' END AS segment "
           "FROM friend_profiles_v2 WHERE is_active=TRUE AND interest_embedding IS NOT NULL "
           f"{_tf} AND block_status IS DISTINCT FROM 'blocked' ORDER BY intimacy_level DESC, random() LIMIT :top_k2) "
           "SELECT friend_id, nickname, intimacy_level, segment, tags, "
           "COALESCE((1-(interest_embedding<=>(SELECT interest_embedding FROM friend_profiles_v2 "
           f"WHERE is_active=TRUE AND interest_embedding IS NOT NULL {_tf} LIMIT 1))), 0.5) AS relevance, "
           "CASE WHEN intimacy_level>=4 THEN 100 WHEN intimacy_level>=3 THEN 80 "
           "WHEN intimacy_level>=2 THEN 60 ELSE 40 END AS priority "
           "FROM target_friends ORDER BY intimacy_level DESC, relevance DESC LIMIT :top_k;")
    ok, output = _exec_sql(sql, {"top_k": str(top_k), "top_k2": str(top_k * 2), "tid": _tid})
    friends = []
    segments = {"VIP": [], "高价值": [], "普通": [], "新朋友": []}
    if ok and output:
        for line in output.split("\n"):
            if not line.strip():
                continue
            parts = line.split("|")
            if len(parts) >= 6:
                try:
                    tags = json.loads(parts[4]) if parts[4] and parts[4] != "null" else []
                    relevance = float(parts[5]) if len(parts) > 5 and parts[5] else 0
                    friend = {"friend_id": parts[0], "nickname": parts[1], "intimacy_level": int(parts[2]),
                              "segment": parts[3], "tags": tags, "relevance_score": round(relevance, 3)}
                    friends.append(friend)
                    seg = friend["segment"]
                    if seg in segments:
                        segments[seg].append(friend["friend_id"])
                except (json.JSONDecodeError, ValueError):
                    continue
    _exec_sql("UPDATE content_publish_log SET recommended_friends=:count, "
              "updated_at=NOW() WHERE content_id=:'cid';",
              {"count": str(len(friends)), "cid": args.content_id})
    _out(True, {"content_id": args.content_id, "recommended_count": len(friends),
                "friends": friends[:top_k], "segments": {k: len(v) for k, v in segments.items() if v}})

def _try_fetch_real_metrics(content_id: str, tenant_id: str = "") -> dict | None:
    """尝试通过opencli-mcp的browser_verify_content获取真实互动数据

    依次查询小红书/B站等平台的创作者数据，汇总为互动指标。
    返回None表示opencli不可用或无数据。
    R5修复(扩展性): 添加tenant_id参数,SQL添加租户过滤
    """
    try:
        _tf = "AND (:'tid' = '' OR tenant_id = :'tid')" if tenant_id else ""
        sql = (f"SELECT title, platforms FROM content_publish_log "
               f"WHERE content_id=:'cid' {_tf};")
        ok, output = _exec_sql(sql, {"cid": content_id, "tid": tenant_id})
        if not ok or not output:
            return None
        parts = output.strip().split("|")
        title = parts[0].strip() if len(parts) > 0 else ""
        platforms_raw = parts[1].strip() if len(parts) > 1 else "{}"
        try:
            platforms = json.loads(platforms_raw.replace("{", "[").replace("}", "]"))
        except (json.JSONDecodeError, ValueError):
            platforms = []

        platform_map = {
            "xiaohongshu": "xiaohongshu",
            "bilibili": "bilibili",
            "zhihu": "zhihu",
            "weibo": "weibo",
        }
        total_views = 0
        total_likes = 0
        total_comments = 0
        total_shares = 0
        found_any = False

        for plat in platforms:
            opencli_plat = platform_map.get(plat)
            if not opencli_plat:
                continue
            try:
                action = "creator-notes" if opencli_plat == "xiaohongshu" else "search"
                cmd = ["opencli", opencli_plat, action]
                if title:
                    cmd.append(title[:50])
                cmd.extend(["--limit", "5", "--json"])
                result = retry_subprocess(cmd, timeout=20, service="opencli-mcp",
                                          encoding="utf-8", errors="ignore")
                if result.returncode != 0:
                    continue
                data = json.loads(result.stdout.strip())
                if not isinstance(data, dict) or not data.get("success"):
                    continue
                items = data.get("data", {}).get("items", [])
                if not items:
                    continue
                for item in items[:3]:
                    total_views += int(item.get("views", 0))
                    total_likes += int(item.get("likes", 0))
                    total_comments += int(item.get("comments", 0))
                    total_shares += int(item.get("shares", 0))
                    found_any = True
            except Exception as e:
                logger.error(f"[content_closed_loop] 数据采集异常: {e}")
                continue

        if not found_any:
            return None

        click_rate = round(total_likes / max(total_views, 1), 4) if total_views > 0 else 0.0
        return {
            "views": total_views, "likes": total_likes,
            "comments": total_comments, "shares": total_shares,
            "click_rate": click_rate, "data_source": "opencli-mcp",
        }
    except Exception as e:
        logger.error(f"[content_closed_loop] 闭环数据获取失败: {e}")
        return None

def _estimate_metrics_from_db(content_id: str, tenant_id: str = "") -> dict:
    """基于发布时间和历史均值估算互动数据（opencli不可用时的降级方案）

    估算逻辑:
    - 从DB查询该内容的发布时间
    - 从DB查询近7天所有内容的平均互动率
    - 用发布时长×平均互动率估算当前数据
    R5修复(扩展性): 添加tenant_id参数,SQL添加租户过滤(防止跨租户数据混合)
    """
    hours_since_publish = 1.0
    avg_views_per_hour = 10
    avg_like_rate = 0.05
    avg_comment_rate = 0.01
    avg_share_rate = 0.005
    _tf = "AND (:'tid' = '' OR tenant_id = :'tid')" if tenant_id else ""

    try:
        sql = (f"SELECT EXTRACT(EPOCH FROM (NOW()-publish_time))/3600 "
               f"FROM content_publish_log WHERE content_id=:'cid' {_tf};")
        ok, output = _exec_sql(sql, {"cid": content_id, "tid": tenant_id})
        if ok and output:
            try:
                hours_since_publish = max(float(output.strip()), 0.5)
            except (ValueError, TypeError) as e:
                logger.error(f"Exception in except block: {e}");
                logger.error(json.dumps({"success": False, "data": {}, "error": str(e), "code": "CONTENT-HOURS-ERR"}))

        sql = (f"SELECT AVG(views), AVG(likes), AVG(comments), AVG(shares) "
               f"FROM content_publish_log WHERE views > 0 "
               f"AND publish_time > NOW() - INTERVAL '7 days' {_tf};")
        ok, output = _exec_sql(sql, {"tid": tenant_id})
        if ok and output:
            parts = output.strip().split("|")
            if len(parts) >= 4:
                try:
                    avg_v = float(parts[0].strip() or "0")
                    avg_l = float(parts[1].strip() or "0")
                    avg_c = float(parts[2].strip() or "0")
                    avg_s = float(parts[3].strip() or "0")
                    if avg_v > 0:
                        avg_views_per_hour = avg_v / 168
                        avg_like_rate = avg_l / max(avg_v, 1)
                        avg_comment_rate = avg_c / max(avg_v, 1)
                        avg_share_rate = avg_s / max(avg_v, 1)
                except (ValueError, TypeError) as e:
                    logger.error(f"Exception in except block: {e}");
                    logger.error(json.dumps({"success": False, "data": {}, "error": str(e), "code": "CONTENT-AVG-ERR"}))
    except Exception as e:
        logger.error(f"content closed loop异常: {e}", exc_info=True)
        logger.warning(f"[content-closed-loop] 估算数据查询异常: {e}")

    est_views = int(avg_views_per_hour * hours_since_publish)
    est_likes = int(est_views * avg_like_rate)
    est_comments = int(est_views * avg_comment_rate)
    est_shares = int(est_views * avg_share_rate)
    est_click_rate = round(avg_like_rate, 4)

    return {
        "views": est_views, "likes": est_likes,
        "comments": est_comments, "shares": est_shares,
        "click_rate": est_click_rate, "data_source": "estimated",
    }

def do_feedback(args) -> None:
    if not _validate_content_id(args.content_id):
        _out(False, {}, f"不安全的content_id: {args.content_id[:50]}", "INVALID_CONTENT_ID")
        return
    is_simulated = getattr(args, 'is_simulated', False)

    tenant_id = getattr(args, 'tenant_id', None)
    _tid = tenant_id or ''
    _tf = "AND (:'tid' = '' OR tenant_id = :'tid')" if _tid else ""

    if is_simulated:
        real_data = _try_fetch_real_metrics(args.content_id, tenant_id=_tid)
        if real_data is not None:
            sql = ("UPDATE content_publish_log SET views=COALESCE(views,0)+:views, "
                   "likes=COALESCE(likes,0)+:likes, comments=COALESCE(comments,0)+:comments, "
                   f"shares=COALESCE(shares,0)+:shares, click_rate=:click_rate, updated_at=NOW() "
                   f"WHERE content_id=:'cid' {_tf} RETURNING content_id, views, likes, comments, shares;")
            ok, output = _exec_sql(sql, {
                "views": str(real_data["views"]), "likes": str(real_data["likes"]),
                "comments": str(real_data["comments"]), "shares": str(real_data["shares"]),
                "click_rate": str(real_data["click_rate"]), "cid": args.content_id, "tid": _tid
            })
            result = {"content_id": args.content_id, **real_data}
            if ok and output:
                parts = output.split("\n")[0].strip().split("|")
                if len(parts) >= 5:
                    try:
                        result = {"content_id": parts[0], "views": int(parts[1]),
                                  "likes": int(parts[2]), "comments": int(parts[3]),
                                  "shares": int(parts[4])}
                    except (ValueError, IndexError) as e:
                        logger.error(f"Exception in except block: {e}");
                        logger.error(json.dumps({"success": False, "data": {}, "error": str(e), "code": "CONTENT-FEEDBACK-ERR"}))
            _out(True, result)
            if tenant_id:
                _update_tenant_analytics(tenant_id, real_data)
            return

        estimated = _estimate_metrics_from_db(args.content_id, tenant_id=_tid)
        estimated["is_estimated"] = True
        # 禁止估算数据写入DB(来源:SKILL.md "auto-feedback/模拟模式→返回REAL_DATA_UNAVAILABLE,禁止假数据写入DB")
        # 估算数据仅用于展示，不执行UPDATE SQL
        result = {"content_id": args.content_id, **estimated, "status": "pending_feedback"}
        _out(True, result, "opencli-mcp不可用,估算数据仅供展示不写入DB,等待真实API数据回填", "REAL_DATA_UNAVAILABLE")
        return  # Fix: 缺少return导致is_simulated分支fall-through到int(args.views)崩溃

    try:
        views = int(args.views)
        likes = int(args.likes)
        comments = int(args.comments)
        shares = int(args.shares)
        click_rate = float(args.click_rate)
    except (ValueError, TypeError) as e:
        _out(False, {}, f"参数类型错误: {e}", "INVALID_PARAMS")
        return
    sql = ("UPDATE content_publish_log SET views=COALESCE(views,0)+:views, "
           "likes=COALESCE(likes,0)+:likes, comments=COALESCE(comments,0)+:comments, "
           f"shares=COALESCE(shares,0)+:shares, click_rate=:click_rate, updated_at=NOW() "
           f"WHERE content_id=:'cid' {_tf} RETURNING content_id, views, likes, comments, shares;")
    ok, output = _exec_sql(sql, {
        "views": str(views), "likes": str(likes), "comments": str(comments),
        "shares": str(shares), "click_rate": str(click_rate), "cid": args.content_id, "tid": _tid
    })
    if ok and output:
        parts = output.split("\n")[0].strip().split("|")
        if len(parts) >= 5:
            try:
                result = {"content_id": parts[0], "views": int(parts[1]), "likes": int(parts[2]),
                          "comments": int(parts[3]), "shares": int(parts[4])}
                _out(True, result)
                if tenant_id:
                    _update_tenant_analytics(tenant_id, {"views": int(parts[1]), "likes": int(parts[2]),
                        "comments": int(parts[3]), "shares": int(parts[4]), "click_rate": click_rate})
                return
            except (ValueError, IndexError):
                logger.warning("[content-closed-loop] 反馈数据解析失败，使用默认值")
    result = {"content_id": args.content_id, "views": args.views, "likes": args.likes,
              "comments": args.comments, "shares": args.shares}
    _out(True, result)

def do_analyze(args) -> None:
    if not _validate_content_id(args.content_id):
        _out(False, {}, f"不安全的content_id: {args.content_id[:50]}", "INVALID_CONTENT_ID")
        return
    _tid = getattr(args, 'tenant_id', '') or ''
    _tf = "AND (:'tid' = '' OR tenant_id = :'tid')" if _tid else ""
    sql = (f"SELECT content_id, title, views, likes, comments, shares, click_rate, "
           f"recommended_friends, publish_time, EXTRACT(EPOCH FROM (NOW()-publish_time))/3600 "
           f"FROM content_publish_log WHERE content_id=:'cid' {_tf};")
    ok, output = _exec_sql(sql, {"cid": args.content_id, "tid": _tid})
    if not ok or not output:
        _out(False, {}, f"内容{args.content_id}不存在", "CONTENT_NOT_FOUND")
        return
    parts = output.split("\n")[0].strip().split("|")
    try:
        if len(parts) < 9:
            _out(False, {}, f"数据格式错误(期望>=9字段,实际{len(parts)}字段)", "DATA_ERROR")
            return

        # V4-C5修复: 加强字段索引越界保护
        def safe_get(parts_list, index, default=0, cast_func=int):
            try:
                val = parts_list[index].strip()
                if not val:
                    return default
                return cast_func(val)
            except (IndexError, ValueError, TypeError):
                return default

        views = safe_get(parts, 2)
        likes = safe_get(parts, 3)
        comments = safe_get(parts, 4)
        shares = safe_get(parts, 5)
        click_rate = safe_get(parts, 6, default=0.0, cast_func=float)
        recommended = safe_get(parts, 7)
        hours = safe_get(parts, 9, default=1.0, cast_func=float)

        engagement = min(100, ((likes / max(views, 1) * 30) + (comments / max(views, 1) * 40) +
                               (shares / max(views, 1) * 30) + (click_rate * 20)) * 100) if views > 0 else 0
        conversion = round((likes + comments + shares) / max(recommended, 1), 3)
        roi = round(engagement * 0.4 + conversion * 100 * 0.3 + min(click_rate * 100, 100) * 0.3, 2)
        level = "优秀" if roi >= 80 else "良好" if roi >= 60 else "一般" if roi >= 40 else "需改进"

        _exec_sql(f"UPDATE content_publish_log SET engagement_score=:engagement, conversion_rate=:conversion, "
                  f"roi_score=:roi, status=CASE WHEN :roi>=70 THEN 'performing_well' "
                  f"WHEN :roi>=40 THEN 'needs_optimization' ELSE 'underperforming' END, "
                  f"updated_at=NOW() WHERE content_id=:'cid' {_tf};",
                  {"engagement": str(engagement), "conversion": str(conversion), "roi": str(roi), "cid": args.content_id, "tid": _tid})
        _out(True, {"content_id": args.content_id, "title": parts[1],
                   "metrics": {"views": views, "likes": likes, "comments": comments, "shares": shares,
                               "click_rate": round(click_rate, 3)},
                   "analysis": {"engagement_score": round(engagement, 2), "conversion_rate": conversion,
                                "roi_score": roi, "performance_level": level, "hours_since_publish": round(hours, 1)}})
    except (ValueError, IndexError) as e:
        logger.error(f"[content-closed-loop] 数据分析异常: {e}", exc_info=True)
        _out(False, {}, f"数据分析错误: {e}", "ANALYSIS_ERROR")

def do_optimize(args) -> None:
    days = min(args.days, 90)
    _tid = getattr(args, 'tenant_id', '') or ''
    _tf = "AND (:'tid' = '' OR tenant_id = :'tid')" if _tid else ""
    # 参数化查询：days通过psql -v传递，避免SQL注入
    # R5修复(扩展性): 添加tenant_id过滤(防止跨租户数据聚合)
    sql = (f"SELECT COUNT(*), COUNT(CASE WHEN roi_score>=70 THEN 1 END), "
           f"COUNT(CASE WHEN roi_score BETWEEN 40 AND 69.99 THEN 1 END), "
           f"COUNT(CASE WHEN roi_score<40 THEN 1 END), "
           f"ROUND(AVG(engagement_score), 2), ROUND(AVG(roi_score), 2), "
           f"ROUND(AVG(views), 0), ROUND(AVG(likes), 1), "
           f"MAX(roi_score), MIN(roi_score) FROM content_publish_log "
           f"WHERE publish_time>=NOW()-INTERVAL '1 day'*:days "
           f"AND status IN ('published','performing_well','needs_optimization','underperforming') {_tf};")
    ok, output = _exec_sql(sql, {"days": str(days), "tid": _tid})
    if not ok or not output:
        _out(True, {"period_days": days, "total_content": 0, "strategies": [],
                     "message": "暂无足够数据"})
        return
    parts = output.split("|")
    if len(parts) < 10:
        _out(False, {}, "统计数据格式错误", "DATA_ERROR")
        return
    try:
        total = int(parts[0])
        performing = int(parts[1])
        needs_opt = int(parts[2])
        underperf = int(parts[3])
        avg_eng = float(parts[4]) if parts[4] else 0
        avg_roi = float(parts[5]) if parts[5] else 0
        avg_views = float(parts[6]) if parts[6] else 0
        avg_likes = float(parts[7]) if parts[7] else 0
        best_roi = float(parts[8]) if parts[8] else 0
        worst_roi = float(parts[9]) if parts[9] else 0

        strategies = []
        if avg_roi < 50:
            strategies.append({"priority": "P0", "type": "urgent", "action": "提升基础互动率",
                               "reason": f"平均ROI({avg_roi:.1f})低于阈值",
                               "suggestion": "增加个性化元素，优化发布时间"})
        if avg_eng < 30:
            strategies.append({"priority": "P1", "type": "engagement", "action": "增强用户参与",
                               "reason": f"平均参与度({avg_eng:.1f})偏低",
                               "suggestion": "添加互动问题、投票等元素"})
        if underperf > total * 0.3:
            strategies.append({"priority": "P1", "type": "content", "action": "内容类型优化",
                               "reason": f"{underperf}篇内容表现不佳(>{total*0.3:.0f}%)",
                               "suggestion": "分析低表现内容共同特征"})
        if best_roi > 70:
            strategies.append({"priority": "P2", "type": "scale", "action": "放大成功模式",
                               "reason": f"最高ROI达到{best_roi:.1f}",
                               "suggestion": "总结高表现内容特征，增加同类产出"})
        if not strategies:
            strategies.append({"priority": "P2", "type": "maintain", "action": "保持当前水平",
                               "reason": f"整体表现稳定(平均ROI={avg_roi:.1f})",
                               "suggestion": "继续监控指标"})

        assessment = "优秀" if avg_roi >= 70 else "良好" if avg_roi >= 50 else "需重点优化"
        _out(True, {"period_days": days,
                     "summary": {"total_content": total, "performing_well": performing,
                                 "needs_optimization": needs_opt, "underperforming": underperf,
                                 "overall_assessment": assessment},
                     "averages": {"engagement_score": avg_eng, "roi_score": avg_roi,
                                  "views": avg_views, "likes": avg_likes},
                     "best_worst": {"best_roi": best_roi, "worst_roi": worst_roi},
                     "strategies": strategies})
    except (ValueError, IndexError) as e:
        _out(False, {}, f"策略生成错误: {e}", "STRATEGY_ERROR")

def do_full_loop(args) -> None:
    """内容闭环全流程: 同步→推荐→反馈→分析→优化→学习

    Fix-B: 先从tenant_publish_records同步真实发布内容(含真实互动指标),
    替代原来创建fake content_id(daily_YYYYMMDD)的行为。
    Fix-C: 学习步骤存储有意义的经验(标题/平台/指标/互动率/ROI/建议),
    替代原来无意义的"content_id=xxx, ROI=0, 等级=需改进"。
    Fix-E: 分析步骤基于真实指标计算ROI,替代原来views=0→ROI=0的问题。

    遵循: 修复提示词R1(运行时证据)/R31(不降级优化)/R43(全局影响分析)/R74(反敷衍修复)
    """
    # Fix-B: 同步真实发布内容到content_publish_log
    synced_ids = _sync_recent_content(days=7)

    if args.content_id:
        cid = args.content_id
    elif synced_ids:
        # 使用最近同步的真实内容(RETURNING按published_at DESC排序,第一条是最新)
        cid = synced_ids[0]
    else:
        # 降级: 无真实发布内容时创建临时记录(仅用于测试/初始化)
        cid = f"daily_{datetime.now().strftime('%Y%m%d')}"
        logger.warning(f"[content-closed-loop] 无可同步的真实发布内容,使用临时content_id={cid}")

    # 查询内容标题、平台和真实指标(用于生成有意义的经验)
    title = args.title or ""
    platform_str = ""
    real_metrics = {}
    tenant_id_for_learn = getattr(args, 'tenant_id', '') or ''  # R5修复: 优先使用CLI传入的tenant_id
    # R8修复(P0+P1): 添加tenant_id过滤+传递tenant_id到_exec_sql设置RLS上下文
    # 根因: 1.content_publish_log启用RLS,不设置app.current_tenant查询返回0行
    #       2.查询无tenant_id过滤可能返回其他租户数据(跨租户泄露)
    query_sql = ("SELECT title, platforms, views, likes, comments, shares, tenant_id "
                 "FROM content_publish_log WHERE content_id=:'cid'")
    _query_pg_vars = {"cid": cid}
    if tenant_id_for_learn:
        query_sql += " AND tenant_id=:'tid'"
        _query_pg_vars["tid"] = tenant_id_for_learn
    query_sql += ";"
    ok, output = _exec_sql(query_sql, _query_pg_vars, tenant_id=tenant_id_for_learn)
    if ok and output:
        parts = output.split("\n")[0].strip().split("|")
        if len(parts) >= 7:
            title = parts[0].strip() if parts[0].strip() else (title or "未命名内容")
            # platforms是TEXT[]格式{douyin,xiaohongshu},去除大括号
            platform_str = parts[1].strip().strip("{}") if parts[1].strip() else "unknown"
            # R5修复: 如果DB有tenant_id且CLI未传,使用DB的tenant_id
            _db_tid = parts[6].strip() if parts[6].strip() else ""
            if _db_tid and not tenant_id_for_learn:
                tenant_id_for_learn = _db_tid
            try:
                real_metrics = {
                    "views": int(parts[2].strip()) if parts[2].strip().lstrip("-").isdigit() else 0,
                    "likes": int(parts[3].strip()) if parts[3].strip().lstrip("-").isdigit() else 0,
                    "comments": int(parts[4].strip()) if parts[4].strip().lstrip("-").isdigit() else 0,
                    "shares": int(parts[5].strip()) if parts[5].strip().lstrip("-").isdigit() else 0,
                }
            except (ValueError, IndexError) as e:
                logger.warning(f"[content-closed-loop] 指标解析失败: {e}")

    steps = {}
    import io
    from contextlib import redirect_stdout

    # Fix-B: 内容已发布时跳过publish步骤(数据已从tenant_publish_records同步)
    if not args.content_id and synced_ids:
        steps["publish"] = {"success": True, "content_id": cid, "skipped": True,
                            "reason": "内容已发布,指标从tenant_publish_records同步"}
    else:
        title = title or f"内容分析_{datetime.now().strftime('%m%d')}"
        args_p = argparse.Namespace(content_id=cid, title=title, content_type="video", topic=None,
                                    platforms=["douyin", "xiaohongshu"], tenant_id=tenant_id_for_learn)
        publish_buf = io.StringIO()
        with redirect_stdout(publish_buf):
            do_publish(args_p)
        publish_data = _parse_step_output(publish_buf.getvalue(), "publish")
        steps["publish"] = {**publish_data, "content_id": cid}

    # do_recommend: 推荐好友
    args_r = argparse.Namespace(content_id=cid, top_k=10, tenant_id=tenant_id_for_learn)
    recommend_buf = io.StringIO()
    with redirect_stdout(recommend_buf):
        do_recommend(args_r)
    recommend_data = _parse_step_output(recommend_buf.getvalue(), "recommend")
    steps["recommend"] = {**recommend_data, "content_id": cid}

    # Fix-E: 反馈步骤 - 真实指标已同步,仍尝试获取更新数据(opencli可用时)
    # R6修复(P2): is_simulated=True表示"尝试获取更新数据但不阻断流程",非纯模拟模式
    # 实际指标已在_sync_recent_content中同步,此步骤会尝试通过opencli获取最新数据
    args_f = argparse.Namespace(content_id=cid, is_simulated=True, tenant_id=tenant_id_for_learn)
    feedback_buf = io.StringIO()
    with redirect_stdout(feedback_buf):
        do_feedback(args_f)
    feedback_data = _parse_step_output(feedback_buf.getvalue(), "feedback")
    steps["feedback"] = {**feedback_data, "content_id": cid}

    # do_analyze: 基于真实指标分析(views/likes等已从tenant_publish_records同步)
    args_a = argparse.Namespace(content_id=cid, tenant_id=tenant_id_for_learn)
    analyze_buf = io.StringIO()
    with redirect_stdout(analyze_buf):
        do_analyze(args_a)
    analyze_data = {}
    try:
        analyze_data = json.loads(analyze_buf.getvalue())
    except Exception as e:
        logger.error(f"content closed loop异常: {e}", exc_info=True)
        logger.warning(f"[content-closed-loop] 分析结果解析失败: {e}")
    steps["analyze"] = {"success": analyze_data.get("success", False), "content_id": cid}

    # do_optimize: 策略优化
    args_o = argparse.Namespace(days=7, tenant_id=tenant_id_for_learn)
    optimize_buf = io.StringIO()
    with redirect_stdout(optimize_buf):
        do_optimize(args_o)
    optimize_data = _parse_step_output(optimize_buf.getvalue(), "optimize")
    steps["optimize"] = {**optimize_data, "content_id": cid}

    # Fix-C: 提取分析结果,生成有意义的经验文本
    roi_score = 0
    perf_level = ""
    if analyze_data.get("success") and analyze_data.get("data", {}).get("analysis"):
        roi_score = analyze_data["data"]["analysis"].get("roi_score", 0)
        perf_level = analyze_data["data"]["analysis"].get("performance_level", "")

    # Fix-C: 生成有意义的经验文本(替代无意义的"content_id=xxx, ROI=0, 等级=需改进")
    # 经验文本包含: 标题/平台/真实指标/互动率/ROI/建议
    # orchestrator的_query_agent_memory_lessons查询此文本并注入到内容生成提示词
    views = real_metrics.get("views", 0)
    likes = real_metrics.get("likes", 0)
    comments = real_metrics.get("comments", 0)
    shares = real_metrics.get("shares", 0)
    engagement_rate = round((likes + comments + shares) / max(views, 1) * 100, 1) if views > 0 else 0

    # 根据表现生成优化建议
    if roi_score >= 70:
        suggestion = "保持当前内容方向,可适当增加同类产出"
    elif roi_score >= 40:
        suggestion = "优化标题吸引力,增加互动引导元素"
    else:
        suggestion = "调整内容选题,参考高表现内容特征,增加个性化元素"

    lesson_text = (
        f"标题'{title}'在{platform_str}: "
        f"播放{views}/赞{likes}/评{comments}/转{shares}, "
        f"互动率{engagement_rate}%, ROI={roi_score}({perf_level}). "
        f"建议: {suggestion}"
    )

    if _GROWTH_SCRIPT.exists():
        try:
            _importance = 8 if roi_score >= 70 else (6 if roi_score >= 50 else 4)
            growth_cmd = [sys.executable, str(_GROWTH_SCRIPT), "--action", "learn",
                          "--scenario", "内容闭环反馈",
                          "--lesson", lesson_text,
                          "--category", "publish_feedback",
                          "--importance", str(_importance),
                          "--agent-id", "default",
                          "--tenant-id", tenant_id_for_learn or "default"]
            growth_result = retry_subprocess(growth_cmd, timeout=15, service="content-closed-loop-growth", retry_on_nonzero=False)
            if growth_result.returncode == 0:
                steps["learn"] = {"success": True, "content_id": cid, "roi_score": roi_score, "lesson": lesson_text}
            else:
                logger.warning(f"[content-closed-loop] self_growth_engine执行失败(返回码{growth_result.returncode}): {growth_result.stderr[:200]}")
                steps["learn"] = {"success": False, "error": f"self_growth_engine执行失败(返回码{growth_result.returncode})", "code": "GROWTH_ENGINE_FAILED"}
        except Exception as e:
            logger.error(f"content closed loop异常: {e}", exc_info=True)
            steps["learn"] = {"success": False, "error": str(e), "code": "GROWTH_ENGINE_EXCEPTION"}
    else:
        logger.warning(f"[content-closed-loop] self_growth_engine.py不存在({_GROWTH_SCRIPT})，学习步骤跳过")
        steps["learn"] = {"success": False, "error": f"self_growth_engine.py not found ({_GROWTH_SCRIPT})", "code": "GROWTH_ENGINE_NOT_FOUND"}

    _out(True, {"loop_id": f"loop_{datetime.now().strftime('%Y%m%d_%H%M%S')}", "content_id": cid,
                 "steps": steps, "overall_success": all(s.get("success", False) for s in steps.values())})

def main():
    parser = argparse.ArgumentParser(description="JueJin内容闭环")
    parser.add_argument("--action", required=True,
                        choices=["full-loop", "publish", "recommend", "feedback", "analyze", "optimize"])
    parser.add_argument("--content-id", dest="content_id", default=None)
    parser.add_argument("--title", default=None)
    parser.add_argument("--content-type", dest="content_type", default="video")
    parser.add_argument("--topic", default=None)
    parser.add_argument("--platforms", nargs="+", default=None)
    parser.add_argument("--top-k", dest="top_k", type=int, default=10)
    parser.add_argument("--auto-feedback", dest="auto_feedback", action="store_true")
    parser.add_argument("--views", type=int, default=0)
    parser.add_argument("--likes", type=int, default=0)
    parser.add_argument("--comments", type=int, default=0)
    parser.add_argument("--shares", type=int, default=0)
    parser.add_argument("--click-rate", dest="click_rate", type=float, default=0)
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--tenant-id", dest="tenant_id", default="", help="租户ID(用于RLS上下文和按租户过滤)")  # R9修复(P1): 支持Cron任务传入租户ID

    args = parser.parse_args()
    actions = {"publish": do_publish, "recommend": do_recommend, "feedback": do_feedback,
               "analyze": do_analyze, "optimize": do_optimize, "full-loop": do_full_loop}
    actions[args.action](args)

if __name__ == "__main__":
    main()
