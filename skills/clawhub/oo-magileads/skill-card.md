## Description:

Magileads enables agents to read, create, update, and delete Magileads contact-list data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Magileads contact lists from an OOMOL-connected account, including listing, retrieving, creating, updating, and deleting contact-list records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer pipeline commands for the oo CLI.

Mitigation: Review setup before installation; prefer a verified package, signed release, or checksum-verified download, and do not let an agent run the remote installer pipeline automatically.

Risk: Write and destructive Magileads actions can change or delete contact-list data.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and expected effect with the user before running write or deletion actions.

## Reference(s):

- [Magileads homepage](https://www.magileads.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-magileads)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas; write and destructive Magileads actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
