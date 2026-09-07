## Description:

Generates Amazon review analysis reports for ARI users, including VOC summaries, pain points, trends, competitor comparisons, exports, and archived report links from collected review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to ask an AI agent for ASIN review analysis, VOC reports, competitor comparisons, and listing improvement guidance based on ARI-collected review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can generate paid ARI reports under account auto-confirm rules.

Mitigation: Set ARI auto-confirm off or explicitly ask for quote-only behavior when checking costs, and review credit usage before confirming paid actions.

Risk: The skill can change future confirmation or monitoring settings that may affect later costs.

Mitigation: Review scheduled collection, watch, and auto-confirm settings after setup and require explicit confirmation before changing recurring behavior.

Risk: The skill requires access to an ARI account through an API key or browser authorization.

Mitigation: Use the documented browser authorization flow or local secret entry, and do not paste API keys into chat or report output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-report)
- [ARI CLI and API reference](references/reference.md)
- [User guide](使用说明.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with occasional shell commands, links, and structured report details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include online report links, export guidance, data-scope notes, credit usage, and account-state dependent confirmation prompts.]

## Skill Version(s):

1.4.7 (source: release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
