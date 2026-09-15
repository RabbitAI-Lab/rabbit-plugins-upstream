## Description:

Helps Amazon sellers validate pre-launch product ideas by using ARI to analyze comparable Amazon reviews for demand signals, pain points, trends, competitor gaps, listing improvements, monitoring, alerts, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to validate new product ideas before launch by analyzing reviews for buyer complaints, purchase motivations, market gaps, competitor weaknesses, and listing or product improvement opportunities. It can also help inspect existing ARI data, generate review-analysis reports, manage monitoring workflows, and export reviewed data when account permissions allow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits for review collection, VOC reports, analysis, leaderboard queries, or advice workflows under ARI confirmation and auto-confirm rules.

Mitigation: Use quote-only language for price checks, keep auto-confirm disabled or limited when desired, and review balance and cost before approving paid actions.

Risk: The skill requires an ARI API key and uses it to access ARI account data and services.

Mitigation: Use the browser authorization flow or local configuration, avoid pasting API keys into chat or generated reports, and rotate the key if exposure is suspected.

Risk: Some operations can persist account state, including schedules, watches, competitor bindings, workbench status, alerts, and future spending-confirmation settings.

Mitigation: Approve persistent changes explicitly and review the resulting schedules, watches, workbench state, and confirmation settings after changes.

Risk: A paid operation that is interrupted may already have generated a report or charged credits.

Mitigation: Check report history or operation status before retrying any confirmed paid operation.

## Reference(s):

- [Skill Listing](https://clawhub.ai/funewa/skills/new-product)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [README](README.md)
- [User Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Account and Authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown, with CLI command snippets, JSON summaries from ARI, and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid analysis and some account actions depend on ARI account balance, permissions, and confirmation rules.]

## Skill Version(s):

1.4.11 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
