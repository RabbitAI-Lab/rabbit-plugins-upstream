import os
import sqlite3
from typing import List

from mcp.server.mcpserver import MCPServer

# ==========================================
# 1. MCP Server 定义 (纯净模式)
# ==========================================
mcp = MCPServer("Ecommerce-Carbon-Analyzer")

# 使用绝对路径确保主子进程数据库一致
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ABS_PATH, "ecommerce.db")


def init_db():
    """初始化数据库并插入示例数据"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS products (id TEXT PRIMARY KEY, name TEXT, weight_kg REAL);
            CREATE TABLE IF NOT EXISTS bom (parent_id TEXT, child_id TEXT, quantity REAL);
            CREATE TABLE IF NOT EXISTS inventory (product_id TEXT, warehouse TEXT, cost REAL, carbon_pkg REAL);
            CREATE TABLE IF NOT EXISTS shipping_rules (from_wh TEXT, to_city TEXT, dist_km REAL, cost_per_kg REAL);

            INSERT OR REPLACE INTO products VALUES ('SET-001', '春季红酒礼盒', 0.5);
            INSERT OR REPLACE INTO products VALUES ('WINE-01', '法国红酒', 1.2);
            INSERT OR REPLACE INTO products VALUES ('GLASS-02', '水晶酒杯', 0.3);

            INSERT OR REPLACE INTO bom VALUES ('SET-001', 'WINE-01', 1.0);
            INSERT OR REPLACE INTO bom VALUES ('SET-001', 'GLASS-02', 2.0);

            INSERT OR REPLACE INTO inventory VALUES ('WINE-01', 'Tianjin', 120.0, 5.0);
            INSERT OR REPLACE INTO inventory VALUES ('GLASS-02', 'Tianjin', 15.0, 1.2);
            INSERT OR REPLACE INTO inventory VALUES ('SET-001', 'Tianjin', 5.0, 0.5);

            INSERT OR REPLACE INTO shipping_rules VALUES ('Tianjin', 'Beijing', 150.0, 2.0);
        """)
        conn.commit()
        conn.close()
        print("数据库初始化完成", file=__import__('sys').stderr)
    except Exception as e:
        print(f"数据库初始化失败: {e}", file=__import__('sys').stderr)


@mcp.tool()
def search_product(keyword: str) -> List[dict]:
    """根据关键词搜索商品ID"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute("SELECT id, name FROM products WHERE name LIKE ?", (f"%{keyword}%",)).fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in res]


@mcp.tool()
def get_product_structure(product_id: str) -> List[dict]:
    """获取BOM构成（子件ID及数量）"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute("SELECT child_id, quantity FROM bom WHERE parent_id = ?", (product_id,)).fetchall()
    conn.close()
    return [{"id": r[0], "qty": r[1]} for r in res]


@mcp.tool()
def get_item_details(product_id: str) -> dict:
    """获取单品重量、成本、碳排放及所在仓库"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute("""
        SELECT p.weight_kg, i.cost, i.carbon_pkg, i.warehouse
        FROM products p JOIN inventory i ON p.id = i.product_id
        WHERE p.id = ?
    """, (product_id,)).fetchone()
    conn.close()
    if res:
        return {"weight": res[0], "cost": res[1], "carbon": res[2], "warehouse": res[3]}
    return {"error": "not found"}


@mcp.tool()
def calculate_shipping(from_wh: str, to_city: str, total_weight: float) -> dict:
    """根据仓库、目标城市和总重量计算运费和碳排放"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute("SELECT dist_km, cost_per_kg FROM shipping_rules WHERE from_wh = ? AND to_city = ?",
                       (from_wh, to_city)).fetchone()
    conn.close()
    if res:
        return {
            "shipping_cost": total_weight * res[1],
            "shipping_carbon": total_weight * res[0] * 0.0001
        }
    return {"error": "no path"}

if __name__ == "__main__":
    init_db()
    mcp.run()