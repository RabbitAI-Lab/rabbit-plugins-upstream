## Description:

Monica CRM enables agents to list and search contacts and create, read, update, or delete contact notes in a connected Monica CRM account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Monica CRM records through an OOMOL-connected account, including contact lookup and contact note management. It is useful when an agent must inspect live action schemas before issuing CRM read, write, or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts for the oo CLI.

Mitigation: Review installer steps before installation and prefer a verified package, pinned release, checksum, or manually inspected installer.

Risk: The skill can modify or delete Monica CRM data.

Mitigation: Confirm exact payloads and intended effects before creating, updating, or deleting CRM records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-monica-crm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Monica CRM homepage](https://www.monicahq.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON payloads for connector actions and returns JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
