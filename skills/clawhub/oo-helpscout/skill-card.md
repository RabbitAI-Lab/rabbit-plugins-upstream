## Description:

Help Scout lets agents read, create, and update Help Scout conversations, customers, inbox metadata, tags, users, workflows, saved replies, and threads through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support operators, and agents use this skill to operate a connected Help Scout account for customer-support workflows, including conversation lookup, replies, assignments, status updates, tags, custom fields, customers, workflows, and saved replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change real Help Scout records, including replies, assignments, statuses, snoozes, tags, custom fields, workflows, conversations, and customers.

Mitigation: Confirm the exact action payload and expected effect with the user before running write or destructive actions.

Risk: Execution depends on an installed oo CLI, a signed-in OOMOL account, an active Help Scout connection, and sufficient OOMOL credits.

Mitigation: Use first-time setup, reconnection, or billing steps only after the matching command error occurs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-helpscout)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Help Scout](https://www.helpscout.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions; command responses are JSON objects with data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
