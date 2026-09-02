## Description:

Generates Amazon review consumer insight reports covering buyer personas, purchase motivations, use cases, pain points, unmet needs, competitive substitutions, and improvement opportunities, with conclusions traced to review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product teams, and market researchers use this skill to collect and analyze Amazon ASIN reviews, generate VOC and consumer insight reports, compare competitors, monitor review trends, and export review or report data for product and listing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI API key for account access.

Mitigation: Use the browser setup flow or ARI_API_KEY, keep the key out of reports and public examples, and avoid storing it in synced or shared folders.

Risk: Some commands can consume paid credits or create ongoing account-side monitoring and future collection costs.

Mitigation: Review the quote or cost note first, and run paid or persistent actions only after the user explicitly confirms the exact command.

Risk: Retrying an interrupted paid command may duplicate charges if the service already generated or archived a report.

Mitigation: Check the latest report or operation status before rerunning a confirmed paid command.

Risk: Consumer insight reports can overstate weak or incomplete review samples.

Mitigation: Label small samples, distinguish direct data from interpretation and recommendations, and use only successfully returned API data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/consumer-insight)
- [ARI CLI and API reference](references/reference.md)
- [ARI API key settings](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and CLI guidance, with JSON, CSV, Markdown, and HTML outputs available through ARI commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid analysis, collection, leaderboard, or advice commands.]

## Skill Version(s):

1.4.3 (source: server release, skill frontmatter, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
