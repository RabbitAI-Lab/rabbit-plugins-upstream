"""MCP Server：电商碳排分析工具层（纯净模式）。

只负责数据查询，不接触任何 LLM，也不向 stdout 打印（会污染 stdio JSON-RPC 通道）。
由 llm_client.py 作为子进程启动，通过 stdio 通信。
"""
import os
import sqlite3
from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Ecommerce-Carbon-Analyzer")

# 用绝对路径，保证主子进程指向同一个数据库文件
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ABS_PATH, "ecommerce.db")


def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS products (id TEXT PRIMARY KEY, name TEXT, weight_kg REAL);
        CREATE TABLE IF NOT EXISTS bom (parent_id TEXT, child_id TEXT, quantity REAL, PRIMARY KEY (parent_id, child_id));
        CREATE TABLE IF NOT EXISTS inventory (product_id TEXT PRIMARY KEY, warehouse TEXT, cost REAL, carbon_pkg REAL);
        CREATE TABLE IF NOT EXISTS shipping_rules (from_wh TEXT, to_city TEXT, dist_km REAL, cost_per_kg REAL, PRIMARY KEY (from_wh, to_city));

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


# 模块级初始化一次（幂等：CREATE IF NOT EXISTS + INSERT OR REPLACE）
init_db()


@mcp.tool()
def search_product(keyword: str) -> List[dict]:
    """根据关键词搜索商品，返回匹配的商品 id 与名称。"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute(
        "SELECT id, name FROM products WHERE name LIKE ?", (f"%{keyword}%",)
    ).fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in res]


@mcp.tool()
def get_product_structure(product_id: str) -> List[dict]:
    """获取某个商品的 BOM 构成（子件 id 与数量）。"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute(
        "SELECT child_id, quantity FROM bom WHERE parent_id = ?", (product_id,)
    ).fetchall()
    conn.close()
    return [{"id": r[0], "qty": r[1]} for r in res]


@mcp.tool()
def get_item_details(product_id: str) -> dict:
    """获取单品重量(kg)、成本(元)、碳排(kg CO2)与所在仓库。"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute(
        """
        SELECT p.weight_kg, i.cost, i.carbon_pkg, i.warehouse
        FROM products p JOIN inventory i ON p.id = i.product_id
        WHERE p.id = ?
        """,
        (product_id,),
    ).fetchone()
    conn.close()
    if res:
        return {"weight": res[0], "cost": res[1], "carbon": res[2], "warehouse": res[3]}
    return {"error": "not found"}


@mcp.tool()
def calculate_shipping(from_wh: str, to_city: str, total_weight: float) -> dict:
    """根据仓库、目的地与总重量计算运费与运输碳排。"""
    conn = sqlite3.connect(DB_PATH)
    res = conn.execute(
        "SELECT dist_km, cost_per_kg FROM shipping_rules WHERE from_wh = ? AND to_city = ?",
        (from_wh, to_city),
    ).fetchone()
    conn.close()
    if res:
        return {
            "shipping_cost": round(total_weight * res[1], 4),
            "shipping_carbon": round(total_weight * res[0] * 0.0001, 4),
        }
    return {"error": "no path"}


if __name__ == "__main__":
    mcp.run()
