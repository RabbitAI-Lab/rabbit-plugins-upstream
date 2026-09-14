## Description:

Analyzes Amazon ASIN star-rating distribution, review trends, negative-review timing, keywords, and related ARI reports to help diagnose rating declines and product issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and agents use this skill to inspect star-rating structure, review themes, trends, competitor signals, alerts, reports, exports, and monitoring for ASIN-level product decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits for collection, analysis, leaderboard, and advice workflows.

Mitigation: Use quote or preview flows for pricing, require explicit confirmation for paid commands when prompted, and set autoconfirm to always ask when per-charge approval is desired.

Risk: The skill needs an ARI API key and can manage ARI review collection, reports, monitoring, alerts, and related account settings.

Mitigation: Authorize through the ARI browser flow or local configuration only, avoid sharing API keys in chat or reports, and perform account-setting changes only after an explicit user request.

Risk: Export workflows can write report or review files to local paths.

Mitigation: Export only to deliberate project or export directories, avoid broad directories such as the home folder, and avoid exporting over existing files unless replacement is intended.

Risk: Review and trend conclusions depend on the ARI-collected sample and may not cover all Amazon reviews or variants.

Mitigation: State the sample size, collection window, site, and known scope limits in outputs, and treat small samples or short windows as directional evidence.

Risk: Monitoring and schedule changes can create ongoing collection behavior and future costs.

Mitigation: Explain the schedule and cost implications before enabling monitoring or scheduled collection, and execute changes only after the user confirms the specific ASIN and cadence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/rating-analysis)
- [ARI CLI and API reference](references/reference.md)
- [ARI Amazon review assistant user guide](使用说明.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis, JSON command responses, and inline shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include report links, exported CSV or Markdown/HTML files, credit usage, sample scope, and warnings when data is insufficient.]

## Skill Version(s):

1.4.11 (source: server release evidence, frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
