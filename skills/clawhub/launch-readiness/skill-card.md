## Description:

Uses existing Amazon product detail and review evidence for an ASIN to check relaunch or listing-update readiness and surface related risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and product teams use this skill to review an existing ASIN's product details and collected reviews before a relaunch or listing update. It focuses on launch readiness, review-backed risks, and operational next steps rather than sales forecasts, ad budgets, supply-chain execution, or inventory actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use ARI account API access to run workflows that consume credits.

Mitigation: Review before installing, set the account to ask before every paid action for safer use, and say '只报价，不执行' when only pricing is desired.

Risk: The skill stores and uses a local ARI API key.

Mitigation: Use only on trusted machines and avoid pasting the key into chat, reports, or command examples.

Risk: The skill can create recurring monitoring or other persistent workflows that may lead to future costs.

Mitigation: Require explicit user confirmation for recurring monitoring and review the quoted cost before enabling it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/launch-readiness)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [Usage Guide](使用说明.md)
- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis and recommendations, with occasional shell commands or configuration steps for setup and troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an existing Amazon ASIN, sufficient review evidence, and an ARI API key; paid actions may require quote and confirmation depending on account settings.]

## Skill Version(s):

1.4.7 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
