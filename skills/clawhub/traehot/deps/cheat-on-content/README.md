# 网红作弊器 / Cheat on Content

> **蜗牛学长** 原创作品 — 内容创作可量化预测系统
>
> 把内容创作变成可校准预测循环：**打分 → 预测 → 发布 → 复盘 → 进化 rubric**

---

## 致敬

本目录包含的是 **蜗牛学长** 的 **"网红作弊器"（cheat-on-content）** skill——一个将内容创作从"玄学"变成"可量化工程"的评分预测系统。

蜗牛学长的这套方法论教会我们一件事：

> **内容不是玄学，是可预测的。** 我们只是把这套方法论搬到了大赛申报上。

Trae-Hot（TRAE AI创造力大赛超级IP孵化系统）的**阶段7打分预测**灵感全部来源于此。蜗牛学长用 25+ 已发视频拟合出的 7 维度评分体系（ER/SR/HP/QL/NA/AB/SAT），证明了"爆款"可以被量化——这正是 Trae-Hot 模拟评委打分的理论基石。

---

## 本目录包含的文件

| 文件 | 说明 |
|------|------|
| `SKILL.md` | cheat-on-content 总协议 + 路由表（完整工作流） |
| `rubric_notes.template.md` | 评分校准笔记模板（你的评分规则进化载体） |
| `starter-rubrics/opinion-video-zero.md` | v0 cold-start 等权占位 rubric（新人起步用） |
| `starter-rubrics/opinion-video.md` | v2 已校准 rubric（25+ 样本拟合，参考用） |

---

## 如何使用

### 如果你要做内容评分预测

将 `rubric_notes.template.md` 复制到你的项目根目录，重命名为 `rubric_notes.md`，然后按 Trae-Hot 的流程使用。

### 如果你要独立使用 cheat-on-content

将整个 `deps/cheat-on-content/` 目录复制到 `.trae/skills/cheat-on-content/`，按 SKILL.md 的路由表触发。

### 新人建议

1. 先用 `opinion-video-zero.md`（v0 等权公式）起步
2. 发完 5 篇、跑完 5 次复盘后，再考虑切到 v2 或自己拟合权重
3. 前 5 篇的预测精度大概 ±50%——这是 cold-start 的数学事实，不是系统失败

---

## 协议

cheat-on-content 的评分体系遵循三条不可妥协原则：

1. **盲预测**：预测必须在看到任何实际数据之前写完
2. **升级 = 全量重打**：rubric 升级时校准池所有样本必须用新公式重打分
3. **rubric 是工作台，不是博物馆**：被推翻的观察删掉，git history 才是档案

---

## 归因

本目录是 cheat-on-content 的精选子集，作为 Trae-Hot 的评分依赖。完整版本请访问蜗牛学长的原始项目。

如果你觉得这套方法论有用，请给蜗牛学长的原始项目点星。