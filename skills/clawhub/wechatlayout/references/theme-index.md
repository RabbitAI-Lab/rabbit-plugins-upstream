# 公众号排版主题注册表

> 本文件是主题信息的**单一来源**。新增主题必须在此登记一行。

| 主题名 | 英文标识 | 主色 | 适用场景 | 组件库文件 | 正文下划线 CSS |
|--------|---------|------|---------|-----------|---------------|
| 翡翠绿 | emerald | `#059669` | 教程/测评/清单/工具盘点/知识整理（信息密度高，卡片丰富） | `theme-emerald.md` | `border-bottom:2px solid #6EE7B7` |
| 石墨灰 | graphite | `#374151` | 设计/科技评论/专业观点/高端品牌（极简留白） | `theme-graphite.md` | `border-bottom:2px solid #9CA3AF` |
| 暖橙 | sunset | `#EA580C` | 美食/生活/旅行/温暖治愈（暖色调，亲切感） | `theme-sunset.md` | `border-bottom:2px solid #FB923C` |
| 海蓝 | ocean | `#2563EB` | 企业/科技/金融/商业分析（专业权威） | `theme-ocean.md` | `border-bottom:2px solid #93C5FD` |
| 胭红 | rose | `#E11D48` | 时尚/美妆/节庆/促销活动（热情活力） | `theme-rose.md` | `border-bottom:2px solid #FB7185` |

## 选主题决策树

```
文章类型？
├─ 教程/操作指南/测评/盘点 → emerald（翡翠绿）
├─ 观点/深度分析/力量感话题 → graphite（石墨灰）或 emerald
├─ 设计/科技评论/高端品牌 → graphite（石墨灰）
├─ 禅意/极简/随笔 → graphite（石墨灰）
├─ 数据复盘/报告 → emerald（翡翠绿）
├─ 美食/探店/生活/旅行/温暖治愈 → sunset（暖橙）
├─ 企业/产品发布/行业分析/金融/案例研究 → ocean（海蓝）
├─ 时尚/穿搭/美妆/节庆/促销/种草 → rose（胭红）
└─ 不确定 → emerald（默认第一行）
```

## 新增主题规范

新主题以 `references/theme-{英文标识}.md` 命名，必须包含：
1. 设计变量速查表
2. 各组件完整 HTML（内联样式 + `<span leaf="">` 包裹）
3. 完整文章模板骨架
4. 文章类型 → 组件组合配方表
5. Markdown → 组件映射规则表

添加后在本文件登记一行，并跑 `python3 scripts/component_lint.py .` 确认 0 严重问题。

## 颜色一致性维护

主题颜色值在 3 处文件中出现，修改任一处的颜色必须同步更新全部位置：

| 位置 | 文件 | 内容 |
|------|------|------|
| ① 注册表 | `theme-index.md`（本文件） | 主题表主色列 + 正文下划线 CSS 列 |
| ② 主题库 | `theme-{id}.md` | 设计变量速查表 + 各组件 HTML 内联色值 |
| ③ 换色规则 | `common-components.md` | 换色规则表（`{{主色}}`/`{{浅底色}}`/`{{下划线色}}` 映射） |

**修改流程：** 改色前先 `grep -rn "旧色值" references/` 扫出全部出现位置，逐处替换后再跑 `python3 scripts/component_lint.py .` 确认 0 严重问题。
