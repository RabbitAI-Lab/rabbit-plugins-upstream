## Description:

VOC洞察 analyzes Amazon reviews through ARI to extract customer personas, purchase motivations, use cases, sentiment, unmet needs, and actionable Listing copy and product improvement suggestions; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to turn Amazon review data into concise VOC reports, trend summaries, competitor comparisons, Listing optimization guidance, and product improvement priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Natural-language analysis requests can spend ARI credits, including through account-level auto-confirm rules.

Mitigation: Use quote-only wording when exploring costs, report credit use when ARI returns it, and set the account to ask before paid actions when the user wants explicit confirmation.

Risk: The skill uses a locally saved ARI API key and sends Amazon review data to ARI.

Mitigation: Install only if the user trusts ARI with the review data, do not paste API keys into chat or reports, and keep requests on the official ARI endpoint unless a custom environment is explicitly intended.

Risk: Recurring schedules, watches, competitor tracking, and autoconfirm settings can create ongoing account effects.

Mitigation: Review current settings before changing them and require clear user consent before enabling monitoring, competitor tracking, or broader auto-confirm thresholds.

## Reference(s):

- [使用说明](使用说明.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI online reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports and concise text summaries with optional shell commands and local export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, CSV/Markdown/HTML export paths, account credit usage, and sample-window notes when returned by ARI.]

## Skill Version(s):

1.4.7 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
