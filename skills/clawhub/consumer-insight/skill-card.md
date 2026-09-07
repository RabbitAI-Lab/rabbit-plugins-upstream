## Description:

Generates Amazon consumer insight reports covering customer profiles, purchase drivers, use cases, pain points, unmet needs, competitor comparisons, trends, and product improvement opportunities grounded in collected review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product operators, and market researchers use this skill to analyze collected Amazon reviews for consumer needs, recurring complaints, buying motivations, competitor gaps, monitoring signals, and report-ready product recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run ARI workflows that spend account credits, and some account rules may allow small paid operations to execute without a fresh confirmation.

Mitigation: Use 'only quote, do not execute' for cost checks, set autoconfirm off when every paid operation should require approval, and confirm credit estimates before paid collection or analysis.

Risk: The skill handles ARI account access and Amazon review data through a local API key.

Mitigation: Use the browser authorization flow, avoid sharing API keys in chat or reports, and install only when access to the ARI account and associated review data is acceptable.

Risk: Custom ARI endpoints can redirect requests containing credentials or review data if intentionally enabled.

Mitigation: Leave ARI_BASE_URL and ARI_ALLOW_CUSTOM_BASE unset unless using a trusted ARI-compatible endpoint that the user deliberately controls.

Risk: Repeated execution after a network interruption can duplicate paid work if the server already generated a report.

Mitigation: Check existing reports or operation status before retrying any interrupted paid command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/consumer-insight)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and Authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and conversational guidance, with occasional shell commands, links, and JSON snippets for setup, troubleshooting, and exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include data scope, cited review evidence, report URLs when returned, credit usage, and clear uncertainty notes for small samples or limited collection windows.]

## Skill Version(s):

1.4.7 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
