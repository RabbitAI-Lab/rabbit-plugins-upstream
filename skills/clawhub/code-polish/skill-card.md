## Description:

Pre-release code review skill that runs project validation, reviews diffs for cleanliness, design, efficiency, and side-effect ordering issues, validates findings, and applies targeted fixes after approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use code-polish before committing or pushing changes to run validation, inspect changed code through multiple review lenses, verify findings, and apply minimal fixes after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run project validation commands selected from repository documentation.

Mitigation: Inspect CLAUDE.md and the configured check command before use, and require explicit approval for command execution when operating in untrusted repositories.

Risk: The skill can edit source files after reviewing findings.

Mitigation: Keep the approval gate before fixes, review proposed findings first, and verify changes with the project's validation command.

Risk: Diff contents can contain instruction-shaped text or secrets.

Mitigation: Treat reviewed diffs as untrusted data, use explicit content boundaries when prompting review agents, and mask credential values in reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tenequm/skills/code-polish)
- [Declared project homepage](https://github.com/tenequm/skills/tree/main/skills/polish)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown review report with file and line references, recommendations, and optional targeted code edits or validation commands after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run repository validation commands and inspect or edit source files when the user approves fixes.]

## Skill Version(s):

2.7.0 (source: server release metadata, skill metadata, and changelog, released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
