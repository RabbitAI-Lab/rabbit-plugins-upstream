## Description:

This skill helps Amazon sellers analyze collected review text to identify frequent terms, co-occurring phrases, positive and negative customer wording, and keyword ideas for listings and ads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators and agents use this skill to query ARI review data, generate keyword and VOC-style review analyses, compare customer language across ratings or competitors, and export reports for listing, advertising, and product-improvement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger paid ARI review-analysis or collection workflows that consume account credits.

Mitigation: Configure the account to ask before every paid action when explicit approval is required, use quote-only requests when evaluating costs, and review credit totals before confirming paid runs.

Risk: The skill can change future approval behavior through autoconfirm settings.

Mitigation: Avoid broad autoconfirm thresholds unless intended; use the ask-before-every-paid-action setting for tighter control.

Risk: The skill can enable recurring monitoring or scheduled collection that may create future costs.

Mitigation: Treat schedule changes as account-management actions, confirm the cadence and cost before enabling them, and periodically review active monitoring.

Risk: The skill requires an ARI account key and has broader review-analysis capabilities than the keyword-focused name suggests.

Mitigation: Install only for accounts where ARI access is acceptable, keep the key out of chat transcripts and reports, and limit use to intended Amazon review-analysis workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-keywords)
- [ARI API Reference](references/reference.md)
- [Usage Guide](使用说明.md)
- [README](README.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and concise text responses, with shell commands or links when setup, troubleshooting, export, or report retrieval requires them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI review data; paid operations may consume account credits under server-side confirmation rules.]

## Skill Version(s):

1.4.8 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
