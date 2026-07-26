"""
类目输入归一化模块
读取 Excel/CSV，自动识别平台（Amazon/Walmart/纯关键词），输出统一结构
"""
import re
import pandas as pd
from pathlib import Path
from urllib.parse import unquote_plus


def detect_platform(raw: str) -> dict:
    """识别单条类目输入的平台和类型"""
    raw = str(raw).strip()
    if not raw or raw == "/" or raw.lower() == "nan":
        return None

    if "amazon.com" in raw.lower():
        category_name = _extract_amazon_category_from_url(raw)
        return {
            "platform": "amazon",
            "input_type": "url",
            "raw": raw,
            "search_keyword": category_name,
            "url": raw,
        }

    if "walmart.com" in raw.lower():
        category_name = _extract_walmart_category_from_url(raw)
        return {
            "platform": "walmart",
            "input_type": "url",
            "raw": raw,
            "search_keyword": category_name,
            "url": raw,
        }

    if ">" in raw:
        parts = [p.strip() for p in raw.split(">")]
        leaf = parts[-1]
        platform = _guess_platform_from_path(raw)
        return {
            "platform": platform,
            "input_type": "path",
            "raw": raw,
            "search_keyword": leaf,
            "category_path": parts,
        }

    return {
        "platform": "both",
        "input_type": "keyword",
        "raw": raw,
        "search_keyword": raw,
    }


def _extract_amazon_category_from_url(url: str) -> str:
    m = re.search(r"/zgbs/([^/]+)", url)
    if m:
        return m.group(1).replace("-", " ")
    m = re.search(r"[?&]k=([^&]+)", url)
    if m:
        return unquote_plus(m.group(1))
    m = re.search(r"/Best-Sellers-([^/]+)", url)
    if m:
        return m.group(1).replace("-", " ")
    parts = url.rstrip("/").split("/")
    return parts[-1].replace("-", " ")


def _extract_walmart_category_from_url(url: str) -> str:
    m = re.search(r"/cp/([^/]+)", url)
    if m:
        return m.group(1).replace("-", " ")
    m = re.search(r"/browse/[^/]+/([^/?]+)", url)
    if m:
        return m.group(1).replace("-", " ")
    m = re.search(r"[?&]q=([^&]+)", url)
    if m:
        return unquote_plus(m.group(1))
    parts = url.rstrip("/").split("/")
    return parts[-1].replace("-", " ")


def _guess_platform_from_path(path: str) -> str:
    amazon_roots = {"home & kitchen", "tools & home improvement", "sports & outdoors",
                    "health & household", "beauty & personal care", "toys & games",
                    "electronics", "automotive", "garden & outdoor", "pet supplies",
                    "office products", "arts, crafts & sewing", "baby", "clothing"}
    first_part = path.split(">")[0].strip().lower()
    if first_part in amazon_roots:
        return "amazon"
    return "both"


def load_categories(file_path: str) -> list:
    path = Path(file_path)
    if path.suffix in (".xlsx", ".xls"):
        df = pd.read_excel(path)
    elif path.suffix == ".csv":
        df = pd.read_csv(path)
    else:
        raise ValueError(f"不支持的文件格式: {path.suffix}，请使用 .xlsx 或 .csv")

    cat_col = _find_category_column(df)
    if cat_col is None:
        raise ValueError("无法自动识别类目列")

    results = []
    for idx, row in df.iterrows():
        val = str(row[cat_col]).strip()
        parsed = detect_platform(val)
        if parsed:
            parsed["row_index"] = idx
            results.append(parsed)

    return results


def _find_category_column(df: pd.DataFrame):
    for col in df.columns:
        col_lower = str(col).lower()
        if any(kw in col_lower for kw in ["类目", "category", "分类", "品类", "cat"]):
            return col

    for col in df.columns:
        sample = df[col].dropna().head(10).astype(str)
        url_count = sample.str.contains(r"amazon\.com|walmart\.com", regex=True).sum()
        path_count = sample.str.contains(r">").sum()
        if url_count >= 3 or path_count >= 3:
            return col

    if len(df.columns) > 0:
        return df.columns[0]
    return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法: python3 category_parser.py <categories.xlsx>")
        sys.exit(1)
    cats = load_categories(sys.argv[1])
    print(f"共解析 {len(cats)} 个类目:")
    for c in cats[:5]:
        print(f"  [{c['platform']}] {c['search_keyword']}")
    if len(cats) > 5:
        print(f"  ... 还有 {len(cats)-5} 个")
