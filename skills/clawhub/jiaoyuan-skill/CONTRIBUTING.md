# 贡献指南 / Contributing

感谢你想为 jiaoyuan.skill 出力。这个项目把教员著作中的思维方法提炼成可复用的决策工具，核心是**准确**与**克制**：引文逐字核对、模式卡反教条、发布物零内部痕迹。欢迎你以下面的方式参与。

## 如何报告问题（Issue）

- 用一句话说明问题（如"第 X 张模式卡引文有误""案例编号重复"）。
- 附上可复现的位置：文件名 + 章节标题 + 出错原文。
- 引文纠错请给出**逐字对照**：现文 vs 你认为的正确原文 + 出处（篇名）。

## 如何提改动（Pull Request）

1. Fork 本仓库，新建分支（如 `fix/quote-xxx` 或 `feat/case-xxx`）。
2. 改动聚焦一件事，避免混入无关修改。
3. 引文改动必须**逐字核对**原文（可 grep `corpus/`），并在 PR 描述里说明出处。
4. 新增模式卡 / 案例请先开 issue 讨论，避免方向不合再返工。
5. 提交信息清晰：`fix:` / `feat:` / `docs:` 前缀 + 一句话说明。

## 引文纠错（最重要）

- 本项目红线：引文逐字核对，禁凭记忆杜撰。所有「语录金句」必须能在 `corpus/` 中 grep 命中原文。
- 发现错误：开 issue 贴出「现文 / 正确原文 / 出处（篇名与版本）」，我们核对后修正并致谢。

## 建议新案例 / 新模式卡

- 说明：①适用场景（哪类现实难题）②涉及的思维方法（对应哪张卡 / 哪个内核）③历史出处（篇名）。
- 案例结构请参照 `cases/` 现有文件（局势 / 判断 / 行动 / 结果 / 可迁移点）。
- 模式卡结构请参照 `patterns/` 现有文件（触发情境 / 思维路径 / 决策原则 / 适用边界 / 语录金句）。

## 行为准则（简要）

- 只讨论思维方法与工具，不进行政治宣传、不评价历史人物与事件。
- 保持专业与尊重；引文与事实问题以原文为准。

---

## English Summary

We welcome contributions in the form of issue reports, verbatim quote corrections, and proposals for new cases or Pattern Cards. All quotations must be verified character-for-character against `corpus/`. Please keep PRs focused, open an issue before proposing new cards or cases, and follow the structure of existing files. This project discusses only thinking methods and tools — no political propaganda, no evaluation of historical figures or events.
