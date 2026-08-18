## Description:

HuaHuaDailyMCP lets agents use HuahuaDaily MCP for authorized portfolio and transaction queries, fund and market data, strategy backtests, quant snapshots, community actions, screenshot recognition, and App-confirmed trade or import requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baiye1997](https://clawhub.ai/user/baiye1997)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query authorized HuahuaDaily portfolio, transaction, fund, market, and strategy data, and to prepare trade or import requests that require final confirmation in the HuahuaDaily App.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive financial portfolio data, including holdings, transaction history, costs, and returns.

Mitigation: Treat the HuahuaDaily Agent Token like a financial credential, limit responses to details needed for the user's request, and revoke the token when access is no longer needed.

Risk: Unpinned installation from a live branch can expose users to unreviewed changes.

Mitigation: Install from ClawHub or a pinned, reviewed release.

Risk: Trade and import workflows could be mistaken for completed writes.

Mitigation: State that trade and import requests are sent to the HuahuaDaily App and only take effect after the user confirms them there.

Risk: Community authorization, follow changes, and community return sync are direct backend write actions.

Mitigation: Ask for explicit user confirmation before calling community write tools and clearly distinguish them from App-confirmed trade or import requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baiye1997/skills/huahua-daily)
- [Artifact README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [HuahuaDaily API base](https://api.huahuadaily.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with JSON MCP tool call examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agent use of HuahuaDaily MCP tools; high-impact trade and import requests require App confirmation.]

## Skill Version(s):

3.5.4 (source: evidence release, SKILL.md frontmatter, README changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
