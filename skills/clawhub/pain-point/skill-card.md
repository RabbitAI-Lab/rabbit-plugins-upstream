## Description:

从 Amazon 评论中提炼买家痛点、未满足需求和产品改进机会，并用原评论佐证结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to analyze ASIN reviews, identify recurring customer pain points, compare competitors, and turn review evidence into product, listing, monitoring, and response actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing-aware workflows can spend ARI credits, including through account auto-confirm rules.

Mitigation: Use quote-only mode or require confirmation before each credit deduction, and review cost prompts before paid analysis runs.

Risk: Autoconfirm, weekly monitoring, competitor tracking, exports, and alert status changes can alter account behavior or ongoing costs.

Mitigation: Require explicit user approval before enabling or changing these settings, and verify the current account status before making changes.

Risk: The skill links a local agent workflow to an ARI account through an API key.

Mitigation: Use browser authorization or local key configuration, and do not paste API keys into chats, reports, or command examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/pain-point)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI usage guide](artifact/使用说明.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and guidance with CLI commands and JSON-backed API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid workflows can spend credits under account confirmation rules; exports and monitoring depend on account plan and user approval.]

## Skill Version(s):

1.4.7 (source: server release metadata, frontmatter, changelog, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
