"""离线自检（无需任何 API Key）：直接通过 MCP 协议调用工具，
走一遍 LLM 本该走的调用链，打印中间结果与最终参考答案，
用于验证 MCP Server 与计算逻辑是否正确。

用法：python offline_check.py
"""
import asyncio
import json
import os
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

SERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ecommerce_server.py")


def extract(result):
    """统一提取工具返回值：优先 structuredContent['result']，否则解析 content 文本。"""
    sc = result.structuredContent
    if sc and isinstance(sc, dict) and "result" in sc:
        return sc["result"]
    texts = [getattr(c, "text", None) for c in result.content]
    texts = [t for t in texts if t is not None]
    if len(texts) == 1:
        return json.loads(texts[0])
    return [json.loads(t) for t in texts]


async def main():
    params = StdioServerParameters(command=sys.executable, args=[SERVER_PATH])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = (await session.list_tools()).tools
            print("可用工具:", [t.name for t in tools])

            # 1. 搜索商品
            r = await session.call_tool("search_product", {"keyword": "红酒礼盒"})
            hits = extract(r)
            print("search_product('红酒礼盒') ->", hits)
            product_id = hits[0]["id"]

            # 2. BOM 构成
            r = await session.call_tool("get_product_structure", {"product_id": product_id})
            bom = extract(r)
            print("get_product_structure ->", bom)

            # 3. 单品详情（含礼盒本身的包装）
            ids = [product_id] + [b["id"] for b in bom]
            details = {}
            for pid in ids:
                r = await session.call_tool("get_item_details", {"product_id": pid})
                details[pid] = extract(r)
                print(f"get_item_details({pid}) ->", details[pid])

            # 4. 单套合计：包装 + 各子件
            weight = details[product_id]["weight"]
            cost = details[product_id]["cost"]
            carbon = details[product_id]["carbon"]
            for b in bom:
                qty = b["qty"]
                weight += details[b["id"]]["weight"] * qty
                cost += details[b["id"]]["cost"] * qty
                carbon += details[b["id"]]["carbon"] * qty

            n = 10
            total_weight = weight * n
            total_cost = cost * n
            total_carbon = carbon * n

            # 5. 运费与运输碳排
            warehouse = details[product_id]["warehouse"]
            r = await session.call_tool(
                "calculate_shipping",
                {"from_wh": warehouse, "to_city": "Beijing", "total_weight": total_weight},
            )
            ship = extract(r)
            print("calculate_shipping ->", ship)

            print("\n===== 参考答案 =====")
            print(f"单套: 重量 {weight} kg, 成本 {cost} 元, 碳排 {carbon} kg CO2")
            print(f"{n} 套商品: 重量 {total_weight} kg, 成本 {total_cost} 元, 碳排 {total_carbon} kg CO2")
            print(f"运费 {ship['shipping_cost']} 元, 运输碳排 {ship['shipping_carbon']} kg CO2")
            print(f"总重量   = {total_weight} kg")
            print(f"总成本   = {total_cost + ship['shipping_cost']} 元")
            print(f"总碳排放 = {total_carbon + ship['shipping_carbon']} kg CO2")


if __name__ == "__main__":
    asyncio.run(main())
