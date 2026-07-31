# HR谈心罗盘 (hr-talk-compass)

> HR 员工谈心与 OD 洞察助手 —— 一个给 AI Agent 使用的 Skill

基于斯坦福《人生设计课》（Bill Burnett & Dave Evans）的设计思维方法论 + 教练式对话技术 + HRBP/OD 实践，让 AI 帮助 HR 系统化地做好员工谈心与组织发展工作。

## 它能做什么

| 场景 | 用哪个 Prompt | 输出 |
|------|--------------|------|
| 明天就要谈，没时间准备 | `prompts/quick-brief.md` | 一页纸提纲（6-9问 + 追问方向 + 边界提醒） |
| 关键人才、高流失风险对话 | `prompts/deep-dialogue.md` | 全案：目标判断 + 提纲 + 模拟陪练 + 预案 |
| 给业务主管/一线经理赋能 | `prompts/manager-toolkit.md` | 经理能独立使用的轻量对话框架 |
| 谈完了，要复盘沉淀 | `prompts/review-insights.md` | 谈心分析报告 + OD 信号 + 行动建议 |

## 核心方法论

1. **仪表盘**：健康/工作/生活平衡/关系 四维打分，先看人在哪
2. **重力问题 vs 真问题**：分清"无法改变的现实"与"可动手设计的问题"
3. **指南针**：员工的工作观 + 人生观，与公司机会是否同向
4. **能量地图**：什么事在滋养他、什么事在消耗他（擅长 ≠ 热爱）
5. **奥德赛计划**：三个都成立的五年版本，打开可能性
6. **原型行动**：不做大决定，先做两周内可启动的低成本尝试

## 文件结构

```
hr-talk-compass/
├── SKILL.md                        ← Skill 主文件（路由 + 总原则 + 伦理红线）
├── WORKFLOW.md                     ← 完整工作流（建议先读）
├── prompts/
│   ├── quick-brief.md              ← 速用版：10分钟出谈心提纲
│   ├── deep-dialogue.md            ← 深度版：关键对话全流程
│   ├── manager-toolkit.md          ← 主管版：业务经理简化工具
│   └── review-insights.md          ← 复盘版：谈后分析 + OD信号沉淀
└── exports/
    ├── quick-brief-纯prompt.txt    ← 纯 Prompt 版（复制粘贴即用）
    └── deep-dialogue-纯prompt.txt
```

## 安装方法

### OpenClaw

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/realzjr/hr-talk-compass.git
```

重启会话后，当对话涉及员工谈心/一对一/保留面谈等场景时，Agent 会自动加载该 Skill。

### Claude Code / 其他支持 Skills 的 Agent

将本仓库克隆到 Agent 的 skills 目录即可（目录结构遵循通用 Skill 规范：`SKILL.md` 含 frontmatter `name` + `description`）：

```bash
# Claude Code（个人级）
git clone https://github.com/realzjr/hr-talk-compass.git ~/.claude/skills/hr-talk-compass

# 或项目级
git clone https://github.com/realzjr/hr-talk-compass.git .claude/skills/hr-talk-compass
```

### 任何 AI（无 Skill 机制）

不需要安装——直接把 `exports/` 目录下的纯 Prompt 文件内容复制粘贴给任何 AI（ChatGPT / Claude / Kimi / DeepSeek……），即可使用。

也可以直接引用单个 prompt 文件：`prompts/quick-brief.md` 等四个文件各自独立成篇，按需取用。

## HR 职业伦理红线（内置约束）

1. 不窥探员工隐私，不用心理技巧操纵员工
2. 发现严重心理危机信号 → 转介专业资源（EAP/心理咨询）
3. AI 不替公司做承诺（晋升、调薪、转岗）
4. 所有建议符合中国劳动法常识
5. 谈心的目的不是"把员工劝回去"，而是帮双方看清最优解是否重合

## License

MIT
