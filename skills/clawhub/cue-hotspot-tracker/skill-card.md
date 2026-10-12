## Description:

用 Cue 扫描 A 股盘中热点与近 24 小时的催化资讯，梳理催化逻辑、受益板块和资金动向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

短线交易者使用此技能追踪 A 股盘中热点、近 24 小时催化消息及可能受影响的板块，作为进一步核实市场信息的参考。

### Deployment Geography for Use:

China (A-share market)

## Known Risks and Mitigations:

Risk: The skill installs and runs unpinned third-party runner code that reads a local Cue API key.

Mitigation: Review or pin the runner before installation, and use it only if you trust its publisher and Cue.

Risk: The runner sends requests to Cue and saves reports locally; scheduled scans repeat this activity.

Mitigation: Protect the API key and local reports, and enable scheduled scans only with the user's explicit consent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-hotspot-tracker)
- [Cue platform](https://cuecue.cn)
- [Cue runner repository (listed in skill instructions; not verified release provenance)](https://github.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-hotspot-tracker)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown report with source links and a link to the original Cue report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers intraday hotspots, catalysts, affected sectors and capital-flow observations; can save a local Markdown copy.]

## Skill Version(s):

1.0.9 (source: server-resolved release; skill frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
