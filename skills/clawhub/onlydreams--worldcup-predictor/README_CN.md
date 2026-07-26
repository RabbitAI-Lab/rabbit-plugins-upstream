# World Cup Predictor Skill

一个用于世界杯和国际足球比赛分析的 agent skill。

它会引导 AI agent 把盘口/市场基线、真实比赛数据、球队新闻、打法匹配、比赛状态动机和赛后复盘放在一起判断，而不是只看赔率、纸面实力或上一场比分。

## 能做什么

- 按证据层分析比赛：市场、数据、新闻、背景、打法匹配。
- 要求 agent 明确说明实际使用了哪些信息源。
- 为完整预测、快速初判、滚球更新、赛后复盘和规则/争议解读选择对应的证据流程。
- 把公开赔率页和博彩市场页当作分析输入，而不是最终结论。
- 对时效性很强的赔率、首发和直播数据记录信息截止时间与来源状态。
- 检查球员可用性、角色状态、打法匹配、小组赛/淘汰赛比赛状态动机和环境因素。
- 支持淘汰赛专项判断，包括 90 分钟结果、晋级倾向、加时、点球大战和替补深度。
- 支持卡牌/纪律预测，结合裁判尺度、犯规点、比赛状态和合理牌数区间。
- 输出紧凑预测：比分、备选比分、赛果与精确比分分别标注信心、失败模式、缺失数据。
- 支持上下文限定的赛后复盘和可选校准记录，不虚构跨会话记忆。

## 免责声明

本技能只用于信息性足球分析。任何预测都有不确定性，也可能出错。

本技能不提供投注建议、金融建议、确定性结果或下注指令。agent 提到的赔率、博彩市场或交易价格，只应被视为分析输入。

## 仓库结构

```text
worldcup-predictor/
├── SKILL.md
├── README.md
├── README_CN.md
├── LICENSE
├── agents/
│   └── openai.yaml
└── references/
    └── prediction-framework.md
```

## 安装

把这个仓库复制或 clone 到你的 agent runtime 支持的 skills 目录。

对于 Codex 风格的本地 skills，常见目录是：

```bash
~/.codex/skills/worldcup-predictor
```

必要入口文件是：

```text
SKILL.md
```

## 使用方式

在需要世界杯或国际足球比赛分析时调用：

```text
Use $worldcup-predictor to analyze Spain vs Portugal using current team news, market baseline, recent match data, style matchup, and match-state incentives.
```

适合的请求包括：

- 赛前预测
- 精确比分预测
- 把盘口/市场作为证据层进行对比
- 小组出线形势分析
- 淘汰赛晋级、加时和点球大战场景分析
- 卡牌/纪律预测
- 球员伤停和首发影响分析
- 打法匹配分析
- 赛后预测复盘

## 信息源纪律

这个技能要求 agent 明确区分：

- 已确认事实
- 媒体报道
- 推断判断
- 用户提供的信息
- 缺失或未检查的信息

agent 不应声称使用了 Sofascore、FotMob、FBref、Polymarket、Stake、官方首发或其他信息源，除非它确实直接读取了公开页面/API，或用户在对话中提供了对应内容。

## License

本项目使用 MIT License。详见 [LICENSE](LICENSE)。
