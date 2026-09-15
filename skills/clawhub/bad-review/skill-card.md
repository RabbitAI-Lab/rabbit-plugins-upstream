## Description:

Analyzes Amazon 1-3 star review feedback for a target ASIN to identify recurring root causes such as product quality, shipping damage, listing mismatch, usage confusion, return drivers, and trend changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to review Amazon ASIN feedback, summarize negative-review drivers, inspect supporting review evidence, and produce practical product, logistics, and listing-copy recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can call ARI on the user's behalf, including flows where ARI auto-confirm rules may spend account credits.

Mitigation: Install only if comfortable granting ARI access, review billing and auto-confirm settings, and ask the agent to quote only or request confirmation before paid actions when cost control matters.

## Reference(s):

- [README](artifact/README.md)
- [User Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with optional ARI report links, CSV exports, and HTML or Markdown report exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid ARI operations may consume account credits under server-side confirmation rules.]

## Skill Version(s):

1.4.11 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
