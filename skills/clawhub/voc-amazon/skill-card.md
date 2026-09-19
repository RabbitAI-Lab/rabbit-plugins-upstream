## Description:

VOC洞察Amazon helps agents use ARI to collect and analyze Amazon reviews, produce VOC and deep-dive reports, identify pain points, purchase motivations, personas, trends, competitor comparisons, alerts, and exportable review or report files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as Amazon sellers and operators use this skill to ask natural-language questions about ASIN reviews, generate VOC and deep-dive reports, compare competitors, monitor changes, handle negative-review workflows, and export review or report data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits for collection, VOC analysis, leaderboard, operations, and advice workflows, and some flows may execute under account auto-confirm rules.

Mitigation: Install only if the user trusts ARI with the relevant review data and credits; set the account to ask before every paid action for strict control and use quote-only requests when pricing is needed without execution.

Risk: Weekly or daily collection, competitor tracking, watches, and auto-confirm settings can persist after the chat.

Mitigation: Confirm the intended ASIN, schedule, cost, and account setting before enabling them, and review or disable schedules, watches, competitors, or auto-confirm limits when ongoing collection is no longer wanted.

Risk: The skill handles ARI API credentials and Amazon review data through the ARI service.

Mitigation: Use the browser authorization flow or ARI_API_KEY configuration only, do not paste secrets into reports or chat output, and revoke or recreate keys from the ARI account page if access should be removed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/voc-amazon)
- [Usage guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Natural-language answers and Markdown reports, with JSON, CSV, Markdown, HTML files, or shell commands when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some collection, analysis, leaderboard, operations, and advice actions may spend ARI account credits under explicit confirmation or account auto-confirm rules.]

## Skill Version(s):

1.4.13 (source: server evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
