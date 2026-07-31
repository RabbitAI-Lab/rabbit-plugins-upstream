# 阶段触发关键词完整表

> 配套主 skill: [SKILL.md](../SKILL.md)

## 触发关键词表

| 阶段 | 关键词 | 路由目标 |
|---|---|---|
| 0a 读论文 | 读论文 / 精读 / 中英对照 / paper reader | `nature-reader` |
| 0b 文献调研 | 文献调研 / 综述 / 找文献 / literature review / PubMed / Scopus | `nature-academic-search` + `academic-researcher` |
| 0b 论文下载 | 论文下载 / 下载 paper | `nature-downloader` |
| 0b 论文卡片 | 论文卡片 / 整理文献 / paper card | `nature-paper-card` |
| 1a 项目初始化 | 项目初始化 / 新论文 / bootstrap / 项目目录 | `paper-bootstrap` |
| 1b 期刊选择 | 期刊选择 / venue / Nature Methods / 投哪本 | `nature-portfolio-playbook` |
| 2a 起草 | 起草 / 写摘要 / 写引言 / 写方法 / 写讨论 / 投稿包 / cover letter | `nature-writing` |
| 2b 结构修复 | 结构修复 / 证据链漂移 / manuscript optimizer | `manuscript-optimizer` |
| 2c Results 修订 | Results 修订 / results section / 结果叙述 | `results-section-revision` |
| 3a 图规划 | 图规划 / 一图一主张 / panel role / figure planner | `figure-planner` |
| 3b 出图 | 出图 / 科研绘图 / 论文 figure / 论文 plot / 图形摘要 / 示意图 | `nature-figure` |
| 3c 图检查 | 图检查 / figure style / 图形正确性 | `figure-style` |
| 4a 统计审计 | 统计审计 / stats audit / p值 / 样本量 / n值 / 多重比较 | `stats-reporting-audit` |
| 4b 统计分析 | 统计分析 / 数据分析 / statistics / data analysis | `nature-statistics` + `nature-data` |
| 5a 引用核验 | 引用核验 / citation verifier / 引用造假 / BibTeX 卫生 | `nature-ref-verifier` + `citation-verifier` |
| 5b 引用补充 | 引用补充 / 加引用 / CNS 引用 / Nature 引用 | `nature-citation` |
| 5c 数据声明 | 数据声明 / data availability / FAIR / accession | `data-availability` |
| 6a 润色 | 润色 / polishing / 学术英语 / LaTeX 排版 / 句子精修 | `nature-polishing` + `scientific-prose-style` |
| 6b 投稿预检 | 投稿预检 / submission audit / 投前检查 | `submission-audit` |
| 7a 审稿模拟 | 审稿模拟 / reviewer / 预审 / 审稿意见 | `nature-reviewer` |
| 7b 返修 | 返修 / rebuttal / response / 逐点回复 / cover letter | `nature-response` |
| D1 转 PPT | 转 PPT / 组会汇报 / 文献汇报 | `nature-paper2ppt` |
| D2 转专利 | 转专利 / paper to patent / 国知局 | `nature-paper-to-patent` |
| D3 写基金 | 写基金 / proposal / 申请书 | `nature-proposal-writer` |
| D4 实验记录 | 实验记录 / experiment log | `nature-experiment-log` |
| D5 会议论文 | 会议论文 / NeurIPS / ICML / ICLR / conference | `conference-paper-writing` |

## 触发词设计原则

- 单字英文词（如 figure / plot / reviewer / response）必须搭配上下文限定词（如"论文 figure"、"reviewer 审稿"）避免误触发
- 中文触发词优先（更精确）
- 衍生场景触发词包含具体场景名（NeurIPS / ICML / ICLR / 国知局）
