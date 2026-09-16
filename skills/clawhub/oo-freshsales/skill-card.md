## Description:

Freshsales helps agents read, create, update, and delete Freshsales CRM contact data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and CRM operators use this skill to operate Freshsales contacts from an agent session, including listing saved-view contacts and creating, updating, retrieving, or deleting contact records after appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that may be unsafe if run without review.

Mitigation: Use official, versioned, signed, or checksum-verified installation steps before installing the oo CLI.

Risk: Write and destructive Freshsales actions can create, modify, or delete CRM contact records.

Mitigation: Require explicit user confirmation of the target record, payload, and expected effect before running write or destructive actions.

Risk: Freshsales operations route through OOMOL's connector.

Mitigation: Install only when the user trusts OOMOL and is comfortable using its connector for Freshsales CRM operations.

## Reference(s):

- [Freshsales skill page](https://clawhub.ai/oomol/skills/oo-freshsales)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Freshsales homepage](https://www.freshworks.com/crm/sales/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Freshsales action responses are returned as JSON by the oo CLI when actions are executed.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
