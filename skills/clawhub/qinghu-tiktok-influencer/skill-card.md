## Description:

青虎AI TikTok 达人带货建联技能帮助代理按站点和类目筛选达人、反向查找竞品商品或店铺关联达人，并基于带货表现生成寄样和建联建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and agents use this skill to research TikTok Shop influencers, compare product and category fit, and prepare prioritized outreach or sampling lists from Qinghu data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API key and sends requests to Qinghu endpoints.

Mitigation: Install only when Qinghu API use is intended, use an appropriate Qinghu key, and confirm endpoint access before relying on results.

Risk: Qinghu requests may spend Qinghu points after user approval.

Mitigation: Ask for approval before tool calls and report actual Qinghu point consumption from the response envelope.

Risk: Larger retrieved datasets may be saved as local spreadsheet files.

Mitigation: Export only expected datasets, keep responses concise, and provide links plus short previews instead of exposing large raw tables in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-influencer)
- [Publisher profile: autoagc](https://clawhub.ai/user/autoagc)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON request examples, shell commands, and spreadsheet file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export local spreadsheet files when retrieved record arrays contain 10 or more items.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
