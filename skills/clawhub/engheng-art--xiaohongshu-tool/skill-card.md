## Description:

xiaohongshu-tool helps agents search public Xiaohongshu notes, retrieve note details and comments, and collect public creator posts for content research, competitor analysis, KOL screening, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, analysts, and developers use this skill to collect authorized public Xiaohongshu data for keyword research, note and comment review, public creator monitoring, trend analysis, and competitor or KOL research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu URLs, and the GUAIKEI_API_TOKEN are sent to the Guaikei API provider during command execution.

Mitigation: Use only authorized public data, review provider terms before use, and run the skill only where token and query disclosure to the provider is acceptable.

Risk: Generated logs may contain research targets, comments, profile data, and xsec_token-bearing Xiaohongshu URLs.

Mitigation: Treat logs as sensitive, avoid shared machines unless access is controlled, and delete or secure logs after analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xiaohongshu-tool)
- [Guaikei API service](https://www.guaikei.com)
- [Options and command reference](artifact/references/options.md)
- [Release changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with shell command examples; command execution returns JSON status, request, metadata, and results objects and writes JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN. Supports keyword, content type, sort, time window, URL, and limit parameters depending on the command.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
