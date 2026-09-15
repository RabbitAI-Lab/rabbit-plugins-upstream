## Description:

Elorus helps agents read, create, and update Elorus contacts, invoices, and products or services through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, finance operators, and developers use this skill to list and retrieve Elorus contacts, invoices, and products or services, and to create or update those records after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could be unsafe if run blindly.

Mitigation: Use an official, version-pinned installation method with checksum or signature verification before installing the oo CLI.

Risk: Write actions can change Elorus contacts, invoices, and products or services.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before executing write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elorus)
- [Elorus homepage](https://www.elorus.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Elorus read results or proposed write payloads; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
