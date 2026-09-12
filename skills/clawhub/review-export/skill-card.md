## Description:

Exports Amazon reviews for a target ASIN to CSV and helps produce review-analysis reports that can be saved as Markdown or HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to export collected review data, summarize customer pain points and trends, compare competitors, and turn review evidence into listing or product-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid analysis can execute and consume credits when account auto-confirm rules apply.

Mitigation: Set autoconfirm to off before exploratory use, ask for quote-only runs when checking costs, and approve paid actions only after reviewing the quoted credits and balance.

Risk: The skill can change persistent account workflows such as schedules, watches, competitors, or billing-confirmation settings.

Mitigation: Review each proposed schedule, watch, competitor, or confirmation-setting change before allowing the skill to execute it.

Risk: Use requires trusting ARI with an account API key and Amazon review data.

Mitigation: Install only if ARI is an acceptable service provider for the account and review data; use browser authorization or local configuration without placing API keys in chat transcripts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-export)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, CSV files, HTML files, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with optional CSV, Markdown, and HTML export files; setup and troubleshooting commands may be shown when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and depends on ARI-collected Amazon review data, account entitlements, and user confirmation settings.]

## Skill Version(s):

1.4.8 (source: frontmatter, changelog, release evidence, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
