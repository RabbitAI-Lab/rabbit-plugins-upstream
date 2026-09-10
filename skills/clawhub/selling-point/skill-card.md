## Description:

This skill helps Amazon operators extract purchase drivers, persuasive selling points, review evidence, trends, competitor differences, and listing copy guidance from ARI-collected Amazon review data for a specified ASIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to turn customer reviews into selling-point priorities, purchase-motivation summaries, listing recommendations, and concise or full review reports. The skill can also guide related review workflows such as competitor comparison, topic inspection, alerts, exports, and ongoing monitoring when the user explicitly requests them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid review collection or AI analysis may run under account auto-confirm rules and consume credits.

Mitigation: Set the account to ask before every paid action if that is the desired posture, use quote-only flows for pricing, and require explicit confirmation when a command reports that confirmation is needed.

Risk: Monitoring, schedule, or watch requests can persist beyond a single analysis and may lead to future collection activity or costs.

Mitigation: Create, resume, pause, or delete monitoring only after the user explicitly requests the change and has been told the cadence, account limits, and cost implications.

Risk: Custom export paths can overwrite local files.

Mitigation: Prefer default export destinations or verify the target path with the user before writing exports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/selling-point)
- [Usage guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [README](artifact/README.md)
- [ARI reports](https://ari.funewa.com/zh/reports)
- [ARI products](https://ari.funewa.com/zh/products)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise text answers, Markdown reports, JSON CLI responses, and local export files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid analysis, exports, and monitoring depend on account entitlements, available review data, and user confirmation settings.]

## Skill Version(s):

1.4.8 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
