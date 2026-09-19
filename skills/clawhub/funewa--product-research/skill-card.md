## Description:

Uses ARI to help agents research Amazon product opportunities by analyzing collected reviews for recurring complaints, purchase drivers, trends, competitor gaps, and evidence-backed improvement ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, marketplace operators, and product researchers use this skill to validate product demand from review evidence, compare competitors, monitor review changes, and turn customer feedback into listing or product-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI credits may be spent when service-side auto-confirm rules allow small or preauthorized analyses to run without fresh per-operation approval.

Mitigation: Use quote-only requests for price checks, or tell the agent to set autoconfirm off before paid work.

Risk: Using the skill requires linking an ARI account and storing an ARI API key locally.

Mitigation: Install only when that account-linking model is acceptable, and avoid sharing the API key in chat or generated reports.

Risk: Interrupted paid analysis streams may already have deducted credits and created a report.

Mitigation: Check the latest saved report before retrying a paid command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/product-research)
- [ARI CLI and API reference](references/reference.md)
- [Usage guide](使用说明.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Natural-language answers and Markdown reports, with optional CSV, Markdown, or HTML exports from ARI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include data scope and caveats when sample size or review coverage is limited.]

## Skill Version(s):

1.4.13 (source: evidence.release.version, SKILL.md frontmatter, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
