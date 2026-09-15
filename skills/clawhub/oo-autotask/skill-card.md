## Description:

Autotask (datto.com) supports Autotask search and read requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support or operations teams use this skill to query Autotask Companies, Contacts, Tickets, entity metadata, and zone information through the oo CLI after their OOMOL account is connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a suspicious verdict because first-time setup includes direct execution of remote installer scripts without verification.

Mitigation: Before installing, verify the oo CLI installer through an official trusted channel and prefer a signed or checksum-verified installation path.

Risk: An agent could run first-time setup commands even when the user only needs an Autotask read or search action.

Mitigation: Use the skill for Autotask read and search tasks, and run authentication, connection, billing, or installer commands only after a matching command failure or explicit user direction.

## Reference(s):

- [Autotask Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-autotask)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Autotask PSA](https://www.datto.com/products/autotask-psa/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
