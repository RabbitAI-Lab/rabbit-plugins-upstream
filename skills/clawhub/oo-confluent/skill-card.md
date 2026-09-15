## Description:

Use this skill to operate Confluent Cloud through the OOMOL-connected oo CLI connector for reading, creating, updating, and deleting organizations, environments, and Kafka clusters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Confluent Cloud resources through an OOMOL-connected account. It supports schema inspection followed by read, write, and destructive connector actions for organizations, environments, and Kafka clusters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can run remote oo CLI installer scripts directly in a shell.

Mitigation: Review and approve the installer path before use; prefer a verified, pinned, or package-manager installation.

Risk: Write and destructive connector actions can change or delete Confluent Cloud resources.

Mitigation: Require explicit user approval for Confluent write or delete actions, including the exact payload and target.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-confluent)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Confluent homepage](https://www.confluent.io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return JSON data with an execution id under meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
