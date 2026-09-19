## Description:

用于快手数据分析、快手视频详情、快手作品数据、互动指标、内容调研和快手内容分析。覆盖 Kuaishou / Kwai，来自GuaiKei社媒数据助手。提供快手关键词搜索、快手博主作品获取、快手视频评论获取等功能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External content creators, marketing teams, analysts, and agents use this skill to search Kuaishou videos, retrieve public creator posts, and collect video comments for content research, competitive monitoring, KOL screening, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, target URLs, and GUAIKEI_API_TOKEN are sent to the GuaiKei API.

Mitigation: Use only when the user accepts this data transfer, scope requests to public Kuaishou data, and avoid exposing the token in prompts, logs, or shell history.

Risk: Generated logs may retain comments, author data, profile or video identifiers, and research targets.

Mitigation: Store logs in protected workspaces, avoid shared machines or CI logs for sensitive research, and delete retained result files when they are no longer needed.

Risk: The security review reports unsafe token troubleshooting guidance in the artifact.

Mitigation: Check only whether GUAIKEI_API_TOKEN is present instead of printing its value, and rotate the token if it has been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishouzhushou)
- [Server-resolved GitHub provenance](https://github.com/why20261/kuaishouzhushou)
- [GuaiKei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls, files]

**Output Format:** [Markdown guidance with shell commands; command execution returns structured JSON and writes result files under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; normal outputs include status, error_code, request metadata, skill metadata, and result data.]

## Skill Version(s):

0.1.0 (source: evidence.release.version; artifact package.json and changelog list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
