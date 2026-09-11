## Description:

Tinker ORCA coordinates parallel multi-agent coding by drafting changes concurrently, applying them under per-file leases, and limiting writes to declared repository-relative paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Tinker ORCA when a coding task can be split into two or more independent edit units and they want an agent to draft changes in parallel, apply them to declared files, verify the result, and optionally commit only after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spawn coding agents with shell plus repository write and delete access.

Mitigation: Install and run it only in repositories where that access is acceptable, and prefer an OS or container sandbox for stronger isolation.

Risk: Write-safety depends partly on spawned agents following the declared file allowlist.

Mitigation: Keep units[].writes as narrow as possible and inspect resulting file changes before accepting or committing them.

Risk: Raw command and external-program options can run caller-supplied commands or tools.

Mitigation: Use named verification presets where possible and enable raw commands or external program paths only when the commands and tools are trusted.

Risk: Optional commit and foreign-work-in-progress behavior can affect git history or another session's uncommitted files.

Mitigation: Leave committing off until changes have been inspected, require explicit commit confirmation, and avoid allowForeignWip unless you intend to snapshot and restore another session's work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/tinker-orca)
- [TinkerClaw repository](https://github.com/globalcaos/tinkerclaw)

## Skill Output:

**Output Type(s):** [code, shell commands, configuration, guidance]

**Output Format:** [Structured workflow results with Markdown summaries and inline code or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce repository file changes and optional git commits when both commit and confirmedCommit are enabled.]

## Skill Version(s):

1.2.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
