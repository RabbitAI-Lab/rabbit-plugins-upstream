## Description:

Ongage lets an agent read, list, update, and upsert Ongage list and contact data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate Ongage contact and list workflows through a connected OOMOL account. It supports read-only lookups and list pagination, plus confirmed write operations for contact updates, upserts, and status changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Ongage contact and list data.

Mitigation: Require explicit user confirmation for contact-status changes, contact updates, and upserts, including the exact payload and intended effect.

Risk: The setup instructions include pipe-to-shell installer commands.

Mitigation: Install the oo CLI only from a trusted and independently verified source, or use a reviewed installation method before enabling the skill.

Risk: Live connector schemas define the authoritative action inputs and outputs.

Mitigation: Inspect the action schema before constructing payloads so requests match the current Ongage connector contract.

## Reference(s):

- [ClawHub Ongage Skill](https://clawhub.ai/oomol/skills/oo-ongage)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ongage Homepage](https://www.ongage.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses containing Ongage data and an execution ID.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
