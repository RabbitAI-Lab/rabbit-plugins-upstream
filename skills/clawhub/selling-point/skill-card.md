## Description:

This skill helps Amazon operators analyze ARI-collected review data to identify positive-review selling points, purchase drivers, customer language, trends, competitor differences, and listing improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and ecommerce teams use this skill to turn review evidence into selling-point, purchase-motivation, keyword, competitor, and listing guidance for ASIN-level product decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through review collection, VOC, analysis, advice, leaderboard, and operations workflows.

Mitigation: Use quote-only behavior or set autoconfirm off when costs should always be approved before execution; review confirmation status and credit use in returned results.

Risk: The skill can change monitoring and watch settings for account-owned products.

Mitigation: Confirm the ASIN, schedule, watch ID, and expected ongoing collection cost before creating, changing, resuming, pausing, or deleting monitoring.

Risk: The skill uses an ARI API key and can send requests to a custom ARI endpoint if custom environment variables are deliberately enabled.

Mitigation: Use browser authorization or local configuration for the API key, do not paste keys into chat, and leave custom ARI endpoint variables unset unless the endpoint is controlled by the user.

Risk: Export commands can write CSV, Markdown, or HTML files locally and may overwrite paths chosen for output.

Mitigation: Review export destinations and file names before running export commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/selling-point)
- [README](artifact/README.md)
- [使用说明](artifact/使用说明.md)
- [ARI CLI 与 API 参考](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown analysis reports, JSON command responses, shell command suggestions, configuration guidance, and optional CSV/Markdown/HTML export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key for account-specific data and may include report URLs, usage details, and credit or confirmation status.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, _meta.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
