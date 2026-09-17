## Description:

Neon helps an agent operate Neon projects through an OOMOL-connected account, including read, create, update, and delete workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Neon projects, branches, databases, operations, and current-user information through the oo CLI using connected account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote CLI installer commands can execute downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI from a verified, versioned, checksum- or signature-validated source before using the skill.

Risk: Write and destructive Neon actions can change or delete projects, branches, and databases.

Mitigation: Confirm the exact target, payload, and expected effect before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-neon)
- [Neon homepage](https://neon.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash, PowerShell, text URLs, and JSON command payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect connector schemas and run Neon actions with JSON payloads.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
