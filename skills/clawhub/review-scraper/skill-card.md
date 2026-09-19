## Description:

This skill helps agents collect, monitor, analyze, and export Amazon review data across eight marketplaces using ARI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to collect Amazon reviews by ASIN and marketplace, inspect trends and negative feedback, generate VOC and operations reports, manage monitoring, and export review or report files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits for collection, analysis, leaderboard, operations, and advice workflows.

Mitigation: Use quote-only flows when pricing is needed, require explicit confirmation before paid commands, and set billing confirmation to ask every time when per-action approval is required.

Risk: The skill can change future billing confirmation behavior through autoconfirm settings.

Mitigation: Treat autoconfirm changes as account-level billing preference changes and confirm the desired threshold or off setting before applying them.

Risk: The skill requires ARI API key access for authenticated workflows.

Mitigation: Use browser authorization or local configuration, avoid sharing the API key in chat or reports, and stop on authentication errors until the key is rebuilt.

Risk: Interrupted paid workflows may already have charged credits or generated reports.

Mitigation: Check existing report or operation status before retrying a paid command, and rerun only when evidence shows no completed result exists.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/review-scraper)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI products](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown and text guidance with bash commands; exported review data may be CSV, and exported reports may be Markdown or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and produces outputs based on ARI-collected Amazon review samples, account entitlements, and confirmed paid workflows.]

## Skill Version(s):

1.4.13 (source: frontmatter, changelog, release evidence, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
