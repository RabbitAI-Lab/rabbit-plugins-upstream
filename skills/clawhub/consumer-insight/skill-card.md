## Description:

Generates ARI-based consumer insight reports for Amazon ASINs, covering customer profiles, purchase drivers, use cases, pain points, unmet needs, competitive alternatives, improvement opportunities, and review-backed evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace users and product operators use this skill to ask natural-language questions about Amazon ASIN reviews and receive consumer research reports, issue summaries, trend and competitive views, monitoring guidance, and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run paid ARI collection or analysis flows, and some flows may execute under account auto-confirm rules.

Mitigation: Ask for quotes before paid work, consider setting autoconfirm off, and verify credit use before confirming paid tasks.

Risk: The skill can manage ARI monitoring, competitors, watches, exports, workbench state, and alert state.

Mitigation: Manually verify any request to enable schedules, add competitors, create watches, export files, or change review or alert state.

Risk: Reports are based on ARI-collected Amazon review samples and may not cover every Amazon review or product variant.

Mitigation: Keep sample size, date range, and variant limits visible, and avoid treating small samples as definitive trend evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/consumer-insight)
- [ARI CLI and API reference](references/reference.md)
- [Usage guide](使用说明.md)
- [README](README.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports and summaries, JSON command responses, CSV/Markdown/HTML exports, and shell command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some collection and analysis workflows may consume ARI credits, and reports depend on ARI-collected Amazon review samples.]

## Skill Version(s):

1.4.13 (source: SKILL.md frontmatter, _meta.json, CHANGELOG.md, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
