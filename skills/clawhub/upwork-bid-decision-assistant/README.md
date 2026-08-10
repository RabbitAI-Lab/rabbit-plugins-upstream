# Upwork 投标判断助手

一个面向中文自由职业者的 Upwork 机会评估 Skill。

它会把职位描述、客户历史、竞争态势与用户自身画像交叉分析，帮助判断：

- 这个工作是否值得投；
- 是否需要使用 Boost；
- 是否值得接受 Invite；
- 客户、预算、范围和付款是否存在风险；
- 当前结论还缺哪些关键证据。

> 本项目是非官方社区项目，与 Upwork 无隶属、合作或背书关系。它提供经验型决策辅助，不保证面试、合同或收入。

## 主要特点

- **先建个人画像**：支持读取 Upwork Freelancer 主页，也支持整页复制、截图、文字或口述。
- **不靠单一数字下结论**：交叉判断工作、客户和竞争三类信息。
- **明确区分投标与 Boost**：不是“值得投”就一定需要 Boost。
- **信息不足不乱猜**：关键数据缺失时，只追问可能改变结论的字段。
- **风险优先**：诈骗、先付款、站外交易、免费核心交付等风险不会被高预算抵消。
- **兼容多种 AI**：支持 Agent Skills 的产品可直接安装；其他模型可使用完整粘贴版。

## 快速开始

### 方式一：安装为 Agent Skill

克隆仓库：

```bash
git clone https://github.com/<你的用户名>/upwork-bid-decision-assistant.git
```

将仓库目录放到 Agent 支持的 Skill 目录。例如：

```text
$HOME/.agents/skills/upwork-bid-decision-assistant/
```

或项目级目录：

```text
.agents/skills/upwork-bid-decision-assistant/
```

核心入口是 [`SKILL.md`](SKILL.md)，详细规则位于 [`references/`](references/)。

### 方式二：直接复制到任意大模型

打开：

[`assets/通用大模型粘贴版.md`](assets/通用大模型粘贴版.md)

复制全文到系统提示词、自定义指令、项目说明或新对话开头。

## 第一次怎么用

优先提供自己的 Upwork Freelancer 公开主页：

```text
这是我的 Upwork Freelancer 主页：<链接>
请先建立个人画像。若链接无法读取，请告诉我需要复制或截图哪些区域。
```

也可以发送主页文字、连续截图，或直接口述技能、项目与报价。Skill 会先整理已确认信息，再用少量问答补齐缺口。

建立画像后，发送职位链接、截图或页面文字：

```text
请使用 Upwork 投标判断助手分析这个工作。
告诉我：
1. 投不投；
2. 是否 Boost；
3. 是否接受 Invite；
4. 主要风险；
5. 还缺哪些会改变结论的信息。
```

## 建议提供的信息

### 工作本身

标题、完整描述、技能、预算或时薪、项目周期、每周工时、筛选问题、发布时间和所需 Connects。

### 客户历史

Payment/Phone Verified、评分与评价、Hire Rate、Total Spent、历史时薪、会员时间、过去项目与付款记录。

### 竞争态势

Proposals、Interviewing、Invites、Unanswered Invites、Last Viewed、已雇佣人数和计划招聘人数。

信息不必一次全部齐全。已有证据足够判断时，Skill 会先给结论；缺失信息可能反转结论时，才会继续追问。

## 输出内容

通常包括：

- 投标建议；
- Boost 建议；
- 判断置信度；
- 正向与风险信号；
- 个人匹配、客户可信度、竞争时效、经济性与执行风险；
- 报价和 Proposal 思路；
- 免费方案边界；
- 缺失信息及其影响。

## 仓库结构

```text
upwork-bid-decision-assistant/
├── SKILL.md                  # Skill 主入口
├── agents/openai.yaml        # Agent 展示与默认调用配置
├── references/               # 判断规则、输入、风险与输出模板
├── assets/                   # 粘贴版、用户说明和画像模板
├── examples/                 # 虚构示例
├── docs/                     # GitHub 发布说明
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
└── LICENSE
```

## 重要边界

- 不保证获得面试、合同或收入。
- 不鼓励绕过 Upwork、站外付款或合同前交换联系方式。
- 不鼓励伪造 Portfolio、证书、评价或 Time Tracker 记录。
- 不根据客户国籍、姓名、族裔或头像直接判断风险。
- Upwork 的界面、Connects、费用和规则会变化；需要精确平台规则时，应核对最新官方信息。
- 不要把身份证、银行信息、账号密码或精确住址放入个人画像。

## 贡献

欢迎提交 Issue 或 Pull Request。请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。不要在公开 Issue 中粘贴真实客户的私人信息、未脱敏聊天或付款资料。

## 授权

本仓库采用 [`Non-Commercial Public License 1.0`](LICENSE)：允许个人和非商业使用、修改与分享，但需保留署名与授权说明，禁止销售、付费分发或将其作为商业产品核心内容重新包装。

这是一份 **source-available（源码可见）** 授权，不是 OSI 认可的开源许可证。
