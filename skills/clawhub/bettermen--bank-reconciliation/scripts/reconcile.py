#!/usr/bin/env python3
"""
银行流水自动对账引擎 — Bank Statement Auto Reconciliation Engine

四步对账流程:
  1. 导入银行流水 (Excel/CSV) — 自动解析日期、金额、摘要
  2. 自动匹配 — 金额+日期精确匹配，成功则自动核销
  3. 智能辅助 — 模糊匹配(金额相近)、关联匹配(摘要推断)、批量操作
  4. 人工复核 — 仅处理系统无法自动匹配的异常项

Usage:
    python reconcile.py --bank <银行流水文件> --books <账面记录文件> [--output result.json] [--report report.html]
"""

import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime, timedelta
from collections import defaultdict

# Fix Windows console encoding for emoji output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --- Optional dependencies ---
pd = None
try:
    import pandas as pd
except ImportError:
    pass

fuzz = None
try:
    from rapidfuzz import fuzz as _fuzz, process as _process
    fuzz = _fuzz
except ImportError:
    try:
        from fuzzywuzzy import fuzz as _fuzz, process as _process
        fuzz = _fuzz
    except ImportError:
        pass


# ============================================================
#  Column Detection — 自动识别银行流水和账面记录的列名
# ============================================================

COLUMN_ALIASES = {
    "date": [
        "交易日期", "日期", "记账日期", "起息日", "date", "transaction_date",
        "trade_date", "value_date", "交易时间", "时间", "time"
    ],
    "amount": [
        "交易金额", "金额", "发生额", "amount", "transaction_amount",
        "trade_amount", "发生金额", "交易额"
    ],
    "debit": [
        "借方金额", "借方", "支出", "转出", "debit", "debit_amount",
        "支出金额", "付款金额", "付款", "支取"
    ],
    "credit": [
        "贷方金额", "贷方", "收入", "转入", "credit", "credit_amount",
        "收入金额", "收款金额", "收款", "存入"
    ],
    "balance": [
        "余额", "balance", "账户余额", "当前余额", "可用余额"
    ],
    "description": [
        "摘要", "交易摘要", "用途", "备注", "交易说明", "description",
        "summary", "memo", "remark", "交易附言", "附言", "对方信息",
        "交易对方", "对方", "对方户名", "交易对手"
    ],
    "counterparty": [
        "对方户名", "对方名称", "交易对方", "收款人", "付款人",
        "counterparty", "counter_party", "对方", "对手名称",
        "对方账号"
    ],
    "voucher_no": [
        "凭证号", "凭证编号", "voucher", "voucher_no", "凭证",
        "单据号", "流水号", "交易流水号"
    ],
}

# 常见的银行列名组合
BANK_FORMATS = {
    "icbc": {"date": "交易日期", "debit": "借方金额", "credit": "贷方金额", "balance": "余额", "description": "摘要"},
    "ccb": {"date": "交易日期", "debit": "支出金额", "credit": "收入金额", "balance": "余额", "description": "摘要"},
    "abc": {"date": "交易日期", "debit": "借方发生额", "credit": "贷方发生额", "balance": "余额", "description": "摘要"},
    "boc": {"date": "记账日期", "debit": "借方金额", "credit": "贷方金额", "balance": "余额", "description": "摘要"},
    "cmb": {"date": "交易日期", "debit": "支出", "credit": "收入", "balance": "余额", "description": "摘要"},
    "cib": {"date": "交易日期", "debit": "借方", "credit": "贷方", "balance": "余额", "description": "摘要"},
    "spd": {"date": "交易日期", "debit": "借方金额", "credit": "贷方金额", "balance": "余额", "description": "摘要"},
}


def detect_column(col_name, category):
    """Detect which category a column belongs to by alias matching."""
    col_lower = str(col_name).strip().lower()
    for alias in COLUMN_ALIASES[category]:
        if alias.lower() in col_lower or col_lower in alias.lower():
            return True
    return False


def auto_map_columns(df):
    """Auto-map DataFrame columns to standard fields."""
    mapping = {}
    cols = df.columns.tolist()

    for category in ["date", "amount", "debit", "credit", "balance", "description", "counterparty", "voucher_no"]:
        for col in cols:
            if detect_column(col, category):
                mapping[category] = col
                break

    # If separate debit/credit not found, try single amount column
    if "amount" in mapping and "debit" not in mapping and "credit" not in mapping:
        # Check if there are separate debit/credit columns we can derive from
        pass
    elif "debit" in mapping and "credit" in mapping:
        pass  # Standard format
    elif "amount" in mapping:
        pass  # Single amount column

    return mapping


# ============================================================
#  Data Loading & Normalization
# ============================================================

def load_file(filepath):
    """Load Excel or CSV file, return DataFrame or list of dicts."""
    ext = os.path.splitext(filepath)[1].lower()

    if ext in ('.xlsx', '.xls'):
        if pd is None:
            raise ImportError("需要安装 pandas 和 openpyxl: pip install pandas openpyxl")
        df = pd.read_excel(filepath, dtype=str)
    elif ext == '.csv':
        # Try multiple encodings
        for enc in ['utf-8', 'gbk', 'gb2312', 'gb18030', 'utf-8-sig']:
            try:
                if pd is not None:
                    df = pd.read_csv(filepath, encoding=enc, dtype=str)
                else:
                    with open(filepath, 'r', encoding=enc) as f:
                        reader = csv.DictReader(f)
                        rows = list(reader)
                    return rows, list(rows[0].keys()) if rows else []
                break
            except (UnicodeDecodeError, UnicodeError):
                continue
        else:
            raise ValueError(f"无法识别文件编码: {filepath}")
    else:
        raise ValueError(f"不支持的文件格式: {ext}，请使用 Excel (.xlsx) 或 CSV (.csv)")

    return df, df.columns.tolist()


def safe_float(value):
    """Safely convert value to float, handling commas, currency symbols."""
    if value is None:
        return 0.0
    s = str(value).strip()
    # Remove currency symbols and commas
    s = re.sub(r'[¥$￥,，\s]', '', s)
    # Handle negative numbers in various formats
    s = s.replace('（', '-').replace('）', '').replace('(', '-').replace(')', '')
    try:
        return round(float(s), 2)
    except ValueError:
        return 0.0


def safe_date(value):
    """Safely parse date from various formats."""
    if value is None:
        return None
    s = str(value).strip()

    # Try common formats
    formats = [
        '%Y-%m-%d', '%Y/%m/%d', '%Y%m%d',
        '%m/%d/%Y', '%d/%m/%Y',
        '%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S',
        '%Y年%m月%d日', '%m月%d日',
        '%d-%b-%Y', '%d/%b/%Y',
    ]
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue

    # Try pandas timestamp
    if pd is not None:
        try:
            ts = pd.Timestamp(s)
            return ts.to_pydatetime()
        except Exception:
            pass

    return None


def normalize_records(raw_data, record_type="bank"):
    """Normalize raw records into standard format.

    Returns list of:
    {
        "id": str,           # unique record ID
        "date": datetime,
        "date_str": str,
        "amount": float,     # positive=收入, negative=支出 (signed)
        "debit": float,      # 借方 (支出)
        "credit": float,     # 贷方 (收入)
        "description": str,
        "counterparty": str,
        "voucher_no": str,
        "balance": float,
        "raw": dict,         # original row data
        "type": "bank" | "book",
        "status": "unmatched",
        "match_id": None,
        "match_score": 0,
        "match_type": None,
    }
    """
    if isinstance(raw_data, tuple):  # (DataFrame, columns)
        df, cols = raw_data
        mapping = auto_map_columns(df)
        records = []

        for idx, row in df.iterrows():
            rec = {
                "id": f"{record_type}_{idx}",
                "date": safe_date(row.get(mapping.get("date", ""), "")),
                "date_str": str(row.get(mapping.get("date", ""), "")).strip(),
                "amount": 0.0,
                "debit": safe_float(row.get(mapping.get("debit", ""), 0)),
                "credit": safe_float(row.get(mapping.get("credit", ""), 0)),
                "description": str(row.get(mapping.get("description", ""), "")).strip(),
                "counterparty": str(row.get(mapping.get("counterparty", ""), "")).strip(),
                "voucher_no": str(row.get(mapping.get("voucher_no", ""), "")).strip(),
                "balance": safe_float(row.get(mapping.get("balance", ""), 0)),
                "raw": {k: str(v) for k, v in row.items()},
                "type": record_type,
                "status": "unmatched",
                "match_id": None,
                "match_score": 0,
                "match_type": None,
            }

            # Determine signed amount (positive = 收入/进账, negative = 支出/出账)
            # Bank perspective: 贷方=收入(+), 借方=支出(-)
            # Book perspective (会计): 借方=收入(+), 贷方=支出(-)
            has_separate_dc = ("debit" in mapping or "credit" in mapping)
            if not has_separate_dc and "amount" in mapping and mapping["amount"] in row:
                rec["amount"] = safe_float(row[mapping["amount"]])
            elif record_type == "bank":
                if rec["debit"] > 0:
                    rec["amount"] = -rec["debit"]  # bank debit = money out = negative
                elif rec["credit"] > 0:
                    rec["amount"] = rec["credit"]  # bank credit = money in = positive
            else:  # book records, accounting convention
                if rec["debit"] > 0:
                    rec["amount"] = rec["debit"]  # book debit of bank account = money in = positive
                elif rec["credit"] > 0:
                    rec["amount"] = -rec["credit"]  # book credit of bank account = money out = negative

            records.append(rec)

        return records
    else:
        # list of dicts (CSV without pandas)
        rows, cols = raw_data
        # Simple mapping by header name
        mapping = {}
        for col in cols:
            for category, aliases in COLUMN_ALIASES.items():
                if detect_column(col, category):
                    mapping[category] = col
                    break

        records = []
        for idx, row in enumerate(rows):
            rec = {
                "id": f"{record_type}_{idx}",
                "date": safe_date(row.get(mapping.get("date", ""), "")),
                "date_str": str(row.get(mapping.get("date", ""), "")).strip(),
                "amount": 0.0,
                "debit": safe_float(row.get(mapping.get("debit", ""), 0)),
                "credit": safe_float(row.get(mapping.get("credit", ""), 0)),
                "description": str(row.get(mapping.get("description", ""), "")).strip(),
                "counterparty": str(row.get(mapping.get("counterparty", ""), "")).strip(),
                "voucher_no": str(row.get(mapping.get("voucher_no", ""), "")).strip(),
                "balance": 0.0,
                "raw": dict(row),
                "type": record_type,
                "status": "unmatched",
                "match_id": None,
                "match_score": 0,
                "match_type": None,
            }

            # Determine signed amount — same convention as pandas branch
            has_separate_dc = ("debit" in mapping or "credit" in mapping)
            if not has_separate_dc and "amount" in mapping:
                rec["amount"] = safe_float(row.get(mapping["amount"], 0))
            elif record_type == "bank":
                if rec["debit"] > 0:
                    rec["amount"] = -rec["debit"]
                elif rec["credit"] > 0:
                    rec["amount"] = rec["credit"]
            else:  # book records, accounting convention
                if rec["debit"] > 0:
                    rec["amount"] = rec["debit"]
                elif rec["credit"] > 0:
                    rec["amount"] = -rec["credit"]

            records.append(rec)

        return records


# ============================================================
#  Matching Engine
# ============================================================

def match_amount(a1, a2, tolerance=0.01):
    """Check if two amounts match within tolerance."""
    return abs(abs(a1) - abs(a2)) <= tolerance


def match_date(d1, d2, tolerance_days=1):
    """Check if two dates match within tolerance days."""
    if d1 is None or d2 is None:
        return False
    diff = abs((d1 - d2).days)
    return diff <= tolerance_days


def match_description(desc1, desc2, threshold=70):
    """Fuzzy match two descriptions using string similarity."""
    if not desc1 or not desc2:
        return 0
    if fuzz is not None:
        # Use token_sort_ratio for better handling of word order
        score = max(
            fuzz.token_sort_ratio(desc1, desc2),
            fuzz.partial_ratio(desc1, desc2),
            fuzz.token_set_ratio(desc1, desc2),
        )
        return score
    else:
        # Fallback: simple keyword overlap
        words1 = set(re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+|\d+', desc1))
        words2 = set(re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+|\d+', desc2))
        if not words1 or not words2:
            return 0
        overlap = len(words1 & words2)
        return (overlap / max(len(words1), len(words2))) * 100


def extract_keywords(desc):
    """Extract meaningful keywords from description."""
    # Remove common noise words
    noise = {'交易', '转账', '汇款', '支付', '收款', '付款', '网银', '手机银行',
             '柜面', 'ATM', 'POS', '银联', '跨行', '本行', '行内', '批量',
             '自动', '电子', '汇入', '汇出', '代收', '代付'}
    words = re.findall(r'[\u4e00-\u9fff]{2,}|[a-zA-Z]{2,}|\d{4,}', desc)
    keywords = [w for w in words if w not in noise]
    return keywords


def find_counterparty_in_desc(desc, counterparty):
    """Check if counterparty name appears in description."""
    if not counterparty or not desc:
        return 0
    if len(counterparty) >= 2 and counterparty in desc:
        return 100
    # Partial match
    if len(counterparty) >= 3:
        for i in range(len(counterparty) - 1):
            seg = counterparty[i:i+2]
            if seg in desc:
                return 70
    return 0


def exact_match(bank_records, book_records, date_tolerance=1, amount_tolerance=0.01):
    """Step 1: Exact matching by amount + date."""
    matched_pairs = []
    used_book_ids = set()

    for bank in bank_records:
        if bank["status"] != "unmatched":
            continue

        best_match = None
        best_score = 0

        for book in book_records:
            if book["status"] != "unmatched":
                continue
            if book["id"] in used_book_ids:
                continue

            # Core matching: amount (absolute value) + date
            if match_amount(bank["amount"], book["amount"], amount_tolerance):
                if match_date(bank["date"], book["date"], date_tolerance):
                    # Calculate score
                    score = 100  # Base score for amount match
                    # Date proximity bonus
                    if bank["date"] and book["date"]:
                        day_diff = abs((bank["date"] - book["date"]).days)
                        if day_diff == 0:
                            score += 20
                        else:
                            score += max(0, 20 - day_diff * 10)

                    # Description bonus
                    desc_score = match_description(bank["description"], book["description"])
                    if desc_score > 60:
                        score += (desc_score - 60) * 0.5

                    # Counterparty bonus
                    cp_score = find_counterparty_in_desc(
                        bank["description"], book.get("counterparty", "")
                    ) or find_counterparty_in_desc(
                        book["description"], bank.get("counterparty", "")
                    )
                    if cp_score > 0:
                        score += cp_score * 0.3

                    if score > best_score:
                        best_score = score
                        best_match = book

        if best_match and best_score >= 80:
            matched_pairs.append((bank, best_match, best_score, "exact"))
            used_book_ids.add(best_match["id"])

    # Apply matches
    for bank, book, score, mtype in matched_pairs:
        bank["status"] = "matched"
        bank["match_id"] = book["id"]
        bank["match_score"] = round(score, 1)
        bank["match_type"] = mtype
        book["status"] = "matched"
        book["match_id"] = bank["id"]
        book["match_score"] = round(score, 1)
        book["match_type"] = mtype

    return len(matched_pairs)


def fuzzy_match(bank_records, book_records, date_tolerance=3, amount_tolerance_percent=0.05,
                desc_threshold=60):
    """Step 2: Fuzzy matching for remaining unmatched records."""
    matched_pairs = []
    used_book_ids = {b["id"] for b in book_records if b["status"] == "matched"}

    for bank in bank_records:
        if bank["status"] != "unmatched":
            continue

        candidates = []
        for book in book_records:
            if book["status"] != "unmatched":
                continue
            if book["id"] in used_book_ids:
                continue

            score = 0
            reasons = []

            # Amount proximity (percentage-based)
            b_amt = abs(bank["amount"])
            k_amt = abs(book["amount"])
            if b_amt > 0 and k_amt > 0:
                amt_diff_pct = abs(b_amt - k_amt) / max(b_amt, k_amt)
                if amt_diff_pct <= amount_tolerance_percent:
                    amt_score = max(0, 40 - amt_diff_pct * 400)
                    score += amt_score
                    if amt_diff_pct == 0:
                        reasons.append("金额完全一致")
                    else:
                        reasons.append(f"金额相差{amt_diff_pct*100:.1f}%")
                elif amt_diff_pct <= amount_tolerance_percent * 2:
                    amt_score = max(0, 20 - amt_diff_pct * 200)
                    score += amt_score
                    reasons.append(f"金额接近(差{amt_diff_pct*100:.1f}%)")
                else:
                    continue  # Amount too different
            else:
                continue

            # Date proximity
            if bank["date"] and book["date"]:
                day_diff = abs((bank["date"] - book["date"]).days)
                if day_diff <= date_tolerance:
                    date_score = max(0, 30 - day_diff * 10)
                    score += date_score
                    if day_diff == 0:
                        reasons.append("日期一致")
                    else:
                        reasons.append(f"日期差{day_diff}天")
                else:
                    date_score = max(0, 10 - (day_diff - date_tolerance) * 2)
                    score += date_score

            # Description similarity
            desc_score = match_description(bank["description"], book["description"])
            if desc_score >= desc_threshold:
                score += desc_score * 0.3
                reasons.append(f"摘要相似度{desc_score}%")
            elif desc_score >= 40:
                score += desc_score * 0.15

            # Counterparty matching
            cp_score = max(
                find_counterparty_in_desc(bank["description"], book.get("counterparty", "")),
                find_counterparty_in_desc(book["description"], bank.get("counterparty", "")),
                match_description(bank.get("counterparty", ""), book.get("counterparty", "")) if bank.get("counterparty") and book.get("counterparty") else 0
            )
            if cp_score > 0:
                score += min(cp_score, 30) * 0.2
                reasons.append("对方信息匹配")

            if score >= 50:
                candidates.append((book, score, reasons))

        if candidates:
            # Sort by score descending
            candidates.sort(key=lambda x: x[1], reverse=True)
            best_book, best_score, reasons = candidates[0]

            if best_score >= 55:
                matched_pairs.append((bank, best_book, best_score, "fuzzy", reasons))
                used_book_ids.add(best_book["id"])

    # Apply matches
    for bank, book, score, mtype, reasons in matched_pairs:
        bank["status"] = "matched"
        bank["match_id"] = book["id"]
        bank["match_score"] = round(score, 1)
        bank["match_type"] = mtype
        bank["match_reasons"] = reasons
        book["status"] = "matched"
        book["match_id"] = bank["id"]
        book["match_score"] = round(score, 1)
        book["match_type"] = mtype

    return len(matched_pairs)


def association_match(bank_records, book_records):
    """Step 3: Association matching — group by counterparty and try to match sums."""
    matched_pairs = []
    used_book_ids = {b["id"] for b in book_records if b["status"] == "matched"}

    # Group unmatched bank records by counterparty
    bank_groups = defaultdict(list)
    for b in bank_records:
        if b["status"] == "unmatched":
            key = b.get("counterparty", "") or extract_keywords(b["description"])[:1]
            key = key[0] if isinstance(key, list) else key
            if key:
                bank_groups[key].append(b)

    book_groups = defaultdict(list)
    for b in book_records:
        if b["status"] == "unmatched":
            key = b.get("counterparty", "") or extract_keywords(b["description"])[:1]
            key = key[0] if isinstance(key, list) else key
            if key:
                book_groups[key].append(b)

    # Try to match groups where sum matches
    for key in set(bank_groups.keys()) & set(book_groups.keys()):
        b_group = [b for b in bank_groups[key] if b["id"] not in {p[0]["id"] for p in matched_pairs}]
        k_group = [b for b in book_groups[key] if b["id"] not in used_book_ids]

        if len(b_group) >= 2 or len(k_group) >= 2:
            b_total = sum(abs(b["amount"]) for b in b_group)
            k_total = sum(abs(b["amount"]) for b in k_group)

            if b_total > 0 and abs(b_total - k_total) / max(b_total, k_total) < 0.05:
                # Batch match the whole group
                for b_rec in b_group:
                    # Find best individual match within the group
                    candidates = [(k, abs(abs(b_rec["amount"]) - abs(k["amount"])))
                                  for k in k_group if k["id"] not in used_book_ids]
                    if candidates:
                        candidates.sort(key=lambda x: x[1])
                        best_book, _ = candidates[0]
                        score = 70  # Association match score
                        matched_pairs.append((b_rec, best_book, score, "association", ["同户名批量匹配"]))
                        used_book_ids.add(best_book["id"])

    # Apply matches
    for bank, book, score, mtype, reasons in matched_pairs:
        bank["status"] = "matched"
        bank["match_id"] = book["id"]
        bank["match_score"] = round(score, 1)
        bank["match_type"] = mtype
        bank["match_reasons"] = reasons
        book["status"] = "matched"
        book["match_id"] = bank["id"]
        book["match_score"] = round(score, 1)
        book["match_type"] = mtype

    return len(matched_pairs)


# ============================================================
#  Main Reconciliation Pipeline
# ============================================================

def reconcile(bank_file, book_file, date_tolerance=1, amount_tolerance=0.01,
              fuzzy_date_tolerance=3, fuzzy_amount_pct=0.05):
    """Run the full 4-step reconciliation pipeline."""
    # Step 1: Load data
    bank_raw = load_file(bank_file)
    book_raw = load_file(book_file)

    print(f"📂 银行流水: {len(bank_raw[0] if isinstance(bank_raw, tuple) else bank_raw[1])} 条记录")
    print(f"📂 账面记录: {len(book_raw[0] if isinstance(book_raw, tuple) else book_raw[1])} 条记录")

    bank_records = normalize_records(bank_raw, "bank")
    book_records = normalize_records(book_raw, "book")

    print(f"✅ 解析完成: 银行 {len(bank_records)} 条, 账面 {len(book_records)} 条")

    # Step 1: Exact match
    n_exact = exact_match(bank_records, book_records, date_tolerance, amount_tolerance)
    print(f"🎯 精确匹配: {n_exact} 对")

    # Step 2: Fuzzy match
    n_fuzzy = fuzzy_match(bank_records, book_records, fuzzy_date_tolerance, fuzzy_amount_pct)
    print(f"🔍 模糊匹配: {n_fuzzy} 对")

    # Step 3: Association match
    n_assoc = association_match(bank_records, book_records)
    print(f"🔗 关联匹配: {n_assoc} 对")

    # Summary
    bank_matched = sum(1 for r in bank_records if r["status"] == "matched")
    bank_unmatched = len(bank_records) - bank_matched
    book_matched = sum(1 for r in book_records if r["status"] == "matched")
    book_unmatched = len(book_records) - book_matched

    total_matched = bank_matched
    total_unmatched = bank_unmatched + book_unmatched
    match_rate = round(bank_matched / max(len(bank_records), 1) * 100, 1)

    print(f"\n📊 对账完成:")
    print(f"   银行流水: {bank_matched} 匹配 / {bank_unmatched} 待确认")
    print(f"   账面记录: {book_matched} 匹配 / {book_unmatched} 待确认")
    print(f"   自动匹配率: {match_rate}%")

    # Build result
    result = {
        "summary": {
            "bank_total": len(bank_records),
            "book_total": len(book_records),
            "bank_matched": bank_matched,
            "bank_unmatched": bank_unmatched,
            "book_matched": book_matched,
            "book_unmatched": book_unmatched,
            "exact_matches": n_exact,
            "fuzzy_matches": n_fuzzy,
            "association_matches": n_assoc,
            "total_matched": bank_matched,
            "total_unmatched": bank_unmatched + book_unmatched,
            "match_rate": match_rate,
            "date_tolerance": date_tolerance,
            "amount_tolerance": amount_tolerance,
            "generated_at": datetime.now().isoformat(),
        },
        "bank_records": bank_records,
        "book_records": book_records,
        "matched_pairs": [],
        "unmatched_bank": [r for r in bank_records if r["status"] == "unmatched"],
        "unmatched_book": [r for r in book_records if r["status"] == "unmatched"],
    }

    # Build matched pairs list
    for bank in bank_records:
        if bank["status"] == "matched" and bank["match_id"]:
            book = next((b for b in book_records if b["id"] == bank["match_id"]), None)
            if book:
                result["matched_pairs"].append({
                    "bank": bank,
                    "book": book,
                    "score": bank["match_score"],
                    "type": bank["match_type"],
                    "reasons": bank.get("match_reasons", []),
                })

    return result


def serialize_result(result):
    """Convert result to JSON-serializable format."""
    def serialize_record(rec):
        d = dict(rec)
        if d.get("date"):
            d["date"] = d["date"].strftime("%Y-%m-%d")
        d.pop("raw", None)  # raw data can be large
        return d

    return {
        "summary": result["summary"],
        "matched_pairs": [
            {
                "bank": serialize_record(p["bank"]),
                "book": serialize_record(p["book"]),
                "score": p["score"],
                "type": p["type"],
                "reasons": p.get("reasons", []),
            }
            for p in result["matched_pairs"]
        ],
        "unmatched_bank": [serialize_record(r) for r in result["unmatched_bank"]],
        "unmatched_book": [serialize_record(r) for r in result["unmatched_book"]],
    }


# ============================================================
#  HTML Report Generation
# ============================================================

def generate_html_report(result, output_path):
    """Generate interactive HTML visualization report."""
    summary = result["summary"]
    serialized = serialize_result(result)

    # Build matched/unmatched tables
    def build_table_rows(records, show_book_ref=False):
        rows = ""
        for i, r in enumerate(records):
            amount_str = f"{r['amount']:,.2f}"
            amount_cls = "positive" if r['amount'] >= 0 else "negative"
            date_str = r.get('date', r.get('date_str', ''))
            desc = r.get('description', '')[:30]
            cp = r.get('counterparty', '')[:15]

            match_info = ""
            if r.get('status') == 'matched':
                match_score = r.get('match_score', 0)
                match_type = r.get('match_type', '')
                match_type_cn = {"exact": "精确匹配", "fuzzy": "模糊匹配", "association": "关联匹配"}.get(match_type, match_type)
                score_color = "#22c55e" if match_score >= 90 else "#eab308" if match_score >= 70 else "#f97316"
                match_info = f'<span style="color:{score_color};font-weight:600">{match_type_cn} ({match_score}分)</span>'
                if show_book_ref and r.get('match_id'):
                    match_info += f' <span style="color:#6b7280;font-size:12px">→ {r["match_id"]}</span>'

            rows += f"""
            <tr>
                <td>{i+1}</td>
                <td>{date_str}</td>
                <td class="{amount_cls}">{amount_str}</td>
                <td title="{r.get('description', '')}">{desc}</td>
                <td>{cp}</td>
                <td>{match_info}</td>
            </tr>"""
        return rows

    bank_rows = build_table_rows(serialized["unmatched_bank"])
    book_rows = build_table_rows(serialized["unmatched_book"])
    matched_rows_data = []
    for p in serialized["matched_pairs"]:
        b = p["bank"]
        k = p["book"]
        matched_rows_data.append({
            "bank_date": b.get("date", ""),
            "bank_amount": b["amount"],
            "bank_desc": b.get("description", "")[:25],
            "book_date": k.get("date", ""),
            "book_amount": k["amount"],
            "book_desc": k.get("description", "")[:25],
            "score": p["score"],
            "type": p["type"],
            "type_cn": {"exact": "精确匹配", "fuzzy": "模糊匹配", "association": "关联匹配"}.get(p["type"], p["type"]),
        })

    matched_rows_html = ""
    for i, m in enumerate(matched_rows_data):
        score_color = "#22c55e" if m["score"] >= 90 else "#eab308" if m["score"] >= 70 else "#f97316"
        matched_rows_html += f"""
            <tr>
                <td>{i+1}</td>
                <td>{m["bank_date"]}</td>
                <td>{m["bank_amount"]:,.2f}</td>
                <td>{m["bank_desc"]}</td>
                <td>{m["book_date"]}</td>
                <td>{m["book_amount"]:,.2f}</td>
                <td>{m["book_desc"]}</td>
                <td><span style="color:{score_color};font-weight:600">{m["type_cn"]}</span></td>
                <td>{m["score"]}</td>
            </tr>"""

    # Match rate color
    rate = summary["match_rate"]
    rate_color = "#22c55e" if rate >= 90 else "#eab308" if rate >= 70 else "#f97316"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>银行流水自动对账报告</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; background: #f5f7fa; color: #1a1a2e; padding: 24px; }}
.container {{ max-width: 1400px; margin: 0 auto; }}
.header {{ background: linear-gradient(135deg, #1a1a2e, #16213e); color: white; padding: 32px; border-radius: 16px; margin-bottom: 24px; }}
.header h1 {{ font-size: 28px; margin-bottom: 8px; }}
.header p {{ color: #94a3b8; font-size: 14px; }}
.dashboard {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }}
.card {{ background: white; border-radius: 12px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }}
.card-label {{ font-size: 13px; color: #64748b; margin-bottom: 8px; }}
.card-value {{ font-size: 32px; font-weight: 700; }}
.card-sub {{ font-size: 12px; color: #94a3b8; margin-top: 4px; }}
.rate-ring {{ display: flex; align-items: center; gap: 16px; }}
.ring {{ width: 80px; height: 80px; border-radius: 50%; background: conic-gradient({rate_color} {rate}%, #e2e8f0 0); display: flex; align-items: center; justify-content: center; }}
.ring-inner {{ width: 64px; height: 64px; border-radius: 50%; background: white; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; }}
.section {{ background: white; border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }}
.section h2 {{ font-size: 18px; margin-bottom: 16px; color: #1a1a2e; display: flex; align-items: center; gap: 8px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
th {{ background: #f8fafc; padding: 10px 12px; text-align: left; font-weight: 600; color: #475569; border-bottom: 2px solid #e2e8f0; white-space: nowrap; }}
td {{ padding: 10px 12px; border-bottom: 1px solid #f1f5f9; }}
tr:hover {{ background: #f8fafc; }}
.positive {{ color: #16a34a; font-weight: 600; }}
.negative {{ color: #dc2626; font-weight: 600; }}
.badge {{ display: inline-block; padding: 2px 8px; border-radius: 9999px; font-size: 11px; font-weight: 600; }}
.badge-exact {{ background: #dcfce7; color: #166534; }}
.badge-fuzzy {{ background: #fef9c3; color: #854d0e; }}
.badge-assoc {{ background: #dbeafe; color: #1e40af; }}
.tabs {{ display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }}
.tab {{ padding: 8px 16px; border-radius: 8px; border: 1px solid #e2e8f0; background: white; cursor: pointer; font-size: 13px; color: #475569; transition: all 0.2s; }}
.tab:hover {{ border-color: #6366f1; color: #6366f1; }}
.tab.active {{ background: #6366f1; color: white; border-color: #6366f1; }}
.tab-panel {{ display: none; }}
.tab-panel.active {{ display: block; }}
.export-btn {{ background: #6366f1; color: white; border: none; padding: 8px 16px; border-radius: 8px; cursor: pointer; font-size: 13px; margin-left: 8px; }}
.export-btn:hover {{ background: #4f46e5; }}
.footer {{ text-align: center; color: #94a3b8; font-size: 12px; margin-top: 32px; }}
</style>
</head>
<body>
<div class="container">

<div class="header">
    <h1>🏦 银行流水自动对账报告</h1>
    <p>生成时间: {summary['generated_at'][:19]} | 日期容差: ±{summary['date_tolerance']}天 | 金额容差: ±{summary['amount_tolerance']}元</p>
</div>

<div class="dashboard">
    <div class="card">
        <div class="card-label">📥 银行流水</div>
        <div class="card-value">{summary['bank_total']}</div>
        <div class="card-sub">条记录</div>
    </div>
    <div class="card">
        <div class="card-label">📚 账面记录</div>
        <div class="card-value">{summary['book_total']}</div>
        <div class="card-sub">条记录</div>
    </div>
    <div class="card">
        <div class="card-label">✅ 自动匹配</div>
        <div class="card-value" style="color: {rate_color}">{summary['total_matched']}</div>
        <div class="card-sub">精确 {summary['exact_matches']} + 模糊 {summary['fuzzy_matches']} + 关联 {summary['association_matches']}</div>
    </div>
    <div class="card">
        <div class="card-label">⚠️ 待确认</div>
        <div class="card-value" style="color: #f97316">{summary['total_unmatched']}</div>
        <div class="card-sub">银行 {summary['bank_unmatched']} + 账面 {summary['book_unmatched']}</div>
    </div>
    <div class="card">
        <div class="rate-ring">
            <div class="ring"><div class="ring-inner" style="color:{rate_color}">{rate}%</div></div>
            <div>
                <div class="card-label">自动匹配率</div>
                <div class="card-sub">{
                    '🎉 优秀！90%以上自动匹配' if rate >= 90 else
                    '👍 良好，少量需人工处理' if rate >= 70 else
                    '🔧 建议检查数据格式或调整容差'
                }</div>
            </div>
        </div>
    </div>
</div>

<div class="section">
    <h2>✅ 匹配明细 <span style="font-size:12px;color:#64748b">({len(matched_rows_data)} 对)</span></h2>
    <div style="overflow-x:auto">
    <table>
        <thead>
            <tr>
                <th>#</th>
                <th>银行日期</th>
                <th>银行金额</th>
                <th>银行摘要</th>
                <th>账面日期</th>
                <th>账面金额</th>
                <th>账面摘要</th>
                <th>匹配类型</th>
                <th>得分</th>
            </tr>
        </thead>
        <tbody>
            {matched_rows_html}
        </tbody>
    </table>
    </div>
</div>

<div class="section">
    <div style="display:flex;justify-content:space-between;align-items:center">
        <h2>⚠️ 待确认记录</h2>
        <button class="export-btn" onclick="exportUnmatched()">📥 导出待确认列表</button>
    </div>

    <div class="tabs">
        <button class="tab active" onclick="switchTab('bank')">银行流水待确认 ({summary['bank_unmatched']})</button>
        <button class="tab" onclick="switchTab('book')">账面记录待确认 ({summary['book_unmatched']})</button>
    </div>

    <div id="tab-bank" class="tab-panel active">
        <div style="overflow-x:auto">
        <table>
            <thead>
                <tr><th>#</th><th>日期</th><th>金额</th><th>摘要</th><th>对方</th><th>状态</th></tr>
            </thead>
            <tbody>{bank_rows or '<tr><td colspan="6" style="text-align:center;color:#94a3b8;padding:24px">🎉 全部匹配完成！</td></tr>'}</tbody>
        </table>
        </div>
    </div>

    <div id="tab-book" class="tab-panel">
        <div style="overflow-x:auto">
        <table>
            <thead>
                <tr><th>#</th><th>日期</th><th>金额</th><th>摘要</th><th>对方</th><th>状态</th></tr>
            </thead>
            <tbody>{book_rows or '<tr><td colspan="6" style="text-align:center;color:#94a3b8;padding:24px">🎉 全部匹配完成！</td></tr>'}</tbody>
        </table>
        </div>
    </div>
</div>

<div class="footer">
    银行流水自动对账引擎 v1.0 · 数据仅保存在本地
</div>

</div>

<script>
function switchTab(tab) {{
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    event.target.classList.add('active');
    document.getElementById('tab-' + tab).classList.add('active');
}}

function exportUnmatched() {{
    const data = {json.dumps({"unmatched_bank": serialized["unmatched_bank"], "unmatched_book": serialized["unmatched_book"]}, ensure_ascii=False)};
    const blob = new Blob([JSON.stringify(data, null, 2)], {{type: 'application/json'}});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'unmatched_records.json';
    a.click();
    URL.revokeObjectURL(url);
}}
</script>
</body>
</html>"""

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return output_path


# ============================================================
#  CLI Entry Point
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="银行流水自动对账引擎 — Bank Statement Auto Reconciliation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python reconcile.py --bank 银行流水.xlsx --books 账面记录.csv
  python reconcile.py --bank 流水.xlsx --books 账目.xlsx --date-tolerance 2 --amount-tolerance 0.05
  python reconcile.py --bank 流水.csv --books 账目.csv --output result.json --report report.html
        """
    )
    parser.add_argument("--bank", required=True, help="银行流水文件路径 (Excel/CSV)")
    parser.add_argument("--books", required=True, help="账面记录文件路径 (Excel/CSV)")
    parser.add_argument("--output", "-o", default="reconciliation_result.json", help="JSON结果输出路径")
    parser.add_argument("--report", "-r", default="reconciliation_report.html", help="HTML报告输出路径")
    parser.add_argument("--date-tolerance", "-d", type=int, default=1, help="日期容差天数 (默认: 1)")
    parser.add_argument("--amount-tolerance", "-a", type=float, default=0.01, help="金额容差 (默认: 0.01)")
    parser.add_argument("--fuzzy-date-tolerance", type=int, default=3, help="模糊匹配日期容差 (默认: 3)")
    parser.add_argument("--fuzzy-amount-pct", type=float, default=0.05, help="模糊匹配金额百分比容差 (默认: 0.05)")
    parser.add_argument("--json-only", action="store_true", help="仅输出JSON，不生成HTML报告")

    args = parser.parse_args()

    # Validate input files
    for f in [args.bank, args.books]:
        if not os.path.exists(f):
            print(f"❌ 文件不存在: {f}", file=sys.stderr)
            sys.exit(1)

    print("=" * 60)
    print("  🏦 银行流水自动对账引擎 v1.0")
    print("=" * 60)

    # Run reconciliation
    result = reconcile(
        args.bank, args.books,
        date_tolerance=args.date_tolerance,
        amount_tolerance=args.amount_tolerance,
        fuzzy_date_tolerance=args.fuzzy_date_tolerance,
        fuzzy_amount_pct=args.fuzzy_amount_pct,
    )

    # Save JSON
    serialized = serialize_result(result)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(serialized, f, ensure_ascii=False, indent=2)
    print(f"\n💾 JSON结果: {args.output}")

    # Generate HTML report
    if not args.json_only:
        report_path = generate_html_report(result, args.report)
        print(f"📊 HTML报告: {report_path}")

    print("\n" + "=" * 60)
    print(f"  ✅ 对账完成 | 匹配率: {result['summary']['match_rate']}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
