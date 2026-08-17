## Description:

Winskill is a Windows Server operations toolbox that helps agents generate PowerShell-based diagnostics, reports, cleanup previews, repair workflows, security audits, remote management actions, and module guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, system administrators, and operations engineers use this skill to investigate and manage Windows Server environments through guided PowerShell snippets, markdown reports, and confirmation-gated operational workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers high-privilege Windows administration, including remote management, credential storage, repair flows, cleanup, service operations, and scheduled baseline collection.

Mitigation: Install only when those administrative capabilities are intended; review generated commands before execution and run with least-privilege accounts where possible.

Risk: Security evidence says the skill makes contradictory safety and offline claims despite exposing admin, remote execution, credential storage, deletion, and persistence-related features.

Mitigation: Do not rely on the skill's offline or read-only claims as a control; require human review for remote management, credential storage, cleanup, repair, and scheduled-task actions.

Risk: Cleanup and repair workflows can delete files, stop services, reset networking, clear caches, or modify system state.

Mitigation: Require an explicit operation preview and confirmation before state-changing commands, and validate backups or restore points before repair or cleanup actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/winskill)
- [Docker Engine on Windows Server documentation](https://docs.docker.com/engine/install/windows-server/)
- [kubectl on Windows documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with PowerShell and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include administrative command proposals, diagnostic tables, reports, and confirmation prompts.]

## Skill Version(s):

3.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
