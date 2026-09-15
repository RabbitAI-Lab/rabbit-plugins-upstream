## Description:

Agora lets an agent manage Agora Console projects through an OOMOL-connected account, including listing projects, checking usage, creating projects, updating status, and managing primary certificates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Agora Console projects from an OOMOL-connected account. It guides agents to inspect live action schemas and run read, write, and certificate-management actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review the installer step before use, prefer a versioned and verifiable official release or package manager, and do not allow an agent to run the remote installer automatically.

Risk: Write actions can create projects, enable or disable projects, and enable or disable primary certificates.

Mitigation: Confirm the exact action payload and intended effect with the user before running any write action.

Risk: The reset_primary_certificate action is destructive and can overwrite an Agora project's primary App Certificate.

Mitigation: Confirm the target project and get explicit approval before running certificate resets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-agora)
- [Agora Homepage](https://www.agora.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use oo connector schema and oo connector run; action responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
