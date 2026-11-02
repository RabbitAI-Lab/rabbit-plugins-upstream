## 十、AI 协同 — 多 Agent 工作流与自动化

### 🤖 Agent-to-Agent Recruiting 趋势

### 行业背景
- **Agent-to-Agent 交互**：Moltbook 等 AI agent 社交网络出现，招聘 agent 直接与候选人的职业管理 agent 对接
- **PeopleGPT**：60+ 数据源聚合，自然语言 prompt 完成人才地图，减少 70% 寻访时间
- **FidForward**：秒级扫描数百万 profile，自动生成 prioritized shortlist
- **Glozo《OpenClaw for Recruiters》指南**：夜间监控 GitHub 贡献者、本地简历 JD 匹配、WhatsApp 候选人回复草稿

### 对猎头的启示
1. **候选人正在 agent 化**——未来候选人可能通过职业管理 agent 接收机会、筛选匹配度、安排面试
2. **AI sourcing 工具是标配不是加分项**——43% 组织已用 AI 做 HR 任务（SHRM），同比从 26% 上升
3. **AI 做广度，人做深度**——Boolean + AI 做 Longlist，猎头做 Shortlist + 关系建立

### 应对策略
- 熟悉主流 AI sourcing 工具（PeopleGPT、FidForward、Juicebox 等）
- 准备标准化机会描述格式，便于候选人 agent 解析
- 继续强化 human-to-human 深度沟通——AI 完成初筛后，猎头价值在信任建立、动机挖掘、谈判促成
- 关注 Agent Skills 开放标准（Anthropic 2025.12，16+ 工具支持）

### 数据基准 — 转化漏斗
- 43% 组织已用 AI 做 HR 任务（SHRM 2026），同比从 26% 上升
- AI 减少 90% 手动寻访时间（Boolean + AI 组合）
- 内部推荐保留率比其他渠道高 40%（Oracle）
- Salesforce 2026 State of Sales：87% 组织使用 AI，54% 已部署 AI agent

***


### 🤖 AI Agent 协同招聘工作流参考

> 来源：Recrew.ai / Saral AI / Onrec — 多 Agent 协同招聘团队

### 多 Agent 分工架构

| Agent 角色 | 职责 | 对应 Pipeline 阶段 |
|-----------|------|-------------------|
| **Technical Recruiter Agent** | JD 解析 + 技术关键词提取 + GitHub/LinkedIn 搜索 | Identified |
| **Communication Specialist Agent** | 个性化触达消息生成 + 跟进序列 | Contacted → Responded |
| **Scheduling Coordinator Agent** | 面试预约 + 日历协调 + 提醒 | Interview |
| **Candidate Nurture Agent** | 长期关系培育 + 行业洞察推送 | Warm Keep |
| **ATS Update Agent** | 自动更新候选人状态 + 标记 Silver Medalist | 全流程 |

### 对 [猎头顾问姓名] 的实际价值
- **不是替代**，是释放时间：AI 做 Longlist 和跟进，你做 Shortlist 和关系
- **跑通流程再升级**：先把现有 SOP 跑顺，再考虑多 Agent 自动化
- **72% 招聘团队已用人机协同**：不是未来时，是现在时

### 最小可行 AI 工作流（立即可用）
```
1. [猎头顾问姓名] 提供 JD → AI 解析提取关键词 + 构建 Boolean
2. AI 生成首批 Longlist（20-30 人）→ [猎头顾问姓名] 做 Shortlist（5-8 人）
3. AI 生成个性化触达消息 → [猎头顾问姓名] 审核后发送
4. AI 追踪回复状态 → [猎头顾问姓名] 做深入沟通
5. AI 生成推荐报告初稿 → [猎头顾问姓名] 修改后提交客户
```

***


### OpenClaw 猎头工作流自动化

### 夜间监控（Passive Monitoring）
> agent 夜间监控 GitHub/LinkedIn/hiring boards，早上推送候选人摘要

**设置方式**：通过 cron 定时任务
- 每天早上 8:00 检查目标公司新岗位/新闻
- 每周一次扫描候选人 LinkedIn 动态
- 发现 hiring signals 自动推送 [猎头顾问姓名]

### 候选人自动跟进
> 通过 WhatsApp/Telegram/微信 自动跟进候选人

**状态追踪**：
- 记录每次沟通到 candidate profile
- 自动判断跟进时机（7 天未联系 → 提醒）
- 根据候选人分类标签选择沟通策略

***


### 🤖 OpenClaw 招聘三大核心工作流（Glozo 指南）

> 每次查询边际成本仅 $0.10-$0.50 API 费，无需按席位付费

| 工作流 | 说明 | 交付 |
|--------|------|------|
| **被动监控** | 夜间监控 GitHub/招聘板/LinkedIn 贡献者变动 | 次日候选人简报 |
| **简历筛选** | 批量 PDF 简历按 JD 评分，输出 CSV | 评分排序表 |
| **跟进对话** | 起草候选人回复，保持上下文 | 人工审批后发送 |

### AI sourcing ROI
- AI sourcing 可实现 **30% 更高的入职质量 + 10% 更低的成本**（HR Executive）
- 8.8% 美国 HR 招聘 JD 已要求 AI 工具技能，比 2025 年初翻倍
- 72% 招聘团队计划 12 个月内引入 AI 智能体
- 58% 招聘人员认为 AI 减少杂活，能专注于候选人关系

***


### 🎙️ 语音 AI 工作流

> 猎头每天大量时间花在电话沟通、候选人面谈、行业会议，这些录音手动整理效率极低

### 推荐工具：Microsoft VibeVoice

**VibeVoice 是什么：**
- 微软 2025-2026 开源的前沿语音 AI 模型家族
- ASR：60 分钟长音频单次处理，输出 Who + When + What 结构化转录
- TTS：90 分钟长语音合成，支持多说话人、情感表达
- Realtime TTS：0.5B 参数，首字延迟 ~300ms

### 四大模型速查

| 模型 | 用途 | 大小 | 特点 |
|------|------|------|------|
| VibeVoice-ASR-7B | 语音→文字 | 7B | 60分钟单次处理，50+语言 |
| VibeVoice-ASR-BitNet | 语音→文字（CPU版） | 1.58GB | 无需GPU，3线程实时推理 |
| VibeVoice-TTS-1.5B | 文字→语音 | 1.5B | 90分钟长音频，4人对话 |
| VibeVoice-Realtime-0.5B | 实时文字→语音 | 0.5B | 首字300ms延迟，流式输入 |

### 猎头条使用场景

**场景 1：候选人通话录音 → 结构化转录**

输入：[猎头顾问姓名] 与候选人的通话录音
输出：结构化的沟通记录，含 PMCC 分析

**场景 2：行业会议/培训录音 → 纪要**

输入：1-2 小时行业峰会录音
输出：结构化会议纪要 + 招聘情报

**场景 3：推荐报告 → 语音版**

输入：候选人推荐报告文字
输出：用好听的声音朗读，通过微信发给客户

### 安装指南

```bash
# 方式一：HuggingFace Transformers（需 transformers >= 4.50.0 或源码）
pip install --upgrade transformers torch torchaudio soundfile

# 方式二：在线 Playground（免安装）
# 搜索 "VibeVoice ASR" 或 "VibeVoice TTS" 即可找到在线 Demo

# 方式三：Azure AI Foundry
# 搜索 "VibeVoice" 即可找到
```

### 注意事项 — 背调
- ASR-BitNet 版仅需 1.58GB 且无需 GPU，最适合本地部署
- 国内网络可能较慢，建议先用 Playground 验证效果
- Python 3.10+ 推荐

***


### 行业洞察自动化

> 不只是新闻聚合，而是 "这新闻意味着什么招聘机会" 的分析

### 晨报升级结构
```
# [日期] 行业洞察晨报


### AI 招聘工具对比评估

### 主流工具对比

| 工具 | 核心能力 | 数据规模 | 适合场景 | 预估价格 |
|------|---------|---------|---------|---------|
| **Apollo.io** | 人才数据库富化、邮件序列 | 2.65 亿联系人 | Cold outreach、线索挖掘 | $49-149/月 |
| **SeekOut** | 多元化人才搜索、技能图谱 | 8 亿+ Profiles | Tech 人才寻访、DEI | 定制报价 |
| **HiredScore** | AI 匹配、内部流动 | 企业自有数据 | 大企业内部招聘 | 定制报价 |
| **Eightfold** | AI 人才智能、职业路径 | 企业自有数据 | 人才管理、继任规划 | 定制报价 |
| **LinkedIn Recruiter** | 社交招聘、InMail | 10 亿+ Users | 全行业通用 | $170-230/月 |
| **ResumeClaw** | 简历→AI Agent | 自建 | 候选人自动化跟进 | OpenClaw Skill |

### 建议
- **Apollo**：如果 [猎头顾问姓名] 经常做 Cold Outreach，值得投入（性价比最高）
- **SeekOut**：如果 Tech 方向需求大，考虑（技能图谱很强）
- **LinkedIn Recruiter**：必备基础工具（已有则不需替代）
- **ResumeClaw**：OpenClaw 免费 Skill，先用起来

### AI + 猎头协同模式（2026 新标杆）
- AI 辅助筛选简历 → 大数据绘制人才地图 → 自动生成候选人报告 = **新标配**
- 猎头不仅要有识人能力，更必须具备 **"AI 协同智商"**
- 360 顾问方向：BD（客户开发）+ 对接 + 交付全面发展，从纯交付转向一站式咨询型服务

### Agent Skills 开放标准（2026）
- Anthropic 2025.12 发布 Agent Skills 开放标准，16+ AI 工具支持（Claude Code、Cursor、Codex、Gemini CLI、VS Code 等）
- 技能 = 一个目录 + SKILL.md 文件，"写一次到处用"
- 渐进式加载，不影响性能
- 猎头工作流可封装为 Skill，跨 Claude Code / Cursor / Codex / Gemini CLI 复用

📖 **延伸阅读**：[references/brief-drift-detection.md](references/brief-drift-detection.md) — Brief Drift Detection（5 类变更监控）


