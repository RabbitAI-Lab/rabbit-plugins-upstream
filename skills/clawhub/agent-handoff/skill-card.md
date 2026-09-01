## Description:

Installs, updates, adopts, or inspects a repository handoff protocol for agent task continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to add a repository-local handoff workflow so future agents can read and update task baton files, follow commit trailer conventions, and inspect handoff status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutating modes persist a handoff workflow in the target repository and affect how future agents handle task state and commits.

Mitigation: Run install, update, or adopt-existing only after explicit confirmation for the target repository; use status mode for read-only inspection.

Risk: The installed runtime policy is written in Chinese, which may obscure exact workflow requirements for some reviewers.

Mitigation: Review the bundled runtime policy before installation when exact handoff semantics matter.

Risk: Repository files managed by the handoff installer could contain local changes.

Mitigation: Rely on the installer conflict checks, which refuse to overwrite managed files when their content is outside expected hashes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/snowsonz/skills/agent-handoff)
- [Installation protocol reference](references/protocol.md)
- [Discovery and trigger compatibility](references/compatibility.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with local shell command execution and repository file changes when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status mode is read-only; install, update, and adopt-existing modes can write repository handoff files, a task template, a ledger script, AGENTS/CLAUDE handoff entries, a symlink, and installation lock metadata.]

## Skill Version(s):

0.1.4 (source: server release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
