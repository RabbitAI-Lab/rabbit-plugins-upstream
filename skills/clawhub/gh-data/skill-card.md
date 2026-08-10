## Description:

股海罗盘 analyzes A-share stock data with historical signal backtesting, pattern mining, ETF fund-flow context, broker research cross-checks, and optional DOCX report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunbinpy](https://clawhub.ai/user/sunbinpy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to gather A-share public market data, request quantitative signal and historical-statistics summaries, review supporting fund-flow and research context, and generate reports. Outputs are informational and should be reviewed as data analysis, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and stores a local API key in plaintext.

Mitigation: Use only in environments where this local key storage is acceptable, protect the home directory, and rotate or remove the key if it may have been exposed.

Risk: The skill can place the API key in purchase links and logs.

Mitigation: Avoid sharing generated links or logs that contain the key, and prefer a publisher update that replaces key-bearing URLs with short-lived checkout tokens.

Risk: The security evidence reports plaintext backend API traffic and hardcoded database credentials.

Mitigation: Review network exposure before deployment and prefer a publisher update that uses HTTPS and removes hardcoded credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunbinpy/skills/gh-data)
- [Publisher profile](https://clawhub.ai/user/sunbinpy)
- [Skill homepage](https://www.oraskl.com/ghdata-admin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown responses with Python code snippets and optional DOCX report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write DOCX reports and chart images to the configured document directory.]

## Skill Version(s):

2.2.48 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
