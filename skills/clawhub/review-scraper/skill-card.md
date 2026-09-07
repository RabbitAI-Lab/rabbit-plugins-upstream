## Description:

Collects, analyzes, monitors, and exports Amazon review data by ASIN across eight Amazon marketplaces through ARI, with quote and confirmation handling for paid workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and analysts use this skill to collect Amazon reviews, inspect review trends and pain points, compare competitors, create reports, monitor subscribed products, and export review or report files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eligible paid ARI workflows can consume account credits under auto-confirm rules without a fresh confirmation prompt.

Mitigation: Before use, configure the account to require confirmation for every credit deduction or explicitly ask for quote-only behavior when evaluating cost.

Risk: The skill can persistently change ARI account confirmation settings when asked to adjust auto-confirm thresholds.

Mitigation: Only change confirmation settings after an explicit user request, and verify the resulting rule with the user.

Risk: The skill saves and uses a local ARI API key for authenticated requests.

Mitigation: Use browser authorization or a local environment variable, avoid sharing API keys in chat, and rotate the key if exposure is suspected.

Risk: Review analysis may be incomplete when sample size, marketplace coverage, variant coverage, or time window is limited.

Mitigation: Present sample scope with conclusions and avoid treating missing or old review data as current trends.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/review-scraper)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown, JSON summaries, shell commands, CSV exports, and Markdown or HTML report exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection and analysis workflows may consume account credits under ARI confirmation or auto-confirm rules.]

## Skill Version(s):

1.4.7 (source: server release, skill frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
