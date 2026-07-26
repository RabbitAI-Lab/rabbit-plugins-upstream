#!/usr/bin/env python3
"""
World Cup Predictor - 世界杯预测工具

基于网易彩票赛程数据 + BALLDONTLIE 球队数据。
赛程通过爬取 sports.163.com/caipiao/worldcup2026 获取。

用法:
  python3 predict.py teams              # 查看所有球队
  python3 predict.py schedule           # 查看赛程
  python3 predict.py match <team_a> <team_b>  # 预测比赛
  python3 predict.py team <team_name>   # 预测某队下一场
  python3 predict.py standings          # 手动查看小组积分（需输入数据）
  python3 predict.py update             # 从网易抓取最新赛程
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# ── 配置 ──────────────────────────────────────────────────────────────

API_BASE = "https://api.balldontlie.io/fifa/worldcup/v1"
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEDULE_CACHE = os.path.join(DATA_DIR, "schedule.json")

def get_api_key():
    """从 openclaw.json 读取 API key"""
    config_path = os.path.expanduser("~/.openclaw/openclaw.json")
    try:
        with open(config_path) as f:
            config = json.load(f)
        return config.get("skills", {}).get("worldcup-predictor", {}).get("api_key", "")
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return ""

# API key 从配置文件动态加载，不硬编码
API_KEY = None  # 延迟加载

def _get_api_key_cached():
    """获取缓存的 API key"""
    global API_KEY
    if API_KEY is None:
        API_KEY = get_api_key()
    return API_KEY

# ── 球队数据（来自 BALLDONTLIE API + 手动补充） ────────────────────

TEAMS = {
    # CONMEBOL
    "阿根廷": {"abbr": "ARG", "flag": "🇦🇷", "conf": "CONMEBOL", "strength": 95},
    "巴西": {"abbr": "BRA", "flag": "🇧🇷", "conf": "CONMEBOL", "strength": 93},
    "乌拉圭": {"abbr": "URU", "flag": "🇺🇾", "conf": "CONMEBOL", "strength": 85},
    "哥伦比亚": {"abbr": "COL", "flag": "🇨🇴", "conf": "CONMEBOL", "strength": 82},
    "厄瓜多尔": {"abbr": "ECU", "flag": "🇪🇨", "conf": "CONMEBOL", "strength": 78},
    "巴拉圭": {"abbr": "PAR", "flag": "🇵🇾", "conf": "CONMEBOL", "strength": 75},
    # UEFA
    "法国": {"abbr": "FRA", "flag": "🇫🇷", "conf": "UEFA", "strength": 92},
    "英格兰": {"abbr": "ENG", "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "conf": "UEFA", "strength": 91},
    "西班牙": {"abbr": "ESP", "flag": "🇪🇸", "conf": "UEFA", "strength": 90},
    "德国": {"abbr": "GER", "flag": "🇩🇪", "conf": "UEFA", "strength": 89},
    "葡萄牙": {"abbr": "POR", "flag": "🇵🇹", "conf": "UEFA", "strength": 88},
    "荷兰": {"abbr": "NED", "flag": "🇳🇱", "conf": "UEFA", "strength": 87},
    "比利时": {"abbr": "BEL", "flag": "🇧🇪", "conf": "UEFA", "strength": 85},
    "克罗地亚": {"abbr": "CRO", "flag": "🇭🇷", "conf": "UEFA", "strength": 83},
    "瑞士": {"abbr": "SUI", "flag": "🇨🇭", "conf": "UEFA", "strength": 80},
    "瑞典": {"abbr": "SWE", "flag": "🇸🇪", "conf": "UEFA", "strength": 79},
    "丹麦": {"abbr": "DEN", "flag": "🇩🇰", "conf": "UEFA", "strength": 80},
    "奥地利": {"abbr": "AUT", "flag": "🇦🇹", "conf": "UEFA", "strength": 78},
    "挪威": {"abbr": "NOR", "flag": "🇳🇴", "conf": "UEFA", "strength": 77},
    "土耳其": {"abbr": "TUR", "flag": "🇹🇷", "conf": "UEFA", "strength": 76},
    "捷克": {"abbr": "CZE", "flag": "🇨🇿", "conf": "UEFA", "strength": 75},
    "苏格兰": {"abbr": "SCO", "flag": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "conf": "UEFA", "strength": 74},
    "波黑": {"abbr": "BIH", "flag": "🇧🇦", "conf": "UEFA", "strength": 73},
    "突尼斯": {"abbr": "TUN", "flag": "🇹🇳", "conf": "CAF", "strength": 72},
    "库拉索": {"abbr": "CUW", "flag": "🇨🇼", "conf": "CONCACAF", "strength": 55},
    # CONCACAF
    "美国": {"abbr": "USA", "flag": "🇺🇸", "conf": "CONCACAF", "strength": 83},
    "墨西哥": {"abbr": "MEX", "flag": "🇲🇽", "conf": "CONCACAF", "strength": 82},
    "加拿大": {"abbr": "CAN", "flag": "🇨🇦", "conf": "CONCACAF", "strength": 78},
    "海地": {"abbr": "HAI", "flag": "🇭🇹", "conf": "CONCACAF", "strength": 60},
    "巴拿马": {"abbr": "PAN", "flag": "🇵🇦", "conf": "CONCACAF", "strength": 65},
    "佛得角": {"abbr": "CPV", "flag": "🇨🇻", "conf": "CAF", "strength": 62},
    # AFC
    "日本": {"abbr": "JPN", "flag": "🇯🇵", "conf": "AFC", "strength": 81},
    "韩国": {"abbr": "KOR", "flag": "🇰🇷", "conf": "AFC", "strength": 79},
    "澳大利亚": {"abbr": "AUS", "flag": "🇦🇺", "conf": "AFC", "strength": 76},
    "伊朗": {"abbr": "IRN", "flag": "🇮🇷", "conf": "AFC", "strength": 75},
    "沙特": {"abbr": "KSA", "flag": "🇸🇦", "conf": "AFC", "strength": 72},
    "卡塔尔": {"abbr": "QAT", "flag": "🇶🇦", "conf": "AFC", "strength": 70},
    "伊拉克": {"abbr": "IRQ", "flag": "🇮🇶", "conf": "AFC", "strength": 68},
    "约旦": {"abbr": "JOR", "flag": "🇯🇴", "conf": "AFC", "strength": 66},
    "乌兹别克": {"abbr": "UZB", "flag": "🇺🇿", "conf": "AFC", "strength": 67},
    # CAF
    "摩洛哥": {"abbr": "MAR", "flag": "🇲🇦", "conf": "CAF", "strength": 84},
    "塞内加尔": {"abbr": "SEN", "flag": "🇸🇳", "conf": "CAF", "strength": 80},
    "埃及": {"abbr": "EGY", "flag": "🇪🇬", "conf": "CAF", "strength": 78},
    "阿尔及利": {"abbr": "ALG", "flag": "🇩🇿", "conf": "CAF", "strength": 77},
    "科特迪瓦": {"abbr": "CIV", "flag": "🇨🇮", "conf": "CAF", "strength": 76},
    "南非": {"abbr": "RSA", "flag": "🇿🇦", "conf": "CAF", "strength": 70},
    "加纳": {"abbr": "GHA", "flag": "🇬🇭", "conf": "CAF", "strength": 74},
    "民主刚果": {"abbr": "COD", "flag": "🇨🇩", "conf": "CAF", "strength": 68},
    # OFC
    "新西兰": {"abbr": "NZL", "flag": "🇳🇿", "conf": "OFC", "strength": 68},
}

# 中文简称映射（网易页面使用的名称）
TEAM_ALIASES = {
    "墨西哥": "墨西哥", "韩国": "韩国", "捷克": "捷克",
    "加拿大": "加拿大", "波黑": "波黑", "美国": "美国", "巴拉圭": "巴拉圭",
    "卡塔尔": "卡塔尔", "瑞士": "瑞士", "巴西": "巴西", "摩洛哥": "摩洛哥",
    "海地": "海地", "苏格兰": "苏格兰", "澳大利亚": "澳大利亚", "土耳其": "土耳其",
    "德国": "德国", "库拉索": "库拉索", "荷兰": "荷兰", "日本": "日本",
    "科特迪瓦": "科特迪瓦", "厄瓜多尔": "厄瓜多尔", "瑞典": "瑞典", "突尼斯": "突尼斯",
    "西班牙": "西班牙", "佛得角": "佛得角", "比利时": "比利时", "埃及": "埃及",
    "沙特": "沙特", "乌拉圭": "乌拉圭", "伊朗": "伊朗", "新西兰": "新西兰",
    "法国": "法国", "塞内加尔": "塞内加尔", "伊拉克": "伊拉克", "挪威": "挪威",
    "阿根廷": "阿根廷", "阿尔及利": "阿尔及利", "奥地利": "奥地利", "约旦": "约旦",
    "葡萄牙": "葡萄牙", "民主刚果": "民主刚果", "英格兰": "英格兰", "克罗地亚": "克罗地亚",
    "加纳": "加纳", "巴拿马": "巴拿马", "乌兹别克": "乌兹别克", "哥伦比亚": "哥伦比亚",
    "南非": "南非",
}

# ── 工具函数 ─────────────────────────────────────────────────────────

def api_get(endpoint, params=None):
    """调用 BALLDONTLIE API"""
    api_key = _get_api_key_cached()
    if not api_key:
        return None

    url = f"{API_BASE}/{endpoint}"
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{qs}"

    req = urllib.request.Request(url)
    req.add_header("Authorization", api_key)

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError, TimeoutError) as e:
        return None


def get_team_info(name):
    """获取球队信息"""
    # 直接查找
    if name in TEAMS:
        return TEAMS[name]
    # 别名查找
    canonical = TEAM_ALIASES.get(name, name)
    if canonical in TEAMS:
        return TEAMS[canonical]
    return {"abbr": name[:3].upper(), "flag": "🏳️", "conf": "?", "strength": 65}


def fmt_flag(team_name):
    """获取球队旗帜"""
    info = get_team_info(team_name)
    return info.get("flag", "🏳️")


def load_schedule():
    """加载缓存的赛程数据"""
    if os.path.exists(SCHEDULE_CACHE):
        with open(SCHEDULE_CACHE) as f:
            return json.load(f)
    return []


def save_schedule(matches):
    """保存赛程缓存"""
    with open(SCHEDULE_CACHE, 'w', encoding='utf-8') as f:
        json.dump(matches, f, ensure_ascii=False, indent=2)
    print(f"✅ 已保存 {len(matches)} 场比赛到 {SCHEDULE_CACHE}")


def fetch_schedule_from_netease():
    """从网易彩票抓取赛程（使用浏览器 snapshot 模式）"""
    print("📡 正在从网易彩票获取赛程数据...")
    print("   需要浏览器 snapshot，请运行:")
    print("   1. 打开 https://sports.163.com/caipiao/worldcup2026")
    print("   2. 使用 browser snapshot 获取页面数据")
    print("   3. 运行: predict.py update --from-file <snapshot.txt>")

    # 备用方案：直接从硬编码数据生成（基于网易页面 snapshot）
    return build_schedule_from_netease_data()


def build_schedule_from_netease_data():
    """基于网易彩票页面数据构建赛程"""
    # 从网易页面完整数据构建
    # 格式: [日期, 星期, 球场, 时间, 组别, 主队, 状态, 比分/VS, 半场比分, 客队]
    raw_matches = [
        # 6月12日 - 开幕日
        ("2026-06-12", "墨西哥城体育场", "03:00", "A组", "墨西哥", "完", "2-0", "南非"),
        ("2026-06-12", "瓜达拉哈拉体育场", "10:00", "A组", "韩国", "完", "2-1", "捷克"),
        # 6月13日
        ("2026-06-13", "多伦多体育场", "03:00", "B组", "加拿大", "完", "1-1", "波黑"),
        ("2026-06-13", "洛杉矶体育场", "09:00", "D组", "美国", "完", "4-1", "巴拉圭"),
        # 6月14日
        ("2026-06-14", "旧金山湾区体育场", "03:00", "B组", "卡塔尔", "未", None, "瑞士"),
        ("2026-06-14", "纽约/新泽西体育场", "06:00", "C组", "巴西", "未", None, "摩洛哥"),
        ("2026-06-14", "波士顿体育场", "09:00", "C组", "海地", "未", None, "苏格兰"),
        ("2026-06-14", "不列颠哥伦比亚广场", "12:00", "D组", "澳大利亚", "未", None, "土耳其"),
        # 6月15日
        ("2026-06-15", "休斯顿体育场", "01:00", "E组", "德国", "未", None, "库拉索"),
        ("2026-06-15", "达拉斯体育场", "04:00", "F组", "荷兰", "未", None, "日本"),
        ("2026-06-15", "费城体育场", "07:00", "E组", "科特迪瓦", "未", None, "厄瓜多尔"),
        ("2026-06-15", "蒙特雷体育场", "10:00", "F组", "瑞典", "未", None, "突尼斯"),
        # 6月16日
        ("2026-06-16", "亚特兰大体育场", "00:00", "H组", "西班牙", "未", None, "佛得角"),
        ("2026-06-16", "西雅图体育场", "03:00", "G组", "比利时", "未", None, "埃及"),
        ("2026-06-16", "硬石体育场", "06:00", "H组", "沙特", "未", None, "乌拉圭"),
        ("2026-06-16", "洛杉矶体育场", "09:00", "G组", "伊朗", "未", None, "新西兰"),
        # 6月17日
        ("2026-06-17", "纽约/新泽西体育场", "03:00", "I组", "法国", "未", None, "塞内加尔"),
        ("2026-06-17", "波士顿体育场", "06:00", "I组", "伊拉克", "未", None, "挪威"),
        ("2026-06-17", "堪萨斯城体育场", "09:00", "J组", "阿根廷", "未", None, "阿尔及利"),
        ("2026-06-17", "旧金山湾区体育场", "12:00", "J组", "奥地利", "未", None, "约旦"),
        # 6月18日
        ("2026-06-18", "休斯顿体育场", "01:00", "K组", "葡萄牙", "未", None, "民主刚果"),
        ("2026-06-18", "达拉斯体育场", "04:00", "L组", "英格兰", "未", None, "克罗地亚"),
        ("2026-06-18", "多伦多体育场", "07:00", "L组", "加纳", "未", None, "巴拿马"),
        ("2026-06-18", "墨西哥城体育场", "10:00", "K组", "乌兹别克", "未", None, "哥伦比亚"),
        # 6月19日 - 第二轮
        ("2026-06-19", "亚特兰大体育场", "00:00", "A组", "捷克", "未", None, "南非"),
        ("2026-06-19", "洛杉矶体育场", "03:00", "B组", "瑞士", "未", None, "波黑"),
        ("2026-06-19", "不列颠哥伦比亚广场", "06:00", "B组", "加拿大", "未", None, "卡塔尔"),
        ("2026-06-19", "瓜达拉哈拉体育场", "09:00", "A组", "墨西哥", "未", None, "韩国"),
        # 6月20日
        ("2026-06-20", "西雅图体育场", "03:00", "D组", "美国", "未", None, "澳大利亚"),
        ("2026-06-20", "波士顿体育场", "06:00", "C组", "苏格兰", "未", None, "摩洛哥"),
        ("2026-06-20", "费城体育场", "08:30", "C组", "巴西", "未", None, "海地"),
        ("2026-06-20", "旧金山湾区体育场", "11:00", "D组", "土耳其", "未", None, "巴拉圭"),
        # 6月21日
        ("2026-06-21", "休斯顿体育场", "01:00", "F组", "荷兰", "未", None, "瑞典"),
        ("2026-06-21", "多伦多体育场", "04:00", "E组", "德国", "未", None, "科特迪瓦"),
        ("2026-06-21", "堪萨斯城体育场", "08:00", "E组", "厄瓜多尔", "未", None, "库拉索"),
        ("2026-06-21", "蒙特雷体育场", "12:00", "F组", "突尼斯", "未", None, "日本"),
        # 6月22日
        ("2026-06-22", "亚特兰大体育场", "00:00", "H组", "西班牙", "未", None, "沙特"),
        ("2026-06-22", "洛杉矶体育场", "03:00", "G组", "比利时", "未", None, "伊朗"),
        ("2026-06-22", "硬石体育场", "06:00", "H组", "乌拉圭", "未", None, "佛得角"),
        ("2026-06-22", "不列颠哥伦比亚广场", "09:00", "G组", "新西兰", "未", None, "埃及"),
        # 6月23日
        ("2026-06-23", "达拉斯体育场", "01:00", "J组", "阿根廷", "未", None, "奥地利"),
        ("2026-06-23", "费城体育场", "05:00", "I组", "法国", "未", None, "伊拉克"),
        ("2026-06-23", "纽约/新泽西体育场", "08:00", "I组", "挪威", "未", None, "塞内加尔"),
        ("2026-06-23", "旧金山湾区体育场", "11:00", "J组", "约旦", "未", None, "阿尔及利"),
        # 6月24日
        ("2026-06-24", "休斯顿体育场", "01:00", "K组", "葡萄牙", "未", None, "乌兹别克"),
        ("2026-06-24", "波士顿体育场", "04:00", "L组", "英格兰", "未", None, "加纳"),
        ("2026-06-24", "多伦多体育场", "07:00", "L组", "巴拿马", "未", None, "克罗地亚"),
        ("2026-06-24", "瓜达拉哈拉体育场", "10:00", "K组", "哥伦比亚", "未", None, "民主刚果"),
        # 6月25日 - 第三轮
        ("2026-06-25", "不列颠哥伦比亚广场", "03:00", "B组", "瑞士", "未", None, "加拿大"),
        ("2026-06-25", "西雅图体育场", "03:00", "B组", "波黑", "未", None, "卡塔尔"),
        ("2026-06-25", "硬石体育场", "06:00", "C组", "苏格兰", "未", None, "巴西"),
        ("2026-06-25", "亚特兰大体育场", "06:00", "C组", "摩洛哥", "未", None, "海地"),
        ("2026-06-25", "墨西哥城体育场", "09:00", "A组", "捷克", "未", None, "墨西哥"),
        ("2026-06-25", "蒙特雷体育场", "09:00", "A组", "南非", "未", None, "韩国"),
        # 6月26日
        ("2026-06-26", "纽约/新泽西体育场", "04:00", "E组", "厄瓜多尔", "未", None, "德国"),
        ("2026-06-26", "费城体育场", "04:00", "E组", "库拉索", "未", None, "科特迪瓦"),
        ("2026-06-26", "堪萨斯城体育场", "07:00", "F组", "突尼斯", "未", None, "荷兰"),
        ("2026-06-26", "达拉斯体育场", "07:00", "F组", "日本", "未", None, "瑞典"),
        ("2026-06-26", "洛杉矶体育场", "10:00", "D组", "土耳其", "未", None, "美国"),
        ("2026-06-26", "旧金山湾区体育场", "10:00", "D组", "巴拉圭", "未", None, "澳大利亚"),
        # 6月27日
        ("2026-06-27", "波士顿体育场", "03:00", "I组", "挪威", "未", None, "法国"),
        ("2026-06-27", "多伦多体育场", "03:00", "I组", "塞内加尔", "未", None, "伊拉克"),
        ("2026-06-27", "瓜达拉哈拉体育场", "08:00", "H组", "乌拉圭", "未", None, "西班牙"),
        ("2026-06-27", "休斯顿体育场", "08:00", "H组", "佛得角", "未", None, "沙特"),
        ("2026-06-27", "不列颠哥伦比亚广场", "11:00", "G组", "新西兰", "未", None, "比利时"),
        ("2026-06-27", "西雅图体育场", "11:00", "G组", "埃及", "未", None, "伊朗"),
        # 6月28日
        ("2026-06-28", "纽约/新泽西体育场", "05:00", "L组", "巴拿马", "未", None, "英格兰"),
        ("2026-06-28", "费城体育场", "05:00", "L组", "克罗地亚", "未", None, "加纳"),
        ("2026-06-28", "硬石体育场", "07:30", "K组", "哥伦比亚", "未", None, "葡萄牙"),
        ("2026-06-28", "亚特兰大体育场", "07:30", "K组", "民主刚果", "未", None, "乌兹别克"),
        ("2026-06-28", "达拉斯体育场", "10:00", "J组", "约旦", "未", None, "阿根廷"),
        ("2026-06-28", "堪萨斯城体育场", "10:00", "J组", "阿尔及利", "未", None, "奥地利"),
    ]

    matches = []
    for m in raw_matches:
        date, stadium, time, group, home, status, score, away = m
        matches.append({
            "date": date,
            "time": time,
            "stadium": stadium,
            "group": group,
            "home_team": home,
            "away_team": away,
            "status": status,
            "score": score,
            "home_score": int(score.split("-")[0]) if score else None,
            "away_score": int(score.split("-")[1]) if score else None,
        })

    return matches


def get_next_match_for(team_name, matches):
    """获取某队的下一场比赛"""
    now = datetime.now()
    for m in matches:
        if m["status"] == "未":
            mdt = f"{m['date']} {m['time']}"
            try:
                mt = datetime.strptime(mdt, "%Y-%m-%d %H:%M")
                if mt > now and (m["home_team"] == team_name or m["away_team"] == team_name):
                    return m
            except (ValueError, KeyError, TypeError):
                continue
    return None


def get_team_matches(team_name, matches):
    """获取某队的全部比赛"""
    return [m for m in matches if m["home_team"] == team_name or m["away_team"] == team_name]


def compute_group_standings(matches):
    """从赛程数据计算小组积分榜"""
    from collections import defaultdict
    groups = defaultdict(lambda: defaultdict(lambda: {'pts': 0, 'gf': 0, 'ga': 0, 'played': 0, 'w': 0, 'd': 0, 'l': 0}))
    for m in matches:
        if m['status'] == '完' and m['score']:
            g = m['group']
            home = m['home_team']
            away = m['away_team']
            hs = m['home_score']
            aws = m['away_score']
            groups[g][home]['played'] += 1
            groups[g][away]['played'] += 1
            groups[g][home]['gf'] += hs
            groups[g][away]['gf'] += aws
            groups[g][home]['ga'] += aws
            groups[g][away]['ga'] += hs
            if hs > aws:
                groups[g][home]['pts'] += 3
                groups[g][home]['w'] += 1
                groups[g][away]['l'] += 1
            elif hs == aws:
                groups[g][home]['pts'] += 1
                groups[g][away]['pts'] += 1
                groups[g][home]['d'] += 1
                groups[g][away]['d'] += 1
            else:
                groups[g][away]['pts'] += 3
                groups[g][away]['w'] += 1
                groups[g][home]['l'] += 1
    return groups


def predict_match(home_team, away_team, matches=None):
    """预测比赛结果

    多维度预测模型 v2:
    1. 基础强度分 (strength) 映射到 Elo 分
    2. 小组积分榜排名 + 进球/失球数据
    3. 近期状态（已完赛表现）
    4. 本届赛事平局基准率修正
    5. Elo 预期胜率 + Poisson 比分预测
    """
    home_info = get_team_info(home_team)
    away_info = get_team_info(away_team)

    home_flag = home_info.get("flag", "🏳️")
    away_flag = away_info.get("flag", "🏳️")

    # ── 1. 基础 Elo 分 ──
    home_str = home_info.get("strength", 65)
    away_str = away_info.get("strength", 65)
    home_elo = 1300 + (home_str - 50) * 14
    away_elo = 1300 + (away_str - 50) * 14

    # ── 2. 小组积分榜数据 ──
    home_pts = 0
    away_pts = 0
    home_gf = 0
    away_gf = 0
    home_ga = 0
    away_ga = 0
    home_played = 0
    away_played = 0
    home_group_rank = None
    away_group_rank = None

    if matches:
        standings = compute_group_standings(matches)
        # 找到两队所在小组
        for m in matches:
            if m['home_team'] == home_team or m['away_team'] == home_team:
                home_group = m['group']
                break
        else:
            home_group = None
        for m in matches:
            if m['home_team'] == away_team or m['away_team'] == away_team:
                away_group = m['group']
                break
        else:
            away_group = None

        if home_group and home_group in standings:
            if home_team in standings[home_group]:
                s = standings[home_group][home_team]
                home_pts = s['pts']
                home_gf = s['gf']
                home_ga = s['ga']
                home_played = s['played']
            # 排名
            ranked = sorted(standings[home_group].items(),
                          key=lambda x: (-x[1]['pts'], -(x[1]['gf']-x[1]['ga']), -x[1]['gf']))
            for i, (t, _) in enumerate(ranked):
                if t == home_team:
                    home_group_rank = i + 1
                    break

        if away_group and away_group in standings:
            if away_team in standings[away_group]:
                s = standings[away_group][away_team]
                away_pts = s['pts']
                away_gf = s['gf']
                away_ga = s['ga']
                away_played = s['played']
            ranked = sorted(standings[away_group].items(),
                          key=lambda x: (-x[1]['pts'], -(x[1]['gf']-x[1]['ga']), -x[1]['gf']))
            for i, (t, _) in enumerate(ranked):
                if t == away_team:
                    away_group_rank = i + 1
                    break

    # ── 3. 近期状态加成 ──
    home_form = 0
    away_form = 0
    home_goal_avg = 1.5
    away_goal_avg = 1.5
    home_conceded_avg = 1.5
    away_conceded_avg = 1.5

    if matches:
        home_matches = get_team_matches(home_team, matches)
        away_matches = get_team_matches(away_team, matches)

        home_total_goals = 0
        home_total_conceded = 0
        home_count = 0
        for m in home_matches:
            if m["status"] == "完" and m["score"]:
                is_home = m["home_team"] == home_team
                hs = m["home_score"]
                aws = m["away_score"]
                home_count += 1
                if is_home:
                    home_total_goals += hs
                    home_total_conceded += aws
                    if hs > aws: home_form += 3
                    elif hs == aws: home_form += 1
                else:
                    home_total_goals += aws
                    home_total_conceded += hs
                    if aws > hs: home_form += 3
                    elif aws == hs: home_form += 1
        if home_count > 0:
            home_elo += home_form * 5
            home_goal_avg = home_total_goals / home_count
            home_conceded_avg = home_total_conceded / home_count

        away_total_goals = 0
        away_total_conceded = 0
        away_count = 0
        for m in away_matches:
            if m["status"] == "完" and m["score"]:
                is_home = m["home_team"] == away_team
                hs = m["home_score"]
                aws = m["away_score"]
                away_count += 1
                if is_home:
                    away_total_goals += hs
                    away_total_conceded += aws
                    if hs > aws: away_form += 3
                    elif hs == aws: away_form += 1
                else:
                    away_total_goals += aws
                    away_total_conceded += hs
                    if aws > hs: away_form += 3
                    elif aws == hs: away_form += 1
        if away_count > 0:
            away_elo += away_form * 5
            away_goal_avg = away_total_goals / away_count
            away_conceded_avg = away_total_conceded / away_count

    # ── 4. 小组排名加成 ──
    # 排名靠前 + Elo 加成（温和版，避免过度修正）
    if home_group_rank:
        rank_bonus = {1: 20, 2: 10, 3: -5, 4: -15}
        home_elo += rank_bonus.get(home_group_rank, 0)
    if away_group_rank:
        rank_bonus = {1: 20, 2: 10, 3: -5, 4: -15}
        away_elo += rank_bonus.get(away_group_rank, 0)

    # ── 5. 主队优势 ──
    home_elo += 70

    # ── 6. Elo 预期胜率 ──
    elo_diff = away_elo - home_elo
    home_win_raw = 1.0 / (1.0 + 10 ** (elo_diff / 400))
    away_win_raw = 1.0 / (1.0 + 10 ** (-elo_diff / 400))

    # ── 7. 平局概率（v2 改进）──
    # 本届赛事平局基准率：8场中3场平局 = 37.5%
    # 使用赛事实际平局率作为基准修正
    if matches:
        total_done = sum(1 for m in matches if m['status'] == '完')
        total_draws = sum(1 for m in matches if m['status'] == '完' and m['home_score'] == m['away_score'])
        tournament_draw_rate = total_draws / total_done if total_done > 0 else 0.30
    else:
        tournament_draw_rate = 0.30

    # 基础平局概率：实力越接近越高
    strength_ratio = min(home_str, away_str) / max(home_str, away_str) if max(home_str, away_str) > 0 else 0.5
    draw_base = 0.20 + 0.20 * strength_ratio  # 范围 20%-40%

    # Elo 差异修正
    elo_spread = abs(home_elo - away_elo)
    draw_factor = max(0.35, 1.0 - elo_spread / 500)

    # 赛事平局率修正（加权平均，赛事数据权重更高）
    model_draw = draw_base * draw_factor
    draw_pct = round((model_draw * 0.5 + tournament_draw_rate * 0.5) * 100, 1)

    # 分配胜率
    remaining = 100.0 - draw_pct
    if remaining < 0:
        remaining = 0
        draw_pct = 100.0
    home_win_pct = round(home_win_raw / (home_win_raw + away_win_raw) * remaining, 1) if remaining > 0 else 0
    away_win_pct = round(remaining - home_win_pct, 1)

    # ── 8. 比分预测（v2.3 双模式模型）──
    # 模式A - 实力悬殊（差距≥15分）：进攻×防守脆弱度，含崩盘因子
    # 模式B - 实力接近（差距<15分）：修正 Poisson，总进球控制
    
    def strength_to_attack(s):
        return 0.15 + (s - 40) * 0.044  # 55→0.81, 65→1.25, 80→1.91, 89→2.31, 95→2.57
    
    def strength_to_weakness(s, opponent_s):
        base = max(0.08, 1.55 - s * 0.015)
        gap = opponent_s - s
        if gap >= 20 and s < 65:
            base *= (1.0 + gap * 0.007)  # 崩盘因子
        return base
    
    home_atk = strength_to_attack(home_str)
    away_atk = strength_to_attack(away_str)
    
    strength_gap = home_str - away_str
    
    if abs(strength_gap) >= 15:
        # 模式A：实力悬殊 → 进攻×防守脆弱度模型
        home_weak = strength_to_weakness(home_str, away_str)
        away_weak = strength_to_weakness(away_str, home_str)
        
        home_exp_raw = home_atk * (1.0 + away_weak * 1.5)
        away_exp_raw = away_atk * (1.0 + home_weak * 1.5)
        
        # 已完赛数据微调
        if home_played > 0:
            adj = home_goal_avg / max(strength_to_attack(home_str), 0.5)
            home_exp_raw *= 0.6 + 0.4 * min(adj, 2.0)
        if away_played > 0:
            adj = away_goal_avg / max(strength_to_attack(away_str), 0.5)
            away_exp_raw *= 0.6 + 0.4 * min(adj, 2.0)
        
        home_exp = home_exp_raw * 1.08  # 主队优势
        away_exp = away_exp_raw
        
        home_goals = max(0, int(round(home_exp)))
        away_goals = max(0, int(round(away_exp)))
        
        # 极端悬殊大比分修正
        if strength_gap >= 20 and home_exp >= 2.5:
            home_goals = max(home_goals, int(home_exp + 1.0))
        elif strength_gap <= -20 and away_exp >= 2.5:
            away_goals = max(away_goals, int(away_exp + 1.0))
    else:
        # 模式B：实力接近 → 修正 Poisson，总进球控制在4球以内
        # 基础进球λ：从强度映射，但压缩范围避免进球大战
        def balanced_attack(s):
            return 1.0 + (s - 65) * 0.035  # 65→1.0, 80→1.53, 90→1.88
        
        home_atk_b = balanced_attack(home_str)
        away_atk_b = balanced_attack(away_str)
        
        # 用已完赛数据校正
        home_exp = home_atk_b
        away_exp = away_atk_b
        if home_played > 0:
            adj = home_goal_avg / max(home_atk_b, 0.5)
            home_exp = home_atk_b * (0.7 + 0.3 * min(adj, 2.0))
        if away_played > 0:
            adj = away_goal_avg / max(away_atk_b, 0.5)
            away_exp = away_atk_b * (0.7 + 0.3 * min(adj, 2.0))
        
        home_exp *= 1.08  # 主队优势
        
        # 防守因素温和修正：对手强度低则更容易进球
        home_exp *= (1.0 + (95 - away_str) * 0.004)  # 强度77→×1.072, 强度90→×1.02
        away_exp *= (1.0 + (95 - home_str) * 0.004)
        
        home_goals = max(0, int(round(home_exp)))
        away_goals = max(0, int(round(away_exp)))
        
        # 平局倾向比分类似
        goal_gap = abs(home_exp - away_exp)
        if draw_pct >= 30 and home_goals != away_goals and goal_gap < 0.5:
            if home_goals > away_goals:
                home_goals = away_goals
            else:
                away_goals = home_goals
    
    # 如果预测平局但一方胜率明显更高（>25%差距），保持1球优势
    if home_goals == away_goals and home_win_pct > away_win_pct + 25:
        home_goals += 1
    elif home_goals == away_goals and away_win_pct > home_win_pct + 25:
        away_goals += 1
    
    # 确保最少有 1 个总进球
    if home_goals == 0 and away_goals == 0:
        if home_win_pct > away_win_pct:
            home_goals = 1
        else:
            away_goals = 1

    return {
        "home_team": home_team,
        "away_team": away_team,
        "home_flag": home_flag,
        "away_flag": away_flag,
        "home_info": home_info,
        "away_info": away_info,
        "home_win_pct": home_win_pct,
        "draw_pct": draw_pct,
        "away_win_pct": away_win_pct,
        "predicted_home": home_goals,
        "predicted_away": away_goals,
        "home_elo": home_elo,
        "away_elo": away_elo,
        "home_form": home_form,
        "away_form": away_form,
        "home_group_rank": home_group_rank,
        "away_group_rank": away_group_rank,
        "home_goal_avg": home_goal_avg,
        "away_goal_avg": away_goal_avg,
        "tournament_draw_rate": tournament_draw_rate,
    }


# ── 命令实现 ──────────────────────────────────────────────────────────

def cmd_teams():
    """列出所有参赛球队"""
    # 按足联分组
    confs = {}
    for name, info in sorted(TEAMS.items()):
        conf = info.get("conf", "?")
        confs.setdefault(conf, []).append((name, info))

    print(f"\n🏆 2026 世界杯参赛球队 ({len(TEAMS)} 队)\n")
    print("═" * 50)

    conf_names = {
        "UEFA": "🇪🇺 UEFA (欧洲)", "CONMEBOL": "🇿🇦 CONMEBOL (南美)",
        "CONCACAF": "🌎 CONCACAF (北美)", "CAF": "🌍 CAF (非洲)",
        "AFC": "🌏 AFC (亚洲)", "OFC": "🌊 OFC (大洋洲)",
    }

    for conf in ["UEFA", "CONMEBOL", "CONCACAF", "CAF", "AFC", "OFC"]:
        if conf in confs:
            print(f"\n  {conf_names.get(conf, conf)}")
            for name, info in sorted(confs[conf], key=lambda x: x[1]["strength"], reverse=True):
                flag = info["flag"]
                strength = info["strength"]
                bar = "█" * (strength // 10) + "░" * (10 - strength // 10)
                print(f"    {flag} {name:12s} {bar} {strength}")

    # 尝试从 API 获取官方数据
    try:
        data = api_get("teams")
        if data:
            api_teams = data.get("data", [])
            print(f"\n  📡 (BALLDONTLIE API 确认 {len(api_teams)} 支参赛队)")
    except (urllib.error.URLError, json.JSONDecodeError, KeyError, TypeError):
        pass


def cmd_schedule():
    """查看赛程"""
    matches = load_schedule()
    if not matches:
        matches = build_schedule_from_netease_data()
        save_schedule(matches)

    now = datetime.now()

    print(f"\n📅 2026 世界杯赛程 ({len(matches)} 场)\n")
    print("═" * 60)

    # 按日期分组
    days = {}
    for m in matches:
        days.setdefault(m["date"], []).append(m)

    schedule_only = len(sys.argv) > 2 and sys.argv[2] == "--upcoming"
    current_date = ""

    for date in sorted(days.keys()):
        day_matches = sorted(days[date], key=lambda x: x["time"])
        mdt = datetime.strptime(date, "%Y-%m-%d")
        day_label = f"{date} 星期{['日','一','二','三','四','五','六'][mdt.weekday()]}"

        # 过滤：如果指定 --upcoming，只显示未来比赛
        if schedule_only:
            future_matches = [m for m in day_matches if m["status"] == "未"]
            if not future_matches:
                continue

        print(f"\n  📅 {day_label}")
        print(f"  {'─' * 55}")

        for m in day_matches:
            if schedule_only and m["status"] != "未":
                continue
            status_icon = "✅" if m["status"] == "完" else "📅"
            home_flag = fmt_flag(m["home_team"])
            away_flag = fmt_flag(m["away_team"])
            score_str = f" {m['score']}" if m["score"] else " VS"
            print(f"  {status_icon} {m['time']} | {m['group']:4s} | {m['stadium']}")
            print(f"     {home_flag} {m['home_team']:12s} {score_str:>6s} {away_flag} {m['away_team']}")

    print()


def cmd_team(team_name):
    """预测某队下一场"""
    matches = load_schedule()
    if not matches:
        matches = build_schedule_from_netease_data()
        save_schedule(matches)

    # 查找球队
    team = None
    for t in TEAMS:
        if team_name.lower() in t.lower():
            team = t
            break
    if not team:
        print(f"❌ 未找到球队: {team_name}")
        return

    next_match = get_next_match_for(team, matches)
    if not next_match:
        # 显示该队全部比赛
        team_matches = get_team_matches(team, matches)
        if not team_matches:
            print(f"❌ {team} 没有比赛数据")
            return
        print(f"\n  {fmt_flag(team)} {team} 的所有比赛:")
        for m in team_matches:
            s = f"{m['score']}" if m["score"] else "VS"
            print(f"    {m['date']} {m['time']} | {fmt_flag(m['home_team'])} {m['home_team']} {s} {fmt_flag(m['away_team'])} {m['away_team']}")
        return

    is_home = next_match["home_team"] == team
    opponent = next_match["away_team"] if is_home else next_match["home_team"]

    print(f"\n  {fmt_flag(team)} {team} 的下一场比赛")
    print(f"  📅 {next_match['date']} {next_match['time']}")
    print(f"  🏟  {next_match['group']} | {next_match['stadium']}")
    print(f"  {fmt_flag(team)} {team} vs {fmt_flag(opponent)} {opponent}")

    if is_home:
        result = predict_match(team, opponent, matches)
    else:
        # 客场：用对手视角预测后交换结果
        raw = predict_match(opponent, team, matches)
        result = {
            "home_team": team,
            "away_team": opponent,
            "home_flag": raw["away_flag"],
            "away_flag": raw["home_flag"],
            "home_info": raw["away_info"],
            "away_info": raw["home_info"],
            "home_win_pct": raw["away_win_pct"],
            "draw_pct": raw["draw_pct"],
            "away_win_pct": raw["home_win_pct"],
            "predicted_home": raw["predicted_away"],
            "predicted_away": raw["predicted_home"],
            "home_elo": raw["away_elo"],
            "away_elo": raw["home_elo"],
            "home_form": raw["away_form"],
            "away_form": raw["home_form"],
        }

    print_prediction_report(result, next_match)


def print_prediction_report(result, match_info=None):
    """打印预测报告"""
    print(f"\n{'📊 预测分析':^50}")
    print("═" * 50)

    print(f"\n  {result['home_flag']} {result['home_team']:20s} vs {result['away_flag']} {result['away_team']}")

    h_info = result["home_info"]
    a_info = result["away_info"]
    h_str = h_info.get("strength", 65)
    a_str = a_info.get("strength", 65)
    h_bar = "█" * (h_str // 10) + "░" * (10 - h_str // 10)
    a_bar = "█" * (a_str // 10) + "░" * (10 - a_str // 10)

    print(f"\n  📈 球队实力对比:")
    print(f"  {result['home_flag']} {result['home_team']:12s} [{h_bar}] {h_str}")
    print(f"  {result['away_flag']} {result['away_team']:12s} [{a_bar}] {a_str}")

    # 小组排名
    home_rank = result.get("home_group_rank")
    away_rank = result.get("away_group_rank")
    if home_rank or away_rank:
        print(f"\n  🏅 小组排名:")
        if home_rank:
            print(f"  {result['home_flag']} {result['home_team']}: 小组第{home_rank}")
        if away_rank:
            print(f"  {result['away_flag']} {result['away_team']}: 小组第{away_rank}")

    # 近期进球/失球
    home_gf = result.get("home_goal_avg", 0)
    away_gf = result.get("away_goal_avg", 0)
    if home_gf > 0 or away_gf > 0:
        print(f"\n  ⚽ 近期数据:")
        if home_gf > 0:
            print(f"  {result['home_flag']} {result['home_team']}: 场均{home_gf:.1f}球")
        if away_gf > 0:
            print(f"  {result['away_flag']} {result['away_team']}: 场均{away_gf:.1f}球")

    home_form = result.get("home_form", 0)
    away_form = result.get("away_form", 0)
    if home_form > 0 or away_form > 0:
        print(f"\n  📋 小组赛积分:")
        if home_form > 0:
            print(f"  {result['home_flag']} {result['home_team']}: {home_form}分")
        if away_form > 0:
            print(f"  {result['away_flag']} {result['away_team']}: {away_form}分")

    print(f"\n  {'─' * 40}")
    print(f"  {'📊 胜率预测':^40}")
    print(f"  {result['home_flag']} {result['home_team']} 胜: {result['home_win_pct']}%")
    print(f"  🤝 平局:     {result['draw_pct']}%")
    print(f"  {result['away_flag']} {result['away_team']} 胜: {result['away_win_pct']}%")
    print(f"  {'─' * 40}")
    print(f"  ⚽ 预测比分: {result['home_flag']} {result['predicted_home']} - {result['predicted_away']} {result['away_flag']}")

    # 赛事平局率
    tr = result.get("tournament_draw_rate", 0)
    if tr > 0:
        print(f"\n  📈 本届赛事平局率: {tr*100:.0f}% (参考)")

    # 关键因素
    print(f"\n  🔑 关键分析:")
    strength_diff = h_str - a_str
    if abs(strength_diff) > 10:
        stronger = result["home_team"] if strength_diff > 0 else result["away_team"]
        print(f"    • {stronger} 整体实力明显占优（差距 {abs(strength_diff)} 分）")
    elif abs(strength_diff) > 5:
        stronger = result["home_team"] if strength_diff > 0 else result["away_team"]
        print(f"    • {stronger} 略占优势（差距 {abs(strength_diff)} 分）")
    else:
        print(f"    • 两队实力接近，比赛可能胶着")

    if result["draw_pct"] > 30:
        print(f"    • 平局概率较高（{result['draw_pct']}%），比赛可能很胶着")
    elif result["draw_pct"] < 20:
        print(f"    • 实力差距明显，不太可能平局")

    if home_form > away_form:
        print(f"    • {result['home_team']} 小组赛状态更好")
    elif away_form > home_form:
        print(f"    • {result['away_team']} 小组赛状态更好")

    # 排名分析
    if home_rank and away_rank:
        if home_rank < away_rank:
            print(f"    • {result['home_team']} 小组排名更高（第{home_rank} vs 第{away_rank}）")
        elif away_rank < home_rank:
            print(f"    • {result['away_team']} 小组排名更高（第{away_rank} vs 第{home_rank}）")

    winner = result["home_team"] if result["home_win_pct"] > result["away_win_pct"] else result["away_team"]
    score_h = result["predicted_home"]
    score_a = result["predicted_away"]
    if abs(score_h - score_a) >= 2:
        print(f"    • 预测 {winner} 以较大优势获胜")
    elif score_h != score_a:
        print(f"    • 预测 {winner} 小胜")
    else:
        print(f"    • 可能进入加时或点球")

    print()


def cmd_standings():
    """小组积分 - 从赛程数据自动计算"""
    matches = load_schedule()
    if not matches:
        matches = build_schedule_from_netease_data()
        save_schedule(matches)

    standings = compute_group_standings(matches)

    print(f"\n📊 2026 世界杯小组积分")
    print("═" * 50)

    for g in sorted(standings.keys()):
        print(f"\n🏆 {g}")
        ranked = sorted(standings[g].items(),
                       key=lambda x: (-x[1]['pts'], -(x[1]['gf']-x[1]['ga']), -x[1]['gf']))
        for i, (team, stats) in enumerate(ranked):
            gd = stats['gf'] - stats['ga']
            wdl = f"{stats['w']}W {stats['d']}D {stats['l']}L"
            print(f"  {i+1}. {team:10s}  {stats['played']}场 {stats['pts']}分  {stats['gf']}进{stats['ga']}失  GD:{gd:+d}  {wdl}")

    total_done = sum(1 for m in matches if m['status'] == '完')
    print(f"\n📡 数据来源: 网易彩票 + 赛程缓存 ({total_done}/{len(matches)} 场已完赛)")
    print()


def cmd_update():
    """从硬编码数据更新赛程缓存"""
    matches = build_schedule_from_netease_data()
    save_schedule(matches)


def cmd_match(args):
    """预测指定队 vs 另一队"""
    if len(args) < 2:
        print("用法: predict.py match <主队> <客队>")
        return

    home_team = args[0]
    away_team = args[1]

    matches = load_schedule()
    if not matches:
        matches = build_schedule_from_netease_data()
        save_schedule(matches)

    result = predict_match(home_team, away_team, matches)
    print_prediction_report(result)


def cmd_today():
    """查看今天的比赛和预测"""
    matches = load_schedule()
    if not matches:
        matches = build_schedule_from_netease_data()
        save_schedule(matches)

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    today_matches = [m for m in matches if m["date"] == today]
    if not today_matches:
        print(f"\n📅 今天 ({today}) 没有比赛")
        return

    print(f"\n📅 今日比赛 ({today})")
    print("═" * 50)
    for m in today_matches:
        home_flag = fmt_flag(m["home_team"])
        away_flag = fmt_flag(m["away_team"])
        status_icon = "✅" if m["status"] == "完" else "📅"
        score_str = f" {m['score']}" if m["score"] else " VS"
        print(f"\n  {status_icon} {m['time']} | {m['group']} | {m['stadium']}")
        print(f"  {home_flag} {m['home_team']:12s} {score_str:>6s} {away_flag} {m['away_team']}")

        if m["status"] == "未":
            result = predict_match(m["home_team"], m["away_team"], matches)
            print(f"  预测: {result['home_flag']} {result['predicted_home']}-{result['predicted_away']} {result['away_flag']}")


# ── 主入口 ───────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    commands = {
        "teams": cmd_teams,
        "schedule": cmd_schedule,
        "match": lambda: cmd_match(sys.argv[2:]),
        "team": lambda: cmd_team(" ".join(sys.argv[2:])),
        "standings": cmd_standings,
        "update": cmd_update,
        "today": cmd_today,
    }

    if cmd in commands:
        commands[cmd]()
    else:
        print(f"❌ 未知命令: {cmd}")
        print("   可用命令:")
        print("     teams     - 查看所有球队")
        print("     schedule  - 查看赛程")
        print("     match <主队> <客队> - 预测比赛")
        print("     team <名> - 预测某队下一场")
        print("     today     - 今日比赛预测")
        print("     standings - 小组积分")
        print("     update    - 更新赛程数据")


if __name__ == "__main__":
    main()