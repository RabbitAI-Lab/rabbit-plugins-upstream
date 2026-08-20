---
name: ab-testing
description: "A/B 测试框架，支持内容/策略/定价等多维度测试，自动统计显著性并选择最优方案。 触发词：A-B测试/内容测试/策略对比/显著性分析 不触发：内容发布/数据分析/商品管理"
version: 1.0.0
user-invocable: true
tools: [read, exec]
dependencies: [content-analytics, sales-analytics]
metadata:
  layer: plugin
  priority: "P2"
  openclaw:
    emoji: "🧪"
    os: ["win32", "linux", "darwin"]
    requires:
      bins: ["python"]
      config: []

---

> **核心功能**: 本技能提供/商品管理等能力。

> **运行环境**: 本Skill的exec脚本必须使用 **Python 3.11.x** (`.venv/Scripts/python.exe`) 执行。禁止使用系统Python 3.14+。验证: `./.venv/Scripts/python.exe --version` → `Python 3.11.x`



# AB Testing Skill 详细设计

> **引用**: [00_全面详细设计.md - A/B 测试章节](file:///d:/JueJin/docs/design/00_全面详细设计.md)
>
> **来源**: JueJin CEO办公室优化增强 Skill

**版本**: v1.2
**创建日期**: 2026-04-05
**更新日期**: 2026-04-07
**状态**: 设计中
**优先级**: P2(优化增强)

---

## 一、Skill 概述

### 1.1 功能定位

| 项目 | 说明 |
|:-----|:-----|
| **Skill名称** | `ab-testing-skill` |
| **所属部门** | CEO 办公室 |
| **优先级** | P2(优化增强) |
| **功能** | A/B 测试设计、流量分配、显著性统计、最优方案选择 |

### 1.2 核心机制

本 Skill 通过 `memory_search` 读取测试数据,`exec` 调用统计脚本计算显著性,结果存储于 memory/ab-tests/ 目录,通过 `read`/`write` 管理测试配置。

---

## 二、使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| **内容测试** | 新内容模板上线 | 测试不同模板的转化效果 |
| **策略测试** | 新互动策略 | 测试不同策略的回复率 |
| **定价测试** | 新定价方案 | 测试不同定价的转化率 |
| **查询结果** | CEO 查询/定时任务 | 查看测试进展和结论 |

---

## 三、工作流

### 3.0 完整5步闭环(P3-02增强)

```
假设生成 → 自动分流 → 执行测试 → 统计分析 → 自动决策
   ↑            ↑           ↑          ↑          ↑
 hypothesis   create     result    significance  decide
```

| 步骤 | exec命令 | 说明 |
|:-----|:---------|:-----|
| 1.假设生成 | `ab_testing.py hypothesis` | 规则模板自动生成假设+样本量+分流策略 |
| 2.创建测试 | `ab_testing.py create` | 创建实验,均匀分流(uniform) |
| 3.执行收集 | `ab_testing.py result` | 按变体记录每次转化结果 |
| 4.统计分析 | `ab_testing.py significance` | Z检验计算p值/置信度/提升幅度 |
| 5.自动决策 | `ab_testing.py decide` | 根据显著性+提升幅度自动采纳/保留/继续 |

### 3.1 创建测试流程

```
1. 接收测试请求
   ├── 输入: test_type, variants, sample_size
   └── 验证: 参数有效性(至少2个变体)

2. 设计测试
   ├── 生成测试ID: ab_test_YYYYMMDD_NN
   ├── 分配流量比例: 默认均匀分配
   └── 计算所需样本量: 基于统计功效

3. 存储测试配置
   ├── write 保存至 memory/ab-tests/test_ID.json
   ├── 记录: 测试类型、变体、流量分配、目标样本量
   └── 状态: running

4. 返回结果
   └── 输出: test_id, variants, status
```

### 3.2 数据收集与统计分析流程

```
1. 定时触发(Cron: 每日)
   ├── 读取 memory/ab-tests/ 下所有 running 测试
   └── 对每个测试执行以下步骤

2. 收集数据
   ├── memory_search 检索测试相关数据
   ├── 读取 memory/*.md 日志获取用户行为
   └── 按变体分组,计算各变体指标

3. 统计显著性
   ├── exec 调用 scripts/ab_testing.py significance
   ├── 输入: 各变体的样本量、转化数
   ├── 计算: p值、置信区间、统计功效
   └── 输出: 是否显著、最优变体

4. 判断测试状态
   ├── 样本量达标且显著 → 得出结论,标记 completed
   ├── 样本量未达标 → 继续收集,标记 running
   └── 运行超30天 → 强制结束,标记 inconclusive

5. 存储结果
   ├── write 更新测试配置文件
   ├── write 保存统计报告至 memory/ab-tests/test_ID_report.md
   └── 如已完成 → exec 通知脚本通知 CEO 结论（注：message由OpenClaw内置处理）

6. 返回结果
   └── 输出: test_status, winner(如有), significance
```

---

## 四、测试类型与指标

### 4.1 内容测试

| 测试对象 | 核心指标 | 辅助指标 |
|:---------|:---------|:---------|
| 内容模板 | 转化率(关注/购买) | 播放量、完播率 |
| 标题风格 | 点击率 | 播放量、互动率 |
| 发布时间 | 播放量(24h) | 互动率 |

### 4.2 策略测试

| 测试对象 | 核心指标 | 辅助指标 |
|:---------|:---------|:---------|
| 打招呼方式 | 回复率 | 关系推进速度 |
| 聊天频率 | 用户满意度(不删好友率) | 聊天时长 |
| 关系推进时机 | 转化率(付费) | 推进成功率 |

### 4.3 定价测试

| 测试对象 | 核心指标 | 辅助指标 |
|:---------|:---------|:---------|
| 产品价格 | 转化率(购买) | 客单价 |
| 优惠策略 | 转化率 | 复购率 |
| 付费时机 | 转化率 | 用户满意度 |

---

## 五、显著性判断标准

| 指标 | 阈值 | 说明 |
|:-----|:-----|:-----|
| p 值 | < 0.05 | 统计显著 |
| 置信区间 | 95% | 结果可信度 |
| 最小样本量 | 每变体30 | 低于此值不做判断 |
| 最小提升幅度 | > 10% | 低于此值认为无差异 |

---

## 六、exec 脚本调用方式

| 操作 | 命令 | 输入 | 输出 |
|:-----|:-----|:-----|:-----|
| 显著性计算 | `python scripts/ab_testing.py significance --variant-a 15,100 --variant-b 10,100` | 各变体转化数/样本数 | JSON p值、结论 |
| 样本量计算 | `python scripts/ab_testing.py sample_size --baseline 0.10 --mde 0.10` | 基线转化率、最小检测效果 | JSON 所需样本量 |
| 假设生成(P3-02) | `python scripts/ab_testing.py hypothesis --test-type content --baseline-rate 0.10 --mde 0.15` | 测试类型、基线率、MDE | JSON 假设列表+样本量+分流策略 |
| 自动决策(P3-02) | `python scripts/ab_testing.py decide --test-id ab_test_20260407_01` | 测试ID | JSON 决策(采纳/保留/继续)+原因 |
| 创建实验 | `python scripts/ab_testing.py create --name "标题测试" --metric ctr --variants A,B` | 名称、指标、变体列表 | JSON test_id、状态 |
| 记录结果 | `python scripts/ab_testing.py result --test-id <参数> --variant A --value 1` | 测试ID、变体、值 | JSON 累计样本量 |

---

## 七、输入格式

### 7.1 创建测试

```json
{
  "test_type": "content",
  "variants": [
    {"id": "A", "name": "模板A", "template": "template_a"},
    {"id": "B", "name": "模板B", "template": "template_b"}
  ],
  "sample_size": 100,
  "metric": "conversion_rate"
}
```

### 7.2 查询测试

```json
{
  "action": "query",
  "test_id": "ab_test_20260407_01"
}
```

---

## 八、输出格式

### 8.1 创建测试结果

```json
{
  "success": true,
  "data": {
    "test_id": "ab_test_20260407_01",
    "test_type": "content",
    "variants": ["A", "B"],
    "status": "running",
    "sample_size": 100
  }
}
```

### 8.2 测试完成结果

```json
{
  "success": true,
  "data": {
    "test_id": "ab_test_20260407_01",
    "status": "completed",
    "winner": "A",
    "significance": {
      "p_value": 0.023,
      "confidence": 0.95,
      "lift": "15%"
    },
    "variants": {
      "A": {"conversions": 15, "samples": 100, "rate": 0.15},
      "B": {"conversions": 10, "samples": 100, "rate": 0.10}
    }
  }
}
```

---

## 九、异常处理

| 异常类型 | 错误代码 | 处理方式 |
|:---------|:---------|:---------|
| 样本不足 | INSUFFICIENT_SAMPLE | 返回当前进度,建议继续收集 |
| 变体数量 < 2 | INVALID_VARIANTS | 返回参数校验错误 |
| 统计脚本失败 | SCRIPT_ERROR | 记录错误日志,下次重试 |
| 测试不存在 | TEST_NOT_FOUND | 返回错误提示 |
| 参数无效 | INVALID_PARAMS | 返回参数校验错误 |

---

## 十、数据存储

### 10.1 测试配置 (memory/ab-tests/)

```markdown
# A/B 测试 - ab_test_20260407_01

## 基本信息
- 类型: 内容模板测试
- 创建时间: 2026-04-07
- 状态: running
- 目标样本量: 100/变体

## 变体
| 变体 | 名称 | 流量分配 | 样本量 | 转化数 | 转化率 |
|:-----|:-----|:---------|:-------|:-------|:-------|
| A | 模板A | 50% | 65 | 10 | 15.4% |
| B | 模板B | 50% | 62 | 6 | 9.7% |

## 显著性
- p值: 0.18 (未显著)
- 状态: 继续收集数据
```

---

## 十一、Cron 调度配置

```jsonc
// openclaw.json cron 配置
{
  "cron": {
    "ab_analyze": "0 10 * * *"     // 每日10点分析进行中的测试
  }
}
```

---

## 十二、与其他 Skills 协作

### 12.1 与 content-analytics-skill 协作

content-analytics 提供内容效果指标(播放/完播/互动),本 Skill 用于对比不同内容模板的 A/B 测试效果。

### 12.2 与 sales-analytics-skill 协作

sales-analytics 提供销售和转化数据,本 Skill 用于评估不同定价/策略的转化效果。

---

## 十三、变更历史

| 版本 | 日期 | 作者 | 变更说明 |
|:-----|:-----|:-----|:---------|
| v1.0 | 2026-04-05 | AI Agent | 初稿 |
| v1.1 | 2026-04-07 | AI Agent | 修复:移除 Python 类代码,移除禁止工具 |
| v1.2 | 2026-04-07 | AI Agent | 补充 exec 调用、显著性标准、Cron 配置、数据存储、协作关系、完整示例 |
| v1.3 | 2026-07-06 | AI Agent | P3-02增强:补全5步闭环(假设生成hypothesis+自动决策decide),规则模板驱动不依赖LLM |
| v1.4 | 2026-07-11 | AI Agent | P0-V2-02增强:新增compare命令(从content_stats自动采集数据对比A/B表现)+create命令新增--variant-contents参数+portal_get_ab_test_results API |
