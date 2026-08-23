## Description:

用抽奖工具通过已授权的 LottoTool MCP，引导运营人员配置奖项、玩法、中奖率和开奖时间，并在用户确认后预览、创建或编辑微信小程序抽奖活动。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zouzixuan](https://clawhub.ai/user/zouzixuan)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and marketing teams use this skill to turn natural-language campaign requirements into confirmed LottoTool lottery activity configurations for WeChat mini-program promotions. It supports preview-first creation and editing of activities after the user explicitly confirms the final configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or edit lottery activities in an authorized LottoTool account.

Mitigation: Install and use it only for accounts where the operator trusts LottoTool and WorkBuddy; require preview plus explicit confirmation before any create or update action.

Risk: Physical-prize fulfillment can involve recipient name, phone, and address collection.

Mitigation: Make activity terms and privacy practices clear about why the data is collected, who can access it, retention duration, and deletion options.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zouzixuan/skills/lottotool-lottery-activity)
- [LottoTool Website](https://52choujiang.cn)
- [配置结构](artifact/references/config-schema.md)
- [自然语言示例](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown responses with concise lists, JSON configuration snippets, and optional connector installation instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Markdown image output for a returned mini-program QR code; write actions require successful preview and explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
