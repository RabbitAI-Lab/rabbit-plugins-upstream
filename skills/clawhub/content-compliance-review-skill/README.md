# 内容合规审查 Skill

面向中国大陆自媒体创作者的发布前内容合规筛查工具。它帮助你在发布到抖音、小红书、微信视频号和微信公众号之前，检查口播、文案、字幕、画面、链接、广告主张及互动引导中的风险，并给出可以直接执行的修改建议。

> 这是一套预审与决策辅助规则，不保证平台审核通过，也不替代律师或平台官方意见。

## 能解决什么问题

- 同一内容准备发多个平台，不清楚平台差异。
- 带货、种草或品牌合作内容，担心虚假宣传、广告标识和功效承诺。
- 医疗、金融、教育、食品、法律等专业内容，不确定资质和表达边界。
- 视频文案看起来没问题，但画面、二维码、字幕或评论引导可能踩线。
- 内容被下架后，希望依据公开规则定位可能原因，而不是只扫描“敏感词”。

## 审查范围

Skill 会根据实际提供的素材检查：

- 标题、正文、话题标签和评论区话术
- 口播、字幕、背景音与声音仿冒
- 封面、视频帧、人物、产品、制服、二维码和背景物品
- 商品功效、销量、价格、排名、证言和前后对比
- 赞助、佣金、赠品、抽奖、购买链接和私域导流
- AI 生成或深度合成内容的标识、身份真实性和侵权风险
- 未成年人、隐私、版权、危险行为和其他受众安全问题

## 已覆盖平台

| 平台 | 当前覆盖 |
| --- | --- |
| 抖音 | 社区规则、未成年人、医疗健康、营销、AI 生成内容及法律行业补充 |
| 小红书 | 社区互动、商业合作、种草与效果对比、医疗医美、未成年人及珠宝文玩 |
| 微信视频号 | 通用内容、直播、营销、金融与健康科普、AI 内容及微短剧版权 |
| 微信公众号 | 原创与低质内容、导流互动、广告、金融医疗、流量作弊及 AI 内容 |
| 中国大陆广告法律基线 | 广告真实性、可识别性、绝对化表达、医疗、保健食品、教育、投资、房地产、烟酒及 AI 标识 |

当前规则库包含 **125 条平台检查规则和 13 条广告法律检查规则**。

规则并非全部具有相同权威等级。每条记录都标注 `Authority`、`Status`、来源、日期和适用表面：

- `law`：法律法规或监管机关文件
- `official`：能够定位的官方平台规则
- `campaign`：专项治理或阶段性要求
- `heuristic`：经验性风险模式
- `unknown`：来源或现行状态仍需核实

无法确认最新官方原文的规则，审查报告必须标为“待核实”，不能冒充当前平台政策。

## 安装

### Codex

Codex 支持从用户级 `$HOME/.agents/skills` 或仓库级 `.agents/skills` 读取 skill。

用户级安装：

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/xiaoxiaochen5678-dot/content-compliance-review-skill.git \
  "$HOME/.agents/skills/content-compliance-review"
```

仅在当前仓库使用：

```bash
mkdir -p .agents/skills
git clone https://github.com/xiaoxiaochen5678-dot/content-compliance-review-skill.git \
  .agents/skills/content-compliance-review
```

Codex 通常会自动检测新 skill；如果没有出现，请重启 Codex。

### Claude Code

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/xiaoxiaochen5678-dot/content-compliance-review-skill.git \
  "$HOME/.claude/skills/content-compliance-review"
```

如果你的 Claude Code 版本使用其他 skill 目录，以该版本的官方说明为准。

### WorkBuddy

当前仓库尚未验证已经上架 WorkBuddy 技能市场。若你的 WorkBuddy 版本支持从 GitHub 仓库或本地文件夹导入 skill，请选择本仓库或包含 `SKILL.md` 的根目录；具体入口以你安装版本的产品说明为准。

### 更新

进入安装目录后执行：

```bash
git pull --ff-only
```

不要在已有同名真实目录上直接覆盖安装；先备份自己的修改和规则资料。

## 使用示例

在 Codex 中可以直接调用：

```text
$content-compliance-review
帮我审查这段口播，准备同时发抖音和小红书。
```

也可以自然地提出需求：

```text
这是一条品牌赞助的护肤品视频，请检查口播、字幕、前后对比图和购买引导。
```

```text
这段医疗科普准备发微信视频号，哪些地方需要资质、来源或风险提示？
```

```text
这篇公众号文章里有 AI 图片和抽奖活动，请做发布前合规审查。
```

## 输出内容

每次审查至少包含：

1. 发布结论：暂不发布、修改后再审、可发布但需人工确认或未发现明显风险。
2. 审查范围：已检查和无法检查的素材表面。
3. 问题清单：具体位置、风险等级、依据层级和可能后果。
4. 修改建议：尽量保留原意的最小安全修改。
5. 平台差异：同一内容在不同平台的处理区别。
6. 待确认事项：资质、授权、证据、同意和时效性缺口。
7. 边界提示：不承诺过审，不帮助规避审核或迁移违规行为。

## 安全与隐私

- 审查前应删除或遮盖密码、验证码、身份证号、支付信息、账号恢复资料和未公开客户数据。
- 不要为认证或解封向非官方代办提交账号密码、证件原件或付款。
- Skill 本身不包含外部 API；但内容是否联网、发送到哪里、是否保存，取决于承载它的 Agent、模型服务、启用工具和用户配置。处理敏感素材前请核对宿主产品的数据政策。
- 不进行人脸身份识别，不推断敏感属性；只检查发布所需的合规风险。

## 已知限制

- 主要面向中国大陆平台，不覆盖海外平台法律与社区规则。
- 平台规则持续变化，带日期或 `unknown` 状态的结论应在发布前查阅最新官方页面。
- “最、第一、治疗、收益”等词只是复核线索，不能脱离广告属性、语境和证据机械判违规。
- 无法查看的图片、视频、音频、链接落地页和评论区会明确列为未检查范围。
- 不能保证发布成功、流量表现、账号不受处罚或监管机关不采取行动。

## 维护规则库

平台规则位于 [`references/platforms/`](references/platforms/)，广告法律基线位于 [`references/laws/`](references/laws/)。新增规则时请遵循 [`references/rule-schema.md`](references/rule-schema.md) 的证据字段，不要用二手经验覆盖已核实规则。

修改规则后运行：

```bash
python3 scripts/validate_rules.py
```

## 项目结构

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── common-risks.md
│   ├── laws/
│   ├── platforms/
│   └── rule-schema.md
└── scripts/validate_rules.py
```

## 许可证

[MIT License](LICENSE)

你可以使用、修改和分发本项目。转载或二次发布时，请保留许可证和版权声明。平台名称及平台规则的相关权利归各自权利人所有。
