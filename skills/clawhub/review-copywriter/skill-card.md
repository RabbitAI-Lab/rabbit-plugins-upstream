## Description:

将 Amazon 评论中的购买动因、疑问和体验语言整理为 Listing 优化方向与证据清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and ecommerce teams use this skill to turn collected Amazon reviews for a product into evidence-backed Listing copy planning, issue prioritization, and improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits when paid analysis, collection, leaderboard, or advice commands are confirmed or auto-confirmed.

Mitigation: Use quote-only wording for cost checks, set autoconfirm off when explicit approval is required, and review returned credit costs before confirming paid runs.

Risk: The skill can change account monitoring or confirmation settings, including schedules, watches, competitors, and auto-confirm thresholds.

Mitigation: Approve only the specific schedule, watch, competitor, or auto-confirm change requested, and verify the ASIN, site, watch ID, and cost note before execution.

Risk: The skill uses a local ARI API key and may export account review or report data.

Mitigation: Keep the API key out of chats and reports, export only to intended local paths, and install only if ARI is trusted with the relevant Amazon review and report data.

Risk: Custom ARI endpoint environment variables could redirect key-bearing requests away from the official service.

Mitigation: Leave ARI_BASE_URL and ARI_WEB_URL unset unless intentionally using a trusted self-hosted or development endpoint with the required custom-base opt-in.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/funewa/skills/review-copywriter)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Dedicated operations workflow](artifact/references/operation-workflow.md)
- [ARI account and API key page](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI products page](https://ari.funewa.com/zh/products)
- [ARI reports page](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise text guidance with optional shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and Amazon product context such as ASIN and site; paid actions follow quote, confirmation, and account auto-confirm rules.]

## Skill Version(s):

1.4.8 (source: server release metadata, SKILL.md frontmatter, CHANGELOG, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
