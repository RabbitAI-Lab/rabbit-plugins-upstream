## Description:

Installs, updates, adopts, or inspects a repository-level handoff protocol that governs how future agent sessions start work, hand off tasks, and commit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they need to install or maintain a persistent handoff protocol in a git repository for future agent sessions. It is not intended for ordinary task continuation; the installed runtime skill handles that workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill persists a repository-level handoff workflow that changes how future agents operate in the target repository.

Mitigation: Use write modes only for repositories where that behavior is intended, and confirm the target path and mode before installation or update.

Risk: Write modes add or update AGENTS.md, CLAUDE.md, .agents handoff files, the task template, tools/ledger.sh, and a .claude skill symlink.

Mitigation: Review the disclosed file list before confirmation; the installer performs content-hash conflict checks and refuses to overwrite unexpected local changes.

Risk: The installed runtime rules are written in Chinese, which may be unsuitable for teams that cannot review or maintain them.

Mitigation: Install only when users understand or accept the Chinese runtime protocol; normal user-facing communication should still follow the user's language preferences.

Risk: The installed runtime includes a disaster-recovery path that can use external tooling to read prior session history when a task baton is lost.

Mitigation: Use that path only after explicit user consent to read the prior session history, and confirm the recovered result before writing it to the repository.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/snowsonz/skills/agent-handoff-skill)
- [Protocol Maintenance Reference](references/protocol.md)
- [Discovery and Trigger Compatibility](references/compatibility.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command output and repository file changes when write mode is confirmed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status mode is read-only; write modes modify repository handoff files, task templates, ledger tooling, and client configuration only after explicit confirmation.]

## Skill Version(s):

0.1.10 (source: server release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
