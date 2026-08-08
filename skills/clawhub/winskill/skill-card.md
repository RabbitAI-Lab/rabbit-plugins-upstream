## Description:

Winskill helps agents provide Windows Server administration guidance for disk analysis, safe cleanup, IIS and service checks, update diagnostics, security auditing, performance monitoring, container checks, compliance review, and multi-server operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

IT administrators, operators, and developers use this skill to ask an agent for Windows Server diagnostics, maintenance command guidance, and operational review steps across local and remote server environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary identifies broad remote command execution and credential storage risk in the remote-management workflow.

Mitigation: Install only when multi-server Windows administration is intended, review every remote command before execution, and avoid the remote-management module unless stored credentials and arbitrary remote execution are acceptable.

Risk: The security summary identifies scheduled tasks and destructive repair or cleanup steps that can conflict with read-only or offline safety expectations.

Mitigation: Use read-only diagnostics by default, require explicit confirmation for service changes, cleanup, repair, and scheduled-task operations, and do not deploy this skill in restricted or offline environments as written.

## Reference(s):

- [ClawHub winskill release page](https://clawhub.ai/fyniujin/skills/winskill)
- [Docker Engine on Windows Server installation documentation](https://docs.docker.com/engine/install/windows-server/)
- [kubectl on Windows installation documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline PowerShell and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may require administrator review and explicit user confirmation before execution.]

## Skill Version(s):

3.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
