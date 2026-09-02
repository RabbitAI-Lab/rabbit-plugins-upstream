---
name: ecommerce-carbon-analyzer
description: 电商碳排分析助手。给定“发 N 套某商品到某城市”，通过 MCP 工具查询 BOM 构成、单品重量/成本/碳排与运费，计算总重量、总成本、总碳排放。Use when the user asks about 礼盒/商品 的重量、成本、碳排放计算，或需要 llm+mcp 的电商物流碳排分析。
license: MIT
---

# 电商碳排分析助手 (Ecommerce Carbon Analyzer)

## 何时使用

当用户需要计算某商品（尤其带 BOM 的礼盒/套装）的**总重量、总成本、总碳排放**，例如：

- “发 10 套红酒礼盒到北京，算一下总重量、总成本、总碳排放”
- “帮我算这批货的运费和碳排”

本 skill 提供：数据模型、4 个 MCP 工具的语义、计算规则、参考实现脚本与参考标准答案。

## 数据模型（SQLite：ecommerce.db）

| 表 | 字段 | 说明 |
|----|------|------|
| products | id, name, weight_kg | 商品主数据（含成品/包装自身重量） |
| bom | parent_id, child_id, quantity | BOM 子件构成 |
| inventory | product_id, warehouse, cost, carbon_pkg | 单品成本、碳排、所在仓库 |
| shipping_rules | from_wh, to_city, dist_km, cost_per_kg | 运输路线 |

内置数据：

- `SET-001` 春季红酒礼盒（包装 0.5 kg / 5 元 / 0.5 kg CO2）
- BOM：`WINE-01` 法国红酒 ×1（1.2 kg / 120 元 / 5.0 kg CO2）+ `GLASS-02` 水晶酒杯 ×2（0.3 kg / 15 元 / 1.2 kg CO2）
- 路线 Tianjin → Beijing：150 km，2 元/kg

## 四个 MCP 工具

1. `search_product(keyword)` → 按关键词搜商品 id
2. `get_product_structure(product_id)` → 返回 BOM 子件（id + qty）
3. `get_item_details(product_id)` → 返回 {weight, cost, carbon, warehouse}
4. `calculate_shipping(from_wh, to_city, total_weight)` → 返回 {shipping_cost, shipping_carbon}

## 计算规则（重要）

1. 先 `search_product` 定位目标商品 id。
2. `get_product_structure` 拿 BOM，对每个子件 `get_item_details` 后按数量累加。
3. **礼盒本身（SET-001）既是成品又有独立重量/成本/碳排，属于包装，要一并计入**——这是最容易漏的一步。
4. `calculate_shipping` 算运费与运输碳排（碳排 = 重量 × 距离 × 0.0001）。
5. 总成本 = 商品成本 + 运费；总碳排放 = 商品碳排 + 运输碳排。

## 参考标准答案（10 套红酒礼盒发北京）

```
单套：重量 2.3 kg，成本 155 元，碳排 7.9 kg CO2
10 套：重量 23 kg，成本 1550 元，碳排 79 kg CO2
运费 46 元，运输碳排 0.345 kg CO2
总重量   = 23 kg
总成本   = 1596 元
总碳排放 = 79.345 kg CO2
```

## 参考实现

脚本随本 skill 打包在同目录下：

- `ecommerce_server.py` — MCP Server（工具层）
- `llm_client.py` — LLM + MCP 客户端（openai / deepseek / anthropic 三种后端）
- `offline_check.py` — 无需 API Key 的离线自检
- `requirements.txt` / `.env.example` — 依赖与 API Key 模板

```bash
pip install -r requirements.txt
python offline_check.py                                   # 验证计算逻辑
python llm_client.py --provider openai --model gpt-4o     # 用模型跑
python llm_client.py --provider deepseek --model deepseek-chat
python llm_client.py --provider anthropic --model claude-sonnet-4-6
```

**回答用户时**：优先按上面的计算规则直接给出结果并展示过程；如需完整 LLM+MCP 链路演示，运行 `llm_client.py`。
