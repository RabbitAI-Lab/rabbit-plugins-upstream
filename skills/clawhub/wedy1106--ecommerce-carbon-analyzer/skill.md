---
name: ecommerce-carbon-analyzer
version: 1.0.0
description: 电商碳足迹与成本分析器 - 通过 MCP 协议连接电商数据库，利用 LLM 多轮推理自动计算商品发货的总重量、总成本和总碳排放。支持 BOM 展开、多仓库查询及物流规则计算。
author: jujing
tags:
  - ecommerce
  - carbon-footprint
  - mcp
  - logistics
  - cost-calculator
  - multi-turn-agent
---

# 电商碳足迹与成本分析器 (Ecommerce Carbon & Cost Analyzer)

## 描述

本 Skill 实现了一个完整的 **LLM + MCP (Model Context Protocol)** 应用，能够自动通过多轮对话方式调用 MCP 工具，完成以下任务：

1. 根据关键词搜索商品
2. 展开商品 BOM（物料清单）结构
3. 获取各子件的重量、成本、碳排放及仓库信息
4. 根据发货地和目的地计算运费及运输碳排放
5. 汇总输出总重量、总成本、总碳排放

## 触发场景

当用户提出以下类型的问题时，自动激活此 Skill：

- "给北京发10套红酒礼盒，算下总重量、成本和碳排放"
- "计算发货成本 / 碳足迹"
- 提到关键词：`红酒礼盒`、`电商发货`、`BOM`、`碳排放`、`物流成本`
- 需要多步工具调用来完成计算的任务

## 项目结构