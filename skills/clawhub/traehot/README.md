# Trae-Hot — TRAE AI创造力大赛超级IP孵化系统

> 批量申报引擎：选题→报名帖→HTML产品页→初赛深化→初赛帖→模拟评委打分→视频脚本→打分预测→回收。
> 目标：大量demo过报名→初赛，拿到5W视频流量激励，把IP账号做起来。

> 活动规则详情介绍：https://www.trae.cn/ai-creativity?utm_source=community

<img width="1923" height="937" alt="image" src="https://github.com/user-attachments/assets/9c45ba65-17f9-4130-abc9-82d1f4ef7b8c" />

<img width="766" height="1603" alt="image" src="https://github.com/user-attachments/assets/74ee1f4e-1242-4f90-9361-a8144133b6ae" />

---

## 作者

| 项目 | 信息 |
|------|------|
| 创作者 | **@PandLeeAI** |
| 联系邮箱 | **PandLee@qq.com** |
| 抖音 | **@熊黎 \| PandLeeAI** |
| 开源协议 | MIT License |

---

## 文件结构

```
trae-hot-v2.0/
├── README.md                          # 本文件（分发说明）
├── SKILL.md                           # trae-hot 主skill文件（8阶段工作流）
├── state.md                           # 空白模板（记录你的demo进度和账号数据）
├── rubric.md                          # 自包含评分参考（无需安装cheat-on-content）
├── demo-template/                     # 申报材料模板（7个阶段模板）
│   ├── 选题.md
│   ├── 报名帖.md
│   ├── 初赛帖.md
│   ├── 视频脚本.md
│   ├── 模拟评委打分.md
│   ├── 打分预测.md
│   └── 回收.md
└── deps/
    └── cheat-on-content/              # 网红作弊器（依赖 + 致敬蜗牛学长）
        ├── README.md                  # 致敬与归因说明
        ├── SKILL.md                   # 总协议 + 路由表
        ├── rubric_notes.template.md   # 评分模板（复制到项目根目录使用）
        └── starter-rubrics/
            ├── opinion-video.md       # v2 已校准 rubric（25+ 样本）
            └── opinion-video-zero.md  # v0 cold-start 等权占位
```

---

## 快速安装

### 方式一：仅安装 Trae-Hot（推荐，最简单）

```bash
# 1. 复制 skill 文件到你的项目
你的项目/
├── .trae/
│   └── skills/
│       └── trae-hot/
│           ├── SKILL.md      ← 从本zip复制
│           └── state.md      ← 从本zip复制（空白模板）
└── rubric.md                 ← 从本zip复制（可选，自包含评分参考）
```

### 方式二：完整安装（含网红作弊器依赖）

```bash
# 1. 复制 trae-hot skill
cp -r trae-hot-v2.0/SKILL.md 你的项目/.trae/skills/trae-hot/
cp -r trae-hot-v2.0/state.md 你的项目/.trae/skills/trae-hot/

# 2. 复制 cheat-on-content 依赖（可选，深度评分用）
cp -r trae-hot-v2.0/deps/cheat-on-content/ 你的项目/.trae/skills/cheat-on-content/

# 3. 复制评分模板到项目根目录
cp trae-hot-v2.0/deps/cheat-on-content/rubric_notes.template.md 你的项目/rubric_notes.md

# 4. 复制自包含评分参考（可选）
cp trae-hot-v2.0/rubric.md 你的项目/
```

### 填写 state.md

打开 `.trae/skills/trae-hot/state.md`，填入你的账号信息。首次使用可留空，每完成一个demo后更新。

### 开始使用

在TRAE对话中输入以下任一关键词即可触发：

- "开始新demo" / "做新选题" / "大赛申报"
- "报名帖" / "初赛帖" / "视频脚本"
- "打分预测" / "模拟评委"

---

## 评分系统说明

本skill的**阶段7打分预测**依赖内容评分体系。评分有两种方式：

### 轻量模式（默认）
使用本zip附带的 `rubric.md` 作为自包含评分参考——包含 v0 等权公式、7维度定义、三原则预检、Bucket预测方案。**不需要安装 cheat-on-content。**

### 深度模式（推荐进阶用户）
安装 `deps/cheat-on-content/` 到 `.trae/skills/cheat-on-content/`，获得完整的 5 阶段闭环（打分→预测→发布→复盘→进化rubric）。这是蜗牛学长"网红作弊器"的完整方法论。

---

## 适用场景

- TRAE AI创造力大赛报名/初赛申报
- 批量制作demo冲5W流量券
- 内容视频脚本+打分预测
- IP账号孵化

---

## 更新日志

### v2.0 (2026-07-10)
- 新增飞书群盲盒活动完整工作流（参与门槛、3行模板、冲刺日行动清单）
- 新增5W流量券批量申领策略分析（规则依据 + 风险提示 + 安全打法）
- 新增抖音人气通道详细规则（人气分公式、最低门槛、数据口径）
- 新增 Session ID 完整格式说明（3段不能丢！常见错误对照）
- 初赛帖模板更新：增加"打招呼"section，强化 Session ID 完整性要求
- 视频脚本模板更新：产品体验视频导向（惊艳成品→可玩功能→关键过程→获取方式）
- 新增选题合规检查清单（6项逐项确认）
- 新增官方比赛规则完整版（报名帖审核标准、初赛评审4维度、FAQ）
- 8阶段工作流全面细化，每个阶段有明确的触发条件、动作、产出和确认机制

### v1.0 (2026-06-19)
- 首次发布
- 8阶段引导式工作流
- 7位独立人格模拟评委
- 自包含评分rubric + 完整cheat-on-content依赖

---

## 致敬

本skill的评分预测体系灵感来源于 **蜗牛学长** 的 **"网红作弊器"（cheat-on-content）** skill——一个将内容创作从"玄学"变成"可量化工程"的评分系统。蜗牛学长用 25+ 已发视频拟合出 7 维度评分体系（ER/SR/HP/QL/NA/AB/SAT），证明了"爆款"可以被量化。Trae-Hot 在此基础上集成了大赛申报全流程。

> **内容不是玄学，是可预测的。** 我们只是把这套方法论搬到了大赛申报上。

本zip包 `deps/cheat-on-content/` 目录包含了网红作弊器的核心文件，作为 Trae-Hot 的评分依赖。如果你觉得这套方法论有用，请给蜗牛学长的原始项目点星。
