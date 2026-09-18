## Description:

Confluent helps agents operate Confluent Cloud through an OOMOL-connected oo CLI connector for reading, creating, updating, and deleting resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Confluent Cloud organizations, environments, and Kafka clusters and to manage environments through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote OOMOL CLI installer directly in a shell.

Mitigation: Review the installer before running it, and prefer a versioned or package-manager install with checksum or signature verification.

Risk: Write and destructive Confluent actions can change or delete cloud environments.

Mitigation: Inspect the live action schema, confirm the exact target and payload, and get explicit approval before write or delete actions.

## Reference(s):

- [ClawHub Confluent skill page](https://clawhub.ai/oomol/skills/oo-confluent)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Confluent homepage](https://www.confluent.io)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON connector responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
