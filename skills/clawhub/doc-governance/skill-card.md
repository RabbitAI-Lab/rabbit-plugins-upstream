## Description:

Doc-governance helps agents audit, initialize, and check a repository's documentation governance by comparing documentation structure, references, plans, and declared contracts against project files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to find drift between project documentation and implementation, install ADR and plan governance scaffolding, and run repeatable checks before plans, commits, or pull requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing with init --yes creates persistent git and Claude Code hooks that can block commits or file writes after the session ends.

Mitigation: Review the planned changes first, run init without --yes for a dry run, and remove the installed hook files or settings entries if the project should stop enforcing them.

Risk: The security verdict is suspicious because the installer has been reported to have a path-boundary flaw involving writable Claude settings outside the chosen repository.

Mitigation: Use init --yes only after inspecting .claude/settings.json and hook paths for symlinks, and prefer audit/check when evaluating repositories you do not fully trust.

Risk: Pattern-based documentation checks can miss unusual phrasing or produce incorrect findings.

Mitigation: Treat clean runs as no detected issue rather than proof, and review reported findings against the relevant incident or source file before changing documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/doc-governance)
- [Skill instructions](artifact/SKILL.md)
- [Documentation governance framework](artifact/framework.md)
- [Incident list](artifact/incidents.md)
- [ADR template README](artifact/templates/adr-README.md)
- [Plan template README](artifact/templates/plan-README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated repository files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [audit and check are read-only; init --yes can write repository governance files and persistent hooks]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
