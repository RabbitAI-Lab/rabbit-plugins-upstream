# 设计切片：smart-charts-8.1.1

> **来源**：`<本地参考目录>\Desktop\积木logo\skill参考收藏目录\smart-charts-8.1.1.zip`（21 文件 / 约 1.2MB；13 py ≈ 190KB + 3 份 ECharts 资产 ≈ 1MB）
> **形态**：C 工具编排型（tool）+ 重工程 —— 表格数据 → 离线交互式 ECharts HTML，26 类图表
> **采样日期**：2026-09-07　**执行模式**：**三产出**（亮点 + 蓝图 + 自省）

---

## 三产出清单

| # | 产出 | 文件 | 状态 |
|:--:|---|---|---|
| ① | **亮点**（外部采样） | [1-highlights.md](1-highlights.md) · [absorbed.json](absorbed.json) | ✅ **已入库**：A-513~A-524（12 条）+ 元设计 DP-204~206（3 条） |
| ② | **蓝图**（逆向拆解） | [3-blueprint.md](3-blueprint.md) | ✅ 六段式（总览/架构分层/模块划分/工作流/设计模式表/检查清单） |
| ③ | **自省**（正向验证） | [4-self-benchmark.md](4-self-benchmark.md) | ✅ 四层对照，10 项特质 → 3 项三层全缺 |
| 附 | 元设计详版 | [2-principles.md](2-principles.md) | ✅ DP-204/205/206 展开 + "不可判 → 可判"替换表 |

---

## 落库状态

- **条目库** `references/design-blocks-library.md`：A-513~A-524 已入条目区；B0X 索引 7 行更新（B01+1 / B03+1 / B04+2 / B05+2 / B07+2 / B08+2 / B09+2）
- **原则库** `references/design-principles-library.md`：DP-204~206 已入条目区 + §三速查表 3 行
- **归属格**：B01 条件 / B03 事实 / B04 问题 / B05 分析 / B07 结构 / B08 行动 / B09 验收

---

## 一句话结论

**造不出它的工程密度（那是设计目标差异，不是能力差异）；真正该改的是一条根因——我们把"一致性"当纪律管，它把"一致性"当架构管。**

三项三层全缺（T1 单一事实来源 / T4 安全 PoC / T10 跨落点权威源）中，**T4 建议不补**（元 skill 无不可信代码执行场景），T1 + T10 同根因。

---

## 它自身的 3 处缺陷（当范例也要看反面）

| ID | 缺陷 | 实证 |
|---|---|---|
| **D1** | 版本校验**空头支票**：`__init__.py:3-5` 声明由 regression_check 强制校验，但全库无脚本读 SKILL.md frontmatter | `regression_check.py` grep `version` = 0 命中 |
| **D2** | 自检项数 **133 写死文档**，无机器校验 | REFERENCE.md:15；数字当前准确但必漂移 |
| **D3** | 自检脚本**主路由无入口** | `grep -rn "regression_check" --include="*.md"` 仅命中 REFERENCE.md |

**共同根因与 westock-data 的 D1/D3/D4 完全同构**：跨落点一致性没有机器校验。
**仅此一项我们比它强**：validate 第 10 项专治"文档写的数字 ≠ 实际"。

---

## 评估摘要（六维）

| 维度 | 评级 | 要点 |
|---|:--:|---|
| 架构设计 | **A** | 五层分层 + L4 内核层（stats_kernels）消灭双消费漂移 |
| 接口组织 | **A** | argparse 统一 + 结构化 JSON 错误 + 26 类选型表一表三层 |
| 错误处理与容错 | **A** | 错误码枚举 + suggestion 必带；E1–E8 端到端断言 code_name |
| 安全 | **A** | 三层校验（黑名单 + AST 白名单 + 安全 builtins）+ 5 个真实逃逸 PoC |
| 输出标准化 | **A-** | stdout 契约 6 字段；解读注入 HTML；**但 133 项数无自检** |
| 可扩展性 | **B+** | 加图表类型需动 renderers + plot_stats + 选型表三处 |
| 边界划分 | **A-** | 四段式带可数阈值；**但自检脚本未进主路由** |

---

## 已覆盖不收（防重复入库，登记备查）

| 它的做法 | 我们已有对等物 |
|---|---|
| 错误码表 + suggestion 必带 | A-410 错误码表带建议处理列 |
| 依赖声明带 reason 注释 | A-414 运行时依赖声明带 reason |
| 三层文案/主题收口 | 我们的"重复收口 1 处"纪律（**但缺模块头否定式声明，见 A-522**） |
| 默认策略不打扰用户 | A-404 可逆性决定确认等级（**A-518 是其可判据化升级版**） |
| 沙箱三层校验 | 元 skill 无该场景（T4 建议不补） |

---

## 待办（用户拍板）

| 优先级 | 事项 | 落点 |
|:--:|---|---|
| **P0** | validate 加第 13 项：**版本双落点一致性**（config.json = SKILL.md frontmatter = dist） | `scripts/validate_skill.py` |
| **P1** | `run_user_tests.py`（25 用例，实测全过）接进自检链路 + SKILL.md 给入口 | validate `--full` / SKILL.md |
| **P1** | 蓝图两套骨架改为引用/生成关系（DP-204 落地） | `blocks.py` / `blueprint-template.md` |
| **P2** | benchmark B1 增「样本分类」前置（已补 v0.9.0） | skill-rebuild |
