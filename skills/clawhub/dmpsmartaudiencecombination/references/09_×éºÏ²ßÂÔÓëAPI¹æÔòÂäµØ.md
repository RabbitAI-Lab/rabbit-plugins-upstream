# 09 组合策略与 API 规则落地（组合人群）

> 对齐：`combination-rules_2.md` + 明日DMP OPENAPI 组合人群规则。

## 1. 组合前置
- 组合必须基于“用户已选择的入选集”（MUST/PREFERRED/OPTIONAL/EXCLUDE）。
- 不得把 TopN 候选直接笛卡尔组合。

## 2. 递进组合策略（循序渐进）
1) MUST 打底：M = m1 AND m2 ... AND mk
2) 逐步叠加 PREFERRED：M + p1 → M + p1 + p2 ...
3) OPTIONAL 仅用于扩量/备选：在目标允许时加入
4) EXCLUDE 永远不得出现

## 3. 与业务目标的组合倾向（简化版）
- 覆盖/拉新：尽量避免过度收窄（少叠加条件）
- 精准获客：允许多条件叠加收窄
- 品牌：核心TA + 泛兴趣扩量

## 4. DMP combine/create 规则落地（data 结构）

### 4.0 ⚠️⚠️⚠️ 三条铁律（违反必出bug）

**铁律1：同tags数组内是OR，跨资源元素用op:and连接才是AND！**
```json
// ❌ 致命错误！这是"女 OR 美妆个护"，不是AND！
[{"audiences":[],"tags":[15705,15564]}]
// ✅ 正确！"女 AND 美妆个护"
// HTTP API格式：[{"op":"and","rule":{"audience":[],"tag":[15705]}},{"op":"noop","rule":{"audience":[],"tag":[15564]}}]
// MCP格式：[{"audiences":[],"tags":[15705]},{"op":"and"},{"audiences":[],"tags":[15564]}]
```

**铁律2：禁止手写rules_json！必须通过 rules_helper.build_rules_http() 或 build_rules_mcp() 构建，创建前必须validate！**

**铁律3：所有DMP API调用必须走dmp_api_client.py（鉴权技能签名），禁止裸写urllib/requests绕过鉴权！**

### 4.1 两种格式（HTTP API vs MCP工具）—— 不可混用！

| 场景 | 构建函数 | 格式特征 |
|------|---------|---------|
| 技能脚本（create_must_baseline/calc_overlap/build_combinations）走HTTP API | `rules_helper.build_rules_http(or_groups)` | `[{op,rule:{audience,tag}},...]` 最后op=noop |
| 通过MCP工具DMP_MCP__create_combined_audience创建 | `rules_helper.build_rules_mcp(or_groups)` | `[{audiences,tags},{op:and},...]` 奇数长度无noop |

### 4.2 结构约束

**HTTP API格式（build_rules_http输出）：**
- data为list，每个元素：`{"op":"and"/"not"/"noop","rule":{"audience":[],"tag":[tagId,...]}}`
- rule.tag中多个tagId为**OR关系**
- rule.audience中为已有人群ID（overlap场景使用）
- op表示当前rule与下一个rule的关系
- **最后一个op必须是noop**
- 单rule最多100个标签/人群，总rule≤50

**MCP工具格式（build_rules_mcp输出）：**
- data为list，**资源元素和操作元素交替排列**：资源-op-资源-op-...-资源
- **列表长度必须为奇数**
- 资源元素：`{"audiences":[],"tags":[tagId,...]}`（audiences/tags内OR）
- 操作元素：`{"op":"and"}` 或 `{"op":"not"}`
- **不需要noop**，最后一个资源直接结束
- 总元素≤99

### 4.3 组建原则（两种格式通用）
- **每个维度单独成一个资源/rule**（性别/年龄/兴趣/地域/活跃）
- **组内OR**：同一维度多个标签放在同一rule.tag（HTTP）或tags（MCP）数组里
- **组间AND**：不同维度资源之间用op:"and"连接
- **排除NOT**：用op:"not"连接排除资源

### 4.4 正确格式示例

**示例1：女 AND 美妆个护（两个维度AND）**
```python
from rules_helper import build_rules_http, build_rules_mcp
or_groups = [[15705], [15564]]  # 女, 美妆个护
http_rules = build_rules_http(or_groups)  # 给dmp_api_client用
mcp_rules  = build_rules_mcp(or_groups)   # 给MCP工具用
```

**示例2：女 AND (20-24 OR 25-29 OR 30-34) AND (一线 OR 二线) AND 美妆个护**
```python
or_groups = [
    [15705],              # 女
    [15687,15688,15689],  # 20-24 OR 25-29 OR 30-34
    [34080,34082],        # 一线 OR 二线
    [15564],              # 美妆个护
]
```

### 4.5 规则校验清单（创建前必须逐项通过validate_rules）
- [ ] 使用rules_helper构建，没有手写JSON？
- [ ] 同维度OR标签是否在同一个rule/tag（HTTP）或tags（MCP）数组里？
- [ ] 需要AND的跨维度标签是否分成了独立rule/资源元素？
- [ ] HTTP格式：最后op=noop？
- [ ] MCP格式：长度为奇数？
- [ ] validate_rules_http()/validate_rules_mcp()返回空错误列表？
- [ ] 所有tagId都是isDirectory=1的目录节点？

## 5. 上限与校验
- 单任务最多 50 个 rule
- 单 rule 最多 100 个标签/人群数据
- 标签必须 isDirectory=1
- tagId/audienceId 必须在租户权限内，否则创建失败

## 6. 输出
- 组合方案：可读表达式（A AND (B OR C) AND D ...）
- API data JSON（可直接用于调用）
- 组合理由（基于 Overlap/质量/目标）
