## Description:

Courier helps agents operate Courier through the OOMOL-connected oo CLI to read, create, update, delete, and send Courier data without handling raw credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Courier profiles, subscription lists, and messages from an agent workflow through the oo CLI. It supports read operations, state-changing updates, and destructive Courier actions with confirmation requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask users to run remote installer scripts directly in a shell.

Mitigation: Review the installer path first and prefer a verified, versioned oo CLI source with checksums or signatures.

Risk: Courier write, send, and delete actions can change or remove production data.

Mitigation: Confirm the exact payload, target, and effect with the user before approving state-changing or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-courier)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Courier Homepage](https://www.courier.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing Courier action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
