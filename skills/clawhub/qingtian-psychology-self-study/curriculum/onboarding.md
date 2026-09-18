# Onboarding 一键默认开跑脚本与定制话术（参考）

> 本文件是 `SKILL.md` 第四节的详细脚本补充。**v2.1 起：咨询师实战训练台定位**——新用户以默认配置直接开始，一句话可定制。主流程以 SKILL.md 为准。

## 默认配置（一键开跑）

| 参数 | 默认值 | 说明 |
|---|---|---|
| level | beginner | 零基础起点 |
| goal | counselor | 咨询方向（咨询师训练台默认） |
| timeBudget | standard | ~10h/周 |

## 一句话定制（可选）

| 参数 | 识别词（含数字） | 写入字段 |
|---|---|---|
| level | 零基础 / 新手 / 从零 / beginner ; 有基础 / 进阶前 / intermediate ; 进阶 / 高级 / advanced | userConfig.level |
| goal | 兴趣 / 好奇 / 探索 / interest ; 准咨询师 / 咨询 / 从业 / 咨询师 / counselor ; 考研 / 学术 / 论文 / academic | userConfig.goal |
| timeBudget | 轻量 / 少 / 5 / light ; 标准 / 一般 / 10 / standard ; 强化 / 多 / 20 / intensive | userConfig.timeBudget |

- 一句话可含多个参数（如「我零基础想做咨询每周10小时」）。
- 无法解析 → 忽略该句，保持默认/现值，不阻塞、不反问。
- 中途退出 → 已解析项已落盘，下次「继续」从断点续接。

## 配置→起点阶段映射

| level | 起始阶段 | 阶段 id |
|---|---|---|
| beginner | 入门启蒙 | enlightenment |
| intermediate | 主要流派（跳过启蒙） | schools |
| advanced | 深化整合（跳过启蒙/流派/领域） | integration |
