## Description:

VOC洞察 uses ARI to analyze Amazon reviews and produce customer voice insights, including personas, purchase motivations, usage scenarios, sentiment, unmet needs, Listing copy suggestions, and product improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and supporting agents use this skill to turn collected review data into concise customer insights, trend summaries, competitive comparisons, Listing optimization guidance, and product improvement priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid credit-consuming ARI actions may run without fresh per-run approval when account auto-confirm rules apply.

Mitigation: Set the account to ask before every paid action when needed, use "only quote, do not execute" while exploring costs, and review quoted credits before confirmed runs.

Risk: The skill uses an ARI API key and sends Amazon review data to ARI services.

Mitigation: Install only if the user trusts ARI with that data, use browser authorization or local configuration, and avoid pasting API keys into chat or reports.

Risk: Schedule, watch, competitor, and autoconfirm changes can persist beyond one chat session.

Mitigation: Confirm these account-level changes explicitly, summarize the active setting after changes, and review ongoing collection costs before enabling monitoring.

Risk: Export features can write review CSV files or report files to local paths.

Mitigation: Confirm export intent and destination before using exports, especially when reports or review data may contain commercially sensitive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/voc-insight)
- [README](README.md)
- [Usage guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text summaries, with occasional shell commands and JSON-derived status details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, credit usage, sample windows, CSV/Markdown/HTML export paths, and account confirmation status when returned by ARI.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
