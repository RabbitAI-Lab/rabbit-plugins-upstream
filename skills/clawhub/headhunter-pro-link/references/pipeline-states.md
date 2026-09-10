# Pipeline 状态机

> 来源：headhunter-pro SKILL.md v15.0

## Pipeline 状态定义

```
[Identified] → [Contacted] → [Responded] → [Screened] → [Shortlisted] 
           → [Client Submitted] → [Interviewing] → [Offer Stage] → [Placed]
```

### 状态说明

| 状态 | 说明 | 触发条件 | 退出条件 |
|---|---|---|---|
| **Identified** | 已识别候选人 | Boolean/人才地图找到 | 首次触达 |
| **Contacted** | 已触达 | 发送首次消息 | 候选人回复 |
| **Responded** | 已回复 | 候选人回复消息 | 完成初步筛选 |
| **Screened** | 已筛选 | 完成简历评估 + 电话初筛 | 进入短名单 |
| **Shortlisted** | 短名单 | 通过 9+1 评分 ≥ 7.0 | 提交给客户 |
| **Client Submitted** | 已提交客户 | 客户收到推荐报告 | 客户确认面试 |
| **Interviewing** | 面试中 | 进入面试流程 | 通过全部面试 |
| **Offer Stage** | 谈薪阶段 | 客户发出 Offer | 候选人接受/拒绝 |
| **Placed** | 已入职 | 候选人入职 | 入职 6 个月护航期结束 |

### 回退状态

| 状态 | 回退原因 | 后续动作 |
|---|---|---|
| **Contacted → Identified** | 消息被忽略/拒绝 | 30 天后重新触达或标记"暂不联系" |
| **Responded → Contacted** | 候选人暂停沟通 | 等待 14 天后温和跟进 |
| **Screened → Shortlisted** | 评分不足但潜力高 | 进入 Silver Medalist 管道 |
| **Client Submitted → Screened** | 客户拒绝 | 了解拒绝原因，调整后重新评估 |
| **Interviewing → Client Submitted** | 面试未通过 | 了解反馈，标记差距项 |
| **Offer Stage → Interviewing** | 谈判破裂 | 尝试挽回或进入备选 |
| **Offer Stage → Placed** | 候选人拒绝 Offer | 了解原因，调整策略 |

## 阶段 SLA

| 阶段 | 目标时长 | 超时动作 |
|---|---|---|
| Identified → Contacted | ≤ 48h | 标记"需优先触达" |
| Contacted → Responded | ≤ 7 天 | 发送跟进消息 |
| Responded → Screened | ≤ 5 天 | 安排初筛通话 |
| Screened → Shortlisted | ≤ 3 天 | 完成 9+1 评分 |
| Shortlisted → Client Submitted | ≤ 48h | 生成推荐报告 |
| Client Submitted → Interviewing | ≤ 7 天 | 催促客户反馈 |
| Interviewing → Offer Stage | ≤ 14 天 | 了解面试进展 |
| Offer Stage → Placed | ≤ 7 天 | 协助谈薪 |

**48h 反馈 SLA（v12.0 新增）：**
- 候选人提交简历后，48 小时内必须给予首次反馈
- 超时预警话术："Hi [姓名]，你的简历我已经仔细看过，正在和客户做初步对齐，预计 [时间] 给你详细反馈。"

## 转化率基准

| 阶段转换 | 行业基准 | 优秀水平 | 计算公式 |
|---|---|---|---|
| Contacted → Responded | 15-25% | 30%+ | 回复数 / 触达数 |
| Responded → Screened | 40-60% | 70%+ | 初筛数 / 回复数 |
| Screened → Shortlisted | 20-40% | 50%+ | 短名单数 / 初筛数 |
| Shortlisted → Interviewing | 50-70% | 80%+ | 面试数 / 短名单数 |
| Interviewing → Offer | 30-50% | 60%+ | Offer 数 / 面试数 |
| Offer → Placed | 60-80% | 90%+ | 入职数 / Offer 数 |

**整体转化率（Contacted → Placed）：**
- 行业基准：0.5-2%
- 优秀水平：3-5%

## Pipeline 健康度指标

1. **Pipeline 深度**：每个阶段候选人数量应呈漏斗状
2. **Pipeline 速度**：候选人平均在各阶段停留时间
3. **Pipeline 转化率**：各阶段之间的转换效率
4. **Pipeline 新鲜度**：最近 30 天内新增的候选人占比
5. **Pipeline 质量**：Shortlisted 以上候选人的 9+1 评分均值
