## Description:

Installs or updates a repository-level handoff protocol that governs how future agent sessions start work, hand off tasks, and commit state in a git repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository maintainers use this skill when they explicitly want to install, update, adopt, or inspect a persistent agent handoff protocol in a git repository. It is intended for controlled repositories where future agent workflows should follow the installed handoff rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that symlinked AGENTS.md or CLAUDE.md files can lead the installer to copy local file contents into the target repository.

Mitigation: Install or update only after confirming AGENTS.md and CLAUDE.md are regular files in a trusted repository, then review the resulting diff before committing or pushing.

Risk: The installed protocol persistently changes future agent behavior in the repository, including task-state commits and a consent-gated history recovery workflow.

Mitigation: Use the skill only when the user explicitly requests installation, update, adoption, or status inspection, and disclose the persistent workflow changes before write modes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/snowsonz/skills/agent-handoff-skill)
- [Protocol maintenance reference](references/protocol.md)
- [Discovery and invocation compatibility](references/compatibility.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with local shell command execution and repository file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write persistent handoff files, a Claude skill link, task templates, and an installation lock in the target git repository after explicit user confirmation.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata and VERSION file)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
