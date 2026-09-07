## Description:

采集指定 Amazon ASIN 的评论并导出 CSV，同时生成可导出为 Markdown 或 HTML 的 AI 评论分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators and ecommerce analysts use this skill to collect Amazon review data for an ASIN, export review CSV files, and turn existing review samples into concise operational reports. It also supports review monitoring, competitor comparisons, alerts, and report exports when the user's ARI account and plan allow them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run paid collection, analysis, leaderboard, and advice actions, and some account rules may allow small paid actions to proceed without another prompt.

Mitigation: Review quotes and current autoconfirm settings before paid work; set autoconfirm off when every paid action should require approval.

Risk: Monitoring, schedule, competitor, and account-setting changes can affect future collection behavior and costs.

Mitigation: Confirm the ASIN, site, schedule, competitor relationship, and stated cost before approving management changes.

Risk: A custom ARI_BASE_URL could direct authenticated requests away from the official ARI service.

Mitigation: Use the default ARI endpoint unless the user controls the HTTPS endpoint and intentionally sets ARI_ALLOW_CUSTOM_BASE=1.

Risk: Retrying interrupted paid operations can duplicate work or charges if the service already generated and archived the result.

Mitigation: Check reports or operation status before re-running a paid command after NETWORK_ERROR, WAIT_TIMEOUT, or ARI_STREAM_INTERRUPTED.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-export)
- [README](README.md)
- [Usage guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON responses, CSV files, and Markdown or HTML report exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid analysis, collection, monitoring, and exports depend on account balance, confirmation settings, and plan entitlements.]

## Skill Version(s):

1.4.7 (source: server release evidence, artifact frontmatter, _meta.json, CHANGELOG, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
