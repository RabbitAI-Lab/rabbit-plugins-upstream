## Description:

亚马逊行业对标 Skill helps Amazon sellers compare an ASIN's category star-rating and negative-review-rate position, with paid access to category leaderboards for product selection and competitive positioning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to inspect review-based category benchmarks for an ASIN, compare star-rating and negative-review-rate position, and request leaderboard or broader ARI review workflows when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found that the skill goes beyond category benchmarking into paid analysis, account settings, monitoring, alerts, and local exports.

Mitigation: Install only when broad ARI Amazon review and operations assistance is intended; constrain prompts to benchmark and leaderboard tasks when narrower behavior is desired.

Risk: Paid collection, analysis, leaderboard, monitoring, and advice workflows can consume account credits or change ongoing account behavior.

Mitigation: Turn autoconfirm off or ask for quotes only before paid actions, and review costs, schedules, competitor bindings, and watch changes before approving them.

Risk: Local exports can write report or review files to user-selected paths.

Mitigation: Avoid arbitrary export paths and review the destination before approving export commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/industry-benchmark)
- [User guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Natural-language guidance and Markdown summaries with optional shell commands and report/export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use ARI account authorization, existing review data, paid analysis, leaderboard, monitoring, alert, and export workflows depending on the user's request and confirmation settings.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
