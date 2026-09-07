## Description:

跨境电商评论分析 Skill supports review collection, VOC reports, topic summaries, competitor comparison, and localization guidance across eight Amazon marketplaces, and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce operators use this skill to analyze marketplace reviews, compare consumer feedback across regions, and decide where product, listing, monitoring, or localization changes are warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits or change future confirmation behavior through agent-assisted workflows.

Mitigation: Use quote and balance checks, honor confirmationRequired responses, consider setting autoconfirm off, and confirm costs before schedules, watches, leaderboards, reports, or paid analyses.

Risk: ARI API keys are stored locally or supplied through ARI_API_KEY and could be exposed if copied into chat, reports, examples, or shared files.

Mitigation: Use browser authorization when possible, do not paste keys into conversation or generated reports, keep local configuration private, and rotate or revoke keys if exposure is suspected.

Risk: A custom ARI_BASE_URL could redirect requests carrying credentials to an unintended host.

Mitigation: Use the default ARI service unless the user explicitly trusts the target environment, and require ARI_ALLOW_CUSTOM_BASE=1 before custom endpoints are used.

Risk: Review samples, marketplace coverage, variants, and time windows may be incomplete, which can make trend or localization conclusions misleading.

Mitigation: Report the actual sample range and collection window, distinguish direct data from inference, and avoid drawing firm conclusions from small samples or unsupported variant coverage.

Risk: Interrupted paid collection or analysis may already have charged credits and produced a report.

Mitigation: Check existing reports or task status before retrying any paid operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/cross-border)
- [Usage guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown analysis with JSON command results and optional local CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state sample scope, time window, costs or credits used, and report links when returned.]

## Skill Version(s):

1.4.7 (source: frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
