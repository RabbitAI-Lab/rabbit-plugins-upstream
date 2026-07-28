---
slug: "db-free"
name: "db-free"
version: "1.0.2"
displayName: "数据库设计与运维(免费版)"
summary: "识别并规避基础数据库连接、事务、查询与数据完整性陷阱。数据库设计与运维免费版，提供基础的数据库陷阱识别与规避能力. 核心能力包括： - 基础连接管理（连接池耗尽、空闲连接清理） - 基础事务"
summary_zh: "识别并规避基础数据库连接、事务、查询与数据完整性陷阱。数据库设计与运维免费版，提供基础的数据库陷阱识别与规避能力. 核心能力包括： - 基础连接管理（连接池耗尽、空闲连接清理） - 基础事务"
license: "MIT"
description: "|-. 适用于需要db相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  数据库设计与运维免费版，提供基础的数据库陷阱识别与规避能力.
  核心能力包括：
  - 基础连接管理（连接池耗尽、空闲连接清理）
  - 基础事务陷阱（死锁、丢失更新、显式提交）
  - 基础查询优化（N+1查询、外键索引、无界SELECT）
  - 基础数据完整性（唯一约束、时区存储、金额精度）
  高级功能（Schema变更安全策略、备份恢复、复制陷阱、扩展性规划）为付费版专享.
tags:
  - - select
  - automation
  - productivity
  - developer-tools
  - update
  - api
  - balance
  - order
  - 陷阱
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
pricing_tier: free
---
# 数据库设计与运维（免费版）

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 数据库设计与运维(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 概述

帮助识别和规避数据库使用中的基础陷阱，覆盖连接管理、事务、查询性能与数据完整性四大领域.
## 核心能力
### 基础连接管理
| 陷阱 | 表现 | 规避方案 |
|:-----|:-----|:-----|
| 连接池耗尽 | 应用静默挂起 | 设置最大连接数，监控连接池使用率 |
| 空闲连接占用内存 | 大量空闲连接耗尽内存 | 设置 `idle_in_transaction_session_timeout`，定期清理 |

> **升级提示**：Serverless连接泄漏处理（`RDS Proxy`、`PgBouncer`）、连接阻塞Schema变更的 `lock_timeout` 策略为付费版专享功能.

### 基础事务陷阱
| 陷阱(续)| 表现 | 规避方案 |
|---:|---:|---:|
| 死锁 | 多事务以不同顺序锁定相同资源 | 统一加锁顺序，使用 `SELECT FOR UPDATE` 预锁定 |
| 丢失更新 | 读-改-写无锁导致并发覆盖 | 使用 `SELECT FOR UPDATE` 悲观锁或乐观锁（版本号） |
| 隐式自动提交差异 | 不同数据库自动提交行为不一致 | 显式使用 `BEGIN`/`COMMIT`，不依赖隐式行为 |

> **升级提示**：长事务MVCC锁膨胀、只读事务阻塞 `VACUUM` 清理等高级事务陷阱为付费版专享功能.

### 基础查询优化
| 问题 | 原因 | 优化方案 |
|:---:|:---:|:---:|
| N+1查询 | ORM懒加载关联关系 | 预加载（`eager load`）或批量查询 |
| 外键缺索引 | JOIN和级联删除全表扫描 | 为外键列创建索引 |
| 无界SELECT | `SELECT * FROM huge_table` 导致OOM | 必须加 `LIMIT`，或使用游标分批读取 |

> **升级提示**：大IN子句拆分优化、`COUNT(*)` 近似计数（`pg_class.reltuples`）为付费版专享功能.

### 基础数据完整性

| 陷阱 | 后果 | 保障方案 |
|:------|------:|:------|
| 应用层唯一检查竞态 | 并发下产生重复数据 | 使用数据库唯一约束（`UNIQUE`） |
| 时区混乱 | 跨时区显示错误 | 存储 `UTC`，显示时转换（`TIMESTAMPTZ`） |
| 浮点数存金额 | 舍入误差导致账目不平 | 使用 `DECIMAL` 或整数分（`INTEGER` 存分） |

> **升级提示**：CHECK约束管理、外键缺失致孤儿行处理为付费版专享功能。Schema变更安全策略（带默认值加列、`CREATE INDEX CONCURRENTLY`、列重命名与删除顺序）、备份恢复优秀实践（PITR、备份验证）、复制陷阱预防（脑裂、故障转移）、扩展性限制规划（1亿行分片、Autovacuum监控）为付费版专享功能.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY=${API_KEY:?请设置环境变量}
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 使用流程

1. **场景识别**：判断当前属于连接、事务、查询还是完整性问题
2. **陷阱匹配**：在对应类别中查找匹配的陷阱描述与规避方案
3. **方案选择**：根据数据库类型选择具体实现命令
4. **执行验证**：按方案执行后验证结果

## 示例

### 示例1：避免丢失更新

```sql
-- 错误: 读-改-写无锁，并发下丢失更新
SELECT balance FROM accounts WHERE id = 1;  -- 读到 balance=100
UPDATE accounts SET balance = 80 WHERE id = 1;  -- 丢失了另一事务的扣减
# ...
-- 正确: 使用 SELECT FOR UPDATE 悲观锁
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;  -- 加行锁
UPDATE accounts SET balance = balance - 20 WHERE id = 1;
COMMIT;
```

### 示例2：金额存储

```sql
-- 错误: 浮点数存金额（舍入误差）
CREATE TABLE bad_orders (total FLOAT);  -- 0.1+0.2 = 0.30000000000000004
# ...
-- 正确: DECIMAL 精确存储
CREATE TABLE good_orders (total DECIMAL(10,2));  -- 0.10+0.20 = 0.30
```

### 示例3：避免N+1查询

```python
# 错误: N+1查询（100个订单 = 101次查询）
orders = Order.objects.all()
for order in orders:
    print(order.customer.name)  # 每次循环1次查询
# ...
# 正确: 预加载（2次查询）
orders = Order.objects.select_related('customer').all()
for order in orders:
    print(order.customer.name)  # 无额外查询
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| `deadlock detected` 死锁 | 多事务以不同顺序锁定相同资源 | 统一加锁顺序，捕获死锁异常后检查网络连接和配置后重试事务 |
| `too many connections` 连接耗尽 | 连接池配置过小 | 设置 `max_connections` 上限，监控连接数 |
| `out of memory` 查询OOM | `SELECT *` 无界查询加载全表 | 添加 `LIMIT`，或使用游标分批读取 |
| `duplicate key value` 唯一约束冲突 | 应用层检查与插入之间存在竞态 | 使用数据库唯一约束（`UNIQUE`）替代应用层检查 |
| `integer out of range` 整数溢出 | `INT` 最大值 2147483647 不足 | 改用 `BIGINT`（最大 9223372036854775807） |

## 常见问题

### Q1: 为什么浮点数不能存金额？
A: IEEE 754浮点数无法精确表示十进制小数。`0.1 + 0.2` 在浮点数中等于 `0.30000000000000004`。必须使用 `DECIMAL(10,2)` 或整数分存储.
### Q2: 如何避免N+1查询？
A: 使用ORM的预加载功能（如Django的 `select_related` / `prefetch_related`），将关联数据通过JOIN一次性查出，避免循环中逐条查询.
### Q3: 连接池应该设置多大？
A: 建议从 `pool_size = 10` 开始，根据监控调整。Serverless环境的高级连接池方案（`RDS Proxy`、`PgBouncer`）为付费版专享功能.
### Q4: 如何安全地修改表结构？
A: Schema变更安全策略（带默认值加列的三步法、`CREATE INDEX CONCURRENTLY`、列重命名与删除顺序）为付费版专享功能。免费版建议在低峰期执行Schema变更，并做好备份.
### Q5: 单表超过1亿行怎么办？
A: 扩展性限制规划（分片策略、Autovacuum监控、统计信息更新）为付费版专享功能。免费版建议先尝试按时间或哈希分区表.
## 已知限制

- 免费版不包含Schema变更安全策略
- 免费版不包含备份与恢复优秀实践
- 免费版不包含复制陷阱预防（脑裂、故障转移重连）
- 免费版不包含扩展性限制规划（1亿行分片、IOPS瓶颈监控）
- 免费版不包含高级事务陷阱（MVCC锁膨胀、只读事务阻塞清理）
- 免费版不包含大IN子句与COUNT(*)优化
- 升级至付费版可解锁全部8大类陷阱与规避方案

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "数据库设计与运维(免费版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "db"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
