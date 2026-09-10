## Description:

Installs, updates, adopts, or inspects a repository-level handoff protocol that governs future agent task handoffs, summaries, and commit trailers in a git repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they want an agent to install, update, adopt, or inspect a persistent handoff protocol in a git repository. It helps future agent sessions resume work through a task baton, archive summaries, and a commit ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently changes repository agent rules.

Mitigation: Install it only in repositories where future agents should follow the handoff workflow, and review the installed runtime policy before using write modes.

Risk: The security summary reports an edge-case update bug that can remove unrelated AGENTS.md content.

Mitigation: Keep backups or a clean version-control state before write modes, and review AGENTS.md changes carefully after adopt or update operations.

Risk: The recovery path can read specified prior-session history and place extracted summaries into Git.

Mitigation: Approve recovery only when that history access is acceptable, and review extracted summaries before they are written or committed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/snowsonz/skills/agent-handoff-skill)
- [Publisher profile](https://clawhub.ai/user/snowsonz)
- [Protocol maintenance reference](references/protocol.md)
- [Compatibility reference](references/compatibility.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and repository file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires sh and git, plus either shasum or sha256sum for hash checks.]

## Skill Version(s):

0.1.12 (source: server-resolved release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
