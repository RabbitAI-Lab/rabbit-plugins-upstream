# JYS 结构改造交接

## 结果

- 套件：`jys` + `jys-s1` 至 `jys-s5`
- 目标：在不改变短剧业务规则的前提下，增加默认下一 Skill、统一工作区契约、完整状态续接、数据库回滚保护和最小回归检查。
- 发布状态：仅本地改造，未发布 GitHub。

## 参考与范围

- 参考：`qiaomu-meta-skill` 2.8.1 的资源边界、触发边界、回滚和证据分层规则。
- 基线：改造前的 JYS 六 Skill 套件。
- 外部同类 Skill 调研：不适用。本次是针对已确认结构缺陷的内部兼容改造，没有改变领域方法或引入外部机制。

## 保留、调整与新增

- `keep`：保留主控 + S1-S5 分工、普通/产品强绑定路线、逐段确认和最终文本交付。
- `adapt`：子 Skill 仍可显式调用，但自然语言请求默认由 `jys` 主控；每轮通过 `next_skill` 自动续接。
- `reject`：不迁移共享数据库，不增加六套重复测试或无用途的发布文件。
- `invent`：新增统一工作区契约、状态尾注、v1→v2 保守迁移、数据库单份 `.bak` 与版本记录。

## 优势与证据

- `design advantage`：所有子 Skill 显式读取同一工作区契约，不再互相读取对方的共享创作规则。
- `design advantage`：状态覆盖 S1-S5、S4 两阶段、最终确认以及默认下一 Skill。
- `validated advantage`：以 `scripts/validate_suite.py` 验证入口隔离、资源链接、索引、状态字段和依赖边界。
- `validated advantage`：以 `scripts/eval_state_routing.py` 运行确定性默认续接案例。

## 验证与限制

- 静态套件验证：通过，125 个 Markdown 文件无断链、索引或入口错误；见 `reports/validation.json`。
- 确定性状态路由：8/8 通过；见 `reports/state-routing-eval.json`。
- Provider-backed 自动触发评估：`missing evidence`。
- 四位真实使用者的完整端到端复核：`missing evidence`。
- 数据库仍位于 Skill 安装目录；通过备份、原子写入顺序和版本记录降低风险，但不能消除重装覆盖风险。
