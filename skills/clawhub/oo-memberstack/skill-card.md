## Description:

This skill enables agents to read, create, update, and delete Memberstack data through the OOMOL Memberstack connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Memberstack members through OOMOL-connected credentials, including reading member records, changing member data, managing free plans, and verifying member JWTs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include network-fetched installer commands that execute directly in a shell.

Mitigation: Do not let an agent run the remote installer automatically; install the oo CLI only through a reviewed or signed vendor method.

Risk: The skill can create, update, delete, and modify Memberstack member and plan data.

Mitigation: Confirm the exact target, payload, and expected effect before approving write or destructive connector actions.

Risk: Memberstack operations rely on OOMOL as an intermediary for credentials and connector execution.

Mitigation: Install only when OOMOL is an acceptable intermediary for the workspace and account being managed.

## Reference(s):

- [Memberstack homepage](https://www.memberstack.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Memberstack connection](https://console.oomol.com/app-connections?provider=memberstack)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses with data and execution metadata when actions run.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
