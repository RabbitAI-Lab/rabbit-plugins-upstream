## Description:

结合商品详情与评论证据，检查 Amazon Listing 在移动端的阅读顺序、信息密度和理解阻碍；仅用于移动端表达诊断，不用于广告、库存或自动发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to evaluate mobile Listing readability and information priority from ARI product detail and review evidence, then receive optimization guidance. It is suited for mobile expression diagnosis, not advertising, inventory, order analysis, or automatic Amazon page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through paid analysis or collection workflows, and some flows may run under account auto-confirm rules.

Mitigation: Use quote-only flows for pricing checks, set auto-confirm to ask every time when explicit approval is required, and confirm paid tasks before execution.

Risk: The skill requires ARI account access and stores an ARI API key locally or reads it from ARI_API_KEY.

Mitigation: Use the documented browser authorization or environment variable path, never paste keys into chat or reports, and revoke or recreate a key if it is exposed.

Risk: Exports can write report or review files to local paths selected by the user.

Mitigation: Choose non-sensitive output locations and avoid --out paths that point to existing or sensitive files.

Risk: Persistent account settings such as auto-confirm, schedules, monitoring, or competitor bindings can affect future behavior and costs.

Mitigation: Change persistent settings only after explicit user instruction, state the current rule or cost impact, and use manual/off settings when ongoing automation is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/mobile-listing)
- [ARI CLI 与 API 参考](references/reference.md)
- [专属运营工作流](references/operation-workflow.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text guidance, with JSON or shell-command output for advanced CLI workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, saved file paths, credit usage, request IDs, and ARI account status.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
