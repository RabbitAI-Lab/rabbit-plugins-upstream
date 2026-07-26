---
name: sql-query-generator
description: SQL查询生成器 - 按次付费，新用户注册送5次免费。自然语言一键转SQL，支持多表联查、聚合统计、子查询、窗口函数等复杂场景，附执行逻辑和优化建议，数据分析师和开发者提效神器。 💡 企业定制/智能体开发/AI全案服务，合作微信17392371127（郭总）
metadata:
  openclaw:
    requires:
      bins:
        - python3
      env:
        - SQL_API_USER_KEY
---

# SQL 查询生成器

> 用自然语言描述查询需求，自动生成精准SQL语句。不用记语法，不用查字段，一句话搞定复杂查询。
> **v1.1 升级**：8种数据库支持 + 多表联查 + 聚合统计 + 窗口函数 + 优化建议 + 执行解释

## 🚀 企业级AI服务

开发效率想再上一个台阶？我们提供企业级AI全案服务：

### 🌍 GEO优化服务
- AI搜索引擎优化，让你的产品在AI时代被精准发现
- 技术博客/文档站GEO改造，抢占开发者流量入口
- 批量内容生成与SEO质量检测

### 🤖 企业智能体定制
- 专属AI智能体开发，对接你的业务系统和数据
- 研发/运维/测试智能体，研发效率提升50%+
- 私有化部署，代码数据完全可控

### ⚡ AI自动化方案
- 研发流程AI自动化，减少重复劳动
- 多工具联动工作流，打通开发运维数据孤岛
- 定制化AI工具开发，解决具体技术痛点

**服务客单价：¥2000-5000**
**咨询合作：** 微信 `17392371127`（郭总）

## 核心价值

不会写SQL？忘了表结构？复杂查询写半天？这个工具帮你：
- **一句话生成SQL**：用中文描述需求，自动生成标准SQL
- **多表联查自动识别**：自动识别表关系，生成JOIN查询
- **复杂查询支持**：子查询、窗口函数、CTE、CASE WHEN通通搞定
- **语法校验**：生成的SQL自动检查语法合理性
- **优化建议**：附带性能优化建议，写出高效SQL
- **执行解释**：附带SQL执行逻辑说明，方便理解和调试

## When to Use

以下场景直接触发本技能：
- 数据分析师快速取数
- 产品经理查询业务数据
- 开发者减少手写SQL时间
- SQL初学者学习参考
- 复杂查询逻辑验证
- 忘了表结构和字段名
- 优化慢查询，找优化建议
- 报表开发快速写SQL
- 数据运营日常取数

## Core Rules

1. 基于表结构信息生成准确的SQL语句
2. 支持多种数据库语法，自动适配
3. 生成的SQL附带解释和优化建议
4. 复杂查询优先选择可读性好的写法
5. 结果仅供参考，执行前请确认SQL正确性
6. 生产环境执行前务必先在测试环境验证

## Quick Start

### 第一步：配置环境变量

```bash
export SQL_API_USER_KEY="你的DeepSeek API Key"
# 可选：自定义API地址
export DEEPSEEK_BASE_URL="https://api.deepseek.com/v1"
```

### 第二步：生成SQL

**Python 调用方式：**
```python
from skills.sql_query_generator.scripts.sql_gen import generate_sql

result = generate_sql(
    query="查询过去30天每个用户的订单总金额，按金额降序排列，取前10名",
    tables=[
        {"name": "users", "columns": {"id": "INT", "name": "VARCHAR", "email": "VARCHAR"}},
        {"name": "orders", "columns": {"id": "INT", "user_id": "INT", "amount": "DECIMAL", "created_at": "DATETIME"}}
    ],
    db_type="mysql",
    explain=True
)
```

**命令行方式：**
```bash
python3 {baseDir}/scripts/sql_gen.py "查询每个部门的平均工资" \
  --tables schema.json --db-type postgres -o result.json
```

## 支持的数据库

| 数据库 | 说明 | 语法特点 |
|--------|------|----------|
| MySQL | 最常用的关系型数据库 | LIMIT、AUTO_INCREMENT、反引号 |
| PostgreSQL | 功能强大的开源数据库 | LIMIT/OFFSET、序列、双引号 |
| SQL Server | 微软企业级数据库 | TOP、IDENTITY、方括号 |
| Oracle | 甲骨文企业级数据库 | ROWNUM、序列、 dual 表 |
| SQLite | 轻量级嵌入式数据库 | LIMIT、AUTOINCREMENT |
| Hive | 大数据数仓SQL引擎 | 分区表、分桶、特殊函数 |
| Spark SQL | 大数据计算引擎 | DataFrame风格、窗口函数丰富 |
| ClickHouse | OLAP列式数据库 | 高性能聚合、特殊函数 |

## Input Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 自然语言描述的查询需求 |
| `tables` | list | 是 | 表结构信息列表 |
| `db_type` | string | 否 | 数据库类型，默认mysql |
| `explain` | bool | 否 | 是否生成执行解释，默认true |
| `optimize` | bool | 否 | 是否给出优化建议，默认true |
| `dialect` | string | 否 | SQL方言版本 |

### tables 参数格式

```json
[
  {
    "name": "表名",
    "columns": {
      "字段名": "字段类型",
      "字段名2": "字段类型"
    },
    "primary_key": "id",  // 可选
    "description": "表说明"  // 可选
  }
]
```

## Output Structure

```json
{
  "sql": "生成的SQL语句",
  "db_type": "数据库类型",
  "explanation": "查询逻辑解释",
  "complexity": "simple/medium/high",
  "tables_used": ["使用的表列表"],
  "optimization_tips": ["优化建议列表"],
  "key_points": ["关键点说明"]
}
```

### 输出说明

- **sql**：生成的完整SQL语句，可直接执行
- **explanation**：查询逻辑的自然语言解释，帮助理解
- **complexity**：查询复杂度评估（简单/中等/复杂）
- **tables_used**：查询涉及的表
- **optimization_tips**：性能优化建议，包括索引建议、写法优化等
- **key_points**：需要注意的关键点

## 支持的查询类型

### 基础查询
- 简单SELECT查询
- 条件筛选（WHERE）
- 排序（ORDER BY）
- 分页（LIMIT/TOP）
- 去重（DISTINCT）

### 聚合统计
- COUNT/SUM/AVG/MAX/MIN
- GROUP BY 分组
- HAVING 筛选
- 多维度聚合

### 多表联查
- INNER JOIN
- LEFT JOIN / RIGHT JOIN
- FULL OUTER JOIN
- 自连接
- 多表级联

### 高级查询
- 子查询
- 窗口函数（ROW_NUMBER/RANK/SUM OVER等）
- CTE（WITH子句）
- CASE WHEN 条件表达式
- UNION/UNION ALL
- 子查询（IN/EXISTS）

## 典型使用场景

### 场景一：产品经理看数据
想看"过去7天每天的新增用户数和次日留存率"，不用找数据团队，自己就能生成SQL查。

### 场景二：开发者快速取数
开发时需要查个数据，但忘了表结构和具体字段名，描述一下需求直接生成，比自己写快3倍。

### 场景三：SQL新手学习
初学者不知道某类查询怎么写，描述需求生成SQL，附带解释，边用边学。

### 场景四：复杂查询优化
写了一个复杂SQL跑的慢，让AI分析优化建议，看看哪里能加索引、哪里能优化写法。

### 场景五：跨数据库迁移
从MySQL迁到PostgreSQL，有些语法不一样，让AI帮你转换适配。

## 常见问题 FAQ

**Q1: 生成的SQL一定正确吗？**
A: 大部分情况下是正确的，但建议执行前先检查一下，特别是涉及生产数据的。复杂查询可能需要微调。

**Q2: 我不提供表结构能生成吗？**
A: 提供表结构信息能生成更准确的SQL。如果不提供，AI会基于查询描述生成通用SQL框架，你需要自己替换表名和字段名。

**Q3: 支持存储过程/触发器吗？**
A: 目前主要优化查询类SQL（SELECT），也支持INSERT/UPDATE/DELETE，但存储过程、触发器等复杂数据库对象建议用专业工具。

**Q4: 生成的SQL性能怎么样？**
A: AI会尽量生成高效的写法，并给出优化建议。但实际性能还取决于数据量、索引、数据库配置等因素。重要查询建议做EXPLAIN分析。

**Q5: 可以生成多语句的复杂脚本吗？**
A: 可以，但建议一次一个主要查询，这样生成的质量更高。太复杂的脚本建议拆分成多个查询。

## Limitations & Notes

- 生成的SQL仅供参考，执行前请确认正确性
- 生产环境执行前务必先在测试环境验证
- 表结构信息越完整，生成的SQL越准确
- 超复杂的查询可能需要人工微调
- 建议对重要查询做EXPLAIN性能分析
- 不支持非关系型数据库（NoSQL）的查询生成

## References

- 模型：基于DeepSeek大语言模型
- 支持数据库：MySQL/PostgreSQL/SQL Server/Oracle/SQLite/Hive/Spark SQL/ClickHouse
- 优化建议：基于SQL性能最佳实践
