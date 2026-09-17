## Description:

抖音数据助手 helps agents retrieve and analyze public Douyin search results, hotlist topics, creator posts, and video comments through Node.js command-line tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content operators, analysts, and agents use this skill to collect public Douyin data for short-video topic research, competitor monitoring, trend tracking, comment analysis, and structured reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a GUAIKEI_API_TOKEN and evidence.security reports insecure token handling.

Mitigation: Use a dedicated, revocable token with limited quota, avoid exposing terminal sessions or logs, and rotate the token after shared or high-risk use.

Risk: Keywords, creator URLs, video IDs, and target links may be sent to guaikei.com for API-backed retrieval.

Mitigation: Review data-sharing expectations before use and avoid submitting confidential campaign terms, private URLs, or sensitive investigation targets.

Risk: Collected public social data may be stored locally in generated logs.

Mitigation: Run the skill in a controlled workspace, remove generated logs after analysis, and avoid shared, backed-up, or CI environments when local retention is not acceptable.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-data-assistant)
- [抖音数据获取官网](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-data-assistant)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and JSON command output from the skill tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command output is structured JSON on stdout; logs and status messages are separated on stderr.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
