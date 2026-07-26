#!/usr/bin/env python3
"""MODIS Product Query Tool - Comprehensive NASA MODIS satellite product database query script."""

import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(SKILL_DIR, "data")
PRODUCTS_FILE = os.path.join(DATA_DIR, "products.json")
GEE_CODES_FILE = os.path.join(DATA_DIR, "gee_codes.json")

# Optional --place resolver. Lives in the vendored _geoskill_core/ folder.
# Import as a package (`_geoskill_core.aoi`) so the relative imports inside
# `aoi.py` (e.g. `from .manifest import AOIManifest`) resolve correctly.
if SKILL_DIR not in sys.path:
    sys.path.insert(0, SKILL_DIR)
try:
    from _geoskill_core.aoi import resolve_place as _resolve_place  # type: ignore
    from _geoskill_core.aoi import NoMatchError as _NoMatchError  # type: ignore
    _HAS_AOI = True
except Exception:  # noqa: BLE001
    _resolve_place = None
    _NoMatchError = Exception
    _HAS_AOI = False


# MODIS products are global (or near-global) by default. Any product whose
# `name` doesn't mention a regional / non-global scope is treated as global.
# The list below lists known non-global products to keep filtering accurate
# when the catalog grows.
_NON_GLOBAL_KEYWORDS = ("regional", "local", "site", "tile", "subset", "polar")

CATEGORY_MAP = {
    "vegetation_indices": "植被指数",
    "surface_reflectance": "地表反射率",
    "land_surface_temperature": "地表温度",
    "land_cover": "土地覆盖",
    "thermal_anomalies": "热异常/火灾",
    "lai_fpar": "叶面积指数/FPAR",
    "evapotranspiration": "蒸散发",
    "gpp_npp": "总/净初级生产力",
    "brdf_albedo": "BRDF/反照率",
    "vegetation_continuous_fields": "植被连续场",
    "water_mask": "水体掩膜",
    "burned_area": "燃烧面积",
    "snow_cover": "积雪",
}

PLATFORM_MAP = {
    "Terra": "Terra卫星",
    "Aqua": "Aqua卫星",
    "Combined": "Terra+Aqua融合",
}

RESOLUTION_ORDER = ["250m", "500m", "500m/1km", "1km", "0.05°"]


def load_data() -> Tuple[Dict, Dict]:
    """Load products.json and gee_codes.json data files."""
    with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
        products_data = json.load(f)
    with open(GEE_CODES_FILE, "r", encoding="utf-8") as f:
        gee_data = json.load(f)
    return products_data, gee_data


def search_products(query: str, data: Dict, max_results: int = 10) -> List[Dict]:
    """Search products by keyword with scoring. Supports bilingual search."""
    products = data["products"]
    query_lower = query.lower()
    scored_results = []

    cn_category_map = {v: k for k, v in CATEGORY_MAP.items()}
    cn_platform_map = {v: k for k, v in PLATFORM_MAP.items()}

    for product in products:
        score = 0
        pid = product["id"].lower()
        name = product["name"].lower()
        name_cn = product["name_cn"].lower()
        category = product["category"]
        platform = product["platform"]
        resolution = product["resolution"]
        desc = product.get("description", "").lower()
        desc_cn = product.get("description_cn", "").lower()

        if query_lower == pid:
            score = 100
        elif query_lower in pid:
            score = 80
        elif query_lower in name or query_lower in name_cn:
            score = 60
        elif query_lower in category or query_lower in CATEGORY_MAP.get(category, "").lower():
            score = 50
        elif query_lower == CATEGORY_MAP.get(category, "").lower():
            score = 55
        elif query_lower in platform.lower() or query_lower == PLATFORM_MAP.get(platform, "").lower():
            score = 40
        elif query_lower in resolution.lower():
            score = 30
        elif query_lower in desc or query_lower in desc_cn:
            score = 20
        elif query_lower in cn_category_map and cn_category_map[query_lower] == category:
            score = 55
        elif query_lower in cn_platform_map and cn_platform_map[query_lower] == platform:
            score = 40

        for band in product.get("bands", []):
            if query_lower in band.get("name", "").lower() or query_lower in band.get("description_cn", "").lower():
                score = max(score, 25)
                break

        if score > 0:
            scored_results.append((score, product))

    scored_results.sort(key=lambda x: (-x[0], x[1]["id"]))
    return [item[1] for item in scored_results[:max_results]]


def get_product_by_id(product_id: str, data: Dict) -> Optional[Dict]:
    """Look up a product by its ID."""
    for product in data["products"]:
        if product["id"].upper() == product_id.upper():
            return product
    return None


def get_products_by_category(category: str, data: Dict) -> List[Dict]:
    """Filter products by category key or Chinese name."""
    cat_key = category.lower()
    if cat_key not in CATEGORY_MAP:
        for k, v in CATEGORY_MAP.items():
            if v == category:
                cat_key = k
                break
    return [p for p in data["products"] if p["category"].lower() == cat_key]


def get_products_by_platform(platform: str, data: Dict) -> List[Dict]:
    """Filter products by platform (Terra, Aqua, Combined)."""
    platform_lower = platform.lower()
    platform_key = platform_lower
    for k, v in PLATFORM_MAP.items():
        if platform_lower == k.lower() or platform_lower == v.lower():
            platform_key = k.lower()
            break
    return [p for p in data["products"] if p["platform"].lower() == platform_key]


def get_products_by_resolution(resolution: str, data: Dict) -> List[Dict]:
    """Filter products by resolution."""
    results = []
    res_lower = resolution.lower()
    for p in data["products"]:
        if res_lower in p["resolution"].lower():
            results.append(p)
    return results


def format_product_summary(p: Dict) -> str:
    """Format a one-line product summary."""
    cat_cn = CATEGORY_MAP.get(p["category"], p["category"])
    return f"{p['id']:12s} | {p['platform']:8s} | {p['resolution']:10s} | {p['temporal_resolution']:10s} | {cat_cn}"


def format_product_detail(p: Dict) -> str:
    """Format full product details."""
    lines = []
    lines.append("=" * 70)
    lines.append(f"Product ID: {p['id']}")
    lines.append(f"产品名称: {p['name_cn']}")
    lines.append(f"Name: {p['name']}")
    lines.append("-" * 70)
    lines.append(f"Platform/平台: {p['platform']} ({PLATFORM_MAP.get(p['platform'], '')})")
    lines.append(f"Category/类别: {p['category']} ({CATEGORY_MAP.get(p['category'], '')})")
    lines.append(f"Resolution/分辨率: {p['resolution']}")
    lines.append(f"Temporal Resolution/时间分辨率: {p['temporal_resolution']}")
    lines.append(f"Time Range/时间范围: {p['start_date']} ~ {p['end_date']}")
    lines.append(f"Version/版本: v{p['version']}")
    lines.append(f"Stage/阶段: {p['stage']}")
    lines.append(f"PI/首席研究员: {p.get('pi', 'N/A')}")
    lines.append(f"DOI: {p.get('doi', 'N/A')}")
    lines.append(f"GEE Collection: {p.get('gee_collection', 'N/A')}")
    lines.append("")
    lines.append(f"Description: {p.get('description', 'N/A')}")
    lines.append(f"中文介绍: {p.get('description_cn', 'N/A')}")

    if p.get("algorithms"):
        lines.append("")
        lines.append("Algorithms/算法:")
        for algo in p["algorithms"]:
            lines.append(f"  - {algo}")

    if p.get("bands"):
        lines.append("")
        lines.append("Bands/波段:")
        for band in p["bands"]:
            scale_str = f"x{band['scale']}" if band.get("scale", 1) != 1 else ""
            offset_str = f" +{band['offset']}" if band.get("offset") else ""
            wl_str = f" ({band['wavelength']})" if band.get("wavelength") else ""
            unit_str = f" [{band['units']}]" if band.get("units") else ""
            lines.append(f"  {band['name']:30s} {band['dtype']:8s} {scale_str}{offset_str}{unit_str}{wl_str}")
            lines.append(f"    {band.get('description_cn', band.get('description', ''))}")

    if p.get("official_url"):
        lines.append("")
        lines.append(f"Official Page: {p['official_url']}")
    if p.get("download_url"):
        lines.append(f"Download: {p['download_url']}")

    lines.append("=" * 70)
    return "\n".join(lines)


def format_gee_code(product_id: str, data: Dict, gee_data: Dict) -> str:
    """Return GEE code example for a product. Auto-generate if not in gee_codes.json."""
    pid_upper = product_id.upper()

    if pid_upper in gee_data:
        entry = gee_data[pid_upper]
        return (
            f"// {'='*60}\n"
            f"// {entry['description']}\n"
            f"// {entry['description_cn']}\n"
            f"// {'='*60}\n\n"
            f"{entry['code']}\n\n"
            f"{'='*60}\n"
            f"// 中文注释版本:\n"
            f"{'='*60}\n\n"
            f"{entry['code_cn']}"
        )

    product = get_product_by_id(pid_upper, data)
    if not product:
        return f"Product '{product_id}' not found."

    gee_collection = product.get("gee_collection", "N/A")
    bands = product.get("bands", [])
    main_band = bands[0]["name"] if bands else "None"
    resolution = product["resolution"]

    if "250" in resolution:
        scale = 250
    elif "500" in resolution:
        scale = 500
    elif "1km" in resolution or "1 km" in resolution:
        scale = 1000
    elif "0.05" in resolution:
        scale = 5000
    else:
        scale = 500

    auto_code = f"""// {'='*60}
// Auto-generated GEE code for {pid_upper}
// {product.get('description_cn', '')}
// {'='*60}

var collection = ee.ImageCollection('{gee_collection}');

var roi = ee.Geometry.Rectangle([110, 30, 120, 40]);

var filtered = collection
  .filterDate('2020-01-01', '2020-12-31')
  .filterBounds(roi);

print('Number of images:', filtered.size());

var median = filtered.median();
Map.addLayer(median, {{}}, '{pid_upper} Median');
Map.centerObject(roi, 6);
"""

    auto_code_cn = f"""// {'='*60}
// {pid_upper} 自动生成的GEE代码
// {product.get('description_cn', '')}
// {'='*60}

var collection = ee.ImageCollection('{gee_collection}');

// 定义研究区域
var roi = ee.Geometry.Rectangle([110, 30, 120, 40]);

// 筛选数据
var filtered = collection
  .filterDate('2020-01-01', '2020-12-31')
  .filterBounds(roi);

print('影像数量:', filtered.size());

// 可视化
var median = filtered.median();
Map.addLayer(median, {{}}, '{pid_upper} 中值');
Map.centerObject(roi, 6);
"""

    return (
        f"{auto_code}\n\n"
        f"{'='*60}\n"
        f"// 中文注释版本:\n"
        f"{'='*60}\n\n"
        f"{auto_code_cn}"
    )


def format_download_info(product_id: str, data: Dict) -> str:
    """Format download information for a product."""
    product = get_product_by_id(product_id, data)
    if not product:
        return f"Product '{product_id}' not found."

    lines = []
    lines.append(f"Download Information for {product['id']}")
    lines.append(f"{product['name_cn']}")
    lines.append("=" * 50)
    lines.append("")
    lines.append("Official Download Sources:")
    lines.append(f"  1. LAADS DAAC: https://ladsweb.modaps.eosdis.nasa.gov/")
    lines.append(f"  2. NASA Earthdata Search: https://search.earthdata.nasa.gov/")
    lines.append(f"  3. LP DAAC Data Pool: https://e4ftl01.cr.usgs.gov/")
    lines.append("")
    if product.get("download_url"):
        lines.append(f"Direct Download: {product['download_url']}")
    if product.get("doi"):
        lines.append(f"DOI: {product['doi']}")
    lines.append("")
    lines.append("Command Line Download (wget):")
    lines.append(f'  wget --user YOUR_USER --password YOUR_PASS "{product.get("download_url", "URL")}"')
    lines.append("")
    lines.append("Note: NASA Earthdata account required.")
    lines.append("Register at: https://urs.earthdata.nasa.gov/")
    lines.append("")
    lines.append("AppEEARS (area subset): https://appeears.earthdatacloud.nasa.gov/")
    lines.append("Google Earth Engine: Use collection ID directly")
    lines.append(f"  Collection: {product.get('gee_collection', 'N/A')}")

    return "\n".join(lines)


def compare_products(id1: str, id2: str, data: Dict) -> str:
    """Compare two products side-by-side."""
    p1 = get_product_by_id(id1, data)
    p2 = get_product_by_id(id2, data)

    if not p1 or not p2:
        missing = []
        if not p1:
            missing.append(id1)
        if not p2:
            missing.append(id2)
        return f"Product(s) not found: {', '.join(missing)}"

    lines = []
    lines.append("=" * 80)
    lines.append(f"{'Attribute':<25s} | {p1['id']:25s} | {p2['id']:25s}")
    lines.append("-" * 80)

    attrs = [
        ("Name (CN)", "name_cn"),
        ("Platform", "platform"),
        ("Category", "category"),
        ("Resolution", "resolution"),
        ("Temporal Res.", "temporal_resolution"),
        ("Start Date", "start_date"),
        ("End Date", "end_date"),
        ("Version", "version"),
        ("Stage", "stage"),
        ("PI", "pi"),
        ("DOI", "doi"),
        ("GEE Collection", "gee_collection"),
    ]

    for label, key in attrs:
        v1 = p1.get(key, "N/A")
        v2 = p2.get(key, "N/A")
        lines.append(f"{label:<25s} | {v1:<25s} | {v2:<25s}")

    lines.append("-" * 80)
    lines.append(f"{'Bands':<25s} | {', '.join(b['name'] for b in p1.get('bands', []))}")
    lines.append(f"{'':25s} | {', '.join(b['name'] for b in p2.get('bands', []))}")
    lines.append("=" * 80)

    return "\n".join(lines)


def get_statistics(data: Dict) -> Dict:
    """Compute database statistics."""
    products = data["products"]
    stats = {
        "total_products": len(products),
        "categories": {},
        "platforms": {},
        "resolutions": {},
        "versions": {},
        "stages": {},
    }

    for p in products:
        cat = p["category"]
        stats["categories"][cat] = stats["categories"].get(cat, 0) + 1

        plat = p["platform"]
        stats["platforms"][plat] = stats["platforms"].get(plat, 0) + 1

        res = p["resolution"]
        stats["resolutions"][res] = stats["resolutions"].get(res, 0) + 1

        ver = p["version"]
        stats["versions"][ver] = stats["versions"].get(ver, 0) + 1

        stage = p["stage"]
        stats["stages"][stage] = stats["stages"].get(stage, 0) + 1

    return stats


def format_statistics(stats: Dict) -> str:
    """Format database statistics."""
    lines = []
    lines.append("=" * 50)
    lines.append("MODIS Product Database Statistics")
    lines.append("=" * 50)
    lines.append(f"Total Products: {stats['total_products']}")
    lines.append("")

    lines.append("By Category:")
    for cat, count in sorted(stats["categories"].items(), key=lambda x: -x[1]):
        cat_cn = CATEGORY_MAP.get(cat, cat)
        lines.append(f"  {cat:<35s} {cat_cn:<15s} {count:3d} products")

    lines.append("")
    lines.append("By Platform:")
    for plat, count in sorted(stats["platforms"].items(), key=lambda x: -x[1]):
        plat_cn = PLATFORM_MAP.get(plat, plat)
        lines.append(f"  {plat:<20s} {plat_cn:<15s} {count:3d} products")

    lines.append("")
    lines.append("By Resolution:")
    for res, count in sorted(stats["resolutions"].items(), key=lambda x: -x[1]):
        lines.append(f"  {res:<20s} {count:3d} products")

    lines.append("")
    lines.append("By Version:")
    for ver, count in sorted(stats["versions"].items()):
        lines.append(f"  v{ver:<18s} {count:3d} products")

    lines.append("")
    lines.append("By Stage:")
    for stage, count in sorted(stats["stages"].items()):
        lines.append(f"  {stage:<20s} {count:3d} products")

    lines.append("=" * 50)
    return "\n".join(lines)


def list_categories(data: Dict) -> str:
    """List all categories with product counts."""
    products = data["products"]
    cat_counts = {}
    for p in products:
        cat = p["category"]
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    lines = []
    lines.append("=" * 55)
    lines.append("MODIS Product Categories")
    lines.append("=" * 55)
    lines.append(f"{'Category (EN)':<35s} {'Category (CN)':<15s} {'Count':>5s}")
    lines.append("-" * 55)

    for cat_key, cat_info in data.get("categories", {}).items():
        count = cat_counts.get(cat_key, 0)
        lines.append(f"{cat_info.get('name', cat_key):<35s} {cat_info.get('name_cn', ''):<15s} {count:>5d}")

    lines.append("-" * 55)
    lines.append(f"{'TOTAL':<50s} {len(products):>5d}")
    lines.append("=" * 55)
    return "\n".join(lines)


# ── Task-oriented presets (batch3 v0.2.0+) ─────────────────────────────────────
# Maps a user task to one or more recommended MODIS products.
# Used by the `preset` and `task` commands.

TASK_PRESETS = {
    "lst-uhi": {
        "description": "城市热岛分析：8 天合成 Terra 1km LST",
        "products": ["MOD11A2", "MYD11A2"],
        "category": "land_surface_temperature",
    },
    "lst-daily": {
        "description": "城市热岛：逐日 Terra/Aqua 1km LST",
        "products": ["MOD11A1", "MYD11A1"],
        "category": "land_surface_temperature",
    },
    "ndvi-250m": {
        "description": "16 天 250m NDVI 植被指数（最精细）",
        "products": ["MOD13Q1"],
        "category": "vegetation_indices",
    },
    "ndvi-500m": {
        "description": "16 天 500m NDVI",
        "products": ["MOD13A1"],
        "category": "vegetation_indices",
    },
    "ndvi-1km": {
        "description": "16 天 1km NDVI",
        "products": ["MOD13A2"],
        "category": "vegetation_indices",
    },
    "fire-daily": {
        "description": "逐日 1km 火点 / 热异常",
        "products": ["MOD14A1", "MYD14A1"],
        "category": "thermal_anomalies",
    },
    "fire-8d": {
        "description": "8 天 1km 火点合成",
        "products": ["MOD14A2", "MYD14A2"],
        "category": "thermal_anomalies",
    },
    "burned-area": {
        "description": "月值 500m 燃烧面积",
        "products": ["MCD64A1"],
        "category": "burned_area",
    },
    "landcover-yearly": {
        "description": "年值 500m 土地覆盖（IGBP 17 类）",
        "products": ["MCD12Q1"],
        "category": "land_cover",
    },
    "water-mask": {
        "description": "250m 水体掩膜",
        "products": ["MOD44W"],
        "category": "water_mask",
    },
    "snow-daily": {
        "description": "逐日 500m 积雪覆盖",
        "products": ["MOD10A1", "MYD10A1"],
        "category": "snow_cover",
    },
    "lai-8d": {
        "description": "8 天 500m LAI/FPAR",
        "products": ["MOD15A2H", "MYD15A2H"],
        "category": "lai_fpar",
    },
    "et-8d": {
        "description": "8 天 500m 蒸散发",
        "products": ["MOD16A2"],
        "category": "evapotranspiration",
    },
    "gpp-8d": {
        "description": "8 天 500m GPP",
        "products": ["MOD17A2H"],
        "category": "gpp_npp",
    },
    "albedo-16d": {
        "description": "16 天 500m NBAR / 反照率",
        "products": ["MCD43A4", "MCD43A3"],
        "category": "brdf_albedo",
    },
    "surface-reflectance-daily": {
        "description": "逐日 250/500m 地表反射率",
        "products": ["MOD09GA", "MYD09GA"],
        "category": "surface_reflectance",
    },
}


# ── Task keyword filter (for the `task` command) ───────────────────────────────
# Maps free-text task keywords to category + product hints.

TASK_KEYWORDS = {
    "vegetation": ("vegetation_indices", "NDVI / EVI 植被指数"),
    "ndvi": ("vegetation_indices", "NDVI"),
    "evi": ("vegetation_indices", "EVI"),
    "lst": ("land_surface_temperature", "地表温度"),
    "temperature": ("land_surface_temperature", "地表温度"),
    "热岛": ("land_surface_temperature", "城市热岛"),
    "uhi": ("land_surface_temperature", "城市热岛"),
    "fire": ("thermal_anomalies", "火点 / 热异常"),
    "火灾": ("thermal_anomalies", "火点"),
    "burned": ("burned_area", "燃烧面积"),
    "燃烧": ("burned_area", "燃烧"),
    "landcover": ("land_cover", "土地覆盖"),
    "land-cover": ("land_cover", "土地覆盖"),
    "土地覆盖": ("land_cover", "土地覆盖"),
    "water": ("water_mask", "水体掩膜"),
    "水体": ("water_mask", "水体"),
    "snow": ("snow_cover", "积雪"),
    "积雪": ("snow_cover", "积雪"),
    "lai": ("lai_fpar", "叶面积指数"),
    "fpar": ("lai_fpar", "FPAR"),
    "蒸散发": ("evapotranspiration", "ET"),
    "evapotranspiration": ("evapotranspiration", "ET"),
    "gpp": ("gpp_npp", "GPP"),
    "npp": ("gpp_npp", "NPP"),
    "初级生产力": ("gpp_npp", "GPP/NPP"),
    "albedo": ("brdf_albedo", "反照率"),
    "反照率": ("brdf_albedo", "反照率"),
    "reflectance": ("surface_reflectance", "地表反射率"),
    "反射率": ("surface_reflectance", "地表反射率"),
}


def show_help() -> str:
    """Return help text."""
    return """
MODIS Product Query Tool | MODIS产品数据查询工具
=================================================

Usage: python modis_products.py <command> [args] [--qa PATH]

Commands:
  search <keyword> [--limit N]     Search products by keyword (bilingual)
  show <product_id>                Show detailed product information
  gee <product_id>                 Show GEE code example
  download <product_id>            Show download information
  category <category_name>         List products in a category
  categories                       List all categories with counts
  platform <platform>              Filter by platform (Terra/Aqua/Combined)
  resolution <resolution>          Filter by resolution (250m/500m/1km)
  compare <id1> <id2>              Compare two products side-by-side
  stats                            Show database statistics
  preset <name> | list             Apply a task-oriented preset (e.g. lst-uhi, ndvi-250m)
  task <keyword>                   Filter by task (e.g. fire, ndvi, lst, 火灾, 积雪)
  task-list                        List all available task keywords
  place <name>                     Resolve a Chinese place name to bbox and list
                                   MODIS products that cover it (offline +
                                   Open-Meteo + Nominatim via _geoskill_core).
  help                             Show this help message

Options (any command):
  --qa PATH                        Write a JSON run-summary sidecar to PATH
                                   (records command / primary input / matched
                                   products / timestamp). Works with every
                                   command above.

Examples:
  python modis_products.py search NDVI
  python modis_products.py search 植被指数 --qa search.qa.json
  python modis_products.py show MOD13Q1 --qa mod13q1.qa.json
  python modis_products.py gee MOD11A1
  python modis_products.py category vegetation_indices
  python modis_products.py platform Terra
  python modis_products.py resolution 500m
  python modis_products.py compare MOD13Q1 MYD13Q1
  python modis_products.py stats
  python modis_products.py preset list
  python modis_products.py preset lst-uhi
  python modis_products.py task fire
  python modis_products.py task 火灾
  python modis_products.py place 北京市
  python modis_products.py place 长江三角洲 --qa place.qa.json
"""


def write_qa_summary(qa_path: str, command: str, args: List[str], result: Dict) -> None:
    """Write a JSON run-summary sidecar (Phase 5 optimization).

    Records the command, parsed inputs (query / product id / category / platform /
    resolution / task / preset), and result counts (matched / n_results / products).
    """
    import json as _json
    import os as _os
    from datetime import datetime as _dt, timezone as _tz

    # Build a parsed-args dict for the most common commands.
    parsed: Dict[str, Any] = {"raw": list(args)}
    # Order matters: prefer command-specific keys first so the sidecar
    # records the *user-typed* primary, not an inferred category.
    extras = (
        result.get("query")
        or result.get("product_id")
        or result.get("task")
        or result.get("preset")
        or result.get("place")
        or result.get("category")
        or result.get("platform")
        or result.get("resolution")
    )
    if extras is not None:
        parsed["primary"] = extras
    if "results" in result and isinstance(result["results"], list):
        parsed["n_results"] = len(result["results"])
    if "products" in result and isinstance(result["products"], list):
        parsed["matched_products"] = result["products"]
    if result.get("bbox"):
        parsed["bbox"] = result["bbox"]
    if result.get("n_covered") is not None:
        parsed["n_covered"] = result["n_covered"]

    summary = {
        "skill": "modis-product-search",
        "command": command,
        "version": "0.2.0",
        "timestamp": _dt.now(_tz.utc).isoformat(),
        "parsed": parsed,
        "result_keys": sorted([k for k in result.keys() if k != "output"]),
    }
    qa_p = _os.path.abspath(qa_path)
    parent = _os.path.dirname(qa_p)
    if parent:
        _os.makedirs(parent, exist_ok=True)
    with open(qa_p, "w", encoding="utf-8") as f:
        _json.dump(summary, f, ensure_ascii=False, indent=2)


def main(args: Optional[List[str]] = None) -> Any:
    """Main entry point for the MODIS product query tool."""
    if args is None:
        args = sys.argv[1:]

    if not args:
        return {"help": show_help(), "status": "ok"}

    # Phase 5: extract --qa PATH from tail of args (so any subcommand can
    # request a JSON run-summary sidecar without special-casing each branch).
    qa_path: Optional[str] = None
    if "--qa" in args:
        idx = args.index("--qa")
        if idx + 1 < len(args):
            qa_path = args[idx + 1]
            args = args[:idx] + args[idx + 2:]
        else:
            return {"error": "Usage: <command> [...] --qa PATH"}

    result = _dispatch(args)

    if qa_path and isinstance(result, dict):
        command = args[0].lower() if args else "help"
        try:
            write_qa_summary(qa_path, command, args, result)
        except OSError as e:
            result = {**result, "qa_error": f"could not write {qa_path}: {e}"}

    return result


def _dispatch(args: List[str]) -> Any:
    """Inner dispatch — returns the per-command result dict. Split out from
    main() so --qa handling can wrap it."""
    if not args:
        return {"help": show_help(), "status": "ok"}

    command = args[0].lower()
    data, gee_data = load_data()

    if command == "help":
        return {"help": show_help(), "status": "ok"}

    elif command == "search":
        if len(args) < 2:
            return {"error": "Usage: search <keyword> [--limit N]"}
        query = args[1]
        max_results = 10
        if "--limit" in args:
            idx = args.index("--limit")
            if idx + 1 < len(args):
                max_results = int(args[idx + 1])
        results = search_products(query, data, max_results)
        if not results:
            return {"query": query, "results": [], "message": "No products found."}
        output = f"Search results for '{query}' ({len(results)} found):\n\n"
        for p in results:
            output += format_product_summary(p) + "\n"
        return {"query": query, "results": [p["id"] for p in results], "output": output}

    elif command == "show":
        if len(args) < 2:
            return {"error": "Usage: show <product_id>"}
        product = get_product_by_id(args[1], data)
        if not product:
            return {"error": f"Product '{args[1]}' not found."}
        output = format_product_detail(product)
        return {"product_id": product["id"], "output": output}

    elif command == "gee":
        if len(args) < 2:
            return {"error": "Usage: gee <product_id>"}
        product = get_product_by_id(args[1], data)
        if not product:
            return {"error": f"Product '{args[1]}' not found."}
        output = format_gee_code(product["id"], data, gee_data)
        return {"product_id": product["id"], "output": output}

    elif command == "download":
        if len(args) < 2:
            return {"error": "Usage: download <product_id>"}
        product = get_product_by_id(args[1], data)
        if not product:
            return {"error": f"Product '{args[1]}' not found."}
        output = format_download_info(product["id"], data)
        return {"product_id": product["id"], "output": output}

    elif command == "category":
        if len(args) < 2:
            return {"error": "Usage: category <category_name>"}
        cat_key = args[1].lower()
        valid_cats = list(CATEGORY_MAP.keys()) + list(CATEGORY_MAP.values())
        if cat_key not in [c.lower() for c in valid_cats]:
            return {"error": f"Invalid category. Use 'categories' to list all."}
        results = get_products_by_category(args[1], data)
        if not results:
            return {"category": args[1], "results": [], "message": "No products found."}
        cat_cn = CATEGORY_MAP.get(cat_key, cat_key)
        output = f"Category: {args[1]} ({cat_cn}) - {len(results)} products:\n\n"
        for p in results:
            output += format_product_summary(p) + "\n"
        return {"category": args[1], "results": [p["id"] for p in results], "output": output}

    elif command == "categories":
        output = list_categories(data)
        return {"output": output}

    elif command == "platform":
        if len(args) < 2:
            return {"error": "Usage: platform <Terra|Aqua|Combined>"}
        results = get_products_by_platform(args[1], data)
        if not results:
            return {"platform": args[1], "results": [], "message": "No products found."}
        plat_cn = PLATFORM_MAP.get(args[1].capitalize(), args[1])
        output = f"Platform: {args[1]} ({plat_cn}) - {len(results)} products:\n\n"
        for p in results:
            output += format_product_summary(p) + "\n"
        return {"platform": args[1], "results": [p["id"] for p in results], "output": output}

    elif command == "resolution":
        if len(args) < 2:
            return {"error": "Usage: resolution <250m|500m|1km>"}
        results = get_products_by_resolution(args[1], data)
        if not results:
            return {"resolution": args[1], "results": [], "message": "No products found."}
        output = f"Resolution: {args[1]} - {len(results)} products:\n\n"
        for p in results:
            output += format_product_summary(p) + "\n"
        return {"resolution": args[1], "results": [p["id"] for p in results], "output": output}

    elif command == "compare":
        if len(args) < 3:
            return {"error": "Usage: compare <product_id1> <product_id2>"}
        output = compare_products(args[1], args[2], data)
        return {"products": [args[1], args[2]], "output": output}

    elif command == "stats":
        stats = get_statistics(data)
        output = format_statistics(stats)
        return {"stats": stats, "output": output}

    elif command == "preset":
        # New in batch3: list or apply a task-oriented preset
        if len(args) < 2:
            return {"error": "Usage: preset <name>|list",
                    "available": sorted(TASK_PRESETS.keys())}
        if args[1].lower() == "list":
            lines = ["Available task presets:"]
            for name, p in sorted(TASK_PRESETS.items()):
                lines.append(f"  {name:<28} {p['description']}")
            return {"presets": sorted(TASK_PRESETS.keys()),
                    "output": "\n".join(lines)}
        preset_name = args[1]
        if preset_name not in TASK_PRESETS:
            return {"error": f"Unknown preset: {preset_name}",
                    "available": sorted(TASK_PRESETS.keys())}
        p = TASK_PRESETS[preset_name]
        products = p["products"]
        # Show details for each product in the preset
        lines = [f"Preset: {preset_name} — {p['description']}", "=" * 60]
        rows = []
        for pid in products:
            prod = get_product_by_id(pid, data)
            if prod:
                rows.append(prod)
                lines.append(format_product_summary(prod))
        lines.append("\nUse `show <id>` for full details, `gee <id>` for GEE code, "
                     "`download <id>` for download info.")
        return {"preset": preset_name, "products": products,
                "records": rows, "output": "\n".join(lines)}

    elif command == "task":
        # New in batch3: filter by task keyword
        if len(args) < 2:
            return {"error": "Usage: task <keyword>  (e.g. task fire, task ndvi, task 火灾)"}
        keyword = args[1].lower()
        if keyword not in TASK_KEYWORDS:
            # Fallback: try matching by category or platform
            return {
                "error": f"Unknown task: {keyword}",
                "available": sorted(TASK_KEYWORDS.keys()),
                "hint": "Try `task list` for all available keywords.",
            }
        cat, label = TASK_KEYWORDS[keyword]
        results = get_products_by_category(cat, data)
        # Filter to known 'current' products (avoid legacy duplicates)
        cur_ids = {"MOD13Q1", "MOD13A1", "MOD13A2", "MOD13A3",
                   "MOD11A1", "MOD11A2", "MYD11A1", "MYD11A2",
                   "MCD12Q1", "MCD12Q2", "MOD14A1", "MYD14A1",
                   "MOD14A2", "MYD14A2", "MCD64A1",
                   "MOD09GA", "MOD09A1", "MOD15A2H", "MYD15A2H",
                   "MOD16A2", "MOD16A3", "MOD17A2H", "MCD43A4",
                   "MCD43A3", "MCD43A1",
                   "MOD44W", "MOD10A1", "MYD10A1", "MOD10A2"}
        if results:
            results = [r for r in results if r["id"] in cur_ids] or results
        lines = [f"Task: {keyword} → {label}  (category={cat})", "=" * 60]
        for r in results:
            lines.append(format_product_summary(r))
        lines.append(f"\n{len(results)} product(s) found. Use `show <id>` for details.")
        return {"task": keyword, "category": cat, "label": label,
                "products": [r["id"] for r in results],
                "output": "\n".join(lines)}

    elif command == "task-list":
        # Convenience alias for `task list`
        lines = ["Available task keywords (use as `task <keyword>`):"]
        for kw, (cat, label) in sorted(TASK_KEYWORDS.items()):
            lines.append(f"  {kw:<28} {label}  → {cat}")
        return {"tasks": sorted(TASK_KEYWORDS.keys()),
                "output": "\n".join(lines)}

    elif command == "place":
        # New in batch-C: resolve a Chinese place name to bbox and list
        # MODIS products that cover the bbox. All current products are global
        # so every product covers the place; the place/bbox is reported so
        # downstream tools can chain (download / subset).
        if len(args) < 2:
            return {"error": "Usage: place <name>  (e.g. place 北京市, place 长江三角洲)"}
        place_name = args[1]
        if not _HAS_AOI or _resolve_place is None:
            return {
                "error": "--place requires _geoskill_core/aoi.py (vendored)",
                "hint": "Ensure the skill ships with _geoskill_core/aoi.py.",
            }
        try:
            manifest = _resolve_place(place_name, buffer_deg=0.0)
        except _NoMatchError as exc:
            return {"error": f"Place resolution failed: {exc}", "place": place_name}
        except Exception as exc:  # noqa: BLE001
            return {"error": f"Place resolution failed: {exc}", "place": place_name}
        bbox = list(manifest.bbox_wgs84) if manifest.bbox_wgs84 else None
        if not bbox or len(bbox) != 4:
            return {"error": "place resolved without a bbox", "place": place_name}
        # All global products cover the place; flag any that are explicitly
        # non-global by name as excluded.
        all_products = data["products"]
        covered: List[Dict] = []
        excluded: List[Dict] = []
        for prod in all_products:
            name_lc = (prod.get("name") or "").lower()
            if any(kw in name_lc for kw in _NON_GLOBAL_KEYWORDS):
                excluded.append(prod)
            else:
                covered.append(prod)
        lines = [
            f"Place: {place_name}",
            f"  bbox (W,S,E,N): {bbox[0]:.4f}, {bbox[1]:.4f}, {bbox[2]:.4f}, {bbox[3]:.4f}",
            f"  resolver: {manifest.resolver}",
            f"  confidence: {manifest.confidence}",
            "",
            f"{len(covered)} MODIS product(s) cover this place:",
        ]
        for p in covered:
            lines.append(format_product_summary(p))
        if excluded:
            lines.append("")
            lines.append(f"{len(excluded)} product(s) excluded (non-global):")
            for p in excluded:
                lines.append(format_product_summary(p))
        return {
            "place": place_name,
            "bbox": bbox,
            "resolver": manifest.resolver,
            "confidence": manifest.confidence,
            "n_covered": len(covered),
            "n_excluded": len(excluded),
            "covered_ids": [p["id"] for p in covered],
            "excluded_ids": [p["id"] for p in excluded],
            "output": "\n".join(lines),
        }

    else:
        return {"error": f"Unknown command: {command}", "help": show_help()}


if __name__ == "__main__":
    result = main()
    print(json.dumps(result, indent=2, ensure_ascii=False))
