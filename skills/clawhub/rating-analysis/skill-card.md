## Description:

Analyzes an Amazon ASIN's star-rating structure, review trends, negative-review timing, and ARI review data to help diagnose rating declines and produce review insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to diagnose Amazon review rating structure, identify low-star review patterns, compare trends, monitor product changes, and generate ARI-backed review analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits under account auto-confirm rules.

Mitigation: Set auto-confirm off or use quote-only flows when approval is required before paid analysis.

Risk: The skill can persist account-level settings and manage review data, monitoring, exports, and related ARI workflows.

Mitigation: Review schedule, watch, competitor, export, and auto-confirm changes before approving ongoing or account-affecting actions.

Risk: The skill requires an ARI API key.

Mitigation: Use the documented ARI authorization flow or environment variable handling, avoid placing secrets in prompts or reports, and rotate the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/rating-analysis)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing and credits](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Natural-language guidance, Markdown analysis reports, shell command suggestions, and exported review/report files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI account rules for paid analysis, monitoring, and exports.]

## Skill Version(s):

1.4.13 (source: frontmatter, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
