# Competitive Landscape（内部参考，2026-09-16）

> 用途：评测应对、运营话术、差异化声明的事实底稿。**不进 SKILL.md 正文**（SH 概述会渲染正文）。

## 定位图（agent skills 生态，引用研究赛道）

| Skill | 定位 | 相对规模 | 与本 skill 关系 |
|---|---|---|---|
| deep-research-pro | 深度研究（多源检索+报告） | ~59k dl | 只研不验：引用自产自信。是「被替代对象」而非竞品——用户被假引用伤过就会找我们 |
| smartlib | 引用核验工具 | ~6.9k dl | 只验不研：没有研究流程。与我们是相邻功能，可共存 |
| **cite-holmes** | **研究 + 逐条自证引用（唯一组合）** | 8k+ dl（双平台，09-16） | 差异化 = 五态判定 + 官方数据库逐条核验 + CiteScore + 医学模式 + 审计导出 |

## 差异化声明（可对外说的）

1. 全场唯一「深度研究 + 机器自证引用」结合体：报告里每条引用带五态判定与人工复核区。
2. 核验走官方数据库（DOI.org / NCBI E-utilities / export.arxiv.org / archive.org），非启发式。
3. 可机检伪造类型已覆盖 9 类（假 DOI/错引/假 PMID/假 arXiv/拼接/期刊名/作者名/死链/重复），
   边界诚实：指向真实可信页面的精心伪造由语义层把关。
4. 纯标准库零依赖、跨平台、可离线结构检查；BibTeX/CSV/HTML 三种交付物。

## 跟随策略

- 评测失分点即下一版 backlog（TRACE 4.6→4.8 的路径已验证有效：按评测重排优先级）。
- 竞品发版脉冲是曝光窗口：对方发版当日我们在 SH 的搜索关联曝光会抬头（观察过两次）。
- 不做功能对标军备竞赛；守住「每条引用都核验 + 诚实边界」的核心心智。

## 关联

- 诊断真源：归墟 note_1789221108_9d4922（v1.1.1 停滞 29 天根因分析）
- 评测轨迹：v1.3 4.6 → v1.5 4.6（结构变化：T 滑坡暴露国内适配）→ v1.6 4.8（R 满分）

## 2026-09-19 增补（v1.9 自调研，引用经本体验证 CiteScore 55/C，8/8 可达）

### 学术界定调（背书素材）

- **Nature 2026-04**：数万篇 2025 年论文可能含 AI 生成的无效引用；**Nature 2026-05**：
  四个仓库 2025 年论文/预印本合计 **14 万+假引用**（社科预印本最高）。
- **arXiv 2026-06 政策**：论文若显示未检查的 AI 输出（含幻觉引用）→ 作者禁投一年。
  = 我们「投稿前结论」行（v1.9）的政策锚点；话术："arXiv 会因幻觉引用禁投作者——
  投稿前先跑一遍 cite-holmes"。
- **Badalova & Mayr, arXiv 2607.22693（2026-07）**：评测五家检测工具
  （CheckIfExist / HalluCiteChecker / Hallucinator / HalRef / RefChecker），
  结论=没有一家可无人监督运行；共性短板=引用提取错误、元数据不全、库覆盖有限、
  校验不一致；作者呼吁 **transparent multi-source detection systems**。
  → cite-holmes 已是七源（DOI.org/E-utilities/arXiv/archive.org/Crossref-RW/
  OpenAlex/S2）+ auditjson 透明工作底稿，方向被第三方背书。

### 竞品动作

- **Paperpile Citation Checker（2026-05-27 发布）**：免费 web 工具，粘贴 BibTeX
  逐条核查。入口=`.bib` 文件 → 我们 v1.9 已补齐 BibTeX 导入，且多了研究流程整合
  与审计台账。
- **GPTZero Hallucination Detector**：从检测写作 AI 痕迹扩展到幻觉引用检测
  （NeurIPS 2025 扫描出 100+ 假引用即其研究）。

### 基础设施变化（已落地应对）

- **OpenAlex 2026-02 起生产调用需 API key**（每日免费额度）→ v1.9 支持
  `--openalex-key`/`OPENALEX_API_KEY` + 403 可操作提示（09-19 实测免钥仍 200）。
- **Crossref 2026-07-21 限速分层**；2026-05 Labs API 撤稿注记停更（REST 是唯一
  前进路径，v1.8 路线正确）→ v1.9 `--mailto` polite pool + 429 Retry-After。
- **S2 免钥可用但记录质量参差**（实测 10.1002/art.42566 登记为期刊目录页）→
  v1.9 设计为「只确认不降级」的第二路确认源。

### 国内需求侧

- 科技部 2025-11 撤稿论文专项整治（抄袭/造假/买卖论文/虚构同行评审）；
  卫健委 2026-05「论文工厂」通报零容忍。= 中文市场对撤稿检测/引用验真的需求
  政策背书（SKILL_ZH 概述可呼应，不直接引用政策文号做营销）。

### 分发（发布后任务，非 v1.9 范围）

- agent skills 生态目录：skills.sh / SkillsMP / AgenticSkills / Skills Directory /
  Awesome Skills（2026-09 已有对比测评）。ClawHub+SH 之外逐个铺。

