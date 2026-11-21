# 数据契约

元简从 `0.1.2` 起随包提供机器可读契约及其 JSON Schema，`0.1.3`
开始提供行业注册表、首批种子题与安全示例：

- `data/industry-registry.json`：行业注册表、关键词、证据维度和扩展接口。
- `data/security-role-map.json`：6 个安全岗位族与 4 个职级。
- `data/evidence-ledger.json`：简历证据账本，记录责任、动作、规模、结果和边界。
- `data/source-registry.json`：来源层级、日期、刷新周期、失效周期和许可复核状态。
- `data/question-bank.json`：18 道原创种子题；6 个安全岗位族各 3 道，
  覆盖知识、情境和简历追问三类。
- `data/dual-role-contract.json`：求职者和 HR 的数据访问、导出及受保护属性边界。

`data/evidence-ledger.json` 中的唯一条目为 `EXAMPLE_ONLY` 公开示例，明确
`user_confirmed=false`、`export_allowed=false`，不属于任何真实候选人。

## 行业扩展接口

新增行业时在 `industry-registry.json` 中追加对象，并保持：

- `id` 唯一且使用小写字母、数字和下划线；
- 非兜底行业提供可区分的关键词；
- 提供 `evidence_dimensions`、`question_dimensions` 和可选 `role_map_ref`；
- 全表只保留一个 `is_fallback=true` 的兜底行业；
- 扩展后运行 `contracts` 和 `doctor`。

当前网络安全行业有详细岗位族与种子题；其他行业先使用注册表中的通用证据和追问
维度，后续可按同一结构增加专属岗位族与题库。

## 校验

离线校验随包契约：

```bash
python scripts/yotta_resume.py contracts --format json
```

直接运行独立校验器：

```bash
python scripts/contract_validate.py --root data --format json
```

成功返回退出码 `0`；主 CLI 的契约校验失败返回 `6`。独立校验器失败返回非零退出码。

## 安全边界

- 默认策略为 `deny`。
- HR 默认不能读取候选人私有证据账本、原始简历或分析报告。
- 跨角色导出必须提供字段清单并确认，默认只导出投递版简历。
- 年龄、性别、婚育、民族、宗教、籍贯、残障和照片等受保护属性不得进入评分字段。
- 来源许可未确认时只允许事实提炼、链接引用和自主改写，不复制长段原文。
- 社区面经只可作练习提示，不能作为标准答案。
- 示例证据不得改写为候选人经历，也不得进入导出简历或分析报告。
