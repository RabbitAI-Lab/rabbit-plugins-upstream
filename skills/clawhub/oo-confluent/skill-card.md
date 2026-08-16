## Description:

Use this skill to operate Confluent Cloud through OOMOL's oo CLI for reading, creating, updating, and deleting Confluent resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Confluent Cloud organizations, environments, and Kafka clusters through an OOMOL-connected Confluent account. The skill supports read actions directly and requires explicit confirmation before create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete Confluent Cloud environments.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write or destructive action runs.

Risk: The skill depends on OOMOL's oo CLI and a connected Confluent account.

Mitigation: Install and use the oo CLI only when trusted, and connect a Confluent account with only the permissions intended for this skill.

Risk: Connector action schemas may change over time.

Mitigation: Fetch the live action schema before constructing each connector payload.

## Reference(s):

- [ClawHub Confluent Skill](https://clawhub.ai/oomol/skills/oo-confluent)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Confluent](https://www.confluent.io)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
