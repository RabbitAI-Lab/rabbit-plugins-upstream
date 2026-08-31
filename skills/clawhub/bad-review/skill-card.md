## Description:

采集并分析指定 Amazon ASIN 的评论，重点拆解 1-3 星负面反馈的根因、趋势和可执行的产品与 Listing 改进建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to inspect negative review patterns, identify product, logistics, description, and usability issues, and turn review evidence into product and Listing improvements. The skill can also support recurring monitoring, exported reports, and competitor comparison when the user has an ARI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has authority beyond one-off negative review analysis, including paid workflows, exports, recurring monitoring, schedule changes, competitor binding, and watch management.

Mitigation: Before allowing writes or paid execution, confirm the exact ASIN, site, cost, report or export destination, and whether any schedule, competitor binding, or watch will keep running after the current task.

Risk: Interrupted paid workflows may already have charged credits and archived a report.

Mitigation: Check the relevant reports or operation status before retrying a confirmed paid command, and only rerun when no completed result exists.

Risk: ARI account credentials could be exposed through reports, command examples, or an unintended custom API host.

Mitigation: Keep API keys in the ARI user config or environment only, never include them in output, and use a custom ARI base URL only when the user has explicitly confirmed it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bad-review)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured JSON responses, CSV exports, HTML report exports, and CLI command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection, AI analysis, leaderboard, and advice workflows require explicit user confirmation before execution.]

## Skill Version(s):

1.4.3 (source: server release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
