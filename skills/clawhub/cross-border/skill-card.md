## Description:

Analyzes ARI-collected Amazon reviews across eight marketplaces to compare customer complaints, trends, VOC signals, competitors, and localization opportunities for cross-border e-commerce operators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agents use this skill to review Amazon customer feedback, compare marketplace-specific issues, generate VOC and operational reports, and decide where product or listing localization may be needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access an ARI account and review data after authorization.

Mitigation: Install only when comfortable granting that access, authorize through the ARI browser flow, and avoid putting API keys in chat or reports.

Risk: Some ARI analysis flows can spend credits or proceed under server auto-confirm rules without a fresh per-action confirmation.

Mitigation: Before paid analysis, ask for quote-only behavior or ask to confirm before every charge, then review the quoted cost and balance before approving execution.

Risk: Monitoring schedules can create future review collection costs.

Mitigation: Review schedule settings, cadence, and returned cost notes before enabling or changing monitoring.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/cross-border)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Report Center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown reports with occasional shell commands or JSON-derived summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, CSV or Markdown/HTML export guidance, and cost or confirmation details returned by ARI.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, server release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
