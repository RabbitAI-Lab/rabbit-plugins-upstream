## Description:

Combines Amazon review frequency, customer-experience impact, and product information to prioritize evidence-based product feature improvements; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and product teams use this skill to rank product improvement priorities from collected Amazon review evidence, including issue frequency, low-star impact, trends, and listing recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits for paid review collection, analysis, leaderboard queries, and advice generation.

Mitigation: Use quote-first flows and keep per-charge approval enabled unless the user intentionally configures an auto-confirm threshold.

Risk: The skill can change account confirmation rules or enable recurring monitoring that may create future collection costs.

Mitigation: Treat auto-confirm, monitoring, competitor tracking, export, and account-confirmation changes as account-changing actions that require explicit user approval.

Risk: The skill requires an ARI API key and can access account review and report data.

Mitigation: Use browser authorization or local key configuration, do not paste keys into reports or prompts, and avoid custom ARI_BASE_URL values unless the user controls the HTTPS endpoint.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/feature-priority)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Dedicated product-priority operations workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with optional ARI CLI command output, report links, CSV exports, or HTML/Markdown report exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish observed review data from inferred recommendations and include data scope, sample limits, credit usage, and report links when available.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, scripts/ari.py, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
