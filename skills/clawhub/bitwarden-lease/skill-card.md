## Description:

Bitwarden Lease helps local agents and terminal workflows reuse an unlocked Bitwarden CLI session through an owner-only macOS broker without exposing BW_SESSION.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers, local AI agent users, and terminal users use this skill to install, operate, diagnose, and safely consume a local macOS Bitwarden CLI lease for authorized credential-backed work without persisting BW_SESSION.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A same-user local broker can run allowed Bitwarden CLI commands for up to 24 hours after one unlock.

Mitigation: Install only on trusted macOS user accounts, keep the socket owner-only, review or pin the installed source, and avoid shared or untrusted accounts.

Risk: Secret-bearing Bitwarden command output can be exposed if captured in an agent transcript, log, CI output, or project file.

Mitigation: Route secret output directly into the smallest authorized one-shot consumer, suppress diagnostics that might echo it, and avoid persisting retrieved values.

## Reference(s):

- [Security contract](references/security-contract.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and command-output interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not produce or expose Bitwarden sessions; secret-bearing command output should be routed only into authorized consumers.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
