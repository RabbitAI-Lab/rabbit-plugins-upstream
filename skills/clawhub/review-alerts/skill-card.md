## Description:

订阅 Amazon ASIN 后，该 skill 帮助用户监控差评突增和星级下滑，读取未读预警，并基于已采集评论生成根因分析、回复建议和经营报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to monitor review sentiment, identify negative-review spikes, inspect severe reviews, compare competitors, and turn collected review evidence into product, listing, keyword, and customer-response guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits through review collection, VOC analysis, competitive analysis, leaderboard requests, operations reports, or reply-advice generation.

Mitigation: Review quotes before paid actions, use "only quote, do not execute" when pricing is the goal, and set autoconfirm off if every credit-spending action should require confirmation.

Risk: The skill can persist future account behavior by changing auto-confirm settings or monitoring schedules.

Mitigation: Confirm requests that alter auto-confirm thresholds, schedules, competitors, exports, watch state, or workbench status before execution.

Risk: The skill requires an ARI API key and uses it to access review data and account actions.

Mitigation: Authorize only through the browser-based ARI flow or local hidden input, avoid pasting API keys into chat, and install only if granting this access is acceptable.

Risk: Review analysis can be misleading when samples are small, old, incomplete, or not representative of all variants.

Mitigation: Report sample size, date range, site, and data limitations; avoid presenting missing data, old reviews, or newly imported historical reviews as current trends.

## Reference(s):

- [ARI CLI 与 API 参考](references/reference.md)
- [使用说明](使用说明.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-alerts)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and links; some CLI paths return JSON or local export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grounded in ARI-collected Amazon review data and may include report URLs, CSV/Markdown/HTML exports, sample-size caveats, credit usage, and account-action status.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
