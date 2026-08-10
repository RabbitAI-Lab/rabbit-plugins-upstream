# 意图识别（parse-intent）

将用户的自然语言输入解析为：讨论模式 + 角色组合 + 场景模板。

## 输入

用户原始输入（可能包含议题、角色指定、模式暗示）。

支持两种触发形式：

1. **自然语言**："帮我从多个角度分析一下..."
2. **斜杠命令**：`/roundtable <议题> [--mode=...] [--roles=...] [--no-interrupt]`

## 解析步骤

### 0. 斜杠命令解析（如触发）

如果用户输入以 `/roundtable` 开头：

1. 移除前缀 `/roundtable`，剩余部分作为议题与参数
2. 解析可选参数：
   - `--mode=快速|标准|深度` → 覆盖默认模式
   - `--roles=角色1,角色2,...` → 显式指定参与角色
   - `--no-interrupt` → 设置全程不中断标志
3. 参数去除后剩余文字作为 `<议题>`

示例：

```
/roundtable 评估这个AI产品方案 --roles=devil-advocate,ai-product-manager,llm-architect --mode=深度
```

解析结果：
- 议题："评估这个AI产品方案"
- 模式：深度
- 显式角色：devil-advocate, ai-product-manager, llm-architect

### 1. 前置检查

判断议题是否适合圆桌讨论（见 SKILL.md 第一节）。
若不适合，直接给出分析并说明理由，不启动圆桌。

### 2. 显式角色指定

匹配用户输入中的角色关键词：

| 关键词 | 映射 |
|--------|------|
| 产品经理 / PM / 产品总监 | experts/ai-llm/ai-product-manager 或 experts/product/* |
| 技术总监 / CTO / 架构师 | experts/engineering/distributed-systems 或 experts/ai-llm/llm-architect |
| 市场总监 / CMO / 市场 | （动态生成市场专家或 roles/optimist） |
| 增长 / 运营 | experts/product/growth-pm |
| 财务 / CFO / 成本 | roles/resource-constraint |
| 用户视角 / 客户 | roles/user-advocate |
| 唱反调 / 挑刺 / 风险 | roles/devil-advocate |
| 真实人名（张小龙、乔布斯等） | → 蒸馏流程（tools/distill-character.md） |

结合议题领域消歧：如"产品经理"在 AI 议题下 → ai-product-manager。

### 3. 场景模板匹配

用议题关键词匹配 `references/templates/*.yaml` 中的 `domain_keywords`。
匹配成功则加载模板的角色配置。

### 4. 条件触发专家

对匹配到的模板，检查 `conditional_experts` 中的 `when` 正则/关键词，
命中则将对应专家加入推荐列表。

### 5. 模式识别

| 用户表达 | 模式 |
|----------|------|
| "简单讨论" "快速看看" "粗略" | 快速（3 角色 1 轮） |
| 默认 | 标准（4-5 角色 3 轮） |
| "深入" "全面" "战略级" "重大" | 深度（5-7 角色 3 轮 + 检索） |

### 6. 组装推荐

```
L1 必选（模板 required_roles）
+ L1 可选（按模式数量补足）
+ L2 推荐（模板 suggested + conditional 命中）
+ L2 用户显式指定
+ L3 蒸馏人物（如有）
= 推荐角色组合
```

## 输出（节点 A · 启动确认）

向用户展示，等待确认后再进入编排：

```
📋 议题理解：{一句话复述议题}
🎯 匹配模板：{模板名}（{模式}模式，预计 {N} 轮）
👥 推荐角色：
  1. {角色} — {立场/职责一句话}
  2. ...
📝 任务装饰器预览：
  - 用户上下文：{已识别的个人信息/约束}
  - 领域适配：{将为各角色注入的领域引子}
💡 你的选项：
  - 回复"开始"确认启动
  - 替换 / 增加 / 移除角色
  - 调整模式（快速/标准/深度）
  - 补充更多上下文（会写入任务装饰器）
  - 设"全程不中断"（跳过轮次间检查点，仅保留异常介入与报告确认）
  - 取消
```

**默认等待用户确认，不自动启动。** 例外：用户在议题中已明确"直接开始/不用确认"时可跳过本节点。
本节点是 orchestrate-agents.md 节点 A 的入口，详见编排协议。
