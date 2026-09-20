# Changelog

## 24.0.0 (2026-09-18) — 本周升级

### Fixed
- CHANGELOG 版本号对齐（24.0.0 对应 v24 发布，此前误写为 v23 bump 记录）
- 核心原则 #31/#37 首次触达给价值重复表述合并
- 核心原则 #18/#19 AI协同 + 批判性思维重复表述合并
- 历史版本注释清理（v10.0 更新、v12.0 新增等内联标注，CHANGELOG 已记录）
- CHANGELOG 历史记录恢复（v14-v23 全部保留）

### Changed
- SKILL.md 瘦身：4252 行 → ~3200 行（164K → ~120K）
- skill.yml 输出契约细化：12 个 task_type 独立 output schema

## 23.0.0 (2026-09-18)

### Changed
- onboarding-support.md 正文链接补全（10/10 References 全覆盖）
- 版本号 bump v22.0.0 → v23.0.0

## 22.0.0 (2026-09-18)

### Changed
- 10 个 References 正文引用全链接（从 0→9 次）— AI 执行时能直接看到深度参考文档
- H1 标题版本号对齐（v17.0 → v22.0）
- 附录 References 索引整合为单一完整表格
- skill.yml 版本对齐 SKILL.md frontmatter

## 21.0.0 (2026-09-18)

### Changed
- H1 标题版本号对齐（v17.0 → v21.0）
- 附录 References 索引整理为单一完整表格（消除重复/断裂）
- 10 个 references 文件全部在 SKILL.md 中建立引用链接

## 20.0.0 (2026-09-10)

### Changed
- ClawHub 发布修复：description 字段从 85KB 全量嵌入精简为摘要
- skill.yml version 对齐 SKILL.md frontmatter

## 19.0.0 (2026-09-10)

### New
- skill.yml 输入契约完全对齐 12 阶段工作流（6 → 12 个 task_type）
- 新增 task_type: offer_negotiation, onboarding_support, data_optimization, ai_workflow, compliance_ecosystem, workflow_sop
- 完整索引全部 10 个 references 文件（onboarding-support, outreach-scripts, pipeline-states 等）

### Changed
- 修复 ClawHub SUSPICIOUS 根因：description 字段从 85KB 全量嵌入精简为 52 字符摘要
- skill.yml 版本对齐 SKILL.md frontmatter（15.0.0 → 19.0.0）
- 顶层 ## 标题从散列结构统一为 12 阶段商业逻辑顺序（〇～十二 + 附录）

### Fixed
- 重复 ### 标题清零（9 组 → 0 组）
- 快速指令 #1-7 补全（从 #8 起始 → #1-#16 完整覆盖）
- SKILL.md.v16.backup 清理，不再阻塞 SkillHub 发布

## 18.0.0 (2026-09-09)

### Changed
- 按猎头商业逻辑全面重构：从版本号堆叠改为 12 阶段端到端工作流
- 核心原则 39 条完整保留，快速指令 16 条全覆盖
- 10 个 references/ 文件全部索引
- 空行压缩优化（连续 4+ → 3）

## 15.0.0 (2026-09-02)

### New
- Talent Gap Analysis（咨询先行模式）：四步人才差距分析流程（Business Diagnosis → Role Necessity → Talent Gap → Co-create Success Profile）
- 垂直行业深耕评估：9+1 维度评分新增行业专属洞察维度
- Offer 谈判 7 问检查表
- 候选人 Persona 构建框架
- 企业客户关系深度维护（四阶段 + 5 关键动作 + 3 案例）
- 职位需求对齐 SOP（JTIF 框架：Job → Talent → Interview → Follow-up）
- Purple Squirrel 管理流程
- 中间阶层候选人识别与应对指南
- AI Agent 协同招聘工作流参考
- GitHub Proof of Work 5 信号评估模块
- 推荐报告素材收集 SOP
- 语音 AI 工作流（VibeVoice）
- AI 原生能力评估维度
- 48h 反馈 SLA 追踪
- AI 使用披露 & 薪资透明化话术

### Changed
- 9 维度评分扩展为 9+1 维度（+批判性思维/适应性，Korn Ferry 2026 #1 需求技能）
- 入职追踪从 90 天扩展为 6 个月融合支持
- 核心原则从 26 条扩展至 39 条
- 移除个人身份信息（已匿名化）
- 短名单质量控制升级（v9.1）
- Silver Medalist 管道管理（v9.2）
- 转化率基准更新（v12.0）
- 核心原则新增：AI 协同智商、批判性思维优先级（v10.0）

### Security
- 无外部网络调用
- 仅文件操作 + 文本生成
- 最小权限模型
- 候选人个人信息不输出到文件外

## 14.0.0 (2026-08-27)

### Changed
- 入职追踪从 90 天升级为 6 个月融合支持
- 新增 AI 原生能力评估维度

## 13.1 (2026-08-25)

### Changed
- 触达话术库升级（GitHub 技术人才 + LinkedIn 被动 + 中间阶层三轨）
- Silver Medalist 再利用机制落地

## 13.0 (2026-08)

### New
- 语音 AI 工作流
- 候选人体验 2026 核心差异化

## 12.0 (2026)

### New
- 48h 反馈 SLA 追踪
- AI 使用披露 & 薪资透明化话术
- AI Agent Recruiter 竞品全景
- ClawHub 发布准备
- 转化型猎头关键理念
- Talent Mapping 2026 方法论升级

### Changed
- 核心原则更新：AI 协同智商、批判性思维优先级
- 转化率基准更新

## 11.0

### New
- 核心原则 34-39 条
- Anti-Rationalization 检查
- Hitting Rate 统计

## 10.0

### Changed
- 核心原则从 15→26 条
- 新增 AI 协同智商、批判性思维优先级

## 9.x

### New
- v9.2: Silver Medalist 管道管理
- v9.1: 短名单质量控制、客户长期人才顾问服务、候选人多样性评估
