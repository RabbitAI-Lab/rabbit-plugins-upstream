## Description:

Amazon-VOC helps agents collect Amazon reviews through ARI and produce voice-of-customer reports covering pain points, purchase drivers, user profiles, usage scenarios, competitor comparisons, trends, and listing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to connect an ARI account, gather Amazon review data for specific ASINs, and turn that data into VOC, deep-dive, trend, variant, competitor, benchmark, alert, and workbench outputs. The skill is intended for product and listing decisions where paid account actions are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an ARI account and API key to agent-run review analysis workflows.

Mitigation: Install only when that account connection is acceptable, keep the API key out of reports and prompts, and use the documented setup or local configuration paths.

Risk: Some collection, analysis, leaderboard, operations, advice, and recurring monitoring actions can affect credits, billing, or account state.

Mitigation: Review quotes and account effects first, add --confirm only after explicit user approval, and be deliberate before enabling recurring monitoring or changing workbench/watch state.

Risk: Exports can write review or report data to local paths that may already exist or contain sensitive locations.

Mitigation: Choose export paths carefully and avoid using export --out with sensitive or existing file paths.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [Amazon-VOC README](artifact/README.md)
- [ARI API Key](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Products](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown and text guidance with shell commands; CLI responses may include JSON, CSV, Markdown, HTML, report URLs, and local export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid analysis, collection, leaderboard, operations, and advice actions require explicit confirmation before execution.]

## Skill Version(s):

1.4.3 (source: server release metadata, artifact frontmatter, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
