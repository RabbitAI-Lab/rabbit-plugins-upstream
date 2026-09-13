## Description:

Record and analyze local token usage from Codex, Claude Code, OpenClaw, Hermes Agent, OpenCode, DeepSeek Harness, WorkBuddy, and WorkBuddy AI with the published token-stats CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baijian](https://clawhub.ai/user/baijian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose local agent source coverage, collect daily token-usage snapshots, analyze historical date ranges, and configure periodic local recording. Reports describe available local usage counters and should not be treated as billing records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an opaque external token-stats binary that can read broad private AI session stores.

Mitigation: Install only from a trusted publisher, verify release checksums, prefer narrow agent selectors first, and review the exact source directories before collection.

Risk: Periodic collection can install a persistent local recorder and continue reading selected agent stores in the background.

Mitigation: Enable the LaunchAgent or scheduler only after confirming interval, source scope, and output directories; remove or disable it when recurring collection is no longer needed.

Risk: Token reports, snapshots, and logs may reveal sensitive usage patterns or local project context.

Mitigation: Keep generated records local, restrict filesystem permissions, and periodically delete snapshot or log directories that are no longer needed.

## Reference(s):

- [Token Recording Reference](references/token-recording.md)
- [baijian/token-stats](https://github.com/baijian/token-stats)
- [token-stats v0.0.2 release](https://github.com/baijian/token-stats/releases/tag/v0.0.2)
- [Latest token-stats release](https://github.com/baijian/token-stats/releases/latest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local daily token records, optional per-run snapshots, scheduler logs, and LaunchAgent configuration when periodic collection is requested.]

## Skill Version(s):

0.0.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
