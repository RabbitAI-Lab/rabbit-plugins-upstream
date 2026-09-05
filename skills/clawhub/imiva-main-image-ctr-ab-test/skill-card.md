## Description:

帮助品牌商家、电商运营、设计与内容团队通过 IMIVA MCP 生成商品主图、卖点图和场景图变体，用于主图点击率 A/B 测试，并支持预算确认、任务追踪和结果交付。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

品牌商家、电商运营、设计与内容团队使用该 skill 将商品素材、卖点、渠道和规格整理为 IMIVA MCP 任务，生成用于主图点击率 A/B 测试的电商图片变体。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to IMIVA for ecommerce media generation and exposes broader paid MCP actions and environment access than the main-image A/B testing purpose clearly scopes.

Mitigation: Use a dedicated IMIVA token, run it from an environment without unrelated secrets, confirm credit costs before creating tasks, and limit use to the intended IMIVA tools.

Risk: Generated commercial product media can include inaccurate product facts, claims, prices, certifications, or unlicensed reference elements.

Mitigation: Verify product facts, claims, pricing, certifications, likeness rights, copyright status, and platform rules before publishing; use only authorized references.

Risk: Paid media-generation tasks may be duplicated if failures or timeouts are retried without checking the original task.

Mitigation: Save the task ID, query the original task before retrying, and use budget or idempotency controls where the active IMIVA tools support them.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/imiva-main-image-ctr-ab-test)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP tool calls that create paid media-generation tasks after user confirmation.]

## Skill Version(s):

1.0.0 (source: target metadata, release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
