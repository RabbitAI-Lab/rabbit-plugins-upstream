## Description:

Audits AGENTS.md and CLAUDE.md runtime configuration files, produces a scorecard with prioritized fixes, and can help apply approved repairs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to evaluate whether project AGENTS.md or CLAUDE.md files are concise, actionable runtime configuration rather than project manuals. It returns a scored audit, prioritized remediation guidance, and optional approved edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads project runtime configuration files, related documentation pointers, and selected project metadata during audits.

Mitigation: Run it only in projects where those files may be inspected, and avoid placing secrets in AGENTS.md, CLAUDE.md, or linked runtime-configuration documents.

Risk: Repair suggestions can change project runtime configuration if the user approves edits.

Mitigation: Review the proposed changes before approval and inspect the resulting diff before committing.

Risk: The optional scripts/run-all-doctors.sh suite can call sibling doctor tools, including environment checks beyond the core document checker.

Mitigation: Use the broader suite only after confirming that the additional checks and sibling tools are in scope for the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-md-doctor-skill)
- [Project homepage](https://github.com/huiyonghkw/hekouwang-claude-md-doctor-skill)
- [Doctor suite reference](references/doctor-suite.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with prioritized recommendations, optional file edits, shell commands, and JSON when the checker is run with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read AGENTS.md, CLAUDE.md, related documentation pointers, and project metadata while auditing; repair actions require user approval.]

## Skill Version(s):

1.3.2 (source: server release metadata, frontmatter, and changelog released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
