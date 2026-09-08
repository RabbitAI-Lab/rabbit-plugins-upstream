## Description:

Record and analyze local token usage from Codex, Claude Code, OpenClaw, Hermes Agent, OpenCode, and DeepSeek Harness with the published token-stats CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baijian](https://clawhub.ai/user/baijian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to record local token-usage snapshots, analyze stored date ranges, break down usage by agent, model, session, or rate-limit bucket, and set up periodic local collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The macOS recorder installs a recurring LaunchAgent that automatically refreshes local token-usage records.

Mitigation: Enable scheduling only after reviewing the LaunchAgent behavior, use the narrowest agent selector needed, and choose a modest refresh interval.

Risk: Raw JSON reports and recorder logs can include local paths, session metadata, and other sensitive local usage details.

Mitigation: Keep reports, snapshots, and logs private; restrict file permissions and avoid sharing raw JSON unless those details have been reviewed.

## Reference(s):

- [Token Recording Reference](references/token-recording.md)
- [baijian/token-stats public distribution](https://github.com/baijian/token-stats)
- [token-stats v0.0.1 release baseline](https://github.com/baijian/token-stats/releases/tag/v0.0.1)
- [Latest token-stats release](https://github.com/baijian/token-stats/releases/latest)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are based on local usage counters and may include storage paths, warnings, missing-agent notes, and session details.]

## Skill Version(s):

0.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
