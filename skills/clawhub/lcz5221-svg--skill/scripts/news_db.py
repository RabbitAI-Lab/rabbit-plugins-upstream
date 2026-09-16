#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻数据库模块 - SQLite
保存标题/简介/重点时间/地点/人物，用于查重和记录。
"""
import sqlite3
import os
import hashlib
from datetime import datetime

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "news_database")
DB_PATH = os.path.join(DB_DIR, "news.db")


def get_conn():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,            -- 引人注目的标题
            intro TEXT,                     -- 简介
            key_time TEXT,                  -- 重点时间
            location TEXT,                  -- 地点
            people TEXT,                    -- 人物
            content TEXT,                   -- 口播文案（大白话）
            category TEXT,                  -- 国内 / 国际
            source TEXT,                    -- 来源
            url TEXT,                       -- 原文链接
            fingerprint TEXT UNIQUE,        -- 去重指纹
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.commit()
    conn.close()


def fingerprint(title, key_time, location, people):
    """生成查重指纹：标题+时间+地点+人物 不能改变，作为去重依据。"""
    raw = f"{title}|{key_time}|{location}|{people}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def exists(fp):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM news WHERE fingerprint=?", (fp,))
    row = cur.fetchone()
    conn.close()
    return row is not None


def insert_news(record):
    """record: dict with title/intro/key_time/location/people/content/category/source/url"""
    fp = fingerprint(record.get("title", ""), record.get("key_time", ""),
                     record.get("location", ""), record.get("people", ""))
    if exists(fp):
        return False, fp
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO news (title, intro, key_time, location, people, content, category, source, url, fingerprint)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (
        record.get("title", ""),
        record.get("intro", ""),
        record.get("key_time", ""),
        record.get("location", ""),
        record.get("people", ""),
        record.get("content", ""),
        record.get("category", ""),
        record.get("source", ""),
        record.get("url", ""),
        fp,
    ))
    conn.commit()
    conn.close()
    return True, fp


def recent_news(limit=50):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM news ORDER BY id DESC LIMIT ?", (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


if __name__ == "__main__":
    init_db()
    print(f"数据库初始化完成: {DB_PATH}")
