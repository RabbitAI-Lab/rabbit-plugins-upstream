#!/usr/bin/env python3
"""
AI Daily Briefing - 去重数据库管理
DB 文件:<workspace>/.data/ai-daily-briefing.db
"""

import sqlite3
import hashlib
import re
import os
from pathlib import Path

# DB 路径:优先环境变量,其次 workspace 默认位置
DB_PATH = os.environ.get(
    "AI_DAILY_DB_PATH",
    os.path.expanduser("~/.openclaw/workspace/.data/ai-daily-briefing.db"),
)

# SimHash 实现(纯 Python,无外部依赖)
def _tokenize(text: str) -> list[str]:
    """简单分词:英文按空格+标点,中文按字"""
    # 英文单词
    tokens = re.findall(r'[a-zA-Z0-9_]+', text.lower())
    # 中文单字
    tokens += re.findall(r'[\u4e00-\u9fff]', text)
    return tokens

def _simhash(text: str, hash_bits: int = 64) -> int:
    """
    计算 64 位 SimHash 指纹。
    纯 Python 实现,无外部依赖。
    返回值已转换为有符号 64 位整数(兼容 SQLite INTEGER)。
    """
    tokens = _tokenize(text)
    if not tokens:
        return 0

    # 每位权重累加
    v = [0] * hash_bits

    for token in tokens:
        # 用 MD5 生成稳定的 hash(前 8 字节 = 64 bit)
        h = hashlib.md5(token.encode('utf-8')).digest()
        token_hash = int.from_bytes(h[:8], 'big')

        for i in range(hash_bits):
            bit = (token_hash >> i) & 1
            if bit:
                v[i] += 1
            else:
                v[i] -= 1

    # 生成指纹
    fingerprint = 0
    for i in range(hash_bits):
        if v[i] > 0:
            fingerprint |= (1 << i)

    # 转为有符号 64 位整数(兼容 SQLite INTEGER)
    if fingerprint >= (1 << 63):
        fingerprint -= (1 << 64)

    return fingerprint

def _hamming_distance(a: int, b: int, bits: int = 64) -> int:
    """计算两个 SimHash 指纹的汉明距离(处理有符号整数)"""
    # 转为无符号 64 位再异或
    if a < 0:
        a += (1 << 64)
    if b < 0:
        b += (1 << 64)
    xor = a ^ b
    return bin(xor).count('1')

# ID 提取

def extract_tweet_id(url: str) -> str | None:
    """从 X/Twitter URL 中提取原始推文 ID"""
    # 匹配 x.com/user/status/1234567890 或 twitter.com/user/status/1234567890
    m = re.search(r'(?:x\.com|twitter\.com)/[^/]+/status/(\d+)', url)
    return m.group(1) if m else None

def extract_arxiv_id(url: str) -> str | None:
    """从 arXiv URL 中提取论文 ID"""
    m = re.search(r'arxiv\.org/(?:abs|search)/([^/?]+)', url)
    if m:
        return m.group(1)
    # search URL 格式:arxiv.org/search/?searchtype=all&query=...
    return None

def extract_source_id(url: str, section: str) -> str | None:
    """
    根据板块和数据源 URL 提取唯一 ID。
    X/Twitter: 原始推文 ID
    arXiv: 论文 ID
    GitHub: repo full name
    Product Hunt: product slug
    博客: None(用 URL hash)
    """
    # X/Twitter
    tweet_id = extract_tweet_id(url)
    if tweet_id:
        return f"tweet:{tweet_id}"

    # arXiv
    arxiv_id = extract_arxiv_id(url)
    if arxiv_id:
        return f"arxiv:{arxiv_id}"

    # GitHub
    m = re.search(r'github\.com/([^/]+/[^/]+)', url)
    if m:
        return f"github:{m.group(1).rstrip('/')}"

    # Product Hunt
    m = re.search(r'producthunt\.com/products/([^/?]+)', url)
    if m:
        return f"ph:{m.group(1)}"

    return None

# 数据库操作
def get_db() -> sqlite3.Connection:
    """获取数据库连接,自动建表"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS news_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id TEXT,                    -- 原始 ID(tweet:123, arxiv:2607.08716, github:owner/repo, ph:slug)
            url_hash TEXT,                     -- URL 的 SHA-256
            simhash INTEGER,                   -- title+description 的 64 位 SimHash
            title TEXT,
            url TEXT,
            description TEXT,
            section TEXT,                      -- 板块:industry / agent_eng / frontier / github / producthunt
            collected_date TEXT,               -- 采集日期 YYYY-MM-DD
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_source_id ON news_items(source_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_url_hash ON news_items(url_hash)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_simhash ON news_items(simhash)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_section ON news_items(section)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_date ON news_items(collected_date)")
    conn.commit()
    return conn

def url_hash(url: str) -> str:
    """计算 URL 的 SHA-256"""
    return hashlib.sha256(url.encode('utf-8')).hexdigest()

def is_duplicate(
    conn: sqlite3.Connection,
    title: str,
    url: str,
    description: str,
    section: str,
    simhash_threshold: int = 5,
) -> tuple[bool, str]:
    """
    检查是否重复。

    去重顺序:
    1. source_id 精确匹配(tweet ID / arxiv ID / github repo / PH slug)
    2. URL hash 精确匹配
    3. SimHash 语义近似匹配(同板块内,汉明距离 ≤ threshold)

    返回:(是否重复, 原因)
    """
    # 1. source_id 精确匹配
    sid = extract_source_id(url, section)
    if sid:
        row = conn.execute(
            "SELECT 1 FROM news_items WHERE source_id = ? LIMIT 1", (sid,)
        ).fetchone()
        if row:
            return True, f"source_id 重复: {sid}"

    # 2. URL hash 精确匹配
    uh = url_hash(url)
    row = conn.execute(
        "SELECT 1 FROM news_items WHERE url_hash = ? LIMIT 1", (uh,)
    ).fetchone()
    if row:
        return True, "URL hash 重复"

    # 3. SimHash 近似匹配(同板块内)
    sh = _simhash(f"{title} {description}")

    # 只查最近 30 天的同板块条目,减少计算量
    rows = conn.execute(
        "SELECT simhash, title FROM news_items WHERE section = ? AND collected_date >= date('now', '-30 days')",
        (section,)
    ).fetchall()

    for existing_simhash, existing_title in rows:
        if existing_simhash is not None:
            dist = _hamming_distance(sh, existing_simhash)
            if dist <= simhash_threshold:
                return True, f"SimHash 近似重复 (距离={dist}): {existing_title[:50]}"

    return False, sh  # 返回 simhash 值供插入使用

def insert(
    conn: sqlite3.Connection,
    title: str,
    url: str,
    description: str,
    section: str,
    collected_date: str,
    simhash_value: int | None = None,
) -> int:
    """
    插入一条新闻。如果 simhash_value 已计算则直接用,否则重新计算。
    返回插入的 rowid。
    """
    sid = extract_source_id(url, section)
    uh = url_hash(url)
    if simhash_value is None:
        simhash_value = _simhash(f"{title} {description}")

    cursor = conn.execute(
        """INSERT INTO news_items
           (source_id, url_hash, simhash, title, url, description, section, collected_date)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (sid, uh, simhash_value, title, url, description, section, collected_date)
    )
    conn.commit()
    return cursor.lastrowid

def check_and_insert(
    conn: sqlite3.Connection,
    title: str,
    url: str,
    description: str,
    section: str,
    collected_date: str,
    simhash_threshold: int = 5,
) -> tuple[bool, str]:
    """
    检查去重并插入。如果不重复则插入。

    返回:(是否为重复, 原因或 simhash)
    """
    is_dup, result = is_duplicate(conn, title, url, description, section, simhash_threshold)

    if is_dup:
        return True, result

    # result 是 simhash 值
    insert(conn, title, url, description, section, collected_date, result)
    return False, "插入成功"

def batch_check_and_insert(
    conn: sqlite3.Connection,
    items: list[dict],
    section: str,
    collected_date: str,
    simhash_threshold: int = 5,
) -> dict:
    """
    批量检查去重并插入。

    items: [{"title": ..., "url": ..., "description": ...}, ...]

    返回:
    {
        "total": N,
        "duplicates": M,
        "inserted": K,
        "duplicate_details": [{"title": ..., "reason": ...}, ...]
    }
    """
    total = len(items)
    duplicates = 0
    inserted = 0
    duplicate_details = []

    for item in items:
        is_dup, result = check_and_insert(
            conn,
            item["title"],
            item["url"],
            item.get("description", ""),
            section,
            collected_date,
            simhash_threshold,
        )

        if is_dup:
            duplicates += 1
            duplicate_details.append({"title": item["title"], "reason": result})
        else:
            inserted += 1

    return {
        "total": total,
        "duplicates": duplicates,
        "inserted": inserted,
        "duplicate_details": duplicate_details,
    }

def get_stats(conn: sqlite3.Connection) -> dict:
    """获取数据库统计信息"""
    total = conn.execute("SELECT COUNT(*) FROM news_items").fetchone()[0]
    by_section = conn.execute(
        "SELECT section, COUNT(*) FROM news_items GROUP BY section ORDER BY COUNT(*) DESC"
    ).fetchall()
    by_date = conn.execute(
        "SELECT collected_date, COUNT(*) FROM news_items GROUP BY collected_date ORDER BY collected_date DESC LIMIT 7"
    ).fetchall()

    return {
        "total": total,
        "by_section": {s: c for s, c in by_section},
        "recent_dates": {d: c for d, c in by_date},
    }

def cleanup_old(conn: sqlite3.Connection, days: int = 90) -> int:
    """清理超过 N 天的旧数据,返回删除条数"""
    cursor = conn.execute(
        "DELETE FROM news_items WHERE collected_date < date('now', ?)",
        (f'-{days} days',)
    )
    conn.commit()
    return cursor.rowcount





def _check_cli(title: str, url: str, description: str, section: str, db_path: str = None):
    """去重检查 CLI 实现。"""
    if db_path:
        os.environ["AI_DAILY_DB_PATH"] = db_path
    conn = get_db()
    is_dup, reason = is_duplicate(conn, title, url, description, section)
    if is_dup:
        print(f"DUPLICATE: {reason}")
    else:
        print(f"NEW: {reason}")
    conn.close()


def _insert_cli(input_path: str, section: str, date: str, db_path: str = None):
    """批量入库 CLI 实现。"""
    import json
    if db_path:
        os.environ["AI_DAILY_DB_PATH"] = db_path
    conn = get_db()

    with open(input_path) as f:
        items = json.load(f)

    for item in items:
        check_and_insert(
            conn,
            item["title"],
            item["url"],
            item.get("description", ""),
            section,
            date,
        )

    print(f"Inserted {len(items)} items into section {section}")
if __name__ == "__main__":
    import argparse, json, subprocess, os

    parser = argparse.ArgumentParser(description="AI Daily Briefing - 去重 + URL 校验 + 入库 + 聚合")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # check: 去重检查
    p_check = sub.add_parser("check", help="检查单条是否重复")
    p_check.add_argument("--title", required=True)
    p_check.add_argument("--url", required=True)
    p_check.add_argument("--description", default="")
    p_check.add_argument("--section", required=True)
    p_check.add_argument("--db", default=None)

    # insert: 批量入库
    p_ins = sub.add_parser("insert", help="批量入库")
    p_ins.add_argument("--input", required=True)
    p_ins.add_argument("--section", required=True)
    p_ins.add_argument("--date", required=True)
    p_ins.add_argument("--db", default=None)

    # aggregate: 主 agent 聚合
    p_agg = sub.add_parser("aggregate", help="聚合所有板块,构造飞书卡片并发送")
    p_agg.add_argument("--date", required=True, help="采集日期 YYYY-MM-DD")
    p_agg.add_argument("--db", default=None)
    p_agg.add_argument("--dry-run", action="store_true", help="只输出卡片 JSON,不发送")

    # test: 自测
    p_test = sub.add_parser("test", help="运行自测")

    args = parser.parse_args()

    if args.cmd == "check":
        _check_cli(args.title, args.url, args.description, args.section, args.db)

    elif args.cmd == "insert":
        _insert_cli(args.input, args.section, args.date, args.db)

    elif args.cmd == "aggregate":
        # 聚合所有板块
        from common import load_env, default_output_dir
        load_env()

        date = args.date
        output_dir = default_output_dir(date)
        sections = ["industry", "github", "producthunt", "agent_eng", "frontier"]
        section_titles = {
            "industry": "📢 行业动态",
            "github": "🚀 GitHub Trending Top 5",
            "producthunt": "🏆 Product Hunt Top 5",
            "agent_eng": "🔧 Agent 工程实践",
            "frontier": "🔬 前沿技术研究",
        }

        all_items = {}

        for section in sections:
            path = f"{output_dir}/{section}.json"
            try:
                with open(path) as f:
                    items = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                items = []
            all_items[section] = items

        # 入库
        if args.db:
            os.environ["AI_DAILY_DB_PATH"] = args.db
        conn = get_db()
        for section in sections:
            for item in all_items.get(section, []):
                check_and_insert(conn, item["title"], item["url"], item.get("description", ""), section, date)
        conn.close()

        # 构造飞书卡片
        elements = []
        for section in sections:
            items = all_items.get(section, [])
            if not items:
                continue

            elements.append({"tag": "markdown", "content": f"**{section_titles[section]}**"})

            lines = []
            for item in items:
                line = f"[{item['title']}]({item['url']}) - {item.get('description', '')} · {item.get('metric', '')}"
                lines.append(line)

            elements.append({"tag": "markdown", "content": "\n".join(lines)})
            elements.append({"tag": "hr"})

        elements.append({"tag": "note", "elements": [{"tag": "plain_text", "content": "数据源:Hacker News · GitHub API · Product Hunt · Agent 工程 · 前沿技术研究"}]})

        card = {
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {"tag": "plain_text", "content": f"📡 {date} AI Daily"},
                "template": "blue"
            },
            "elements": elements
        }

        card_json = json.dumps(card, ensure_ascii=False)

        if args.dry_run:
            print(card_json)
        else:
            # 发送飞书卡片
            feishu_app_id = os.environ.get("FEISHU_APP_ID", "")
            feishu_chat_id = os.environ.get("FEISHU_CHAT_ID", "")
            feishu_open_id = os.environ.get("FEISHU_OPEN_ID", "")

            if not feishu_app_id or not feishu_chat_id:
                print("Error: FEISHU_APP_ID or FEISHU_CHAT_ID not set")
                exit(1)

            result = subprocess.run(
                ["lark-cli", "--profile", feishu_app_id, "--as", "bot",
                 "im", "+messages-send",
                 "--chat-id", feishu_chat_id,
                 "--msg-type", "interactive",
                 "--content", card_json],
                capture_output=True, text=True
            )

            if result.returncode != 0:
                # 发送失败,私信用户
                print(f"Card send failed: {result.stderr}")
                if feishu_open_id:
                    subprocess.run(
                        ["lark-cli", "--profile", feishu_app_id, "--as", "bot",
                         "im", "+messages-send",
                         "--user-id", feishu_open_id,
                         "--msg-type", "text",
                         "--content", f'{{"text":"⚠️ AI Daily 发送失败: {result.stderr}"}}'],
                        capture_output=True
                    )
                exit(1)

            print(f"Card sent to {feishu_chat_id}")

    elif args.cmd == "test":
        conn = get_db()
        print(f"DB: {DB_PATH}")
        print(f"Stats: {get_stats(conn)}")

        test_items = [
            {"title": "GPT-5.6 发布", "url": "https://openai.com/blog/gpt-5-6", "description": "OpenAI 发布 GPT-5.6"},
        ]
        for item in test_items:
            is_dup, reason = check_and_insert(conn, item["title"], item["url"], item["description"], "industry", "2026-07-12")
            print(f"  {'DUPE' if is_dup else 'NEW'}: {item['title']} -> {reason}")

        print(f"\nFinal stats: {get_stats(conn)}")
        conn.close()
