## Description:

Recover lost agent session content and file changes from local OpenClaw conversation logs with streaming search, extraction, optional edit replay, and guarded restore-to-disk workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to find lost OpenClaw sessions, inspect write/edit operations, recover file contents, and restore or rebuild files from local session history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search results and full-content extraction can expose secrets or private data stored in local conversation logs.

Mitigation: Review matched sessions before using --show-content or --restore, use narrow search windows and file filters, and avoid printing full content unless it is needed.

Risk: Restore operations can overwrite existing files, especially when --yes is used in non-interactive contexts.

Mitigation: Prefer --restore-to for a separate recovery path, confirm the target before passing --yes, and keep backups of files that may be overwritten.

Risk: Scan limits, missing QMD archives, reset sessions, or oversized skipped logs can lead to incomplete recovery results.

Mitigation: Check warnings in the command output, broaden keywords or date windows when needed, and adjust --max-files only after considering local resource impact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/session-recovery)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, guidance]

**Output Format:** [Terminal text, structured JSON, and optional restored file content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches local OpenClaw JSONL and optional QMD logs; restore operations write files only when explicitly requested.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
